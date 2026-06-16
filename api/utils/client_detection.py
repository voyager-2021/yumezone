import re
import os

REQUIRE_USER_AGENT = os.getenv("REQUIRE_USER_AGENT", "0") == "1"
BLOCK_USER_AGENTS = os.getenv("BLOCK_USER_AGENTS", "0") == "1"

BLOCKED_USER_AGENT_PATTERNS = [
    r"\bheadless(?:chrome)?\b",
    r"\bphantomjs?\b",
    r"\bselenium\b",
    r"\bpuppeteer\b",
    r"\bplaywright\b",
    r"\bwpdt\b",
    r"\bwebdriver\b",
    r"\bpython-requests\b",
    r"\bgo-http-client\b",
    r"\bcurl\b",
    r"\bwget\b",
    r"\bscrapy\b",
    r"\bhttpclient\b",
    r"\blibwww\b",
    r"\bjakarta\b",
    r"\bhttpx\b",
]


def is_obvious_bot_user_agent(user_agent):
    """Return True only for clearly automated or non-browser user agents."""
    ua = (user_agent or "").strip().lower()
    if not ua:
        if not REQUIRE_USER_AGENT:
            return False
        return True
    if not BLOCK_USER_AGENTS:
        return False
    return any(re.search(pattern, ua) for pattern in BLOCKED_USER_AGENT_PATTERNS)
