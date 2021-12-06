################################################################################
# Project by: ErtonDev
# Info: Administrador y distribuidor de licencias para .banco en bot
################################################################################

## MODULES / LIBRARIES
################################################################################
import io
from web.psqlapi import *

## CLASS
################################################################################
class License_manager():
    conn = connect()
    # NOTE: Determina el nivel actual del usuario
    def determinate_license(self, ctx):
        actual_level = get_user(conn, ctx.author.id, "user_lvl")

        level = actual_level[0]
        return level

    # NOTE: Revisa que se cumplan los requisitos esperados del usuario por su nivel de licencia
    def check_license(self, ctx, lvl_num):
        actual_level = get_user(conn, ctx.author.id, "user_lvl")

        level = actual_level[0]

        upgradable = False

        if int(level) >= int(lvl_num):
            upgradable = True

        return upgradable

    ############################################################################
    # TIPOS DE LICENCIA / NIVELES:
    # 0: Licencia estandar con la que se empieza
    # 1: Acceso al juego de la moneda                                           > 500cr 10transac
    # 2: Acceso al Bote                                                         > 2500cr 25transac
    # 3: Acceso a la tragaperras                                                > 10000cr 50transac
    # 4: Acceso al mercado negro                                                > 100000cr 100transac
    # 5: Te has pasado el juego, te llevas un pin en tu cuenta y empiezas de 0  > 500000cr (AdemÃ¡s te llevas el maestro inversor)
    ############################################################################

    # NOTE: Dar licencia
    def asign_license(self, ctx):
        # calcula el siguiente nivel
        actual_level = get_user(conn, ctx.author.id, "user_lvl")

        level = actual_level[0]
        next_level = int(level) + 1

        # aplica la mejora de nivel

        # si el nivel al que sube es 5 debe reiniciar todo y dar prestigio
        if next_level != 5:

            # siguiente nivel
            put_user(conn, ctx.author.id, "user_lvl", next_level)

            # transacciones a cero
            put_user(conn, ctx.author.id, "user_transac", 0)

        else:
            # reinicia la cuenta
            # lvl
            put_user(conn, ctx.author.id, "user_lvl", 0)

            # credit
            put_user(conn, ctx.author.id, "user_cr", 30)

            # transac
            put_user(conn, ctx.author.id, "user_transac", 0)

            # prestigio
            put_user(conn, ctx.author.id, "user_prestige", "*")

    # NOTE: Quita un nivel
    def remove_license(self, ctx):
        # lee el nivel
        actual_level = get_user(conn, ctx.author.id, "user_lvl")

        level = actual_level[0]

        # si el nivel es cero no hace nada
        if level == 0:
            return

        else:
            # en caso de no serlo resta uno
            put_user(conn, ctx.author.id, "user_lvl", int(level) - 1)
