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
    value = f"'{prokey[index][:-8]}', 'name', {str(profiles.get(prokey[index])[0])[1:-1]}, {str(profiles.get(prokey[index])[1])[1:-1]}, {str(profiles.get(prokey[index])[2])[1:-1]}, {str(profiles.get(prokey[index])[3])[1:-1]}, {str(profiles.get(prokey[index])[4])[1:-1]}, {str(profiles.get(prokey[index])[5])[1:-1]}, {str(profiles.get(prokey[index])[6])[1:-1]}, {str(profiles.get(prokey[index])[7])[1:-1]}, {str(profiles.get(prokey[index])[8])[1:-1]}. {str(profiles.get(prokey[index])[9])[1:-1]}"
    api.post(conn, "users", "'user_id', 'user_name', 'user_cr', 'user_e1', 'user_e2', 'user_e3', 'user_e4', 'user_n1', 'user_n2', 'user_lvl', 'user_pt', 'user_prestige', 'usr_transac'", value)
    index = index+1
index1 = 0
for keys in empresas:
    empkey=[]
    for key in empresas:
        empkey.append(key)
    value = f"'{empkey[index1]}', {str(empresas.get(empkey[index1])[0])[1:-1]}, {str(empresas.get(empkey[index1])[1])[1:-1]}"
    api.post(conn, "bot", "'stock', 'cant', 'cr'", value)
    index1 = index1+1
