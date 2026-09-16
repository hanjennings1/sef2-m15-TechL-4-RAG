from __future__ import annotations

import re
from typing import Any

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "can",
    "do", "does",
    "for", "from", "get", "how", "i", "if", "in", "is", "it", "me",
    "my", "need",
    "of", "on", "or", "our", "should", "so", "the", "their", "to",
    "use", "what",
    "when", "where", "who", "why", "with", "you", "your",
}


def tokenize(text: str) -> set[str]:
    """Convert text into a set of searchable lowercase tokens."""
    raw_tokens = re.findall(r"[a-zA-Z0-9']+", text.lower())

    return {
        token.strip("'")
        for token in raw_tokens
        if len(token.strip("'")) > 1 and token.strip("'") not in STOPWORDS
    }