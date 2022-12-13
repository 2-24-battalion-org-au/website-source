
import os
import json

import fetch_google_sheet

OUT='pulled.spreadsheets'

if not os.path.exists(OUT): os.mkdir(OUT)


SHEETIDS={
  'vale.master':'1DQsjA0cTUFDExU-sJiQqzm9DW64gbY2RZSy7MWymbKU',
  'battalion.rolls':'1nxXu3njSVJIg_Mve71OszVab0uj3FZsT9qCPCN8uJpI',
  'member.master':'1gb1b9t2BEtLT_NIpXwWuzKlkwf0ET_ECOypadWlqJTc',
  }

TOC={}

for id in SHEETIDS.values():
  gf=fetch_google_sheet.GSfile(id)
  sn=0
  TOC[ f'{id}' ]=gf.name
  print(f"# Loading: {id} == {gf.name}")
  for w in gf.all_sheets_return():
    sn+=1
#    print(f"  Saving: {sn} {w.name} == {OUT}/{id}--{sn}" )
    n=f'{id}--{sn:03d}.csv'
    w.save2csv(f"{OUT}/{n}")
    TOC[ n ]=w.name


#for k in sorted(TOC):
#  print(k,'=human=',TOC[k])

open(f'{OUT}/_toc_.json','w').write( json.dumps(TOC,sort_keys=True,indent=2)+'\n' )

