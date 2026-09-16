from __future__ import annotations

from flask import Flask, jsonify, request

from ai_client import generate_response
from documents import DOCUMENTS
from rag_service import build_prompt, retrieve_context, source_metadata

def create_app():
    app = Flask(__name__)

    @app.get("/api/health")
    def health_check():
        return jsonify({"status": "ok"})
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)