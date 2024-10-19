#!/usr/bin/env python3
import re
with open("Python_07.fasta","r") as input_file:
    for line in input_file:
        fasta = re.search(r"^>(\S+)\s(.*)",line)
        if fasta:
            print(f"id: {fasta.group(1)},\ndesc: {fasta.group(2)}")
