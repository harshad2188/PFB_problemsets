#!/usr/bin/env python3
import re
#question 3
Counter = 0
contig_list = {}
with open("ecoli_0.25.contigs.fasta","r") as input_file:
    for line in input_file:
        line = line.rstrip()
        fasta = re.search(r"(^>\S+\s*.*)", line) # this pattern will identify line starting only with >
        if fasta: # if it finds fasta only then it will move to print
            header = fasta.group(1)
            contig_list[header] = ""    
            print(fasta.group(1)) # group(1) will get rid of the object, span etc in the print output
            Counter +=1 
        else:
            contig_list[header] = line
            #print(line)    
    #print(Counter)
    print(contig_list)
    
