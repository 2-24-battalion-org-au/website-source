#!/bin/sh

echo ""
echo "#############################################"
echo "# vale: verifying & installing csv files"
echo "#############################################"
date
echo ""

python3 zprocess.py

echo ""
echo ""
echo "#############################################"
echo "# vale: commiting to git and website"
echo "#############################################"
echo ""

mods=""
for f in vale.csv vale_widows.csv
do
  nf=`git status | grep modified | grep "$f" | cut -d: -f 2`
  if [ "$nf" != '' ]; then
    echo "$f -> $nf"
    echo "Detected changes for: $nf"
    git log -1 "$nf"
    mods="$mods $nf"
    echo ""
  fi
done

if [ "$mods" != "" ]; then
  echo "git files changed: $mods"
  git pull
  git add $mods
  git commit -m 'vale roles updated from googlesheet' $mods
  git push
else
  echo "git files NOT changed: skipping"
fi

echo ""
echo ""
echo "#############################################"
echo "# vale: making build date"
echo "#############################################"
echo ""

if [ "$mods" != "" ]; then
  echo "git files changed... updating build date"
  cd ../../webpages

  for f in vale vale_widows
  do
    echo "writing date to $f"
    echo "...${f}_builddate.md"
    d=`git log -1 "$f.csv" | grep Date | cut -c6-`
    echo "<b>last updated:</b> $d" > "${f}_builddate.md"
  done
fi


echo ""




