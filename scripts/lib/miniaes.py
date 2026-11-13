# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""AES-128 in CBC mode, as XML Encryption uses it, for the encryption sets.

Standard library only, and slow: it is meant for files of a few hundred
bytes. `encrypt()` returns what XML Encryption stores for
http://www.w3.org/2001/04/xmlenc#aes128-cbc: the 16-byte IV, then the
ciphertext of the data padded as xmlenc-core1 §5.2 says (the last byte gives
the pad length; here every pad byte holds it, which is also PKCS#7). The key
and IV are fixed by the caller, so the books stay reproducible. These are
test books: the key is no secret.
"""

from __future__ import annotations


def _xtime(a: int) -> int:
    a <<= 1
    return (a ^ 0x11B) if a & 0x100 else a


def _mul(a: int, b: int) -> int:
    r = 0
    while b:
        if b & 1:
            r ^= a
        a, b = _xtime(a), b >> 1
    return r


def _sbox() -> list[int]:
    inv = [0] * 256
    for a in range(1, 256):
        for b in range(1, 256):
            if _mul(a, b) == 1:
                inv[a] = b
                break
    box = []
    for a in range(256):
        x = inv[a]
        s = x
        for _ in range(4):
            x = ((x << 1) | (x >> 7)) & 0xFF
            s ^= x
        box.append(s ^ 0x63)
    return box


SBOX = _sbox()


def _expand(key: bytes) -> list[list[int]]:
    assert len(key) == 16
    w = [list(key[i:i + 4]) for i in range(0, 16, 4)]
    rcon = 1
    for i in range(4, 44):
        t = list(w[i - 1])
        if i % 4 == 0:
            t = [SBOX[b] for b in t[1:] + t[:1]]
            t[0] ^= rcon
            rcon = _xtime(rcon)
        w.append([a ^ b for a, b in zip(w[i - 4], t)])
    return [sum(w[r * 4:r * 4 + 4], []) for r in range(11)]


def _block(state: list[int], rk: list[list[int]]) -> list[int]:
    s = [a ^ b for a, b in zip(state, rk[0])]
    for r in range(1, 11):
        s = [SBOX[b] for b in s]
        s = [s[(i + 4 * (i % 4)) % 16] for i in range(16)]      # ShiftRows (column-major)
        if r != 10:
            m = []
            for c in range(4):
                a = s[4 * c:4 * c + 4]
                m += [_mul(a[0], 2) ^ _mul(a[1], 3) ^ a[2] ^ a[3],
                      a[0] ^ _mul(a[1], 2) ^ _mul(a[2], 3) ^ a[3],
                      a[0] ^ a[1] ^ _mul(a[2], 2) ^ _mul(a[3], 3),
                      _mul(a[0], 3) ^ a[1] ^ a[2] ^ _mul(a[3], 2)]
            s = m
        s = [a ^ b for a, b in zip(s, rk[r])]
    return s


def encrypt_block(key: bytes, block: bytes) -> bytes:
    return bytes(_block(list(block), _expand(key)))


def encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    assert len(iv) == 16
    rk = _expand(key)
    n = 16 - len(data) % 16
    data += bytes([n]) * n
    out, prev = bytearray(iv), list(iv)
    for i in range(0, len(data), 16):
        prev = _block([a ^ b for a, b in zip(data[i:i + 16], prev)], rk)
        out += bytes(prev)
    return bytes(out)
