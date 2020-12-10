

import csv

OURS={}
DVA={}

fname='../../webpages/rolls/battalion-all.csv'
with open(fname) as f:
  reader=csv.reader(f)
  header=[]
  for sl in reader:
    if len(header)<2:
      header.append(sl)
    else:
      OURS[sl[2]]=sl


fname='../dva-ww2rolls/ww2roll.gov.au.csv'
with open(fname) as f:
  reader=csv.reader(f)
  header=[]
  for sl in reader:
    if len(header)<0:
      header.append(sl)
    else:
      DVA[sl[0]]=sl


