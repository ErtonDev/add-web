import random
import time
import os
import io

# GLOBALS
# Autistas Del Discord (25)
min_1 = 70
max_1 = 150
margin_1 = 15

# Send Nudes (100)
min_2 = 10
max_2 = 40
margin_2 = 5

# EMStudio (50)
min_3 = 50
max_3 = 90
margin_3 = 7

# El Hijo Corp. (50)
min_4 = 30
max_4 = 100
margin_4 = 12

# mercado negro
# PozoHub
min_n_1 = 175
max_n_1 = 275
margin_n_1 = 15

# PlsPorn Ent.
min_n_2 = 225
max_n_2 = 325
margin_n_2 = 15

while True:

    time.sleep(30)

    # empresa 1 ################################################################

    # diferencia
    diferencia = random.randint(1, margin_1)

    # datos
    precio_emprs1 = io.open("bolsa/cr/cr_emprs1.txt", 'r')
    cr1 = precio_emprs1.readlines()
    precio_emprs1.close()

    # suma o resta
    if int(cr1[0]) <= min_1 + margin_1:
        suma = True
    elif int(cr1[0]) >= max_1 - margin_1:
        suma = False
    else:
        if random.randint(1, 2) == 1:
            suma = True
        else:
            suma = False


    # calculo y aplicación
    if suma == True:

        aplica_emprs1 = io.open("bolsa/cr/cr_emprs1.txt", 'w')
        aplica_emprs1.write(str(int(cr1[0]) + diferencia))
        aplica_emprs1.close()

    else:

        if int(cr1[0]) - diferencia <= 5:

            aplica_emprs1 = io.open("bolsa/cr/cr_emprs1.txt", 'w')
            aplica_emprs1.write(str(min_1))
            aplica_emprs1.close()

        else:

            aplica_emprs1 = io.open("bolsa/cr/cr_emprs1.txt", 'w')
            aplica_emprs1.write(str(int(cr1[0]) - diferencia))
            aplica_emprs1.close()


    # empresa 2 ################################################################

    # diferencia
    diferencia = random.randint(1, margin_2)

    # datos
    precio_emprs2 = io.open("bolsa/cr/cr_emprs2.txt", 'r')
    cr2 = precio_emprs2.readlines()
    precio_emprs2.close()

    # suma o resta
    if int(cr2[0]) <= min_2 + margin_2:
        suma = True
    elif int(cr2[0]) >= max_2 - margin_2:
        suma = False
    else:
        if random.randint(1, 2) == 1:
            suma = True
        else:
            suma = False

    # calculo y aplicación
    if suma == True:

        aplica_emprs2 = io.open("bolsa/cr/cr_emprs2.txt", 'w')
        aplica_emprs2.write(str(int(cr2[0]) + diferencia))
        aplica_emprs2.close()

    else:

        if int(cr1[0]) - diferencia <= 5:

            aplica_emprs2 = io.open("bolsa/cr/cr_emprs2.txt", 'w')
            aplica_emprs2.write(str(min_2))
            aplica_emprs2.close()

        else:

            aplica_emprs2 = io.open("bolsa/cr/cr_emprs2.txt", 'w')
            aplica_emprs2.write(str(int(cr2[0]) - diferencia))
            aplica_emprs2.close()


    # empresa 3 ################################################################

    # diferencia
    diferencia = random.randint(1, margin_3)

    # datos
    precio_emprs3 = io.open("bolsa/cr/cr_emprs3.txt", 'r')
    cr3 = precio_emprs3.readlines()
    precio_emprs3.close()

    # suma o resta
    if int(cr3[0]) <= min_3 + margin_3:
        suma = True
    elif int(cr3[0]) >= max_3 - margin_3:
        suma = False
    else:
        if random.randint(1, 2) == 1:
            suma = True
        else:
            suma = False

    # calculo y aplicación
    if suma == True:

        aplica_emprs3 = io.open("bolsa/cr/cr_emprs3.txt", 'w')
        aplica_emprs3.write(str(int(cr3[0]) + diferencia))
        aplica_emprs3.close()

    else:

        if int(cr1[0]) - diferencia <= 5:

            aplica_emprs3 = io.open("bolsa/cr/cr_emprs3.txt", 'w')
            aplica_emprs3.write(str(min_3))
            aplica_emprs3.close()

        else:

            aplica_emprs3 = io.open("bolsa/cr/cr_emprs3.txt", 'w')
            aplica_emprs3.write(str(int(cr3[0]) - diferencia))
            aplica_emprs3.close()


    # empresa 4 ################################################################

    # diferencia
    diferencia = random.randint(1, margin_4)

    # datos
    precio_emprs4 = io.open("bolsa/cr/cr_emprs4.txt", 'r')
    cr4 = precio_emprs4.readlines()
    precio_emprs4.close()

    # suma o resta
    if int(cr4[0]) <= min_4 + margin_4:
        suma = True
    elif int(cr4[0]) >= max_4 - margin_4:
        suma = False
    else:
        if random.randint(1, 2) == 1:
            suma = True
        else:
            suma = False

    # calculo y aplicación
    if suma == True:

        aplica_emprs4 = io.open("bolsa/cr/cr_emprs4.txt", 'w')
        aplica_emprs4.write(str(int(cr4[0]) + diferencia))
        aplica_emprs4.close()

    else:

        if int(cr1[0]) - diferencia <= 5:

            aplica_emprs4 = io.open("bolsa/cr/cr_emprs4.txt", 'w')
            aplica_emprs4.write(str(min_4))
            aplica_emprs4.close()

        else:

            aplica_emprs4 = io.open("bolsa/cr/cr_emprs4.txt", 'w')
            aplica_emprs4.write(str(int(cr4[0]) - diferencia))
            aplica_emprs4.close()


    # empresa negra 1 ##########################################################

    # diferencia
    diferencia = random.randint(1, margin_n_1)

    # datos
    precio_emprs_n_1 = io.open("bolsa/cr/cr_emprs_n_1.txt", 'r')
    cr_n_1 = precio_emprs_n_1.readlines()
    precio_emprs_n_1.close()

    # suma o resta
    if int(cr_n_1[0]) <= min_n_1 + margin_n_1:
        suma = True
    elif int(cr_n_1[0]) >= max_n_1 - margin_n_1:
        suma = False
    else:
        if random.randint(1, 2) == 1:
            suma = True
        else:
            suma = False


    # calculo y aplicación
    if suma == True:

        aplica_emprs_n_1 = io.open("bolsa/cr/cr_emprs_n_1.txt", 'w')
        aplica_emprs_n_1.write(str(int(cr_n_1[0]) + diferencia))
        aplica_emprs_n_1.close()

    else:

        if int(cr_n_1[0]) - diferencia <= 5:

            aplica_emprs_n_1 = io.open("bolsa/cr/cr_emprs_n_1.txt", 'w')
            aplica_emprs_n_1.write(str(min_n_1))
            aplica_emprs_n_1.close()

        else:

            aplica_emprs_n_1 = io.open("bolsa/cr/cr_emprs_n_1.txt", 'w')
            aplica_emprs_n_1.write(str(int(cr_n_1[0]) - diferencia))
            aplica_emprs_n_1.close()


    # empresa negra 2 ##########################################################

    # diferencia
    diferencia = random.randint(1, margin_n_2)

    # datos
    precio_emprs_n_2 = io.open("bolsa/cr/cr_emprs_n_2.txt", 'r')
    cr_n_2 = precio_emprs_n_2.readlines()
    precio_emprs_n_2.close()

    # suma o resta
    if int(cr_n_2[0]) <= min_n_2 + margin_n_2:
        suma = True
    elif int(cr_n_1[0]) >= max_n_2 - margin_n_2:
        suma = False
    else:
        if random.randint(1, 2) == 1:
            suma = True
        else:
            suma = False


    # calculo y aplicación
    if suma == True:

        aplica_emprs_n_2 = io.open("bolsa/cr/cr_emprs_n_1.txt", 'w')
        aplica_emprs_n_2.write(str(int(cr_n_2[0]) + diferencia))
        aplica_emprs_n_2.close()

    else:

        if int(cr_n_2[0]) - diferencia <= 5:

            aplica_emprs_n_2 = io.open("bolsa/cr/cr_emprs_n_2.txt", 'w')
            aplica_emprs_n_2.write(str(min_n_2))
            aplica_emprs_n_2.close()

        else:

            aplica_emprs_n_2 = io.open("bolsa/cr/cr_emprs_n_2.txt", 'w')
            aplica_emprs_n_2.write(str(int(cr_n_2[0]) - diferencia))
            aplica_emprs_n_2.close()
