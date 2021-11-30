################################################################################
# Project by: ErtonDev
# Info: Bot de Discord multifuncional.
################################################################################

## MODULES / LIBRARIES
################################################################################
import discord, subprocess, itertools, colorama, random, time, math, os, io, re
from discord.ext import commands, tasks
from colorama import Fore, Back, Style
from discord.utils import find
from itertools import cycle

## EXTERNAL FILES
################################################################################
import logclass
from logclass import Log

from web.psqlapi import *

import niveles
from niveles import License_manager

################################################################################
# Next update notes:
################################################################################

## SETUP
################################################################################
# log
os.system('clear')
colorama.init(autoreset=True)
log = Log()

conn = connect()

# license manager / levels
lvl = License_manager()

# external files
subprocess.Popen(['python3', 'mercado.py']) # exec mercado

# bot
# prefix and globals
client = commands.Bot(command_prefix = '.')
version = "7.8.1"
status = cycle(['.auxilio', 'by 3rt0n', version])

# main event
@client.event
async def on_ready():
    change_status.start()
    print(Fore.LIGHTBLUE_EX + f"----- Bot {str(version)} online -----")

# error handler
# WARNING: Comentar al probar nuevas implementaciones para ver errores
@client.event
async def on_command_error(ctx, error):

    # si no hay acceso
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            title = "Retrocede, zona restringida.",
            description = "Acceso limitado a ciertos roles.",
            color = discord.Color.red()
        )
        embed.set_author(
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )

        await ctx.send(embed = embed)
        log.logFail("N/A", ctx.author.name, "NotAllowedError")

    # si el comando no está contemplado
    if isinstance(error, commands.CommandNotFound):
        log.logFail("N/A", ctx.author.name, "CommandNotFoundError")

# backgorund task
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))



## main EMBEDS
################################################################################
# mantenimiento
def embedMantenimiento(ctx):
    # input
    embed = discord.Embed(
        title = "¡Vaya, este comando está en mantenimiento!",
        description = "Prueba otra vez más tarde o contacta con el administrador.",
        color = discord.Color.gold()
    )

    embed.set_author(
        name = ctx.author.display_name,
        icon_url = ctx.author.avatar_url
    )

    # output
    return embed

# auxilio
def embedAuxilio(ctx, title, commands):
    # input
    embed = discord.Embed(
        title = title,
        description = commands,
        color = discord.Color.blue()
    )

    embed.set_author(
        name = ctx.author.display_name,
        icon_url = ctx.author.avatar_url
    )

    # output
    return embed

# dato
def embedDato(ctx, dato, description = "", optional_color = "blue"):
    # color selection
    if optional_color == "blue":
        chosen_color = discord.Color.blue()
    elif optional_color == "gold":
        chosen_color = discord.Color.gold()
    elif optional_color == "red":
        chosen_color = discord.Color.red()
    else:
        chosen_color = discord.Color.blue()

    # input
    embed = discord.Embed(
        title = dato,
        description = description,
        color = chosen_color
    )

    embed.set_author(
        name = ctx.author.display_name,
        icon_url = ctx.author.avatar_url
    )

    # output
    return embed

# error
def embedError(ctx):
    # input
    embed = discord.Embed(
        title = "Algo anda mal...",
        description = "Comprueba que no te hayas equivocado al escribir el comando.",
        color = discord.Color.red()
    )

    embed.set_image(
        url = "attachment://foto.png"
    )

    embed.set_author(
        name = ctx.author.display_name,
        icon_url = ctx.author.avatar_url
    )

    # output
    return embed



## KEYWORD detection
################################################################################
@client.event
async def on_message(ctx):
    itwas1 = False
    itwas2 = False
    sendMsg = False
    theonedetected = "None"

    # keywords
    keywords1 = ["chupapitos", "xupapitos", "tragasables"]
    keywords2 = ["maricón", "maricon", "marica", "marika", "mricn", "mrcon", "mricon", "marik"]

    # keywords1
    for i in range(len(keywords1)):
        wordsFound = re.findall(keywords1[i], ctx.content.lower())

        if len(wordsFound) != 0:
            countthat = io.open('counter_chupapitos.txt', 'r')
            actualammount = countthat.readlines()
            countthat.close()

            writethat = io.open('counter_chupapitos.txt', 'w')
            thenewammount = int(actualammount[0]) + len(wordsFound)
            writethat.write(str(thenewammount))
            writethat.close()

            itwas1 = True
            sendMsg = True

    # keywords2
    for i in range(len(keywords2)):
        wordsFound = re.findall(keywords2[i], ctx.content.lower())

        if len(wordsFound) != 0:
            countthat = io.open('counter_maricon.txt', 'r')
            actualammount = countthat.readlines()
            countthat.close()

            writethat = io.open('counter_maricon.txt', 'w')
            thenewammount = int(actualammount[0]) + len(wordsFound)
            writethat.write(str(thenewammount))
            writethat.close()

            itwas2 = True
            sendMsg = True

    if sendMsg == True:

        if itwas1 == True and itwas2 == False:
            theonedetected = "Chupapitos"

        elif itwas1 == False and itwas2 == True:
            theonedetected = "Maricón"

        elif itwas1 == True and itwas2 == True:
            theonedetected = "Both"

        await ctx.channel.send("Tú más.")
        log.logEvent(event_type = f"Keyword detected ({theonedetected})")

    # to execute other commands too
    await client.process_commands(ctx)



## PRIVATE commands
################################################################################
# .admin
@client.command()
async def admin(ctx, path = "None", func = "None", arg1 = "None", arg2 = "None"):
    # check admin right
    if ctx.author.id == 548955616153174017 or ctx.author.id == 353159282835062785:

        path = path.lower()
        if isinstance(func, str):
            func = func.lower()
        if isinstance(arg1, str):
            arg1 = arg1.lower()
        if isinstance(arg2, str):
            arg2 = arg2.lower()

        ## RESPECTO A BÁSICOS
        # .admin
        if path == "none":

            await ctx.send(embed = embedDato(ctx, "Oh poderoso Führer... <:saludo:802315699255115826><:elfuhrer:798991064665030672>", "En **.admin auxilio** encontrará todo cuanto necesita..."))
            log.logCall('admin', ctx.author.name)

        # .admin auxilio
        elif path == "auxilio":

            await ctx.send(embed = embedAuxilio(ctx, "Comandos de administrador:", "*Sistema:*\n**.admin shut :** El Hijo se va a dormir.\n\n*Administración:*\n**.admin clean (@usuario) :** Limpia la ficha de un usuario."))
            log.logCall('admin auxilio', ctx.author.name)


        ## RESPECTO A {SISTEMA}
        # .admin shut
        elif path == "shut":
            await ctx.send("*Pues hasta luego.*")
            log.logEvent(event_type = "Shut down")
            quit()

        ## RESPECTO A ADMINISTRACIÓN
        # .admin limpia
        elif path == "clean":
            who = func
            # identifica la persona
            if who[:3] == "<@!" and who[3:-1] != str(ctx.author.id):
                # tal vez no eres tu, pero es una persona
                person = who[3:-1]

            elif who[:2] == "<@" and who[:3] != "<@!" and who[:3] != "<@&" and who[2:-1] != str(ctx.author.id):
                # más de lo mismo, pero para aquellos que mandan el argumento diferente
                person = who[2:-1]

            else:
                # who no es una persona, por lo tanto mostraremos tu cuenta
                person = ctx.author.id

            try:

                abre_ficha = io.open(f"profile/{person}_profile/multas.txt", 'w')
                abre_ficha.write("")
                abre_ficha.close()

                await ctx.send(embed = embedDato(ctx, "Oh poderoso Führer... <:saludo:802315699255115826><:elfuhrer:798991064665030672>", f"La ficha de {person} está limpia."))
                log.logCall(f"admin clean {func}", ctx.author.name)

            except FileNotFoundError:

                await ctx.send(embed = embedDato(ctx, "Oh poderoso Führer... <:saludo:802315699255115826><:elfuhrer:798991064665030672>", f"Me temo que el usuario {person} no está en nuestra base de datos.", "gold"))
                log.logFail(f"admin clean {func}", ctx.author.name, "AccountNotFoundError")

        # if command isn't found
        else:
            # random selector for the image shown
            imageselector = random.randint(1,3)
            file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

            await ctx.send(file = file, embed = embedError(ctx))
            log.logFail(f'admin {path} {func} {arg1} {arg2}', ctx.author.name, 'ArgumentNotFoundError')


    # if no admin right
    else:
        # embed
        file = discord.File("resources/elhijo_ban.png", filename = "foto.png")
        embed = discord.Embed(
        title = "¿¡Qué haces metiendo tus manos aceitosas encima de las cosas del Führer!? ¡Vete, fuix! <:ban:793078436746756126>",
        description = "Este comando alberga un poder descomunal, no debe estar al alcance de cualquiera.",
        color = discord.Color.red()
        )
        embed.set_author(
        name = ctx.author.display_name,
        icon_url = ctx.author.avatar_url
        )
        embed.set_image(
        url = "attachment://foto.png"
        )

        await ctx.send(file = file, embed = embed)
        log.logFail(f'admin', ctx.author.name, 'NotAllowedError')

