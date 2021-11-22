#import psqlapi as api
import io, os

###CONECT
#get the value conn
#conn = api.connect()

###PROFILES
#it puts all discord id's, with all individual information in """profiles""" dicctionary
profiles={} #data
for profile in os.listdir("../profile"): #loop: num of files in profile folder
    list=[] #reusable list, every time the 2 loop finishes the list cleans
    for file in os.listdir("../profile/"+profile): #2loop: num of files in the designd profile
        file = io.open(f"../profile/{profile}/{file}")
        filevalue = file.readlines()
        file.close()
        list.append(filevalue)
        dic = dict.fromkeys([profile], list) #keeps info to update the data
    profiles.update(dic) #updates the profiles dicctionary
print(profiles)

###BOLSA
#it puts all information in 2 separated lists one of the value and the other of the quantity
#cant
cantvalues=[]
for filenames in os.listdir('../bolsa/cant'):
    file = io.open(bolsapath+"/cant/"+filenames, 'r')
    filevalue = file.readlines()
    file.close()
    cantvalues.append(filevalue)
print(cantvalues)
#cr
crvalues=[]
for filenames in os.listdir(bolsapath+'/cr'):
    file = io.open(bolsapath+"/cr/"+filenames, 'r')
    filevalue = file.readlines()
    file.close()
    crvalues.append(filevalue)
print(crvalues)
