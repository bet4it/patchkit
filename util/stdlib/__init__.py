import os
import re

from util import read

__all__ = ['declare']

def declare(linker):
    if not '_terminate' in linker:
        pass
