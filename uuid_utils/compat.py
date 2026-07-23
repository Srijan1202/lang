"""Compatibility helpers used by langchain_core on this workspace."""

from __future__ import annotations

import os
import time
import uuid


def uuid7(timestamp: int | None = None, nanos: int = 0) -> uuid.UUID:
    """Return a UUIDv7-like value without requiring the Rust extension.

    The implementation follows the RFC 9562 field layout closely enough for
    LangChain's tracing and callback identifiers.
    """

    if timestamp is None:
        unix_ns = time.time_ns()
        timestamp, nanos = divmod(unix_ns, 1_000_000_000)

    unix_ms = timestamp * 1000 + nanos // 1_000_000
    unix_ms &= (1 << 48) - 1

    random_bytes = os.urandom(10)
    rand_a = int.from_bytes(random_bytes[:2], "big") & 0x0FFF
    rand_b = int.from_bytes(random_bytes[2:], "big") & ((1 << 62) - 1)

    value = unix_ms << 80
    value |= 0x7 << 76
    value |= rand_a << 64
    value |= 0x2 << 62
    value |= rand_b
    return uuid.UUID(int=value)