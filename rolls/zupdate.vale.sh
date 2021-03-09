#!/bin/sh

OUT='/nas/1t-mirror/korg/sites/appengine/2-24.battalion.org.au/www/.build.txt'


echo "[BEGIN]" > $OUT


cd pull.spreadsheets
sh ./zrun.sh  >> $OUT 2>&1


cd ..


cd vale.verify.install
sh ./zrun.sh  >> $OUT 2>&1


echo "[DONE]" >> $OUT
date >> $OUT


