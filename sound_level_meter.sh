#!/bin/dash

if [ "$1" = "config" ]; then
	echo "graph_title Sound level"
	echo "graph_category xopts"
	echo "soundlevel.label dBSPL"
	exit 0
fi

if [ -e /tmp/8a32ada4c3e0c1f0.csv ]; then
	value=$(cut -f 2 /tmp/8a32ada4c3e0c1f0.csv)
	echo "soundlevel.value ${value}"	
	exit 0
else
	echo "csv file does not exist."
	exit 1
fi
