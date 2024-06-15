#This file will run only on Windows or a computer that has Microsoft Visual C++

from ctypes import *
print(windll.kernel32)  

print(cdll.msvcrt)      

libc = cdll.msvcrt
printf = libc.printf
printf(b"Hello, %s\n", b"World!")


printf(b"Hello, %S\n", "World!")


printf(b"%d bottles of beer\n", 42)


printf(b"%f bottles of beer\n", 42.5)