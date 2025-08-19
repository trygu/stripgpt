"""Core cleaning logic for stripgpt."""
from __future__ import annotations
import re
import unicodedata

START = '\ue200'
END = '\ue201'

PUA_SPAN = re.compile(rf'{START}[\s\S]*?{END}')
ZW_DIR   = re.compile(r'[\u200B\u200C\u200D\u200E\u200F\u202A-\u202E\u2060\u2066-\u2069]')
BARE_TOKEN = re.compile(r'\bturn\d+\w*\d+\b', re.IGNORECASE)
LINE_RANGE = re.compile(r'\bL\d+-L\d+\b')

def clean_text(txt: str, *, kill_bare: bool, normalize: bool) -> str:
	t = PUA_SPAN.sub('', txt)
	t = ''.join(ch for ch in t if unicodedata.category(ch) != 'Co')
	t = ZW_DIR.sub('', t)
	if kill_bare:
		t = BARE_TOKEN.sub('', t)
		t = LINE_RANGE.sub('', t)
	if normalize:
		t = re.sub(r'[ \t]+', ' ', t)
		t = re.sub(r'[ \t]+\n', '\n', t)
		t = t.strip()
	return t

__all__ = ['clean_text', 'START', 'END']

