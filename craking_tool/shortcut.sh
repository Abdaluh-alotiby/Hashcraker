#!/bin/ash


RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

current_directory=$(pwd)
echo "Current working directory: $current_directory"

if [ -e "main.py" ]; then
    mv main.py /bin/main.py
    echo "File successfully moved to /bin/"
else
    echo -e "${RED}Failed file [ main.py] does not exist.${NC}"
fi
echo "alias hashcraker='python3 /bin/main.py'" >> ~/.profile
echo 'you can run script useing hashcraker'
