#!/bin/bash

# Use Gnu find to make a list of Mail messages that have been modified since
# the last time that this was run.
# Bryan Miller
# Gnu find can be installed with 'brew install findutils'

now=`date -u "+%Y-%m-%d %H:%M:%S"`" UTC"
#echo $now

MPATH=$HOME"/Library/Mail/V5/"

# File containing the time of the last time run
timefile=$HOME"/.last_findmails"

# Create the file if it doesn't exist
if [ ! -f $timefile ]; then
	echo "2000-01-01 00:00:00 UTC" > $timefile
fi

# Read timestamp of last time run
read -r prevtime < $timefile
#prevtime="2021-01-28 23:30:00 UTC"
#echo $prevtime

# Run find
cd "$MPATH"
#files=`find . -type f -newermt '2021-01-28 20:30:00' -name *.emlx`
files=`/usr/local/bin/gfind . -type f -newermt "$prevtime" -path "*/All\ Mail.mbox/*" -name "*.emlx" -printf "%p::" | sed "s/::$//"` 

echo $files

# Use the -n command line flag to avoid updating the timestamp (trial run)
if [ $1 != "-n" ]; then
	echo $now > $timefile
fi

# Test of splitting the list by delimiter '::'
# IFS="::"
# arrFiles=$files
# #echo ${arrFiles[1]}
# 
# for f in $arrFiles
# do
# 	echo "$f"
# 	#file=$( echo ${f##/*/} )
# 	id0=`basename "$f" .emlx`
# 	id=`basename "$id0" .partial`
# 	echo $id
# 	#grep mailTagsKeyWords $f
# done
# unset IFS
