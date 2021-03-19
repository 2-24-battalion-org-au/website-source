#!/bin/sh

OUT="../webpages/.build.txt"

echo "[BEGIN]" > "$OUT"


cd pull.spreadsheets
sh ./zrun.sh  >> "../$OUT" 2>&1


cd ..


cd vale.verify.install
sh ./zrun.sh  >> "../$OUT" 2>&1


cd ..


echo "[DONE]" >> "$OUT"
date >> "$OUT"


