import psqlapi as api
import io, os

###CONECT
#get the value conn
conn = api.connect()

###PROFILES
#it puts all discord id's, with all individual information in """profiles""" dicctionary
profiles={} #data
for profile in os.listdir("../profile"): #loop: num of files in profile folder
    list=[] #reusable list, every time the 2 loop finishes the list cleans
    for file in os.listdir("../profile/"+profile): #2loop: num of files in the designd profile
        if file == 'multas.txt':
            pass
        else:
            file = io.open(f"../profile/{profile}/{file}")
            filevalue = file.readlines()
            file.close()
            list.append(filevalue)
            dic = dict.fromkeys([profile], list) #keeps info to update the data
    profiles.update(dic) #updates the profiles dicctionary

###BOLSA
#it puts all information in 2 separated lists one of the value and the other of the quantity
#cant
cantvalues=[]
empresas={'e_1':'','e_2':'','e_3':'','e_4':'','e_n1':'','e_n2':''}
for filenames in os.listdir('../bolsa/cant'):
    file = io.open("../bolsa/cant/"+filenames, 'r')
    filevalue = file.readlines()
    file.close()
    cantvalues.append(filevalue)
#cr
crvalues=[]
for filenames in os.listdir('../bolsa/cr'):
    file = io.open("../bolsa/cr/"+filenames, 'r')
    filevalue = file.readlines()
    file.close()
    crvalues.append(filevalue)
i = 0
for keys in empresas:
    list=[]
    list.append(cantvalues[i])
    list.append(crvalues[i])
    dic = dict.fromkeys([keys], list)
    i = i+1
    empresas.update(dic)

index = 0
for keys in profiles:
    prokey=[]
    for key in profiles:
        prokey.append(key)
    api.post_user(conn, "users",
    prokey[index][:-8], 'name',
    str(profiles.get(prokey[index])[0])[2:-2],
    str(profiles.get(prokey[index])[1])[2:-2],
    str(profiles.get(prokey[index])[2])[2:-2],
    str(profiles.get(prokey[index])[3])[2:-2],
    str(profiles.get(prokey[index])[4])[2:-2],
    str(profiles.get(prokey[index])[5])[2:-2],
    str(profiles.get(prokey[index])[6])[2:-2],
    str(profiles.get(prokey[index])[7])[2:-2],
    str(profiles.get(prokey[index])[8])[2:-2],
    str(profiles.get(prokey[index])[9])[2:-2],
    str(profiles.get(prokey[index])[10])[2:-2])
    index = index+1
index1 = 0
for keys in empresas:
    empkey=[]
    for key in empresas:
        empkey.append(key)
    api.post_bot(conn, "bot", empkey[index1],
    str(empresas.get(empkey[index1])[0])[2:-2],
    str(empresas.get(empkey[index1])[1])[2:-2])
    index1 = index1+1
