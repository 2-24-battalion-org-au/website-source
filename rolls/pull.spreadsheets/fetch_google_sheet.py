import csv

import sys
sys.path.append('lib')
print('# starting')
import gspread

import common

class GSsheet:
  def __init__(self,file,name):
    self.name=name
    self.file=file
    print('# opening sheet',name)
    self.gsheet=self.file.gfile.worksheet(name)
    print('# opening sheet done',name,self.gsheet)
  def save2csv(self,fn):
    all=self.gsheet.get_all_values()
    print('# saving sheet',self.name,fn)
    with open(fn,'w') as cfile:
      cw=csv.writer(cfile,quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
      for i in all:
        cw.writerow(i)
    print('# saved')

class GSfile:
  def __init__(self,name):
    print('# connecting to api')
    self.gapi=gspread.service_account(filename=common.SECRET)
    try:
      print('# opening file by name',name)
      self.gfile=self.gapi.open(name)
    except:
      print('# opening file by key',name)
      self.gfile=self.gapi.open_by_key(name)
  def sheet(self,name):
    return GSsheet(self,name)

