import sys
import hashlib
def sha512(path):
    h = hashlib.sha512()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
        return h.hexdigest()
