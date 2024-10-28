#!/usr/bin/env python3
import re
#question 3
with open("ecoli_0.25.contigs.fasta","r") as input_file:
    for line in input_file:
        fasta = re.search(r"(^>\S+\s*.*)", line) # this pattern will identify line starting only with >
        if fasta: # if it finds fasta only then it will move to print
            print(fasta.group(1)) # group(1) will get rid of the object, span etc in the print output

