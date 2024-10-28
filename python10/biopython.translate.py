#!/usr/bin/env python3
from Bio import SeqIO
import argparse
def main():
    '''Main'''
    parser = argparse.ArgumentParser(description='extract sequences')
    parser.add_argument('fasta')
    args = parser.parse_args()
    out_fh=open("protein_seq.txt","w")

    for seq_record in SeqIO.parse(args.fasta, 'fasta'):
        protein = seq_record.translate()
        #print(seqobj[0:10])
        #print(protein, file=output)
        print(str(protein.seq), file=out_fh)

if __name__ == '__main__':
    main()
    