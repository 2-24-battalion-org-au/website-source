import csv

import sys,os
libpath=os.path.join( os.path.dirname(os.path.abspath(__file__)), 'lib' )
sys.path.append(libpath)
print('# starting')
import gspread

import common

class GSsheet:
  def __init__(self,file,gsheet):
    self.gsheet=gsheet
    self.name=gsheet.title
    self.file=file
  def clear(self):
    self.gsheet.clear()
  def update(self,pos,data,style={},**kw):
    print(dir(self.gsheet.update))
    print(dir(self.gsheet.__doc__))
    print('writing',pos,data,kw)
    self.gsheet.update(pos,data,**kw)
    if style: self.style(pos,style)
  def getrgb(self,rgb):
    rv={}
    if rgb.startswith('#'): rgb=rgb[1:]
    COLORNAMES=['red','green','blue']
    COLORINFO={ 3:{ "steps":(0,1,2), 'stride':1, 'div':15},
                6:{ "steps":(0,2,3), 'stride':2, 'div':255}, }
    info=COLORINFO[len(rgb)]
    for c in info['steps']:
      colstr=rgb[c:c+info['stride']]
      colfloat=float( int(colstr,16) / info['div'] )
      rv[ COLORNAMES[c//info['stride']] ]=colfloat
    return rv
  def style(self,pos,style):
    # see
    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#cellformat
    s=style.copy()
    if '.fg' in s:
      if 'textFormat' not in s: s['textFormat']={}
      s['textFormat']['foregroundColor']=self.getrgb(s['.fg'])
      del s['.fg']
    if '.bg' in s:
      s['backgroundColor']=self.getrgb(s['.bg'])
      del s['.bg']
    self.gsheet.format(pos,s)
  def fetch2csv(self):
    return self.gsheet.get_all_values()
  def save2csv(self,fn):
    all=self.fetch2csv()
    print(f'#     saving:   {self.name}')
    with open(fn,'w') as cfile:
      cw=csv.writer(cfile,quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
      for i in all:
        cw.writerow(i)
    print(f'#   saved to:   {fn}')

class GSfile:
  def __init__(self,name):
    print(  f'# connecting to sheet.api: {name}')
    self.gapi=gspread.service_account(filename=common.SECRET)
    try:
      self.gfile=self.gapi.open_by_key(name)
      print(f'#  opened file by key')
    except:
      self.gfile=self.gapi.open(name)
      print(f'#  opened file by name')
    print(  f"#  sheet.title: {self.gfile.title}")
  def sheet(self,name):
    gsheet=self.gfile.worksheet(name)
    return GSsheet(self,gsheet)
  def sheet_new(self,name,rows="1",cols="20"):
    gsheet=self.gfile.add_worksheet(name,rows=rows,cols=cols)
    return GSsheet(self,gsheet)
  def del_worksheet(self,sheet):
    self.gfile.del_worksheet(sheet)
  def all_sheets(self):
    return self.gfile.worksheets()
  def all_sheets_return(self):
    rv=[]
    for w in self.all_sheets():
      rv.append( GSsheet(self,w) )
    return rv
