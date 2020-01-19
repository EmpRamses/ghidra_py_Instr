#!/usr/bin/env bash

set -x

# Default paths & names
GHIDRA_PATH=~/repos/ghidra_9.2_DEV
SCRIPT_PATH=$(cd "$(dirname "$0")";pwd)        # The script path is the root directory of ghidra_bridge
PROJECT_PATH=~/repos/GhidraProjects/tmp
PROJECT_NAME=tmp
BINARY_PATH=~/repos/GhidraProjects

while getopts 'p:b:m:n:o:' arg;
do
    case $arg in
        p)
            PROJECT_PATH="$OPTARG";;
        b)
            BINARY_PATH="$OPTARG";;
        m)
            PROJECT_NAME="$OPTARG";;
        n)
            BINARY_NAME="$OPTARG";;
        o)
            OUTPUT_PATH="$OPTARG";;
    esac
done

shift $(($OPTIND-1))

echo $OUTPUT_PATH

rm -rf $PROJECT_PATH/$PROJECT_NAME.gpr $PROJECT_PATH/$PROJECT_NAME.rep

time $GHIDRA_PATH/support/analyzeHeadless $PROJECT_PATH $PROJECT_NAME -import $BINARY_PATH/$BINARY_NAME -scriptPath $SCRIPT_PATH -postScript asm_exporter.py $OUTPUT_PATH
