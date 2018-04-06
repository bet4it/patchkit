from util import stdlib
from util import crypto

__all__ = ['declare']

def declare(linker):
    stdlib.declare(linker)
    crypto.declare(linker)
