import csv


file='members.csv'

[', ', 'Title', 'FIRST NAME', 'Paid to End', 'Receipt Details', 'Status', 'LM', "Start M'ship", "Cease M'ship", 'Reason', 'Address 1', 'ADDRESS 2', 'TOWN', 'PCODE', 'EMAIL ADDRESS', 'POST', 'Service No', 'EMAIL', 'M/STAT', 'ARMY NO', 'PHONE', 'UPDATED', 'KNOWN AS', 'NOTES', 'RELATIONSHIP']


class Member:
  def __init__(self,db):
    self.db=db

  def get(self,key):
    return self.db[key]
  def format(self,*keys):
    rv=[ self.db[k.strip()] for k in keys ]
    return ' '.join(rv)


class MembersDB:
  def __init__(self,file='../pull.spreadsheets/pulled.spreadsheets/members.csv'):
    self.members=[]
    self.HEADERS={}
    #
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile) #, delimiter=',', quotechar='|')
        for row in spamreader:
          if not self.HEADERS:
            for i,v in enumerate(row):
              if v==', ': v='surname'
              self.HEADERS[v.lower()]=i
    #        print( self.HEADERS )
          else:
            row=[ ' '.join(r.split()) for r in row]
            row=[ r.strip() for r in row]
            if len(self.HEADERS) != len(row):
              raise Exception()
#            print(row)
            self.members.append( Member( dict(zip(self.HEADERS,row)) ) )
#    print('loaded entries:',len(self.members))

  def find(self,key,val):
    rv=[]
    for m in self.members:
      if m.db[key]==val: rv.append(m)
    return rv
  def filter(self,rvcurrent,key,val):
    rv=[]
    for m in rvcurrent:
      if m.db[key]==val: rv.append(m)
    if not rv: print("No results for",key,val)
    return rv




if __name__=="__main__":
  db=MembersDB()

