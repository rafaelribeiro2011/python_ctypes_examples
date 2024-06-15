#This file will run only on Linux or a computer that has the libc.so.6 file

from ctypes import *

cdll.LoadLibrary("libc.so.6")  

libc = CDLL("libc.so.6")       
printf = libc.printf
printf(b"Hello, %s\n", b"World!")


printf(b"Hello, %S\n", "World!")


printf(b"%d bottles of beer\n", 42)