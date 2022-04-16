def xor(data: bytes, key: bytes) -> bytes:
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, key])))
