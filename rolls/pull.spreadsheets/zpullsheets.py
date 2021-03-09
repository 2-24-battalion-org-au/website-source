import fetch_google_sheet

OUT='pulled.spreadsheets'

gf=fetch_google_sheet.GSfile("Master Vale Roll")
gf.sheet('Service Men').save2csv(OUT+'/vale.csv')
gf.sheet('Widows').save2csv(OUT+'/vale_widows.csv')
