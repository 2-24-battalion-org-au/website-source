
import os
import csv
import datetime
import shutil


import all224

MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December']
MONTHS3letter={ m[:3]:m for m in MONTHS }
MONTHS3letter[MONTHS[9-1][:4]]=MONTHS[9-1]
del MONTHS3letter['May']

SERVICE='EF NX QX SX TX VX WX'.split()

GENOUT='../pull.spreadsheets/pulled.spreadsheets'


def get_latest(base=GENOUT):
  for f in os.listdir(base):
    print('')
    print('')
    print('####',f)
    if f=='zsync.sh':
      pass
    elif f.endswith('.csv'):
      if f=="members.csv":
        pass
      elif f=="vale.csv":
        Google_Soldiers(base+'/'+f)
        install(base,f,'../../webpages/vale.csv')
      elif f.endswith("vale_widows.csv"):
        Google_Widows(base+'/'+f)
        install(base,f,'../../webpages/vale_widows.csv')
    else:
      print("ERROR: dont know how to deal with this file",f)
      raise Exception

def install(srcd,fn,dstpath):
  print('>>>>> install  "%s/%s" %s'%(srcd,fn,dstpath))
  shutil.copy2(srcd+'/'+fn,dstpath)


class Google_Soldiers:

  def check_servicenum(self,sl,snum):
    notin=[]
    if snum not in all224.OURS:
      notin.append('224')
    if snum not in all224.DVA:
      notin.append('dva')
    if notin:
      self.INFO("vet not found in %7s : %s %s"%('+'.join(notin),snum,sl))

  def check_date(self,sl,sdate):
    if len(sdate)==1:
      self.WARN(". Year only",sl)
      int(sdate[0])
      return [ sdate[0] ]
    # must be m+y or d+m+y
    if sdate[-2] in MONTHS3letter:
      self.INFO("... (fixed) abbrev Mnth",sl)
      sdate[-2]=MONTHS3letter[sdate[-2]]
    if sdate[-2] not in MONTHS:
      self.ERROR("!!! BAD!!! Month error",sl)
    if len(sdate)==2:
      self.WARN(". Month+Year only",sl)
      int(sdate[-1])
      return sdate
    if len(sdate)==3:
      int(sdate[0])
      int(sdate[-1])
      return sdate
    self.ERROR("BAD! Dont know date format",sl)
    raise Exception

  def INFO(self,msg,*args):
    print('#.....:'+msg,args)
  def WARN(self,msg,*args):
    print('#!WARN:'+msg,args)
  def ERROR(self,msg,*args):
    print('###ERR:'+msg,args)



  def __init__(self,f):
    self.rows=[]
    self.pyr=None
    self.pdate=None
    with open(f) as fileread:
      csvreader=csv.reader(fileread)
      for l in csvreader:
        self.rows.append( self.process_excel( l ) )

  def process_excel(self,l):
    snum=None
    if l==['','','']:
      pass
    elif l[0].startswith('>##WARNING'):
      pass
    elif l[0].startswith('>## '):
      nyr=int(l[0][-4:])
      if self.pyr and nyr>=self.pyr:
        self.ERROR('year out of order',l,nyr,self.pyr)
      self.pyr=nyr
      self.pdate=datetime.date(self.pyr,12,31)
    else:
      date=l[2]
      snum=l[1]
      name=l[0]
      ndatetxt=self.check_date(l,date.split())
      if len(ndatetxt)==3: ndate=datetime.date(int(ndatetxt[-1]),1+MONTHS.index(ndatetxt[-2]),int(ndatetxt[-3]))
      elif len(ndatetxt)==2: ndate=datetime.date(int(ndatetxt[-1]),1+MONTHS.index(ndatetxt[-2]),1)
      elif len(ndatetxt)==1: ndate=datetime.date(int(ndatetxt[-1]),1,1)
      else: self.ERROR('cant parse date')
      if self.pdate and ndate>self.pdate: self.WARN('dates out of order',l)
      self.pdate=ndate
      self.check_servicenum(l,snum)



class Google_Widows(Google_Soldiers):

  def MOO(self):
    if date=='n.d.':
      self.INFO("fixing n.d. to %s"%(self.noteyear),[name,vet,date])
      date=self.noteyear
    date=self.check_date(   [name,vet,date],date.strip().split()   )

    vet=vet.split()
    vetn=vet[:-1]
    vetsnum=vet[-1]
    if vetsnum!=vetsnum.upper():
      self.INFO("fixed lower case vet serial",name,vet,date)
      vetsnum=vetsnum.upper()
    if vetsnum[:2] not in SERVICE:
      self.ERROR("bad vet snumber",name,vet,date)
    self.check_servicenum(vetn,vetsnum)
    out=[name,vetsnum,vetn,date]
    return out



  def process_excel(self,l):
    snum=None
    l=[ s.strip() for s in l ]
    print("Processing",[l])
    if l==['','','']:
      pass
    elif l[0].startswith('>##WARNING'):
      pass
    elif l[0].startswith('>## '):
      nyr=int(l[0][-4:])
      if self.pyr and nyr>=self.pyr:
        self.ERROR('year out of order',l,nyr,self.pyr)
      self.pyr=nyr
      self.pdate=datetime.date(self.pyr,12,31)
    else:
      date=l[2]
      vet=l[1]
      if vet.startswith('[') and vet.endswith(']'):
        pass
      else:
        self.ERROR('no [] in vet name',l)
      name=l[0]

      snum=vet[1:-1].split()[-1]
      ndatetxt=self.check_date(l,date.split())
      if len(ndatetxt)==3: ndate=datetime.date(int(ndatetxt[-1]),1+MONTHS.index(ndatetxt[-2]),int(ndatetxt[-3]))
      elif len(ndatetxt)==2: ndate=datetime.date(int(ndatetxt[-1]),1+MONTHS.index(ndatetxt[-2]),1)
      elif len(ndatetxt)==1: ndate=datetime.date(int(ndatetxt[-1]),1,1)
      else: self.ERROR('cant parse date')
      if self.pdate and ndate>self.pdate: self.WARN('dates out of order',l)

      self.pdate=ndate
      self.check_servicenum(l,snum)



if __name__=="__main__":
  get_latest()
