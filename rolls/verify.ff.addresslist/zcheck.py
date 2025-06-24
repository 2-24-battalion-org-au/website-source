
import load_db
import load_ff


ff=load_ff.FFlabels()
db=load_db.MembersDB()

mcb='McCabe'

for label in ff.labels:
    print('Label::::',label.__dict__ )
    print('---')
    llines=[]
    llines.append(f'{label.name}')
    llines.append(f'{label.addr1}')
    if label.addr2: llines.append(f'{label.addr2}')
    llines.append(f'{label.city} {label.state} {label.postcode}')
    print('Label::::',llines)
    print('---')
    print(db)

    if label.name=='The Principal':
      match=db.find( 'first name',label.name.split()[-1] )
      continue
    elif label.name=='Mr R & Mrs J Edwards':
      match=db.find( 'surname',label.name.split()[-1] )
      match=db.filter( match, 'title','Mr R' )
      match[0].db['title']='Mr R & Mrs J'
      match[0].db['address 2']='PO Box 392'
    elif label.name=='Mrs M-J Joscelyne':
      match=db.find( 'surname',label.name.split()[-1] )
      match=db.filter( match, 'title','Mrs M-J & Mr A' )
    elif label.name=='The Editor, "Mufti" Anzac House':
      #match=db.find( 'address 2','4 Collins Street')
      match=db.find( 'title','The Editor, "Mufti"')
    elif label.name=='Mrs I Dunstan OAM':
      match=db.find( 'surname','Dunstan OAM')
      match=db.filter( match, 'title','Mrs I')
    elif label.name=='Mrs G Bryant':
      match=db.find( 'surname',label.name.split()[-1] )
      match=db.filter( match, 'title','Mrs' )
      match[0].db['title']='Mrs G'
    elif label.name=='Mr D Muir':
      match=db.find( 'surname',label.name.split()[-1] )
      match=db.filter( match, 'title','Mr D & Mrs M' )
      match[0].db['title']='Mr D'
    elif label.name=='Mrs D Wymond':
      match=db.find( 'surname',label.name.split()[-1] )
      match=db.filter( match, 'title',' '.join(label.name.split()[:-1]) )
      match[0].db['address 2']=match[0].db['address 2'][:-1]


    elif label.name in ['Mr L H McEvoy','Mr N Heathcote','Ms S Miller','Mrs J Riordan','Mr B Cook','Ms C King','Mrs J Monds']:
      continue
    else:
      if 'van Hooydonk' in label.name:
        label.name=label.name.replace('van Hoo','vanHoo')
      match=db.find( 'surname',label.name.split()[-1] )
      print('DB:::::::: match0',match)
      match=db.filter( match, 'title',' '.join(label.name.split()[:-1]) )


    print('DB:::::::: match.result',label.name,match)
    if len(match)!=1:
      print(match)
      raise Exception()
    m=match[0]
    print('DB:::::::: match.result',label.name,m.__dict__)
    mlines=[]
    if m.get('surname'):
      mlines.append( m.format('title','surname') )
    else:
      mlines.append( m.format('first name','title') )
    if m.get('address 1'): mlines.append( m.format('address 1') )
    if m.get('address 2'): mlines.append( m.format('address 2') )
    mlines.append( m.format('town','pcode') )
    if 'Vic' in mlines[-1]: mlines[-1]=mlines[-1].replace('Vic','VIC')
    print('Label::===',llines)
    print('DB:::::===', mlines)
    print('DB==LABEL::',llines==mlines)
    if llines!=mlines:
      if llines[0] not in ['Mr P & Mrs L van Hooydonk','Mrs L Holland','The Editor, "Mufti" Anzac House','Mr J Mollard','Mr R P Weir','Mrs D Cleary','Mrs M-J Joscelyne','Mr S Mollard','Mrs H Robertson','Mr D & Mrs A Neville', 'Mrs G Bryant' ]:
        print("Bad match, exiting")
        break
    print()
print('---- finished ----')

{'surname': 'McCabe', 'title': 'Mrs M', 'first name': 'Mary', 'paid to end': '', 'receipt details': '', 'status': 'W', 'lm': '', "start m'ship": '', "cease m'ship": '', 'reason': '', 'address 1': '', 'address 2': '45 First Street', 'town': 'KINGSWOOD NSW', 'pcode': '2747', 'email address': '', 'post': 'TRUE', 'service no': '', 'email': '', 'm/stat': 'W', 'army no': 'NX172643', 'phone': '047 364 124', 'updated': '', 'known as': '', 'notes': '', 'relationship': 'Widow of Darcy McCabe'}





