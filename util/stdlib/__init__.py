import os
import re

from util import read

__all__ = ['declare']

def declare(linker):
    if not '_terminate' in linker:
        linker.declare(headers=read('stdlib/lib43/src/io.h'))
        linker.declare(headers=read('stdlib/lib43/src/mem.h'))
        linker.declare(headers=read('stdlib/lib43/src/string.h'))
        linker.declare(headers=read('stdlib/lib43/src/syscall.h'))
        linker.declare(headers=read('stdlib/lib43/src/syscalls.h'))
        linker.autodecl(read('stdlib/lib43/src/io.c'))
        linker.autodecl(read('stdlib/lib43/src/mem.c'))
        linker.autodecl(read('stdlib/lib43/src/string.c'))
        linker.autodecl(read('stdlib/lib43/src/syscalls.c'))
        linker.declare(symbols={'syscall':
            'abi_long syscall(int n, abi_long a1, abi_long a2, abi_long a3, abi_long a4, abi_long a5, abi_long a6)'
            }, source=read('stdlib/lib43/arch/x86_64/_syscall.s'), isasm=True)
