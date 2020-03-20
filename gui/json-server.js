"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/* --------------------------------------------------------------------------------------------
 * Copyright (c) 2018 TypeFox GmbH (http://www.typefox.io). All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 * ------------------------------------------------------------------------------------------ */
const fs = require("fs");
const request_light_1 = require("request-light");
const vscode_uri_1 = require("vscode-uri");
const vscode_languageserver_1 = require("vscode-languageserver");
const vscode_json_languageservice_1 = require("vscode-json-languageservice");
const ipcreader_1 = require("./ipcreader");
const ipcwriter_1 = require("./ipcwriter");
function start(reader, writer) {
    const connection = vscode_languageserver_1.createConnection(reader, writer);
    const server = new JsonServer(connection);
    server.start();
    return server;
}
exports.start = start;
start(new ipcreader_1.RemoteElectronIPCMessageReader(), new ipcwriter_1.ElectronIPCMessageWriter());
class JsonServer {
    constructor(connection) {
        this.connection = connection;
        this.documents = new vscode_languageserver_1.TextDocuments();
        this.jsonService = vscode_json_languageservice_1.getLanguageService({
            schemaRequestService: this.resovleSchema.bind(this)
        });
        this.pendingValidationRequests = new Map();
        this.documents.listen(this.connection);
        this.documents.onDidChangeContent(change => this.validate(change.document));
        this.documents.onDidClose(event => {
            this.cleanPendingValidation(event.document);
            this.cleanDiagnostics(event.document);
        });
        this.connection.onInitialize(params => {
            if (params.rootPath) {
                this.workspaceRoot = vscode_uri_1.default.file(params.rootPath);
            }
            else if (params.rootUri) {
                this.workspaceRoot = vscode_uri_1.default.parse(params.rootUri);
            }
            this.connection.console.log("The server is initialized.");
            return {
                capabilities: {
                    textDocumentSync: this.documents.syncKind,
                    codeActionProvider: true,
                    completionProvider: {
                        resolveProvider: true,
                        triggerCharacters: ['"', ':']
                    },
                    hoverProvider: true,
                    documentSymbolProvider: true,
                    documentRangeFormattingProvider: true,
                    executeCommandProvider: {
                        commands: ['json.documentUpper']
                    },
                    colorProvider: true,
                    foldingRangeProvider: true
                }
            };
        });
        this.connection.onCodeAction(params => this.codeAction(params));
        this.connection.onCompletion(params => this.completion(params));
        this.connection.onCompletionResolve(item => this.resolveCompletion(item));
        this.connection.onExecuteCommand(params => this.executeCommand(params));
        this.connection.onHover(params => this.hover(params));
        this.connection.onDocumentSymbol(params => this.findDocumentSymbols(params));
        this.connection.onDocumentRangeFormatting(params => this.format(params));
        this.connection.onDocumentColor(params => this.findDocumentColors(params));
        this.connection.onColorPresentation(params => this.getColorPresentations(params));
        this.connection.onFoldingRanges(params => this.getFoldingRanges(params));
    }
    start() {
        this.connection.listen();
    }
    getFoldingRanges(params) {
        const document = this.documents.get(params.textDocument.uri);
        if (!document) {
            return [];
        }
        return this.jsonService.getFoldingRanges(document);
    }
    findDocumentColors(params) {
        const document = this.documents.get(params.textDocument.uri);
        if (!document) {
            return Promise.resolve([]);
        }
        const jsonDocument = this.getJSONDocument(document);
        return this.jsonService.findDocumentColors(document, jsonDocument);
    }
    getColorPresentations(params) {
        const document = this.documents.get(params.textDocument.uri);
        if (!document) {
            return [];
        }
        const jsonDocument = this.getJSONDocument(document);
        return this.jsonService.getColorPresentations(document, jsonDocument, params.color, params.range);
    }
    codeAction(params) {
        const document = this.documents.get(params.textDocument.uri);
        if (!document) {
            return [];
        }
        return [{
                title: "Upper Case Document",
                command: "json.documentUpper",
                // Send a VersionedTextDocumentIdentifier
                arguments: [Object.assign({}, params.textDocument, { version: document.version })]
            }];
    }
    format(params) {
        const document = this.documents.get(params.textDocument.uri);
        return document ? this.jsonService.format(document, params.range, params.options) : [];
    }
    findDocumentSymbols(params) {
        const document = this.documents.get(params.textDocument.uri);
        if (!document) {
            return [];
        }
        const jsonDocument = this.getJSONDocument(document);
        return this.jsonService.findDocumentSymbols(document, jsonDocument);
    }
    executeCommand(params) {
        if (params.command === "json.documentUpper" && params.arguments) {
            const versionedTextDocumentIdentifier = params.arguments[0];
            const document = this.documents.get(versionedTextDocumentIdentifier.uri);
            if (document) {
                this.connection.workspace.applyEdit({
                    documentChanges: [{
                            textDocument: versionedTextDocumentIdentifier,
                            edits: [{
                                    range: {
                                        start: { line: 0, character: 0 },
                                        end: { line: Number.MAX_SAFE_INTEGER, character: Number.MAX_SAFE_INTEGER }
                                    },
                                    newText: document.getText().toUpperCase()
                                }]
                        }]
                });
            }
        }
    }
    hover(params) {
        const document = this.documents.get(params.textDocument.uri);
        if (!document) {
            return Promise.resolve(null);
        }
        const jsonDocument = this.getJSONDocument(document);
        return this.jsonService.doHover(document, params.position, jsonDocument);
    }
    resovleSchema(url) {
        const uri = vscode_uri_1.default.parse(url);
        if (uri.scheme === 'file') {
            return new Promise((resolve, reject) => {
                fs.readFile(uri.fsPath, 'UTF-8', (err, result) => {
                    err ? reject('') : resolve(result.toString());
                });
            });
        }
        return request_light_1.xhr({ url, followRedirects: 5 }).then(response => {
            return response.responseText;
        }, (error) => {
            return Promise.reject(error.responseText || request_light_1.getErrorStatusDescription(error.status) || error.toString());
        });
    }
    resolveCompletion(item) {
        return this.jsonService.doResolve(item);
    }
    completion(params) {
        const document = this.documents.get(params.textDocument.uri);
        if (!document) {
            return Promise.resolve(null);
        }
        const jsonDocument = this.getJSONDocument(document);
        return this.jsonService.doComplete(document, params.position, jsonDocument);
    }
    validate(document) {
        this.cleanPendingValidation(document);
        this.pendingValidationRequests.set(document.uri, setTimeout(() => {
            this.pendingValidationRequests.delete(document.uri);
            this.doValidate(document);
        }));
    }
    cleanPendingValidation(document) {
        const request = this.pendingValidationRequests.get(document.uri);
        if (request !== undefined) {
            clearTimeout(request);
            this.pendingValidationRequests.delete(document.uri);
        }
    }
    doValidate(document) {
        if (document.getText().length === 0) {
            this.cleanDiagnostics(document);
            return;
        }
        const jsonDocument = this.getJSONDocument(document);
        this.jsonService.doValidation(document, jsonDocument).then(diagnostics => this.sendDiagnostics(document, diagnostics));
    }
    cleanDiagnostics(document) {
        this.sendDiagnostics(document, []);
    }
    sendDiagnostics(document, diagnostics) {
        this.connection.sendDiagnostics({
            uri: document.uri, diagnostics
        });
    }
    getJSONDocument(document) {
        return this.jsonService.parseJSONDocument(document);
    }
}
exports.JsonServer = JsonServer;
//# sourceMappingURL=json-server.js.map