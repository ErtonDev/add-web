from web.psqlapi import *
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

#API connect
conn = connect()

while True:

    time.sleep(30)

    # empresa 1 ################################################################

    # diferencia
    diferencia = random.randint(1, margin_1)

    # datos
    cr1 = get_bot(conn, "e_1", "cr")

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
        put_bot(conn, "e_1", "cr", int(cr1[0]) + diferencia)

    else:

        if int(cr1[0]) - diferencia <= 5:
            put_bot(conn, "'e_1'", "cr", min_1)

        else:
            put_bot(conn, "'e_1'", "cr", int(cr1[0]) - diferencia)

    # empresa 2 ################################################################

    # diferencia
    diferencia = random.randint(1, margin_2)

    # datos
    cr2 = get_bot(conn, "'e_2'", "cr")

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
        put_bot(conn, "'e_2'", "cr", int(cr2[0]) + diferencia)

    else:

        if int(cr1[0]) - diferencia <= 5:
            put_bot(conn, "'e_2'", "cr", min_2)

        else:
            put_bot(conn, "'e_2'", "cr", int(cr2[0]) - diferencia)

    # empresa 3 ################################################################

    # diferencia
    diferencia = random.randint(1, margin_3)

    # datos
    cr3 = get_bot(conn, "'e_3'", "cr")

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
        put_bot(conn, "'e_3'", "cr", int(cr3[0]) + diferencia)

    else:

        if int(cr1[0]) - diferencia <= 5:
            put_bot(conn, "'e_3'", "cr", min_3)

        else:
            put_bot(conn, "'e_3'", "cr", int(cr3[0]) - diferencia)

    # empresa 4 ################################################################

    # diferencia
    diferencia = random.randint(1, margin_4)

    # datos
    cr4 = get_bot(conn, "e_4", "cr")

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
        put_bot(conn, "e_4", "cr", int(cr4[0]) + diferencia)

    else:

        if int(cr1[0]) - diferencia <= 5:
            put_bot(conn, "e_4", "cr", min_4)

        else:
            put_bot(conn, "e_4", "cr", int(cr4[0]) - diferencia)


    # empresa negra 1 ##########################################################

    # diferencia
    diferencia = random.randint(1, margin_n_1)

    # datos
    cr_n_1 = get_bot(conn, "e_n1", "cr")

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
        put_bot(conn, "e_n1", "cr", int(cr_n_1[0]) + diferencia)

    else:

        if int(cr_n_1[0]) - diferencia <= 5:
            put_bot(conn, "e_n1", "cr", min_n_1)

        else:
            put_bot(conn, "e_n1", "cr", int(cr_n_1[0]) - diferencia)

    # empresa negra 2 ##########################################################

    # diferencia
    diferencia = random.randint(1, margin_n_2)

    # datos
    cr_n_2 = get_bot(conn, "e_n2", "cr")

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
        put_bot(conn, "e_n2", "cr", int(cr_n_2[0]) + diferencia)

    else:

        if int(cr_n_2[0]) - diferencia <= 5:
            put_bot(conn, "e_n2", "cr", min_n_2)

        else:
            put_bot(conn, "e_n2", "cr", int(cr_n_2[0]) - diferencia)
