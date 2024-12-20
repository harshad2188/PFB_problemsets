#!/bin/sh


#  Path to Canu.

bin="/Users/pfb2024/PFB_problemsets/genomeassembly/canu-2.2/bin"

#  Report paths.

echo ""
echo "Found perl:"
echo "  " `which perl`
echo "  " `perl --version | grep version`
echo ""
echo "Found java:"
echo "  " `which java`
echo "  " `java -showversion 2>&1 | head -n 1`
echo ""
echo "Found canu:"
echo "  " $bin/canu
echo "  " `$bin/canu -version`
echo ""


#  Environment for any object storage.

export CANU_OBJECT_STORE_CLIENT=
export CANU_OBJECT_STORE_CLIENT_UA=
export CANU_OBJECT_STORE_CLIENT_DA=
export CANU_OBJECT_STORE_NAMESPACE=
export CANU_OBJECT_STORE_PROJECT=




#  Discover the job ID to run, from either a grid environment variable and a
#  command line offset, or directly from the command line.
#
if [ x$CANU_LOCAL_JOB_ID = x -o x$CANU_LOCAL_JOB_ID = xundefined -o x$CANU_LOCAL_JOB_ID = x0 ]; then
  baseid=$1
  offset=0
else
  baseid=$CANU_LOCAL_JOB_ID
  offset=$1
fi
if [ x$offset = x ]; then
  offset=0
fi
if [ x$baseid = x ]; then
  echo Error: I need CANU_LOCAL_JOB_ID set, or a job index on the command line.
  exit
fi
jobid=`expr -- $baseid + $offset`
if [ x$baseid = x0 ]; then
  echo Error: jobid 0 is invalid\; I need CANU_LOCAL_JOB_ID set, or a job index on the command line.
  exit
fi
if [ x$CANU_LOCAL_JOB_ID = x ]; then
  echo Running job $jobid based on command line options.
else
  echo Running job $jobid based on CANU_LOCAL_JOB_ID=$CANU_LOCAL_JOB_ID and offset=$offset.
fi

bgnid=0
endid=0

if [ $jobid -eq 1 ] ; then
  jobid=0001
  bgnid=1
  endid=10728
fi
if [ $jobid -eq 2 ] ; then
  jobid=0002
  bgnid=10729
  endid=12528
fi

if [ $bgnid -eq 0 ]; then
  echo Error: Invalid job $jobid requested, must be between 1 and 2.
  exit 1
fi


if [ -e ./results/$jobid.cns ] ; then
  echo Job finished successfully.
  exit 0
fi

if [ ! -d ./results ] ; then
  mkdir -p ./results
fi




seqStore=../../ecoli.seqStore

$bin/falconsense \
  -S $seqStore \
  -C ../ecoli.corStore \
  -R ./ecoli.readsToCorrect \
  -r $bgnid-$endid \
  -t  4 \
  -cc 4 \
  -cl 1000 \
  -oi 0.75 \
  -ol 500 \
  -p ./results/$jobid.WORKING \
  -cns \
  > ./results/$jobid.err 2>&1 \
&& \
mv ./results/$jobid.WORKING.cns ./results/$jobid.cns \

