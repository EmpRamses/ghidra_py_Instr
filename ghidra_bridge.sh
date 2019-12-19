#!/bin/zsh
# Clone the repo to the host where the ghidra and binary files are located
# git clone https://github.com/justfoxing/ghidra_bridge.git
# Then run this script with as follow.
# The first three arguments are not required. They can be set up as default.
# ./ghidra_bridge.sh -p path_to_project -b path_to_binary_directory -m project_name -n binary_name

# Default paths & names
GHIDRA_PATH=~/Code/ghidra_9.2_DEV
SCRIPT_PATH=~/Code/ghidra_bridge        # The script path is the root directory of ghidra_bridge
PROJECT_PATH=~/Code/GhidraProjects/tmp
PROJECT_NAME=tmp
BINARY_PATH=~/Code/GhidraProjects

while getopts 'p:b:m:n:' arg;
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
    esac
done

shift $(($OPTIND-1))

rm -rf $PROJECT_NAME.gpr $PROJECTNAME.rep

time $GHIDRA_PATH/support/analyzeHeadless $PROJECT_PATH $PROJECT_NAME -import $BINARY_PATH/$BINARY_NAME -scriptPath $SCRIPT_PATH -postscript ghidra_bridge_server.py
