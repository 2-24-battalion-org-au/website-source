#!/bin/sh

echo ""
echo "#############################################"
echo "# vale: pulling google sheets to csv files"
echo "#############################################"
date
echo ""

python3 zpullsheets.py
