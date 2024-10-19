#!/usr/bin/env python3
line_count = 0
total_nts = 0
with open("Python_06.fastq","r") as input_file:
    for line in input_file:
        nt_count = len(line)
        total_nts += nt_count
        print(f"line count: {line_count}")
        line_count +=1
        print(f"line count + 1: {line_count}")
        print(nt_count)
        print(nt_count/line_count)