# .mod
@client.command()
@commands.has_role("Consejo")
async def mod(ctx, path = "None", func = "None", arg1 = "None", user : discord.User = "None"):

    path = path.lower()
    if isinstance(func, str):
        func = func.lower()
    if isinstance(arg1, str):
        arg1 = arg1.lower()

    # no hay argumentos
    if path == "none":

        await ctx.send(embed = embedDato(ctx, "Bienvenido moderador <:saludo:802315699255115826><:elfuhrer:798991064665030672>", "En **.mod auxilio** encontrará todo cuanto necesita..."))
        log.logCall('mod', ctx.author.name)

    # auxilio
    elif path == "auxilio":

        await ctx.send(embed = embedAuxilio(ctx, "Comandos de moderador:", "**.mod puntos add/remove (@usuario) :** Añade (1) o quita (3) puntos de la cuenta de un usuario.\n**.mod ban (razón escrita entre comillas) (tiempo que debería ser banneado escrito entre comillas) (@usuario):** Bannea a un usuario a traves del Hijo dando el motivo.\n**.mod multa (@usuario) (número de la ley incumplida) (@usuario otra vez) :** Multa a un usuario para que el administrador aplique la pena más adelante."))
        log.logCall('mod auxilio', ctx.author.name)

    # dar puntos # NOTE: de uno en uno
    elif path == "puntos" and func == "add":

        pase = False
        who = arg1

        # identifica la persona
        if who[:3] == "<@!":
            # tal vez no eres tu, pero es una persona
            person = who[3:-1]
            pase = True

        elif who[:2] == "<@" and who[:3] != "<@!" and who[:3] != "<@&":
            # más de lo mismo, pero para aquellos que mandan el argumento diferente
            person = who[2:-1]
            pase = True

        else:
            # who no es una persona, por lo tanto mostraremos un error
            imageselector = random.randint(1,3)
            file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

            await ctx.send(file = file, embed = embedError(ctx))
            log.logFail(f"mod {path} {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")


        # la funcionalidad
        if pase == True:

            # mira si tiene cuenta
            try:
                # encuentra el archivo y lo lee
                """
                archivo = io.open(f"profile/{person}_profile/points.txt", 'r')
                puntos = archivo.readlines()
                archivo.close()
                """
                puntos = get_user(conn, f"'{person}'", "user_pt")

                # aplica los cambios
                if int(puntos[0]) >= 0 and int(puntos[0]) + 1 <= 15:

                    """
                    archivo = io.open(f"profile/{person}_profile/points.txt", 'w')
                    archivo.write("")
                    archivo.write(str(int(puntos[0]) + 1))
                    archivo.close()
                    """
                    put_user(conn, f"'{person}'", "user_pt", int(puntos[0]) + 1)

                    # mensaje y log
                    await ctx.send(embed = embedDato(ctx, "¡Entrega de puntos exitosa!", f"De **{puntos[0]}** a **{str(int(puntos[0]) + 1)}**"))
                    log.logCall(f"mod puntos add {arg1}", ctx.author.name, True, f"De {puntos[0]} a {str(int(puntos[0]) + 1)}")

                else:

                    await ctx.send(embed = embedDato(ctx, "¡Entrega de puntos exitosa! Pero sin cambios...", f"El usuario ya tiene el número máximo de puntos: **15**", "gold"))
                    log.logCall(f"mod puntos add {arg1}", ctx.author.name, True, "15 MAX")

            # no tiene cuenta
            except FileNotFoundError:

                await ctx.send(embed = embedDato(ctx, "¡Este usuario no tiene cuenta!", "*Dile que ya tarda en usar .registro*", "gold"))
                log.logFail(f"mod puntos add {arg1}", ctx.author.name, "AccountNotFoundError")

    # quitar puntos # NOTE: de tres en tres
    elif path == "puntos" and func == "remove":

        pase = False
        who = arg1

        # identifica la persona
        if who[:3] == "<@!":
            # tal vez no eres tu, pero es una persona
            person = who[3:-1]
            pase = True

        elif who[:2] == "<@" and who[:3] != "<@!" and who[:3] != "<@&":
            # más de lo mismo, pero para aquellos que mandan el argumento diferente
            person = who[2:-1]
            pase = True

        else:
            # who no es una persona, por lo tanto mostraremos un error
            imageselector = random.randint(1,3)
            file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

            await ctx.send(file = file, embed = embedError(ctx))
            log.logFail(f"mod {path} {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")


        # la funcionalidad
        if pase == True:

            # mira si tiene cuenta
            try:
                # encuentra el archivo y lo lee
                """
                archivo = io.open(f"profile/{person}_profile/points.txt", 'r')
                puntos = archivo.readlines()
                archivo.close()
                """
                puntos = get_user(conn, f"'{person}'", "user_pt")

                # aplica los cambios
                if int(puntos[0]) >= 3:
                    """
                    archivo = io.open(f"profile/{person}_profile/points.txt", 'w')
                    archivo.write("")
                    archivo.write(str(int(puntos[0]) - 3))
                    archivo.close()
                    """
                    put_user(conn, f"'{person}'", "user_pt", int(puntos[0]) - 3)

                    # mensaje y log
                    await ctx.send(embed = embedDato(ctx, "¡Retirada de puntos exitosa!", f"De **{puntos[0]}** a **{str(int(puntos[0]) - 3)}**"))
                    log.logCall(f"mod puntos remove {arg1}", ctx.author.name, True, f"De {puntos[0]} a {str(int(puntos[0]) - 3)}")

                elif int(puntos[0]) < 3 and int(puntos[0]) != 0:
                    """
                    archivo = io.open(f"profile/{person}_profile/points.txt", 'w')
                    archivo.write("")
                    archivo.write("0")
                    archivo.close()
                    """
                    put_user(conn, f"'{person}'", "user_pt", 0)

                    # mensaje y log
                    await ctx.send(embed = embedDato(ctx, "¡Retirada de puntos exitosa!", f"De **{puntos[0]}** a **0**"))
                    log.logCall(f"mod puntos remove {arg1}", ctx.author.name, True, f"De {puntos[0]} a 0")

                else:

                    await ctx.send(embed = embedDato(ctx, "¡Retirada de puntos exitosa! Pero sin cambios...", f"El usuario ya tiene el número mínimo de puntos: **0**", "gold"))
                    log.logCall(f"mod puntos remove {arg1}", ctx.author.name, True, "0 MIN")

            # no tiene cuenta
            except FileNotFoundError:

                await ctx.send(embed = embedDato(ctx, "¡Este usuario no tiene cuenta!", "*Dile que ya tarda en usar .registro*", "gold"))
                log.logFail(f"mod puntos remove {arg1}", ctx.author.name, "AccountNotFoundError")

    # ban
    elif path == "ban":

        # path = ban | func = razón | arg1 = tiempo | user = miembro

        if user == "None" or user == ctx.message.author:

            await ctx.send(embed = embedDato(ctx, "Indica a alguien valido para bannear.", "No te pongas a ti ni dejes el espacio en blanco.", "gold"))
            log.logFail(f"mod ban {func} {arg1} {user}", ctx.author.name, "ArgumentNotFoundError")

        else:

            if func != "None" or arg1 != "None":

                # manda mensaje de confirmación
                await ctx.send(embed = embedDato(ctx, "La operación ha sido llevada a cabo:", f"La petición de banneo de {user} se ha enviado."))
                log.logCall(f"mod ban {func} {arg1} {user}", ctx.author.name, True, f"{user} por {func}")

                # notifica por staff
                channel = client.get_channel(775820270614085674)
                await channel.send(embed = embedDato(ctx, "Petición de ban entrante:", f"A **{user}** de {ctx.author.name}.\n\nRazón: *{func}*\n\nTiempo sugerido: *{arg1}*"))
                log.logEvent("BAN Nominación notificada")

                # registra la acción
                ban_registro = io.open("registro.txt", 'a')
                ban_registro.write(f"\nBAN de {ctx.author.name} a ** {user} ** por {func} durante {arg1}")
                ban_registro.close()
                log.logEvent("BAN Nominación registrada")

                # manda un mensaje de aviso al banneado
                message = f"**Has sido nominado a un ban** por {ctx.author.name}.\n*Razón: {func}*"
                await user.send(message)
                log.logEvent("BAN Nominación enviada al usuario")

            else:
                imageselector = random.randint(1,3)
                file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                await ctx.send(file = file, embed = embedError(ctx))
                log.logFail(f"mod ban {func} {arg1} {user}", ctx.author.name, "ArgumentNotFoundError")

    # multa
    elif path == "multa":

        pase = False
        who = func

        # identifica la persona
        if who[:3] == "<@!":
            # tal vez no eres tu, pero es una persona
            person = who[3:-1]
            pase = True

        elif who[:2] == "<@" and who[:3] != "<@!" and who[:3] != "<@&":
            # más de lo mismo, pero para aquellos que mandan el argumento diferente
            person = who[2:-1]
            pase = True

        else:
            # who no es una persona, por lo tanto mostraremos un error
            imageselector = random.randint(1,3)
            file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

            await ctx.send(file = file, embed = embedError(ctx))
            log.logFail(f"mod {path} {func} {arg1} {user}", ctx.author.name, "ArgumentNotFoundError")

        if pase == True:

            try:

                # accede a la cuenta de el hijo del infractor
                log.logCall(f"mod multa {func} {arg1} {user}", ctx.author.name, True, f"{user} por ley {arg1}")
                cuenta_infractor = io.open(f"profile/{person}_profile/multas.txt", 'a')

                # añade la multa
                cuenta_infractor.write(f"\nInfracción de la ley {arg1}")
                cuenta_infractor.close()
                log.logEvent("MULTA en ficha")

                # manda un mensaje de confirmación
                await ctx.send(embed = embedDato(ctx, "La operación ha sido llevada a cabo:", f"Se ha multado a {user}."))

                # notifica en staff del incidente
                channel = client.get_channel(775820270614085674)
                await channel.send(embed = embedDato(ctx, "Multa entrante:", f"A **{user}** de {ctx.author.name}.\n\nInfracción: Ley número {arg1}"))
                log.logEvent("MULTA comunicada")

                # registra la multa
                ban_registro = io.open("registro.txt", 'a')
                ban_registro.write(f"\nMULTA de {ctx.author.name} a ** {user} ** por la ley {arg1}")
                ban_registro.close()
                log.logEvent("MULTA registrada")

                # notifica al infractor
                message = f"**Has recibido una multa.**\nInfracción: Ley número {arg1}\nPara más detalles sobre tu condena revisa la constitución de ADD\nPara ver tus multas pendientes usa .ficha"
                await user.send(message)
                log.logEvent("MULTA notificada al usuario")

            except FileNotFoundError:

                # si el infractor no tiene cuenta...
                await ctx.send(embed = embedDato(ctx, "El infractor no está registrado en la base de datos.", f"En otras palabras: no tiene una cuenta.\nSe ha notificado a {user} y al administrador sobre esto.\n\n**La multa se aplicará pero no se mostrará en la ficha del infractor.**"))

                # notifica en staff del incidente
                channel = client.get_channel(775820270614085674)
                await channel.send(embed = embedDato(ctx, "Multa entrante:", f"A **{user}** de {ctx.author.name}.\n\nInfracción: Ley número {arg1}\n\n*El infractor no está registrado en la base de datos.*"))
                log.logEvent("MULTA comunicada (El infractor no está en la base de datos)")

                # registra la multa
                ban_registro = io.open("registro.txt", 'a')
                ban_registro.write(f"\nMULTA de {ctx.author.name} a ** {user} ** por la ley {arg1}")
                ban_registro.close()
                log.logEvent("MULTA registrada (El infractor no está en la base de datos)")

                # notifica al infractor
                message = f"**Has recibido una multa.**\nInfracción: Ley número {arg1}\nPara más detalles sobre tu condena revisa la constitución de ADD\nCrea tu cuenta en el hijo con .registro para no perder más información sobre tus multas pendientes."
                await user.send(message)
                log.logEvent("MULTA notificada al usuario (El infractor no está en la base de datos)")

    # argumento no contemplado
    else:
        imageselector = random.randint(1,3)
        file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

        await ctx.send(file = file, embed = embedError(ctx))
        log.logFail(f"mod {path} {func} {arg1} {user}", ctx.author.name, "ArgumentNotFoundError")



## MAIN commands
################################################################################
# .auxilio: Ayuda de comandos
@client.command()
async def auxilio(ctx):

    await ctx.send(embed = embedAuxilio(ctx, "Lista de comandos:",
    "*Comandos privados:*\n**.admin :** Comandos de administrador.\n**.mod :** Comandos de moderador.\n\n*Comandos de funcionalidad:*\n**.ver :** Muestra la versión actual del Hijo.\n**.retrato :** Muestra una imagen del Hijo.\n**.rol :** Asigna roles.\n**.contador :** Contador de palabras.\n\n*Comandos de cuentas:*\n**.perfil :** Para más detalles sobre las cuentas del Hijo.\n\n*Extensiones:*\n**.banco :** Un simulador de inversión integrado.\n**.casino :** Para gastar tu dinero."))
    log.logCall("auxilio", ctx.author.name)



## FUNCTIONAL commands
################################################################################
# .ver: Muestra la versión
@client.command()
async def ver(ctx):

    await ctx.send(embed = embedDato(ctx, "Versión: " + version))
    log.logCall("ver", ctx.author.name)

# .retrato: Manda una foto de elhijo
@client.command()
async def retrato(ctx):
    retrato_var = random.randint(1,5)
    if retrato_var == 1:
        await ctx.send("El pequeño Hijo, 1910", file = discord.File('resources/elhijo5.png'))
    if retrato_var == 2:
        await ctx.send("Día de comunión, 1922", file = discord.File('resources/elhijo3.png'))
    if retrato_var == 3:
        await ctx.send("El Hijo de Autistas del Discord, 1935", file = discord.File('resources/elhijo.png'))
    if retrato_var == 4:
        await ctx.send("Dibujo de una amiga, 1914", file = discord.File('resources/elhijo4.png'))
    if retrato_var == 5:
        await ctx.send("Sin nombre, 1937", file = discord.File('resources/elhijo6.png'))
    log.logCall("retrato", ctx.author.name)

