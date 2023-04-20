#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Document:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content

class DocumentStrategy(ABC):

    @abstractmethod
    def read_file(self, filename):
        pass

    @abstractmethod
    def write_file(self, filename, content):
        pass

class DocumentHandler:
    def __init__(self, document_strategy: DocumentStrategy):
        self._strategy = document_strategy

    def open_document(self, filename):
        content = self._strategy.read_file(filename)
        return Document(content)

    def save_document(self, document, filename):
        content = document.get_content()
        self._strategy.write_file(filename, content)

class TextDocumentStrategy(DocumentStrategy):
    def read_file(self, filename):
        print("Getting content from TXT file...")

    def write_file(self, filename, content):
        # write plain text file content
        print("Saving TXT file...")

class MarkdownDocumentStrategy(DocumentStrategy):
    def read_file(self, filename):
        print("Getting content MARKDOWN file...")

    def write_file(self, filename, content):
        print("Saving MARKDOWN file...")

handler = DocumentHandler(TextDocumentStrategy())
document = handler.open_document("test.txt")
document._content = "This is a plain text document."
handler.save_document(document, "test.txt")

handler = DocumentHandler(MarkdownDocumentStrategy())
document = handler.open_document("test.md")
document._content = "This is a **markdown** document."
handler.save_document(document, "test.md")