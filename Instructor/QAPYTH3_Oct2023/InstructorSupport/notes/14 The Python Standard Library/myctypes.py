#! /usr/bin/python

from ctypes import *

msvcrt = cdll.msvcrt

text = "Hollow World!\n"
msvcrt.printf("%s", text)

mydll = cdll.LoadLibrary("C:\QA\Win32\wn32prg2\Goodies\DllTest\Dlltest\Debug\DllModule7")

mydll.DllFunc7()
