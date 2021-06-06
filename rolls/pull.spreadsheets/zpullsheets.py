import fetch_google_sheet

OUT='pulled.spreadsheets'

gf=fetch_google_sheet.GSfile("Master Vale Roll")
gf.sheet('Service Men').save2csv(OUT+'/vale.csv')
gf.sheet('Widows').save2csv(OUT+'/vale_widows.csv')

gf=fetch_google_sheet.GSfile("1gb1b9t2BEtLT_NIpXwWuzKlkwf0ET_ECOypadWlqJTc")
gf.sheet('2021').save2csv(OUT+'/members.csv')
