import os
import fetch_google_sheet

OUT='pulled.spreadsheets'

if not os.path.exists(OUT): os.mkdir(OUT)


SHEETIDS={
  'vale.master':'1DQsjA0cTUFDExU-sJiQqzm9DW64gbY2RZSy7MWymbKU',
  'member.master':'1nxXu3njSVJIg_Mve71OszVab0uj3FZsT9qCPCN8uJpI',
  }


#gf=fetch_google_sheet.GSfile("Master Vale Roll")
name='vale.master'
id=SHEETIDS[name]
gf=fetch_google_sheet.GSfile(id)
gf.sheet('Service Men').save2csv(f'{OUT}/vale.csv')
gf.sheet('Widows').save2csv(f'{OUT}/vale_widows.csv')

#gf=fetch_google_sheet.GSfile("1gb1b9t2BEtLT_NIpXwWuzKlkwf0ET_ECOypadWlqJTc")
#gf.sheet('2021').save2csv(OUT+'/members.csv')

print('')
print('')
print('')
print("### pulling sheets...")
name='member.master'
id=SHEETIDS[name]
gf=fetch_google_sheet.GSfile(id)
for w in gf.all_sheets_return():
  w.save2csv(f"{OUT}/master-battalion-roll--{w.name}.csv")
