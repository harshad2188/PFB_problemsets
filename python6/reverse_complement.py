#!/usr/bin/env python3
genes = {}
with open("Python.06.seq.txt","r") as seq_read, open("reverse.complement.seq.txt","w") as seq_write:
                                                    
    for line in seq_read:
        gene_id,seq = line.split()
        rev = (seq[::-1])
        rev = rev.replace('A','t')
        rev = rev.replace('T','a')
        rev = rev.replace('G','c')
        rev = rev.replace('C','g')
        print(f'>{gene_id} reverse complement sequence\n{rev.upper()}', file = seq_write)


