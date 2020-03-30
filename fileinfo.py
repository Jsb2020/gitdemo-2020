#第一次编辑

from _future_ import print_function

#第二次修改
import os
import stat
import sys
import time

#第三次修改
if sys.version_info >= (3,0):
    raw_input = input

#第四次修改
file_name = raw_input("Enter a file name: ")

#第五次修改
count = 0
t_char = 0
try:
    with open(file_name) as f:
        line = f.readline()
        t_char += len(line)
        while line:
            count += 1
            line = f.readline()
            t_char += len(line)
except FileNotFoundError as e:
    print(e)
    sys.exit()