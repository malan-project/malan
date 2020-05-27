import sys
import hashlib
def sha512(stream):
    hashfn = hashlib.sha512()
    while True:
        chunk = stream.read(hashfn.block_size)
        if not chunk:
            break
        hashfn.update(chunk)
    return hashfn.hexdigest()