# .rol : Te da roles
@client.command()
async def rol(ctx, role = "none"):

    # check if the user has a profile
    # only users with profile have access
    with_account = True

    try:
        """
        profile_existence = io.open(f"{ctx.author.id}_profile.txt", 'r')
        profile_existence.close()
        """
        get_user(conn, f"'{ctx.author.id}'", "user_id") #el user_id es solo para coger algo y probar si va

    except FileNotFoundError:
        with_account = False

    if with_account == True:

        role = role.lower()

        if role == "none":
            await ctx.send(embed = embedAuxilio(ctx, "Roles disponibles", ".rol Pícaros\n.rol ADDeditorialVIP"))
            log.logCall("rol", ctx.author.name)

        elif role == "pícaros":
            # dar rol
            member = ctx.message.author
            role_togive = find(lambda r: r.name == 'Pícaros', member.guild.roles)
            await member.add_roles(role_togive)

            # message
            await ctx.send(embed = embedDato(ctx, "Rol recibido con éxito!", "El rol Pícaros ya es tuyo. ¡Disfruta de sus privilegios!"))
            log.logCall(f"rol {role}", ctx.author.name)

        elif role == "addeditorialvip":
            # registro
            petition = io.open("registro.txt", 'a')
            petition.write(f"\nPetition: ADDeditorialVIP a {ctx.author.name}")
            petition.close()
            log.logEvent("ROL Petición de {role} registrada")

            # staff
            channel = client.get_channel(775820270614085674)
            await channel.send(embed = embedDato(ctx, "Petición de rol entrante:", f"{ctx.author.name} ha hecho una petición para recibir acceso a ADDeditorialVIP"))
            log.logEvent("ROL Petición de {role} notificada")

            # message
            await ctx.send(embed = embedDato(ctx, "Se ha registrado tu petición", "En caso de ser apto para el rol lo recibirás pronto."))
            log.logCall(f"rol {role}", ctx.author.name, True, "Petition")

        else:
            imageselector = random.randint(1,3)
            file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

            await ctx.send(file = file, embed = embedError(ctx))
            log.logFail(f"rol {role}", ctx.author.name, "ArgumentNotFoundError")

    else:
        await ctx.send(embed = embedDato(ctx, "Necesitas una cuenta.", "Aún no tienes una cuenta de *EL HIJO*\nUsa **.registro** para crear una ahora mismo."))

# .contador : El contador de palabras
@client.command()
async def contador(ctx):
    # counters
    read_chupapitos = io.open('counter_chupapitos.txt', 'r')
    ammount_chupapitos = read_chupapitos.readlines()
    read_chupapitos.close()

    read_maricon = io.open('counter_maricon.txt', 'r')
    ammount_maricon = read_maricon.readlines()
    read_maricon.close()

    # embed
    embed = discord.Embed(
    title = "Palabras muy usadas en el server:",
    description = "Esto dice mucho de nuestra sociedad...",
    color = discord.Color.blue()
    )
    embed.set_author(
    name = ctx.author.display_name,
    icon_url = ctx.author.avatar_url
    )
    embed.add_field(
    name = "Chupapitos",
    value = str(ammount_chupapitos[0]),
    inline = True
    )
    embed.add_field(
    name = "Maricón",
    value = str(ammount_maricon[0]),
    inline = True
    )
    embed.set_footer(
    text = "Muy interesante desde luego."
    )

    await ctx.send(embed = embed)
    log.logCall("contador", ctx.author.name)



## ACCOUNT commands
################################################################################
@client.command()
async def perfil(ctx, who = "Me"):
    # identifica la persona
    if who[:3] == "<@!" and who[3:-1] != str(ctx.author.id):
        # tal vez no eres tu, pero es una persona
        person = who[3:-1]

    elif who[:2] == "<@" and who[:3] != "<@!" and who[:3] != "<@&" and who[2:-1] != str(ctx.author.id):
        # más de lo mismo, pero para aquellos que mandan el argumento diferente
        person = who[2:-1]

    else:
        # who no es una persona, por lo tanto mostraremos tu cuenta
        person = ctx.author.id

    # encuentra el perfil y obtiene la información de este
    try:

        # puntos
        """
        encuentra_puntos = io.open(f"profile/{person}_profile/points.txt", 'r')
        cantidad_puntos = encuentra_puntos.readlines()
        encuentra_puntos.close()
        """
        cantidad_puntos = get_user(conn, f"'{person}'", "user_pt")

        points = cantidad_puntos[0]

        # credits
        """
        encuentra_credit = io.open(f"profile/{person}_profile/credit.txt", 'r')
        cantidad_credit = encuentra_credit.readlines()
        encuentra_credit.close()
        """
        cantidad_credit = get_user(conn, f"'{person}'", "user_cr")

        credit = cantidad_credit[0]

        # nivel
        """
        encuentra_level = io.open(f"profile/{person}_profile/level.txt", 'r')
        cantidad_level = encuentra_level.readlines()
        encuentra_level.close()
        """
        cantidad_level = get_user(conn, f"'{person}'", "user_lvl")

        level = cantidad_level[0]

        # prestige
        """
        encuentra_prestige = io.open(f"profile/{person}_profile/prestige.txt", 'r')
        cantidad_prestige = encuentra_prestige.readlines()
        encuentra_prestige.close()
        """
        cantidad_prestige = get_user(conn, f"'{person}'", "user_prestige")

        if cantidad_prestige[0] == "x" or cantidad_prestige[0] == "x\n":
            prestige = ""
        elif cantidad_prestige[0] == "x*" or cantidad_prestige[0] == "x*\n":
            prestige = " :dollar:"
        elif cantidad_prestige[0] == "x**" or cantidad_prestige[0] == "x**\n":
            prestige = " :euro:"
        elif cantidad_prestige[0] != "x" and cantidad_prestige[0] != "x*" and cantidad_prestige[0] != "x**" and cantidad_prestige[0] != "x\n" and cantidad_prestige[0] != "x*\n" and cantidad_prestige[0] != "x**\n":
            prestige = " :pound:"
        else:
            prestige = ""

        if person == ctx.author.id:
            reminder = f"La cuenta de usuario de **@{ctx.author.name}** en *EL HIJO*.\n¡Accede a tu información hoy mismo!"
        else:
            reminder = "Esta es la cuenta de usuario de otra persona en *EL HIJO*.\nPara acceder a la tuya no menciones a nadie."

    except FileNotFoundError:
        points = "No hay datos"
        credit = "No hay datos"
        level = "No hay datos"
        prestige = ""

        if person == ctx.author.id:
            reminder = "Aún no tienes una cuenta de *EL HIJO*\nUsa .registro para crear una ahora mismo."
        else:
            reminder = "Esta persona aún no tiene una cuenta de *EL HIJO*\nUsa .registro para crear una ahora mismo."

    if person == ctx.author.id:
        # embed
        embed = discord.Embed(
            title = ctx.author.display_name,
            description = reminder,
            color = discord.Color.blue()
        )

        embed.set_thumbnail(
            url = ctx.author.avatar_url
        )

        embed.add_field(
            name = "Puntos",
            value = points
        )

        embed.add_field(
            name = "Créditos",
            value = credit
        )

        embed.add_field(
            name = "Nivel",
            value = level + prestige
        )

        embed.set_footer(
            text = "Accede a información legal con .ficha"
        )

        # output
        await ctx.send(embed = embed)
        log.logCall("perfil", ctx.author.name, True, "Se muestra cuenta propia: " + who)

    else:
        # embed
        embed = discord.Embed(
            title = who,
            description = reminder,
            color = discord.Color.blue()
        )

        embed.add_field(
            name = "Puntos",
            value = points
        )

        embed.add_field(
            name = "Créditos",
            value = credit
        )

        embed.add_field(
            name = "Nivel",
            value = level + prestige
        )

        embed.set_footer(
            text = "No puedes acceder a la información legal de otros."
        )

        # output
        await ctx.send(embed = embed)
        log.logCall("perfil", ctx.author.name, True, "Se muestra cuenta ajena: " + who)

@client.command()
async def registro(ctx):

    # la cuenta ya existe
    try:
        """
        confirmation = io.open(f"profile/{ctx.author.id}_profile/points.txt", 'r')
        confirmation.close()
        """

        confirmation = get_user(conn, ctx.author.id, "user_pt")

        await ctx.send(embed = embedDato(ctx, "¡Pero si ya te has registrado!", "Revisa la información de tu cuenta con .perfil", "gold"))
        log.logFail("registro", ctx.author.name, "AccountExists")

    # nueva cuenta
    except:
        # carpeta
        #create_profile = os.makedirs(f"profile/{ctx.author.id}_profile", exist_ok = True)
        post_user(conn, ctx.author.id, ctx.author.name, 30, 0, 0, 0, 0, 0, 0, 0, 15, "x", 0)

        """
        # archivos
        create_points = io.open(f"profile/{ctx.author.id}_profile/points.txt", 'w')
        create_points.write("15")
        create_points.close()

        create_credit = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
        create_credit.write("30")
        create_credit.close()

        create_level = io.open(f"profile/{ctx.author.id}_profile/level.txt", 'w')
        create_level.write("0")
        create_level.close()

        create_prestige = io.open(f"profile/{ctx.author.id}_profile/prestige.txt", 'w')
        create_prestige.write("x")
        create_prestige.close()

        create_transac = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'w')
        create_transac.write("0")
        create_transac.close()

        create_emprs1 = io.open(f"profile/{ctx.author.id}_profile/emprs1.txt", 'w')
        create_emprs1.write("0")
        create_emprs1.close()

        create_emprs2 = io.open(f"profile/{ctx.author.id}_profile/emprs2.txt", 'w')
        create_emprs2.write("0")
        create_emprs2.close()

        create_emprs3 = io.open(f"profile/{ctx.author.id}_profile/emprs3.txt", 'w')
        create_emprs3.write("0")
        create_emprs3.close()

        create_emprs4 = io.open(f"profile/{ctx.author.id}_profile/emprs4.txt", 'w')
        create_emprs4.write("0")
        create_emprs4.close()

        create_emprs_n_1 = io.open(f"profile/{ctx.author.id}_profile/emprs_n_1.txt", 'w')
        create_emprs_n_1.write("0")
        create_emprs_n_1.close()

        create_emprs_n_2 = io.open(f"profile/{ctx.author.id}_profile/emprs_n_2.txt", 'w')
        create_emprs_n_2.write("0")
        create_emprs_n_2.close()

        create_multas = io.open(f"profile/{ctx.author.id}_profile/multas.txt", 'w')
        create_multas.write("")
        create_multas.close()
        """

        await ctx.send(embed = embedDato(ctx, "¡Tu cuenta ha sido creada con éxito!", ".perfil para más información"))
        log.logCall("registro", ctx.author.name)

@client.command()
async def ficha(ctx, who = "Me"):

    # identifica la persona
    if who[:3] == "<@!" and who[3:-1] != str(ctx.author.id):
        # tal vez no eres tu, pero es una persona
        person = who[3:-1]

    elif who[:2] == "<@" and who[:3] != "<@!" and who[:3] != "<@&" and who[2:-1] != str(ctx.author.id):
        # más de lo mismo, pero para aquellos que mandan el argumento diferente
        person = who[2:-1]

    else:
        # who no es una persona, por lo tanto mostraremos tu cuenta
        person = ctx.author.id

    try:

        abre_ficha = io.open(f"profile/{person}_profile/multas.txt", 'r')
        multas_now = abre_ficha.read()
        abre_ficha.close()

        if person == ctx.author.id:
            await ctx.send(embed = embedDato(ctx, f"Multas pendientes de {ctx.author.name}:", multas_now))
            log.logCall(f"ficha {who}", ctx.author.name, True, "Se muestra cuenta propia: " + who)

        else:
            await ctx.send(embed = embedDato(ctx, f"Multas pendientes de {who}:", multas_now))
            log.logCall(f"ficha {who}", ctx.author.name, True, "Se muestra cuenta ajena: " + who)

    except FileNotFoundError:

        if person == ctx.author.id:
            await ctx.send(embed = embedDato(ctx, f"Multas pendientes de {ctx.author.name}:", "*No hay datos, el usuario no tiene una cuenta.*"))
            log.logCall(f"ficha {who}", ctx.author.name, True, "Se muestra cuenta propia: " + who)

        else:
            await ctx.send(embed = embedDato(ctx, f"Multas pendientes de {who}:", "*No hay datos, el usuario no tiene una cuenta.*"))
            log.logCall(f"ficha {who}", ctx.author.name, True, "Se muestra cuenta ajena: " + who)



