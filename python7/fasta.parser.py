#!/usr/local/bin/python3
import re
#import fastaparser
with open("Python_07.fasta","r") as input_file:
    for line in input_file:
        line=line.rstrip()

better_variable = ['55', '32', '15']
print (better_variable)

for item in better_variable:
    print(item)