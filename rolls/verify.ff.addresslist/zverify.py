import sys
import csv

class Labels:
  def __init__(self,f):
    self.post=[]
    a=[]
    for l in open(f):
      l=l.strip()
      if l:
        a.append( ' '.join(l.split()) )
        if l==l.upper() and not l.startswith('RMB'):
          if a in self.post:
            print('DUPLICATE.post',a)
          else:
            self.post.append( a )
          a=[]
    self.post.sort()

# ['SURNAME', 'Title', 'FIRST NAME', 'PAID TO END', 'RECEIPT DETAIL', 'STATUS', 'LM', "Start M'ship", "Cease M'ship", 'Reason', 'Address 1', 'ADDRESS 2', 'TOWN', 'PCODE', 'EMAIL ADDRESS', 'POST', 'Service No', 'EMAIL', 'M/STAT', 'ARMY NO', 'PHONE', 'UPDATED', 'KNOWN AS', 'NOTES', 'RELATIONSHIP']

class DB:
  def __init__(self,f='../pull.spreadsheets/pulled.spreadsheets/members.csv'):
    self.all=[]
    self.post=[]
    with open(f) as f:
      r=csv.reader(f)
      h=next(r,None)
      h=[ i.lower() for i in h ]
#      print(h)
      for l in r:
        postraw=  [ 'post?==',l[h.index('post')], 'email==',l[h.index('email')].lower() ]
        post=  l[h.index('post')]=='TRUE' and l[h.index('email')].lower()!='yes'
        print('db.raw',l,post,postraw)
#      if l[h.index('post')]=='TRUE' and l[h.index('email')].lower()!='yes':
        a=[]
        for keys in [ ['title','surname'],['address 1'],['address 2'],['town','pcode'] ]:
          aline= ' '.join( [ l[h.index(k)] for k in keys ] )
          if aline: a.append( ' '.join(aline.split()))
        print('dbpa',a)
        self.all.append(a)
        if post:
          if post:
            if a in self.post:
              print('DUPLICATE.DB',a)
            else:
              self.post.append(a)
    self.post.sort()

  def verify(self,labels):
    postl=labels[:]
    postd=self.post[:]
    #
    for a in postl[:]:
      print('CHECK',a,a in postd)
      if a in postd:
        print('# OK',a)
        postl.remove(a)
        postd.remove(a)
    #
    for a in postd:
      m='dont know'
      print('ERR: only in .db.',[ l for l in a ])
      for b in postl:
        if a[0]==b[0]:
          print('  ??possible label address??',b)
      print('')

    #
    for a in postl:
      m='UNKNOWN'
      if a in self.all: m='DB says dont post?'
      print('ERR: only in post',[ l for l in a ],m)
      for b in postd:
        if a[0]==b[0]:
          print('  ??possible db address??',b)
      print('')


if __name__=='__main__':
  if len(sys.argv)==1:
    print('Useage: %s <fflables.txt>'%(sys.argv[0]))
  else:
    labels=Labels(sys.argv[1])
    for a in labels.post:
      print('post',a)
    db=DB()
    for a in db.post:
      print('.db.',a)
    db.verify(labels.post)