## FUNCIONES GRANDES
################################################################################

################################################################################
##---------------------------------BANCO SYS----------------------------------##
################################################################################

# .banco: Sistema de créditos
@client.command()
async def banco(ctx, path = None, func = "None", arg1 = None):

    if path == None:

        await ctx.send(embed = embedDato(ctx, "Esto es .banco", "Para ver los comandos usa **.banco auxilio**"))
        log.logCall(f"banco", ctx.author.name)

    elif path == "auxilio":

        await ctx.send(embed = embedDato(ctx, "Comandos de .banco", "**.banco mercado :** Muestra el precio de las acciones.\n**.banco mercado_negro :** -SECRETO-\n\n**.banco nivel :** Requisitos para subir de nivel.\n**.banco nivel mejora :** Sube de nivel y gana recompensas.\n\n**.banco compra/vende (número de la empresa) (cantidad) :** Comercia.\n**.banco compra_negro/vende_negro** ... : -SECRETO-\n**.banco transac (@usuario) (créditos) :** Regala créditos.\n**.banco trato :** Si tienes menos de 30 créditos y no consiguies avanzar en el juego puedes poner tu cuenta a 30 a cambio de perder un nivel. *(Con la excepción de ser nivel 0)*"))
        log.logCall(f"banco auxilio", ctx.author.name)

    elif path == "mercado":

        try:
            # encontrar los datos para todas las variables
            # 1

            """
            read_cant_emprs1 = io.open(f"profile/{ctx.author.id}_profile/emprs1.txt", 'r')
            actual_cant_emprs1 = read_cant_emprs1.readlines()
            read_cant_emprs1.close()

            read_stock_emprs1 = io.open(f"bolsa/cant/cant_emprs1.txt", 'r')
            actual_stock_emprs1 = read_stock_emprs1.readlines()
            read_stock_emprs1.close()

            read_cr_emprs1 = io.open(f"bolsa/cr/cr_emprs1.txt", 'r')
            actual_cr_emprs1 = read_cr_emprs1.readlines()
            read_cr_emprs1.close()

            # 2
            read_cant_emprs2 = io.open(f"profile/{ctx.author.id}_profile/emprs2.txt", 'r')
            actual_cant_emprs2 = read_cant_emprs2.readlines()
            read_cant_emprs2.close()

            read_stock_emprs2 = io.open(f"bolsa/cant/cant_emprs2.txt", 'r')
            actual_stock_emprs2 = read_stock_emprs2.readlines()
            read_stock_emprs2.close()

            read_cr_emprs2 = io.open(f"bolsa/cr/cr_emprs2.txt", 'r')
            actual_cr_emprs2 = read_cr_emprs2.readlines()
            read_cr_emprs2.close()

            # 3
            read_cant_emprs3 = io.open(f"profile/{ctx.author.id}_profile/emprs3.txt", 'r')
            actual_cant_emprs3 = read_cant_emprs3.readlines()
            read_cant_emprs3.close()

            read_stock_emprs3 = io.open(f"bolsa/cant/cant_emprs3.txt", 'r')
            actual_stock_emprs3 = read_stock_emprs3.readlines()
            read_stock_emprs3.close()

            read_cr_emprs3 = io.open(f"bolsa/cr/cr_emprs3.txt", 'r')
            actual_cr_emprs3 = read_cr_emprs3.readlines()
            read_cr_emprs3.close()

            # 4
            read_cant_emprs4 = io.open(f"profile/{ctx.author.id}_profile/emprs4.txt", 'r')
            actual_cant_emprs4 = read_cant_emprs4.readlines()
            read_cant_emprs4.close()

            read_stock_emprs4 = io.open(f"bolsa/cant/cant_emprs4.txt", 'r')
            actual_stock_emprs4 = read_stock_emprs4.readlines()
            read_stock_emprs4.close()

            read_cr_emprs4 = io.open(f"bolsa/cr/cr_emprs4.txt", 'r')
            actual_cr_emprs4 = read_cr_emprs4.readlines()
            read_cr_emprs4.close()
            """

            actual_cant_emprs1 = get_user(conn, f"'{ctx.author.id}'", "user_e1")
            actual_cant_emprs2 = get_user(conn, f"'{ctx.author.id}'", "user_e2")
            actual_cant_emprs3 = get_user(conn, f"'{ctx.author.id}'", "user_e3")
            actual_cant_emprs4 = get_user(conn, f"'{ctx.author.id}'", "user_e4")

            actual_stock_emprs1 = get_bot(conn, "'e_1'", "cant")
            actual_stock_emprs2 = get_bot(conn, "'e_2'", "cant")
            actual_stock_emprs3 = get_bot(conn, "'e_3'", "cant")
            actual_stock_emprs4 = get_bot(conn, "'e_4'", "cant")

            actual_cr_emprs1 = get_bot(conn, "'e_1'", "cr")
            actual_cr_emprs2 = get_bot(conn, "'e_2'", "cr")
            actual_cr_emprs3 = get_bot(conn, "'e_3'", "cr")
            actual_cr_emprs4 = get_bot(conn, "'e_4'", "cr")

            # embed
            embed = discord.Embed(
                title = "Mercado de la bolsa",
                description = "¿Cómo se muestran los datos?\n**0) Empresa (acciones a la venta) ~(tus acciones)**\nPrecio por acción",
                color = discord.Color.blue()
            )

            embed.set_author(
                name = ctx.author.display_name,
                icon_url = ctx.author.avatar_url
            )

            embed.add_field(
                name = f"1) Autistas Del Discord ({actual_stock_emprs1}) ~{actual_cant_emprs1}",
                value = actual_cr_emprs1,
                inline = False
            )

            embed.add_field(
                name = f"2) Send Nudes ({actual_stock_emprs2}) ~{actual_cant_emprs2}",
                value = actual_cr_emprs2,
                inline = False
            )

            embed.add_field(
                name = f"3) EMStudio ({actual_stock_emprs3}) ~{actual_cant_emprs3}",
                value = actual_cr_emprs3,
                inline = False
            )

            embed.add_field(
                name = f"4) El Hijo Corp. ({actual_stock_emprs4}) ~{actual_cant_emprs4}",
                value = actual_cr_emprs4,
                inline = False
            )

            await ctx.send(embed = embed)
            log.logCall(f"banco mercado", ctx.author.name, True, f"{actual_cr_emprs1} | {actual_cr_emprs2} | {actual_cr_emprs3} | {actual_cr_emprs4}")

        except FileNotFoundError:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail("banco mercado", ctx.author.name, "AccountNotFoundError")

    elif path == "mercado_negro":

        try:
            ## CONTROL de nivel
            ########################################################################
            allowed = lvl.check_license(ctx, 4)
            ########################################################################

            if allowed == True:

                # encontrar los datos para todas las variables
                # n_1

                """
                read_cant_emprs_n_1 = io.open(f"profile/{ctx.author.id}_profile/emprs_n_1.txt", 'r')
                actual_cant_emprs_n_1 = read_cant_emprs_n_1.readlines()
                read_cant_emprs_n_1.close()

                read_stock_emprs_n_1 = io.open(f"bolsa/cant/cant_emprs_n_1.txt", 'r')
                actual_stock_emprs_n_1 = read_stock_emprs_n_1.readlines()
                read_stock_emprs_n_1.close()

                read_cr_emprs_n_1 = io.open(f"bolsa/cr/cr_emprs_n_1.txt", 'r')
                actual_cr_emprs_n_1 = read_cr_emprs_n_1.readlines()
                read_cr_emprs_n_1.close()

                # n_2
                read_cant_emprs_n_2 = io.open(f"profile/{ctx.author.id}_profile/emprs_n_2.txt", 'r')
                actual_cant_emprs_n_2 = read_cant_emprs_n_2.readlines()
                read_cant_emprs_n_2.close()

                read_stock_emprs_n_2 = io.open(f"bolsa/cant/cant_emprs_n_2.txt", 'r')
                actual_stock_emprs_n_2 = read_stock_emprs_n_2.readlines()
                read_stock_emprs_n_2.close()

                read_cr_emprs_n_2 = io.open(f"bolsa/cr/cr_emprs_n_2.txt", 'r')
                actual_cr_emprs_n_2 = read_cr_emprs_n_2.readlines()
                read_cr_emprs_n_2.close()
                """

                actual_cant_emprs_n_1 = get_user(conn, f"'{ctx.author.id}'", "user_n1")
                actual_cant_emprs_n_2 = get_user(conn, f"'{ctx.author.id}'", "user_n2")

                actual_stock_emprs_n_1 = get_bot(conn, "'e_n1'", "cant")
                actual_stock_emprs_n_2 = get_bot(conn, "'e_n2'", "cant")

                actual_cr_emprs_n_1 = get_bot(conn, "'e_n1'", "cr")
                actual_cr_emprs_n_2 = get_bot(conn, "'e_n2'", "cr")

                # embed
                embed = discord.Embed(
                    title = "Mercado negro",
                    description = "¿Cómo se muestran los datos?\n**0) Empresa (acciones a la venta) ~(tus acciones)**\nPrecio por acción",
                    color = discord.Color.dark_grey()
                )

                embed.set_author(
                    name = ctx.author.display_name,
                    icon_url = ctx.author.avatar_url
                )

                embed.add_field(
                    name = f"1) PozoHub ({actual_stock_emprs_n_1}) ~{actual_cant_emprs_n_1}",
                    value = actual_cr_emprs_n_1,
                    inline = False
                )

                embed.add_field(
                    name = f"2) PlsPorn Ent. ({actual_stock_emprs_n_2}) ~{actual_cant_emprs_n_2}",
                    value = actual_cr_emprs_n_2,
                    inline = False
                )

                await ctx.send(embed = embed)
                log.logCall(f"banco mercado_negro", ctx.author.name, True, f"{actual_cr_emprs_n_1} | {actual_cr_emprs_n_2}")

            else:

                await ctx.send(embed = embedDato(ctx, "¡Tu nivel es insuficiente!", "Necesitas ser nivel 4 para usar este comando.", "gold"))
                log.logFail("banco mercado_negro", ctx.author.name, "NotAllowedError")

        except:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail("banco mercado_negro", ctx.author.name, "AccountNotFoundError")

    elif path == "nivel" and func != "mejora":

        try:
            # obtiene la información necesaria
            level = lvl.determinate_license(ctx)
            next_level = int(level) + 1

            # procesos logicos
            if next_level == 1:
                price = "Acceso al juego de la moneda"

                desc1 = "Consigue 500 créditos"
                desc2 = "Haz 10 transacciones"

                # objetivo 1
                """
                check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()
                """

                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                if int(cr_user) >= 500:
                    completion1 = ":white_check_mark: -> *Completado*"
                else:
                    completion1 = f":x: -> *Por completar* ({cr_user})"

                # objetivo 2
                """
                check_transac_user = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'r')
                transac_user = check_transac_user.readlines()
                check_transac_user.close()
                """
                transac_user = get_user(conn, f"'{ctx.author.id}'", "user_transac")

                if int(transac_user) >= 10:
                    completion2 = ":white_check_mark: -> *Completado*"
                else:
                    completion2 = f":x: -> *Por completar* ({transac_user})"

            elif next_level == 2:
                price = "Acceso al juego del bote"

                desc1 = "Consigue 2500 créditos"
                desc2 = "Haz 25 transacciones"

                # objetivo 1
                """
                check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()
                """
                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                if int(cr_user) >= 2500:
                    completion1 = ":white_check_mark: -> *Completado*"
                else:
                    completion1 = f":x: -> *Por completar* ({cr_user})"

                # objetivo 2
                """
                check_transac_user = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'r')
                transac_user = check_transac_user.readlines()
                check_transac_user.close()
                """
                transac_user = get_user(conn, f"'{ctx.author.id}'", "user_transac")

                if int(transac_user) >= 25:
                    completion2 = ":white_check_mark: -> *Completado*"
                else:
                    completion2 = f":x: -> *Por completar* ({transac_user})"

            elif next_level == 3:
                price = "Acceso al juego de la tragaperras"

                desc1 = "Consigue 10000 créditos"
                desc2 = "Haz 50 transacciones"

                # objetivo 1
                """
                check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()
                """
                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                if int(cr_user) >= 10000:
                    completion1 = ":white_check_mark: -> *Completado*"
                else:
                    completion1 = f":x: -> *Por completar* ({cr_user})"

                # objetivo 2
                """
                check_transac_user = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'r')
                transac_user = check_transac_user.readlines()
                check_transac_user.close()
                """
                transac_user = get_user(conn, f"'{ctx.author.id}'", "user_transac")

                if int(transac_user) >= 50:
                    completion2 = ":white_check_mark: -> *Completado*"
                else:
                    completion2 = f":x: -> *Por completar* ({transac_user})"

            elif next_level == 4:
                price = "Desbloquea el misterioso mercado negro..."

                desc1 = "Consigue 100000 créditos"
                desc2 = "Haz 100 transacciones"

                # objetivo 1
                """
                check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()
                """
                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                if int(cr_user) >= 100000:
                    completion1 = ":white_check_mark: -> *Completado*"
                else:
                    completion1 = f":x: -> *Por completar* ({cr_user})"

                # objetivo 2
                """
                check_transac_user = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'r')
                transac_user = check_transac_user.readlines()
                check_transac_user.close()
                """
                transac_user = get_user(conn, f"'{ctx.author.id}'", "user_transac")

                if int(transac_user) >= 100:
                    completion2 = ":white_check_mark: -> *Completado*"
                else:
                    completion2 = f":x: -> *Por completar* ({transac_user})"

            else:
                price = "El rol de Maestro Inversor y una recompensa secreta...\n\n*Al subir a nivel 5 completas el juego y por lo tanto se reiniciará tu cuenta para empezar de nuevo.*\n*Sin embargo .banco te recompensará por cada vez que completes el juego, vale la pena hacerlo varias veces :)*"

                desc1 = "Consigue 500000 créditos"
                desc2 = "Vende todas tus acciones"

                # objetivo 1
                """
                check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()
                """
                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                if int(cr_user) >= 500000:
                    completion1 = ":white_check_mark: -> *Completado*"
                else:
                    completion1 = f":x: -> *Por completar* ({cr_user})"

                # objetivo 2
                """
                check_emprs1_user = io.open(f"profile/{ctx.author.id}_profile/emprs1.txt", 'r')
                emprs1_user = check_emprs1_user.readlines()
                check_emprs1_user.close()

                check_emprs2_user = io.open(f"profile/{ctx.author.id}_profile/emprs2.txt", 'r')
                emprs2_user = check_emprs2_user.readlines()
                check_emprs2_user.close()

                check_emprs3_user = io.open(f"profile/{ctx.author.id}_profile/emprs3.txt", 'r')
                emprs3_user = check_emprs3_user.readlines()
                check_emprs3_user.close()

                check_emprs4_user = io.open(f"profile/{ctx.author.id}_profile/emprs4.txt", 'r')
                emprs4_user = check_emprs4_user.readlines()
                check_emprs4_user.close()

                check_emprs_n_1_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_1.txt", 'r')
                emprs_n_1_user = check_emprs_n_1_user.readlines()
                check_emprs_n_1_user.close()

                check_emprs_n_2_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_2.txt", 'r')
                emprs_n_2_user = check_emprs_n_2_user.readlines()
                check_emprs_n_2_user.close()
                """
                emprs1_user    = get_user(conn, f"'{ctx.author.id}'", "user_e1")
                emprs2_user    = get_user(conn, f"'{ctx.author.id}'", "user_e2")
                emprs3_user    = get_user(conn, f"'{ctx.author.id}'", "user_e3")
                emprs4_user    = get_user(conn, f"'{ctx.author.id}'", "user_e4")
                emprs_n_1_user = get_user(conn, f"'{ctx.author.id}'", "user_n1")
                emprs_n_2_user = get_user(conn, f"'{ctx.author.id}'", "user_n2")


                if emprs1_user == "0" and emprs2_user == "0" and emprs3_user == "0" and emprs4_user == "0" and emprs_n_1_user == "0" and emprs_n_2_user == "0":
                    completion2 = ":white_check_mark: -> *Completado*"
                else:
                    completion2 = ":x: -> *Por completar*"

            await ctx.send(embed = embedDato(ctx, f"Siguiente nivel: {next_level}", f"**Recompensas:**\n{price}\n\n**Objetivos:**\n{completion1} ```{desc1}```\n{completion2} ```{desc2}```"))
            log.logCall(f"banco nivel", ctx.author.name, True, f"Mirando para el nivel {next_level}")

        except:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail("banco nivel", ctx.author.name, "AccountNotFoundError")

    elif path == "nivel" and func == "mejora":

        try:
            level = lvl.determinate_license(ctx)
            next_level = int(level) + 1

            # datos para comparación con los requisitos
            # credits
            """
            check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
            cr_user = check_cr_user.readlines()
            check_cr_user.close()
            """
            cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

            cr_comparation = int(cr_user)

            # transac
            """
            check_transac_user = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'r')
            transac_user = check_transac_user.readlines()
            check_transac_user.close()
            """
            transac_user = get_user(conn, f"'{ctx.author.id}'", "user_transac")

            transac_comparation = int(transac_user)

            # comprueva los requisitos
            # si todo está bien y no cae en ningún return te cobra
            if next_level == 1:

                if cr_comparation >= 500 and transac_comparation >= 10:
                    """
                    cobra_cr = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    cobra_cr.write( str( cr_comparation - 500 ) )
                    cobra_cr.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", "user_cr", f"{cr_comparation-500}")
                else:
                    await ctx.send(embed = embedDato(ctx, "No cumples los requisitos.", "Revisa las condiciones para subir de nivel con **.banco nivel**", "gold"))
                    log.logFail("banco nivel mejora", ctx.author.name, "NotAllowedError")
                    return

            elif next_level == 2:

                if cr_comparation >= 2500 and transac_comparation >= 25:
                    """
                    cobra_cr = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    cobra_cr.write( str( cr_comparation - 2500 ) )
                    cobra_cr.close()
                    """

                    put_user(conn, f"'{ctx.author.id}'", "user_cr", f"{cr_comparation-2500}")
                else:
                    await ctx.send(embed = embedDato(ctx, "No cumples los requisitos.", "Revisa las condiciones para subir de nivel con **.banco nivel**", "gold"))
                    log.logFail("banco nivel mejora", ctx.author.name, "NotAllowedError")
                    return

            elif next_level == 3:

                if cr_comparation >= 10000 and transac_comparation >= 50:
                    """
                    cobra_cr = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    cobra_cr.write( str( cr_comparation - 10000 ) )
                    cobra_cr.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", "user_cr", f"{cr_comparation-10000}")
                else:
                    await ctx.send(embed = embedDato(ctx, "No cumples los requisitos.", "Revisa las condiciones para subir de nivel con **.banco nivel**", "gold"))
                    log.logFail("banco nivel mejora", ctx.author.name, "NotAllowedError")
                    return

            elif next_level == 4:

                if cr_comparation >= 100000 and transac_comparation >= 100:
                    """
                    cobra_cr = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    cobra_cr.write( str( cr_comparation - 100000 ) )
                    cobra_cr.close()
                    """
                    cobra_cr = put_user(conn, f"'{ctx.author.id}'", "user_cr", f"{cr_comparation-100000}")
                else:
                    await ctx.send(embed = embedDato(ctx, "No cumples los requisitos.", "Revisa las condiciones para subir de nivel con **.banco nivel**", "gold"))
                    log.logFail("banco nivel mejora", ctx.author.name, "NotAllowedError")
                    return

            else:

                # concretamente en caso de subir a nivel 5:
                # mira que haya vendido todas las acciones
                """
                check_emprs1_user = io.open(f"profile/{ctx.author.id}_profile/emprs1.txt", 'r')
                emprs1_user = check_emprs1_user.readlines()
                check_emprs1_user.close()

                check_emprs2_user = io.open(f"profile/{ctx.author.id}_profile/emprs2.txt", 'r')
                emprs2_user = check_emprs2_user.readlines()
                check_emprs2_user.close()

                check_emprs3_user = io.open(f"profile/{ctx.author.id}_profile/emprs3.txt", 'r')
                emprs3_user = check_emprs3_user.readlines()
                check_emprs3_user.close()

                check_emprs4_user = io.open(f"profile/{ctx.author.id}_profile/emprs4.txt", 'r')
                emprs4_user = check_emprs4_user.readlines()
                check_emprs4_user.close()

                check_emprs_n_1_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_1.txt", 'r')
                emprs_n_1_user = check_emprs_n_1_user.readlines()
                check_emprs_n_1_user.close()

                check_emprs_n_2_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_2.txt", 'r')
                emprs_n_2_user = check_emprs_n_2_user.readlines()
                check_emprs_n_2_user.close()
                """
                emprs1_user    = get_user(conn, f"'{ctx.author.id}'", "user_e1")
                emprs2_user    = get_user(conn, f"'{ctx.author.id}'", "user_e2")
                emprs3_user    = get_user(conn, f"'{ctx.author.id}'", "user_e3")
                emprs4_user    = get_user(conn, f"'{ctx.author.id}'", "user_e4")
                emprs_n_1_user = get_user(conn, f"'{ctx.author.id}'", "user_n1")
                emprs_n_2_user = get_user(conn, f"'{ctx.author.id}'", "user_n1")

                if cr_comparation >= 500000 and emprs1_user == 0 and emprs2_user == 0 and emprs3_user == 0 and emprs4_user == 0 and emprs_n_1_user == 0 and emprs_n_2_user == 0:
                    """
                    cobra_cr = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    cobra_cr.write( str( cr_comparation - 500000 ) )
                    cobra_cr.close()
                    """
                    cobra_cr = put_user(conn, f"'{ctx.author.id}'", "user_cr", f"{cr_comparation-500000}")
                else:
                    await ctx.send(embed = embedDato(ctx, "No cumples los requisitos.", "Revisa las condiciones para subir de nivel con **.banco nivel**", "gold"))
                    log.logFail("banco nivel mejora", ctx.author.name, "NotAllowedError")
                    return

            # si todo está correcto y no hay return
            # ya te habrá cobrado y ahora:

            # sube de nivel
            # (la función ya reinicia las transac) x ya no, pero el codigo sigue intacto en la función
            lvl.asign_license(ctx)

            await ctx.send(embed = embedDato(ctx, "¡Has subido de nivel!", "Ya puedes acceder a tus recompensas."))
            log.logCall("banco nivel mejora", ctx.author.name, True, next_level)

        except:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail("banco nivel mejora", ctx.author.name, "AccountNotFoundError")

    elif path == "compra" or path == "vende":

        if path == "compra":

            try:
                func = int(func)
                arg1 = int(arg1)

                try:

                    # CONTROLES ####################################################
                    # mira las acciones disponibles
                    """
                    check_cant_stock = io.open(f"bolsa/cant/cant_emprs{func}.txt", 'r')
                    cant_stock = check_cant_stock.readlines()
                    check_cant_stock.close()
                    """
                    cant_stock = get_bot(conn, f"'e_{func}'", "cant")

                    # mira su precio
                    """
                    check_cr_stock = io.open(f"bolsa/cr/cr_emprs{func}.txt", 'r')
                    cr_stock = check_cr_stock.readlines()
                    check_cr_stock.close()
                    """
                    cr_stock = get_bot(conn, f"'e_{func}'", "cr")

                    # mira tu saldo
                    """
                    check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                    cr_user = check_cr_user.readlines()
                    check_cr_user.close()
                    """
                    cr_user = get_user(conn, f"'{ctx.author.id}'", "cr")

                    # calcula las comisiones
                    comisiones = round( ( int(cr_stock[0]) * int(arg1) ) * 0.1 )

                    # compara los datos
                    if int(cant_stock[0]) < int(arg1):

                        await ctx.send(embed = embedDato(ctx, f"No quedan {arg1} acciones de la empresa {func}", f"Revisa las acciones disponibles con **.banco mercado**", "gold"))
                        log.logFail(f"banco compra {func} {arg1}", ctx.author.name, "IndexError")
                        return

                    if (int(cr_stock[0]) * int(arg1)) + comisiones > int(cr_user[0]):

                        await ctx.send(embed = embedDato(ctx, f"No tienes suficiente saldo para llevar a cabo la operación", f"Espera a que baje el precio de las acciones...", "gold"))
                        log.logFail(f"banco compra {func} {arg1}", ctx.author.name, "IndexError")
                        return

                    # si pasas todos los controles y la compra es posible ##########
                    # te cobra el precio de las acciones + comisiones 10%
                    """
                    rest_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    """
                    gastos = int(cr_stock[0]) * int(arg1) + comisiones
                    current_cr = str( int(cr_user[0]) - gastos )
                    """
                    rest_cr_user.write(current_cr)
                    rest_cr_user.close()
                    """
                    put_bot(conn, f"'e_{func}''", "cr", int(current_cr))

                    # resta las acciones compradas a las totales
                    """
                    apply_cant_stock = io.open(f"bolsa/cant/cant_emprs{func}.txt", 'w')
                    apply_cant_stock.write(str( int(cant_stock[0]) - int(arg1) ))
                    apply_cant_stock.close()
                    """
                    put_bot(conn, f"'e_{func}'", "cant", int(cant_stock[0]) - int(arg1))

                    # añade esas acciones a las tuyas
                    """
                    check_stock_user = io.open(f"profile/{ctx.author.id}_profile/emprs{func}.txt", 'r')
                    stock_user = check_stock_user.readlines()
                    check_stock_user.close()
                    """
                    stock_user = get_user(conn, f"'{ctx.author.id}'", f"user_e{func}")

                    """
                    apply_stock_user = io.open(f"profile/{ctx.author.id}_profile/emprs{func}.txt", 'w')
                    apply_stock_user.write(str( int(stock_user[0]) + int(arg1) ))
                    apply_stock_user.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", f"user_e{func}", int(stock_user) + int(arg1))


                    # msg
                    await ctx.send(embed = embedDato(ctx, "Operación satisfecha:", f"Compradas {arg1} acciones de la empresa {func}\nGastos = **{gastos}**"))
                    log.logCall(f"banco compra {func} {arg1}", ctx.author.name, True, f"{arg1} acciones {func} por {gastos}")

                except:

                    imageselector = random.randint(1,3)
                    file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                    await ctx.send(file = file, embed = embedError(ctx))
                    log.logFail(f"banco compra {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

            except:

                imageselector = random.randint(1,3)
                file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                await ctx.send(file = file, embed = embedError(ctx))
                log.logFail(f"banco compra {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

        else:

            try:
                func = int(func)
                arg1 = int(arg1)

                try:

                    # CONTROLES ####################################################
                    # mira si tienes las acciones
                    """
                    check_stock_user = io.open(f"profile/{ctx.author.id}_profile/emprs{func}.txt", 'r')
                    stock_user = check_stock_user.readlines()
                    check_stock_user.close()
                    """
                    stock_user = get_user(conn, f"'{ctx.author.id}'", f"user_e{func}")

                    if int(stock_user[0]) >= int(arg1):
                        pass
                    else:
                        await ctx.send(embed = embedDato(ctx, f"No tienes {arg1} acciones de la empresa {func}", f"Compra con **.banco compra {func} {arg1}**", "gold"))
                        log.logFail(f"banco vende {func} {arg1}", ctx.author.name, "IndexError")
                        return

                    # si pasas todos los controles y la venta es posible ###########
                    # te paga
                    """
                    check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                    cr_user = check_cr_user.readlines()
                    check_cr_user.close()
                    """
                    cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                    """
                    check_cr_stock = io.open(f"bolsa/cr/cr_emprs{func}.txt", 'r')
                    cr_stock = check_cr_stock.readlines()
                    check_cr_stock.close()
                    """
                    cr_stock = get_bot(conn, f"'e_{func}'", "cr")

                    """
                    pay_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    """
                    ingresos = int(cr_stock[0]) * int(arg1)
                    current_cr = str( int(cr_user[0]) + ingresos )
                    """
                    pay_cr_user.write(current_cr)
                    pay_cr_user.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", "user_cr", current_cr)

                    # resta las acciones vendidas a las tuyas
                    """
                    apply_stock_user = io.open(f"profile/{ctx.author.id}_profile/emprs{func}.txt", 'w')
                    apply_stock_user.write(str( int(stock_user[0]) - int(arg1) ))
                    apply_stock_user.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", f"user_e{func}", int(stock_user[0]) - int(arg1))

                    # añade esas acciones a las totales
                    """
                    check_cant_stock = io.open(f"bolsa/cant/cant_emprs{func}.txt", 'r')
                    cant_stock = check_cant_stock.readlines()
                    check_cant_stock.close()
                    """
                    cant_stock = get_bot(conn, f"'e_{func}'", "cant")

                    """
                    apply_cant_stock = io.open(f"bolsa/cant/cant_emprs{func}.txt", 'w')
                    apply_cant_stock.write(str( int(cant_stock[0]) + int(arg1) ))
                    apply_cant_stock.close()
                    """
                    put_bot(conn, f"'e_{func}'", "cant", int(cant_stock[0]) + int(arg1))

                    # msg
                    await ctx.send(embed = embedDato(ctx, "Operación satisfecha:", f"Vendidas {arg1} acciones de la empresa {func}\nIngresos = **{ingresos}**"))
                    log.logCall(f"banco vende {func} {arg1}", ctx.author.name, True, f"{arg1} acciones {func} por {ingresos}")

                except:

                    imageselector = random.randint(1,3)
                    file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                    await ctx.send(file = file, embed = embedError(ctx))
                    log.logFail(f"banco vende {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

            except:

                imageselector = random.randint(1,3)
                file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                await ctx.send(file = file, embed = embedError(ctx))
                log.logFail(f"banco vende {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

    elif path == "compra_negro" or path == "vende_negro":

        if path == "compra_negro":

            try:
                func = int(func)
                arg1 = int(arg1)

                try:

                    # CONTROLES ####################################################
                    # mira las acciones disponibles
                    """
                    check_cant_stock = io.open(f"bolsa/cant/cant_emprs_n_{func}.txt", 'r')
                    cant_stock = check_cant_stock.readlines()
                    check_cant_stock.close()
                    """
                    cant_stock = get_bot(conn, f"'e_n{func}'", "cant")

                    # mira su precio
                    """
                    check_cr_stock = io.open(f"bolsa/cr/cr_emprs_n_{func}.txt", 'r')
                    cr_stock = check_cr_stock.readlines()
                    check_cr_stock.close()
                    """
                    cr_stock = get_bot(conn, f"'e_n{func}'", "cr")

                    # mira tu saldo
                    """
                    check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                    cr_user = check_cr_user.readlines()
                    check_cr_user.close()
                    """
                    cr_user = get_user(conn, f"'{ctx.author.id}'", f"user_n{func}")

                    # calcula las comisiones
                    comisiones = round( ( int(cr_stock[0]) * int(arg1) ) * 0.1 )

                    # compara los datos
                    if int(cant_stock[0]) < int(arg1):

                        await ctx.send(embed = embedDato(ctx, f"No quedan {arg1} acciones de la empresa {func}", f"Revisa las acciones disponibles con **.banco mercado**", "gold"))
                        log.logFail(f"banco compra_negro {func} {arg1}", ctx.author.name, "IndexError")
                        return

                    if (int(cr_stock[0]) * int(arg1)) + comisiones > int(cr_user[0]):

                        await ctx.send(embed = embedDato(ctx, f"No tienes suficiente saldo para llevar a cabo la operación", f"Espera a que baje el precio de las acciones...", "gold"))
                        log.logFail(f"banco compra_negro {func} {arg1}", ctx.author.name, "IndexError")
                        return

                    # si pasas todos los controles y la compra es posible ##########
                    # te cobra el precio de las acciones + comisiones 10%
                    """
                    rest_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    """
                    gastos = int(cr_stock[0]) * int(arg1) + comisiones
                    current_cr = str( int(cr_user[0]) - gastos )
                    """
                    rest_cr_user.write(current_cr)
                    rest_cr_user.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", "user_cr", int(cr_user[0]) - gastos)

                    # resta las acciones compradas a las totales
                    """
                    apply_cant_stock = io.open(f"bolsa/cant/cant_emprs_n_{func}.txt", 'w')
                    apply_cant_stock.write(str( int(cant_stock[0]) - int(arg1) ))
                    apply_cant_stock.close()
                    """
                    put_bot(conn, f"'e_n{func}'", "cant", int(cant_stock[0]) - int(arg1))

                    # añade esas acciones a las tuyas
                    """
                    check_stock_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_{func}.txt", 'r')
                    stock_user = check_stock_user.readlines()
                    check_stock_user.close()
                    """
                    stock_user = get_user(conn, f"'{ctx.author.id}'", f"user_n{func}")

                    """
                    apply_stock_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_{func}.txt", 'w')
                    apply_stock_user.write(str( int(stock_user[0]) + int(arg1) ))
                    apply_stock_user.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", f"user_n{func}", int(stock_user[0]) + int(arg1))

                    # msg
                    await ctx.send(embed = embedDato(ctx, "Operación satisfecha:", f"Compradas {arg1} acciones de la empresa {func}\nGastos = **{gastos}**"))
                    log.logCall(f"banco compra_negro {func} {arg1}", ctx.author.name, True, f"{arg1} acciones {func} por {gastos}")

                except:

                    imageselector = random.randint(1,3)
                    file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                    await ctx.send(file = file, embed = embedError(ctx))
                    log.logFail(f"banco compra_negro {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

            except:

                imageselector = random.randint(1,3)
                file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                await ctx.send(file = file, embed = embedError(ctx))
                log.logFail(f"banco compra_negro {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

        else:

            try:
                func = int(func)
                arg1 = int(arg1)

                try:

                    # CONTROLES ####################################################
                    # mira si tienes las acciones
                    """
                    check_stock_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_{func}.txt", 'r')
                    stock_user = check_stock_user.readlines()
                    check_stock_user.close()
                    """
                    stock_user = get_user(conn, f"'{ctx.author.id}'", f"user_n{func}")

                    if int(stock_user[0]) >= int(arg1):
                        pass
                    else:
                        await ctx.send(embed = embedDato(ctx, f"No tienes {arg1} acciones de la empresa {func}", f"Compra con **.banco compra {func} {arg1}**", "gold"))
                        log.logFail(f"banco vende_negro {func} {arg1}", ctx.author.name, "IndexError")
                        return

                    # si pasas todos los controles y la venta es posible ###########
                    # te paga
                    """
                    check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                    cr_user = check_cr_user.readlines()
                    check_cr_user.close()
                    """
                    cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                    """
                    check_cr_stock = io.open(f"bolsa/cr/cr_emprs_n_{func}.txt", 'r')
                    cr_stock = check_cr_stock.readlines()
                    check_cr_stock.close()
                    """
                    cr_stock = get_bot(conn, f"'e_n{func}'", "cr")

                    """
                    pay_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                    """
                    ingresos = int(cr_stock[0]) * int(arg1)
                    current_cr = str( int(cr_user[0]) + ingresos )
                    """
                    pay_cr_user.write(current_cr)
                    pay_cr_user.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", "user_cr", int(cr_user[0]) + ingresos)

                    # resta las acciones vendidas a las tuyas
                    """
                    apply_stock_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_{func}.txt", 'w')
                    apply_stock_user.write(str( int(stock_user[0]) - int(arg1) ))
                    apply_stock_user.close()
                    """
                    put_user(conn, f"'{ctx.author.id}'", f"user_n{func}", int(stock_user[0]) - int(arg1))

                    # añade esas acciones a las totales
                    """
                    check_cant_stock = io.open(f"bolsa/cant/cant_emprs_n_{func}.txt", 'r')
                    cant_stock = check_cant_stock.readlines()
                    check_cant_stock.close()
                    """
                    cant_stock = get_bot(conn, f"e_n{func}", "cant")

                    """
                    apply_cant_stock = io.open(f"bolsa/cant/cant_emprs_n_{func}.txt", 'w')
                    apply_cant_stock.write(str( int(cant_stock[0]) + int(arg1) ))
                    apply_cant_stock.close()
                    """
                    put_bot(conn, f"'e_n{func}'", "cant", int(cant_stock[0]) + int(arg1))

                    # msg
                    await ctx.send(embed = embedDato(ctx, "Operación satisfecha:", f"Vendidas {arg1} acciones de la empresa {func}\nIngresos = **{ingresos}**"))
                    log.logCall(f"banco vende_negro {func} {arg1}", ctx.author.name, True, f"{arg1} acciones {func} por {ingresos}")

                except:

                    imageselector = random.randint(1,3)
                    file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                    await ctx.send(file = file, embed = embedError(ctx))
                    log.logFail(f"banco vende_negro {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

            except:

                imageselector = random.randint(1,3)
                file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                await ctx.send(file = file, embed = embedError(ctx))
                log.logFail(f"banco vende_negro {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

    elif path == "transac":

        try:
            who = func

            # identifica la persona
            if who[:3] == "<@!" and who[3:-1] != str(ctx.author.id):
                # es una persona
                person = who[3:-1]

            elif who[:2] == "<@" and who[:3] != "<@!" and who[:3] != "<@&" and who[2:-1] != str(ctx.author.id):
                # es una persona con otro formato
                person = who[2:-1]

            else:
                # who no es una persona o eres tu, por lo tanto lo diremos
                imageselector = random.randint(1,3)
                file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                await ctx.send(file = file, embed = embedError(ctx))
                log.logFail(f"banco {path} {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")
                return

            # CONTROLES DE SEGURIDAD PARA MIRAR QUE TODOS LOS ARGUMENTOS SON POSIBLES
            permiso = False
            """
            check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
            cr_user = check_cr_user.readlines()
            check_cr_user.close()
            """
            cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

            try:
                inttester = arg1
                inttester = int(inttester)

            except:
                imageselector = random.randint(1,3)
                file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                await ctx.send(file = file, embed = embedError(ctx))
                log.logFail(f"banco {path} {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")
                return

            if int(cr_user[0]) < int(arg1):
                permiso = False

                await ctx.send(embed = embedDato(ctx, "No tienes tantos créditos.", f"Tienes **{cr_user[0]}** de **{arg1}** créditos.", "gold"))
                log.logFail(f"banco transac {func} {arg1}", ctx.author.name, "IndexError")
                return

            else:
                permiso = True

            try:
                """
                check_cr_user = io.open(f"profile/{person}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()
                """
                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

            except:
                permiso = False

                await ctx.send(embed = embedDato(ctx, "El usuario indicado no tiene cuenta.", f"Prueba con otra persona.", "gold"))
                log.logFail(f"banco transac {func} {arg1}", ctx.author.name, "IndexError")
                return

            # PASADOS LOS CONTROLES YA SE PUEDE EJECUTAR LA OPERACIÓN
            if permiso == True:

                # te quita dinero
                """
                check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()
                """
                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                """
                apply_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                apply_cr_user.write(str( int(cr_user[0]) - int(arg1) ))
                apply_cr_user.close()
                """
                put_user(conn, f"'{ctx.author.id}'", "user_cr", int(cr_user[0]) - int(arg1))

                # da el dinero
                """
                check_cr_user = io.open(f"profile/{person}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()
                """
                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                """
                apply_cr_user = io.open(f"profile/{person}_profile/credit.txt", 'w')
                apply_cr_user.write(str( int(cr_user[0]) + int(arg1) ))
                apply_cr_user.close()
                """
                put_user(conn, f"'{ctx.author.id}'", "user_cr", int(cr_user[0]) + int(arg1))

                # cuenta que has hecho la transacción
                """
                check_transac_user = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'r')
                transac_user = check_transac_user.readlines()
                check_transac_user.close()
                """
                transac_user = get_user(conn, f"'{ctx.author.id}'", "user_transac")

                """
                apply_transac_user = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'w')
                apply_transac_user.write(str( int(transac_user[0]) + 1 ))
                apply_transac_user.close()
                """
                put_user(conn, f"'{ctx.author.id}'", "user_transac", int(transac_user[0]) + 1)

                # manda el mensaje
                await ctx.send(embed = embedDato(ctx, "La transacción ha sido llevada a cabo con éxito", f"La cuenta del usuario indicado ha recibido **{arg1}** créditos."))
                log.logCall(f"banco transac {func} {arg1}", ctx.author.name, True, f"{arg1} cr a la cuenta {func}")

        except:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail(f"banco transac {func} {arg1}", ctx.author.name, "AccountNotFoundError")

    elif path == "trato":

        try:
            # revisa que no exista ninguna forma de ganar dinero
            # aka acciones por vender
            """
            check_emprs1_user = io.open(f"profile/{ctx.author.id}_profile/emprs1.txt", 'r')
            emprs1_user = check_emprs1_user.readlines()
            check_emprs1_user.close()

            check_emprs2_user = io.open(f"profile/{ctx.author.id}_profile/emprs2.txt", 'r')
            emprs2_user = check_emprs2_user.readlines()
            check_emprs2_user.close()

            check_emprs3_user = io.open(f"profile/{ctx.author.id}_profile/emprs3.txt", 'r')
            emprs3_user = check_emprs3_user.readlines()
            check_emprs3_user.close()

            check_emprs4_user = io.open(f"profile/{ctx.author.id}_profile/emprs4.txt", 'r')
            emprs4_user = check_emprs4_user.readlines()
            check_emprs4_user.close()

            check_emprs_n_1_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_1.txt", 'r')
            emprs_n_1_user = check_emprs_n_1_user.readlines()
            check_emprs_n_1_user.close()

            check_emprs_n_2_user = io.open(f"profile/{ctx.author.id}_profile/emprs_n_2.txt", 'r')
            emprs_n_2_user = check_emprs_n_2_user.readlines()
            check_emprs_n_2_user.close()
            """
            emprs1_user = get_user(conn, f"'{ctx.author.id}'", "user_e1")
            emprs2_user = get_user(conn, f"'{ctx.author.id}'", "user_e2")
            emprs3_user = get_user(conn, f"'{ctx.author.id}'", "user_e3")
            emprs4_user = get_user(conn, f"'{ctx.author.id}'", "user_e4")
            emprs_n_1_user = get_user(conn, f"'{ctx.author.id}'", "user_n1")
            emprs_n_2_user = get_user(conn, f"'{ctx.author.id}'", "user_n2")

            # revisa el dinero
            """
            check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
            cr_user = check_cr_user.readlines()
            check_cr_user.close()
            """
            cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

            if int(cr_user[0]) < 30 and int(emprs1_user[0]) == 0 and int(emprs2_user[0]) == 0 and int(emprs3_user[0]) == 0 and int(emprs4_user[0]) == 0 and int(emprs_n_1_user[0]) == 0 and int(emprs_n_2_user[0]) == 0:

                # pon el dinero


                """apply_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                apply_cr_user.write("30")
                apply_cr_user.close()"""

                put_user(conn, f"'{ctx.author.id}'", "user_cr","30" )

                # resta un nivel (menos cuando el nivel es cero)
                lvl.remove_license(ctx)

                await ctx.send(embed = embedDato(ctx, "Operación llevada a cabo.", "¡Procura no arruinarte otra vez!"))
                log.logCall("banco trato", ctx.author.name)

            else:

                await ctx.send(embed = embedDato(ctx, "No cumples los requisitos para recibir ayuda.", "Vuelve a usar este comando si te ves en apuros.", "gold"))
                log.logFail("banco trato", ctx.author.name, "NotAllowedError")

        except:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail("banco trato", ctx.author.name, "AccountNotFoundError")

    else:
        imageselector = random.randint(1,3)
        file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

        await ctx.send(file = file, embed = embedError(ctx))
        log.logFail(f"banco {path} {func} {arg1}", ctx.author.name, "ArgumentNotFoundError")

################################################################################
##---------------------------------BANCO SYS----------------------------------##
################################################################################

################################################################################
##-----------------------------------CASINO-----------------------------------##
################################################################################

# .casino: Para gastar créditos
@client.command()
async def casino(ctx, path = None, arg1 = None):

    if path == None:

        await ctx.send(embed = embedDato(ctx, "Esto es .casino", "Para ver los comandos usa **.casino auxilio**"))
        log.logCall(f"casino", ctx.author.name)

    elif path == "auxilio":

        await ctx.send(embed = embedDato(ctx, "Comandos de .casino", "*Moneda:*\n**.casino moneda detalles :** Detalles sobre el juego de la moneda.\n**.casino moneda :** Dobla o pierde, suerte.\n\n*Bote:*\n**.casino bote detalles :** Detalles sobre el bote.\n**.casino bote :** Cada ciertas inversiones alguien se lo lleva.\n\n*Tragaperras:*\n**.casino tragaperras detalles :** Detalles sobre la tragaperras.\n**.casino tragaperras :** Funde todo tu dinero y consigue más dinero, o no..."))
        log.logCall(f"casino auxilio", ctx.author.name)

    ############################################################################
    # moneda
    elif path == "moneda" and arg1 == "detalles":

        await ctx.send(embed = embedDato(ctx, "¿Cara o cruz?", "Invierte un crédito y si sale...\n\n:coin: **CARA ->** Lo doblas\n:x: **CRUZ ->** Lo pierdes\n\n*Pero recuerda...*\nSi pierdes tendrás que ganar dos veces seguidas para\nrecibir créditos por cada vez que ganes."))
        log.logCall("casino moneda detalles", ctx.author.name)

    elif path == "moneda" and arg1 != "detalles":

        try:
            ## CONTROL de nivel
            ########################################################################
            allowed = lvl.check_license(ctx, 1)
            ########################################################################

            if allowed == True:

                """check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()"""

                cr_user = get_user(conn, f"'{ctx.author.id}'" , "user_cr" )
                if int(cr_user[0]) >= 1:

                    try:

                        chance = random.randint(1,2)

                        if chance == 1:

                            """check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                            cr_user = check_cr_user.readlines()
                            check_cr_user.close()"""

                            cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                            """apply_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                            apply_cr_user.write(str( int(cr_user[0]) + 1 ))
                            apply_cr_user.close()"""

                            put_user(conn, f"'{ctx.author.id}'", "user_cr", str( int(cr_user[0]) + 1 ))

                            await ctx.send(embed = embedDato(ctx, ":coin: Cara", "¡Sigue así!"))
                            log.logCall("casino moneda", ctx.author.name, True, "Gana")

                        else:

                            """check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                            cr_user = check_cr_user.readlines()
                            check_cr_user.close()"""

                            cr_user = get_user(conn,f"'{ctx.author.id}'","user_cr")

                            """apply_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                            apply_cr_user.write(str( int(cr_user[0]) - 1 ))
                            apply_cr_user.close()"""

                            put_user(conn, f"'{ctx.author.id}'", "user_cr", str( int(cr_user[0]) - 1 ))

                            await ctx.send(embed = embedDato(ctx, ":x: Cruz", "Mala suerte..."))
                            log.logCall("casino moneda", ctx.author.name, True, "Pierde")

                    except:

                        imageselector = random.randint(1,3)
                        file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                        await ctx.send(file = file, embed = embedError(ctx))
                        log.logFail(f"casino moneda", ctx.author.name, "ArgumentNotFoundError")

                else:

                    await ctx.send(embed = embedDato(ctx, "Para, eres pobre.", "No tienes dinero para hacer eso...", "gold"))
                    log.logFail(f"casino moneda", ctx.author.name, "IndexError")

            else:
                await ctx.send(embed = embedDato(ctx, "¡Tu nivel es insuficiente!", "Necesitas ser nivel 1 para usar este comando.", "gold"))
                log.logFail("casino moneda", ctx.author.name, "NotAllowedError")

        except:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail("casino moneda", ctx.author.name, "AccountNotFoundError")

    # bote
    elif path == "bote" and arg1 == "detalles":

        check_bote = io.open("casino/juego/bote.txt", 'r')
        val_bote = check_bote.readlines()
        check_bote.close()

        bote = int(val_bote[0])

        await ctx.send(embed = embedDato(ctx, "¿Serás tú el ganador del bote?", f"Invierte un crédito. **Por cada inversión es más probable que ganes el bote.**\n\n**VALOR ACTUAL DEL BOTE:**```{bote} créditos```"))
        log.logCall("casino bote detalles", ctx.author.name)

    elif path == "bote" and arg1 != "detalles":

        try:
            ## CONTROL de nivel
            ########################################################################
            allowed = lvl.check_license(ctx, 2)
            ########################################################################

            if allowed == True:

                """check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                cr_user = check_cr_user.readlines()
                check_cr_user.close()"""

                cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                if int(cr_user[0]) >= 1:

                    try:

                        # cobra
                        """check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                        cr_user = check_cr_user.readlines()
                        check_cr_user.close()"""

                        cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr" )

                        """apply_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                        apply_cr_user.write(str( int(cr_user[0]) - 1 ))
                        apply_cr_user.close()"""

                        put_user(conn, f"'{ctx.author.id}'", "user_cr" , str( int(cr_user[0]) - 1 ) )

                        # lo mete en el bote
                        check_bote = io.open("casino/juego/bote.txt", 'r')
                        val_bote = check_bote.readlines()
                        check_bote.close()

                        bote = int(val_bote[0])

                        apply_bote = io.open("casino/juego/bote.txt", 'w')
                        apply_bote.write(str( bote + 1 ))
                        apply_bote.close()

                        # mira si toca el bote
                        bote_chance = random.randint(1, 20)

                        if bote_chance != 10:

                            check_bote = io.open("casino/juego/bote.txt", 'r')
                            val_bote = check_bote.readlines()
                            check_bote.close()

                            bote = int(val_bote[0])

                            await ctx.send(embed = embedDato(ctx, "Tu crédito ya está en el bote.", f"Si alguien más invierte y ganas el bote\nno solo recuperarás tu dinero, también\nel dinero del resto de jugadores.\n\n**VALOR ACTUAL DEL BOTE:**```{bote} créditos```"))
                            log.logCall("casino bote", ctx.author.name)

                        else:

                            # mira valor del bote
                            check_bote = io.open("casino/juego/bote.txt", 'r')
                            val_bote = check_bote.readlines()
                            check_bote.close()

                            bote = int(val_bote[0])

                            # te da el bote
                            """check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                            cr_user = check_cr_user.readlines()
                            check_cr_user.close()"""

                            cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr" )

                            """apply_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                            apply_cr_user.write(str( int(cr_user[0]) + bote ))
                            apply_cr_user.close()"""

                            put_user(conn, f"'{ctx.author.id}'", "user_cr", str( int(cr_user[0]) + bote ) )

                            # reinicia el bote
                            reset_bote = io.open("casino/juego/bote.txt", 'w')
                            reset_bote.write("0")
                            reset_bote.close()

                            await ctx.send(embed = embedDato(ctx, "¡Ese crédito ha ganado el bote!", f":coin: ¡Enhorabuena! :coin:\n\n**TU PREMIO ES DE:**```{bote} créditos```\n\n*El valor del bote ha vuelto a 0.*"))
                            log.logCall("casino bote", ctx.author.name, True, "BOTE")

                    except FileNotFoundError:

                        imageselector = random.randint(1,3)
                        file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                        await ctx.send(file = file, embed = embedError(ctx))
                        log.logFail(f"casino bote", ctx.author.name, "ArgumentNotFoundError")

                else:

                    await ctx.send(embed = embedDato(ctx, "Para, eres pobre.", "No tienes dinero para hacer eso...", "gold"))
                    log.logFail(f"casino bote", ctx.author.name, "IndexError")

            else:
                await ctx.send(embed = embedDato(ctx, "¡Tu nivel es insuficiente!", "Necesitas ser nivel 2 para usar este comando.", "gold"))
                log.logFail("casino bote", ctx.author.name, "NotAllowedError")

        except:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail("casino bote", ctx.author.name, "AccountNotFoundError")

    # tragaperras
    elif path == "tragaperras" and arg1 == "detalles":

        await ctx.send(embed = embedDato(
            ctx,
            "¿Listo para ser rico?",
            "1 crédito puede convertirse en una fortuna.\n\n**Multiplicadores:**\n" +
            "<:hijo:775045199763734539> <:hijo:775045199763734539> <:hijo:775045199763734539> = **x1000**\n" +
            ":trident: :trident: :trident: = **x250**\n" +
            ":fleur_de_lis: :fleur_de_lis: :fleur_de_lis: = **x100**\n" +
            ":diamond_shape_with_a_dot_inside: :diamond_shape_with_a_dot_inside: :diamond_shape_with_a_dot_inside: = **x75**\n" +
            ":white_flower: :white_flower: :white_flower: = **x50**\n" +
            ":beginner: :beginner: :beginner: = **x25**\n" +
            ":nazar_amulet: :nazar_amulet: :nazar_amulet: = **x10**\n" + "\nJuega a la tragaperras con **.casino tragaperras**"))
        log.logCall("casino tragaperras detalles", ctx.author.name)

    elif path == "tragaperras" and arg1 != "detalles":

        try:
            ## CONTROL de nivel
            ########################################################################
            allowed = lvl.check_license(ctx, 3)
            ########################################################################

            if allowed == True:

                try:

                    """check_cr_user = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'r')
                    cr_user = check_cr_user.readlines()
                    check_cr_user.close()"""
                    cr_user = get_user(conn, f"'{ctx.author.id}'", "user_cr")

                    if int(cr_user[0]) > 1:

                        # genera los números y traduce a emoji
                        slot1 = random.randint(1, 7)
                        slot2 = random.randint(1, 7)
                        slot3 = random.randint(1, 7)

                        if slot1 == 7:
                            emoji1 = "<:hijo:775045199763734539>"
                        elif slot1 == 6:
                            emoji1 = ":trident:"
                        elif slot1 == 5:
                            emoji1 = ":fleur_de_lis:"
                        elif slot1 == 4:
                            emoji1 = ":diamond_shape_with_a_dot_inside:"
                        elif slot1 == 3:
                            emoji1 = ":white_flower:"
                        elif slot1 == 2:
                            emoji1 = ":beginner:"
                        else:
                            emoji1 = ":nazar_amulet:"

                        if slot2 == 7:
                            emoji2 = "<:hijo:775045199763734539>"
                        elif slot2 == 6:
                            emoji2 = ":trident:"
                        elif slot2 == 5:
                            emoji2 = ":fleur_de_lis:"
                        elif slot2 == 4:
                            emoji2 = ":diamond_shape_with_a_dot_inside:"
                        elif slot2 == 3:
                            emoji2 = ":white_flower:"
                        elif slot2 == 2:
                            emoji2 = ":beginner:"
                        else:
                            emoji2 = ":nazar_amulet:"

                        if slot3 == 7:
                            emoji3 = "<:hijo:775045199763734539>"
                        elif slot3 == 6:
                            emoji3 = ":trident:"
                        elif slot3 == 5:
                            emoji3 = ":fleur_de_lis:"
                        elif slot3 == 4:
                            emoji3 = ":diamond_shape_with_a_dot_inside:"
                        elif slot3 == 3:
                            emoji3 = ":white_flower:"
                        elif slot3 == 2:
                            emoji3 = ":beginner:"
                        else:
                            emoji3 = ":nazar_amulet:"

                        # PREMIOS para sumar al multiplier #####################################
                        # 7 7 7 : x1000
                        # 6 6 6 : x250
                        # 5 5 5 : x100
                        # 4 4 4 : x75
                        # 3 3 3 : x50
                        # 2 2 2 : x25
                        # 1 1 1 : x10
                        ########################################################################

                        # compara los números con los tipos de premios
                        if slot1 == 7 and slot2 == 7 and slot3 == 7:
                            multiplier = 1000
                        elif slot1 == 6 and slot2 == 6 and slot3 == 6:
                            multiplier = 250
                        elif slot1 == 5 and slot2 == 5 and slot3 == 5:
                            multiplier = 100
                        elif slot1 == 4 and slot2 == 4 and slot3 == 4:
                            multiplier = 75
                        elif slot1 == 3 and slot2 == 3 and slot3 == 3:
                            multiplier = 50
                        elif slot1 == 2 and slot2 == 2 and slot3 == 2:
                            multiplier = 25
                        elif slot1 == 1 and slot2 == 1 and slot3 == 1:
                            multiplier = 10
                        else:
                            multiplier = 0

                        # calcula las ganancias
                        premio = round(1 * multiplier)

                        # aplica los cambios economicos

                        #cobro = io.open(f"profile/{ctx.author.id}_profile/credit.txt", 'w')
                        pago = str( int(cr_user[0]) - 1 + premio )
                        #cobro.write(pago)
                        #cobro.close()

                        put_user(conn, f"'{ctx.author.id}'", "user_cr", pago)


                        await ctx.send(embed = embedDato(ctx,
                            "Resultado de la partida...",
                            ":trident: :beginner: :white_flower:\n" +
                            f"{emoji1} {emoji2} {emoji3}\n" +
                            ":beginner: :nazar_amulet: :fleur_de_lis:\n\n" + f"Tu inversión de **1** créditos\n se ha convertido en **{premio}** créditos."
                        ))
                        log.logCall(f"casino tragaperras", ctx.author.name, True, "1" + " -> " + str(premio))

                    else:

                        await ctx.send(embed = embedDato(ctx, "Para, eres pobre.", "No tienes dinero para hacer eso...", "gold"))
                        log.logFail(f"casino tragaperras", ctx.author.name, "IndexError")

                except:
                    imageselector = random.randint(1,3)
                    file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

                    await ctx.send(file = file, embed = embedError(ctx))
                    log.logFail(f"casino tragaperras", ctx.author.name, "ArgumentNotFoundError")

            else:

                await ctx.send(embed = embedDato(ctx, "¡Tu nivel es insuficiente!", "Necesitas ser nivel 3 para usar este comando.", "gold"))
                log.logFail("casino tragaperras", ctx.author.name, "NotAllowedError")

        except:
            await ctx.send(embed = embedDato(ctx, "No tienes una cuenta.", "Crea tu cuenta con **.registro** para acceder a estas funciones.", "gold"))
            log.logFail("casino tragaperras", ctx.author.name, "AccountNotFoundError")

    ############################################################################

    else:

        imageselector = random.randint(1,3)
        file = discord.File(f"resources/elhijo_commandnotfound{str(imageselector)}.png", filename = "foto.png")

        await ctx.send(file = file, embed = embedError(ctx))
        log.logFail(f"casino {path} {arg1}", ctx.author.name, "ArgumentNotFoundError")

################################################################################
##-----------------------------------CASINO-----------------------------------##
################################################################################



## SERVER - BOT > IP (token)
################################################################################
client.run('Secret Token, ni de coña la pongo aquí que me tumban el server')
