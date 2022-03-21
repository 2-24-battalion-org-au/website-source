import os
import fetch_google_sheet

OUT='pulled.spreadsheets'

if not os.path.exists(OUT): os.mkdir(OUT)

gf=fetch_google_sheet.GSfile("Master Vale Roll")
gf.sheet('Service Men').save2csv(OUT+'/vale.csv')
gf.sheet('Widows').save2csv(OUT+'/vale_widows.csv')

#gf=fetch_google_sheet.GSfile("1gb1b9t2BEtLT_NIpXwWuzKlkwf0ET_ECOypadWlqJTc")
#gf.sheet('2021').save2csv(OUT+'/members.csv')


gf=fetch_google_sheet.GSfile("1nxXu3njSVJIg_Mve71OszVab0uj3FZsT9qCPCN8uJpI")
for w in gf.all_sheets_return():
  print(w)
  w.save2csv("{OUT}/master-battalion-roll--{w.name}.csv".format(OUT=OUT,w=w))
