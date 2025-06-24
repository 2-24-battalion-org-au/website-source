import sys
import csv


txtfile='FF labels-March 2025.txt'


class Label:
  def __init__(self,lines):
    self.name=None
    self.addr1=None
    self.addr2=None
    self.city=None
    self.state=None
    self.postcode=None
    self.parse(lines)

  def parse(self,lines):
    if lines[0]=='Mrs P Evans': lines[0]='Mrs P R Evans'
    self.name=lines[0]
    self.addr1=lines[1]
    if len(lines)>3: self.addr2=lines[2]
    #
    lastline=lines[-1].split()
    self.city=' '.join( lastline[:-2] )
    self.state=lastline[-2]
    self.postcode=lastline[-1]
#    print(lines)
#    print([self.name,self.addr1,self.addr2,self.city,self.state,self.postcode])


class FFlabels:
  def __init__(self):
    curr=[]
    self.labels=[]
    self.entries=[curr]
    with open(txtfile) as f:
      for l in f.readlines():
#        if '\x0c' in l:
#          n=len(self.entries)
#          if not entries[-1]: n=n-1
#         print('######################################## PAGE',n)
        l=l.strip()
        if not l:
          if curr:
#           print(curr)
            curr=[]
            self.entries.append(curr)
        else:
          curr.append(' '.join(l.split()))

    if not self.entries[-1]: del self.entries[-1]


    for e in self.entries:
      self.labels.append( Label(e) )


if __name__=="__main__":
  ff=FFlabels()
