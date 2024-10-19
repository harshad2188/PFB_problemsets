#!/usr/bin/env python3
import re
with open("Python_07_nobody.txt","r") as input_file, open("Python_07_replaced_nobody.txt","w") as output:
    for line in input_file:
        substitute = re.sub(r"Nobody", "everybody", line)
        #print(substitute,end='',file=output)
        output.write(substitute)
