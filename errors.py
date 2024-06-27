#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil perdir perdão do que permissão)


try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))


try:
    raise ValueError
finally:
    print("Execute isso sempre!")



try:
    names = open("names.txt").readlines() # FileNotFoundError
    1/1 #ZeroDivisionError
#    print(names.banana) #AttributeError
    print(names.append) #AttributeError
except FileNotFoundError as e: #Bare except
    print(f"{str(e)} Missing name in the list")
    sys.exit(1)
    # TODO: usar retry
except ZeroDivisionError:
    print("[Error] You cant divide by zero")
    sys.exit(1)
except (ZeroDivisionError, AttributeError):
    print("[Error] List doesn't have banana")
    sys.exit(1)
else:
    print("Sucesso!")
finally:
    print("Execute isso sempre!")


try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
    
print(names[2])