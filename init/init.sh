#!/usr/bin/env bash

# read the options
TEMP=`getopt -o nh --long no-venv,help -n 'init.sh' -- "$@"`
eval set -- "$TEMP"

help()
{
	echo "This installs prerequisites, gets datasets and"
	echo "tests if the installation seems to work."
	echo ""
	echo "Parameters:"
	echo "  -h|--help: print this message"
	echo "  -n|--no-venv: set this flag if you want to install stuff globally"
}

WITH_VENV=1
# extract options and their arguments into variables.
while true ; do
    case "$1" in
        -n|--no-venv) WITH_VENV=0 ; shift ;;
        -h|--help) help ; exit 0 ;;
        --) shift ; break ;;
        *) echo "Internal error!" ; help ; exit 1 ;;
    esac
done

if [ $WITH_VENV -eq 1 ]; then
	echo "> Creating virtual environment..."
	virtualenv -p python3 venv
	
	# deactivate not needed, is only in the context of this script anyway...
	source venv/bin/activate
else
	echo "> Not using virtual environment..."
	echo "  pip might need root permissions!"
fi

echo "> Installing dependencies with pip"
pip install keras tensorflow jupyter numpy pandas sklearn matplotlib

echo "> Running Python init script"
python init/init.py

echo "> Downloading GloVe embeddings (62MB)..."
wget -O datasets/glove.6B.zip https://owncloud.hpi.de/s/rQpLtl2LDlG0exL/download
cd datasets
unzip glove.6B.zip
rm glove.6B.zip

echo "> All done!"
echo "  In case you ran into errors, consult the internet or your nearest Python expert."
echo "  Ideally, you should test jupyter yourself by starting a notebook and just run some Python code."
