import csv

CSVDIR='../webpages/rolls/'

## put battalion all first!!
CONVERT=[ ( 'battalion-all', 2 ),
          ( 'battalion-overseas', 0 ),
          ( 'casualties', 2 ),
          ( 'kia', 2 ),
          ( 'pow', 2 ),
        ]

WW2ROLLSCSV='ww2roll.gov.au.csv'[:-4]
SNSTARTS=['nx','vx','qx','sx','tx','wx']



class   Person:
  def   __init__(self):
    self.surname=None
    self.servicenumber=None
    self.givennames=None
    self.files=[]
  def   __repr__(self):
    return "Person( %s,%s :  %s )"%( self.servicenumber,self.surname,', '.join( [ '%s@%s'%(f,n) for f,n in self.files]) )



class   Roll:
  def   __init__(self,meta,fn,skip=0):
    self.meta=meta
    self.fname=fn
    self.skip=skip
    self.keys={}
    self.rows=[]
    with open(self.fname+'.csv','r') as csvfile:
      for i in range(0,self.skip):
        l=csvfile.readline()
      spamreader = csv.reader(csvfile)
      for origr in spamreader:
        r=[ i.strip() for i in origr ]
        self.rows.append( r )
    print('# .. ',self.fname,'rows=',len(self.rows))
    for k in self.rows[0]:
      k=k.lower().replace(' ','').replace('_','')
      self.keys[k]=len(self.keys)
    del self.rows[0]
  def   item(self,row,what):
    return row[ self.keys[what] ].lower()

  def   err(self,lineno,what,row,obj=None):
    self.log('ERROR',lineno,what,row,obj=None)
  def   warn(self,lineno,what,row,obj=None):
    self.log('warn ',lineno,what,row,obj=None)
  def   log(self,premsg,lineno,what,row,obj=None):
    print('%s:   %s@%s:    %s'%(premsg,self.fname,lineno,what))
    if row: print('      %s'%(row))
    if obj: print('      %s'%(obj))




class   Meta:
  def   __init__(self):
    self.alldb=[]
    self.rows=[]
    self.by_servicenumber={}
    self.by_surname={}
    self.govdb={}
    #
    self.load()
    self.verify()
    self.verify_us_vs_gov()


  def   err(self,what,row,obj=None):
    self.log('ERROR',what,row,obj)
  def   warn(self,what,row,obj=None):
    self.log('warn ',what,row,obj)
  def   log(self,premsg,what,row,obj=None):
    print('%s:   %s:    %s'%(premsg,'main',what))
    if row: print('      %s'%(row))
    if obj: print('      %s'%(obj))


  def verify(self):
    for sn in self.by_servicenumber:
      our=self.by_servicenumber[sn]
      seen=[]
      for fn,ln in our.files:
        if fn in seen: self.err('duplicate in servicenumber file: '+fn,None,our)
        else: seen.append(fn)


  def verify_us_vs_gov(self):
    print('')
    print('')
    print('## checking vs gov servicenumbers')
    print(self.govdb['vx94591'])
    print(self.by_servicenumber['vx94591'])
    print(self.by_servicenumber['vx94591'].__dict__)
    print('## checking vs gov servicenumbers')
    print('')
    print('')
    print("##### not in govdb")
    n=0
    for sn in self.by_servicenumber:
      our=self.by_servicenumber[sn]
      if sn not in self.govdb:
        print("not in govDB",sn)
        print("    %s"%(our.__dict__))
        n+=1
    print('found %s errors  in ourdb  but  not in govDB'%(n))
    print('')
    print('')
    print("##### not in ourdb")
    n=0
    for sn in self.govdb:
      gov=self.govdb[sn]
      if sn not in self.by_servicenumber:
        print("not in OURDB:",sn)
        print("    %s"%(gov))
        n+=1
    print('found %s errors  not in ourdb  but  in govDB'%(n))
    print('')
    print('')
    #
    print("##### checking in both")
    for sn in self.by_servicenumber:
      our=self.by_servicenumber[sn]
      if sn in self.govdb:
        gov=self.govdb[sn]
        our_pow=sum( [ f.endswith('pow') for f,l in our.files ] ) != 0
        our_kia=sum( [ f.endswith('kia') for f,l in our.files ] ) != 0
        m=[]
        if not our_pow and gov['pow']:
          m.append('ERROR: gov pow but not ours')
        elif our_pow and not gov['pow']:
          m.append('ERROR: our pow but not gov')
        if not our_kia and gov['died']:
          m.append('ERROR: gov DIED but not ours')
        elif our_kia and not gov['died']:
          m.append('ERROR: our DIED but not gov')
        if m:
          print()
          print(our)
          print(gov)
          for a in m:
             print('    %s'%(m))

  def process_gov(self,db):
    t=0
    n=0
    for r in db.rows:
      n=n+1
      snum=r[0].lower()
      snum_valid=sum( [ snum.startswith( bit ) for bit in SNSTARTS] )
      if not snum_valid:
        db.warn(n,'service number doesnt look valid %s'%(snum),r)
      rv={   '@':n,
             'num':db.item(r,'servicenumber'),
             'sname':db.item(r,'lastname'),
             'names':[ db.item(r,'firstname'), db.item(r,'secondname'), db.item(r,'thirdname') ],
             'pow':db.item(r,'prisonerofwar'),
             'died':db.item(r,'deathinservicedate'),
             'unit':db.item(r,'unittypefullname'),
          }
      if rv['pow']=='n': rv['pow']=False
      if rv['died']=='null': rv['died']=False
      self.govdb[ rv['num'] ]=rv
      t+=1
    print('## gov.total lines parsed',t)
    print('## gov.total people found',len(self.rows))


  def load(self):
    print('# loading govdb')
    govdb=Roll( self,WW2ROLLSCSV,0 )
    print('# processing govdb')
    self.process_gov(govdb)
    print()

    print("#################")
    for fn,sk in CONVERT:
      self.alldb.append( Roll(self,CSVDIR+fn,sk) )
    print()
    print('# processing')
    t=0
    maindb=self.alldb[0]
    for d in self.alldb:
      m='## checking file: '+d.fname
      print(m)
      print('='*len(m) )
      n=0
      for r in d.rows:
        n=n+1
        snum=d.item(r,'vxno')
        sn=d.item(r,'surname')
        if not snum:
          d.err(n,'no snumber',r)
        else:
          s=self.find_by_snum(snum)
          if not s:
            if snum and d!=maindb:
              d.err(n,'new snumber not in all list',r,s)
            s=Person()
            self.rows.append( s )
            self.by_servicenumber[snum]=s
            s.servicenumber=snum
            s.surname=sn
          s.files.append( [d.fname[:],n] )
          if s.surname!=sn:
            d.err(n,'surname change: %s >> %s'%([s.surname],[sn]),r,s)
        t+=1
      print()
    print('## total lines parsed',t)
    print('## total people found',len(self.rows))


  def   find_by_snum(self,snum):
    return self.by_servicenumber.get(snum)
#  def   find_by_snum(self,sn):
#    return self.by_surname.get(sn)




m=Meta()




