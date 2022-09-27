#!/bin/sh

OUT="../webpages/.build.txt"

echo "[BEGIN]" > "$OUT"

git log -1 | cat
echo "RV: $?"

cd pull.spreadsheets
sh ./zrun.sh  >> "../$OUT" 2>&1
echo "RV: $?"


cd ..


cd vale.verify.install
sh ./zrun.sh  >> "../$OUT" 2>&1
echo "RV: $?"


cd ..


echo "[DONE]" >> "$OUT"
date >> "$OUT"


git log -1 | cat
echo "RV: $?"
