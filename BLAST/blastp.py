#!/usr/bin/env python3
import subprocess
import sys
import datetime 

# help message
if len(sys.argv) < 4:
    print(f'Usage: {sys.argv[0]}   <query protein fasta>  <formatted database>  <min E-value>')
    exit(1)
# get cmd line params
query = sys.argv[1]
db = sys.argv[2]
evalue = float(sys.argv[3]) # immediately convert to appropriate type

if not query.endswith( ('.fa','.fasta') ):
    print('Query input file needs to end with .fa or .fasta')
    exit(12)

# 2019-10-23 13:49:27.232603
now = str(datetime.datetime.now())
# cut down to 2019-10-23 13:49
now = now[0:16]

#log run command and time/date to screen
print('#' , ' '.join(sys.argv))
print('#' , 'was run on', now)

#generate output file
out = query + '.blastp.out'

# run the command
blastcmd = f'blastp -query {query} -db {db} -outfmt 7 -out {out} -evalue {evalue}'

# object is returned after run command
blastcmd_run = subprocess.run(blastcmd, shell=True , stdout = subprocess.PIPE, stderr=subprocess.PIPE)

# Now we need to check the UNIX return code
# always do this!
# 0 = success
# non-zero =failure
if blastcmd_run.returncode != 0:
    print("FAILED!")
    exit(2)

# now parse results, 
homologs = {}
with open(out,'r') as blast_results:
    for line in blast_results:
        line = line.rstrip()
        if line.startswith('#'): # skip comment lines
            continue
        fields = line.split('\t')
        query = fields[0]
        subject = fields[1]
        evalue = float(fields[10]) # this will be a string because 
                            # we read in from a file
                            # don't forget to convert to float
        # collect hits and evalues into dictionary
        if query not in homologs:
            homologs[query] = [ (subject, evalue) ]
        else:
            homologs[query].append( (subject,evalue) )

print('Hit summary')
for query in sorted(homologs):
    print('Query:',query)
    for data in homologs[query]:
        query,evalue = data
        print(f'{query} E-value={evalue}' )

