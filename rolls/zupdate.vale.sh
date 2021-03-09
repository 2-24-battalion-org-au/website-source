#!/bin/sh

OUT='/nas/1t-mirror/korg/sites/appengine/2-24.battalion.org.au/www/.build/'


echo "[BEGIN]" > $OUT/index.html
date >> $OUT/index.html

echo "Pulling google sheets...."  >> $OUT/index.html
echo "" >> $OUT/index.html
echo "" >> $OUT/index.html

cd pull.spreadsheets
python3 zpullsheets.py   >> $OUT/index.html 2>&1

echo "" >> $OUT/index.html
echo "----------------------" >> $OUT/index.html
echo "" >> $OUT/index.html

echo "Pulling google sheets...." >> $OUT/index.html
echo "" >> $OUT/index.html
echo "" >> $OUT/index.html

cd ..
cd vale.verify.install
python3 zprocess.py    >> $OUT/index.html y 2>&1


echo "[DONE]" >> $OUT/index.html
date >> $OUT/index.html


