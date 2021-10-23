################################################################################
# Project by: ErtonDev
# Info: Administrador y distribuidor de licencias para .banco en bot
################################################################################

## MODULES / LIBRARIES
################################################################################
import io

## CLASS
################################################################################
class License_manager():

    # NOTE: Determina el nivel actual del usuario
    def determinate_license(self, ctx):

        user_level = io.open(f"profile/{ctx.author.id}_profile/level.txt", 'r')
        actual_level = user_level.readlines()
        user_level.close()

        level = actual_level[0]
        return level

    # NOTE: Revisa que se cumplan los requisitos esperados del usuario por su nivel de licencia
    def check_license(self, ctx, lvl_num):

        user_level = io.open(f"profile/{ctx.author.id}_profile/level.txt", 'r')
        actual_level = user_level.readlines()
        user_level.close()

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
    # 5: Te has pasado el juego, te llevas un pin en tu cuenta y empiezas de 0  > 500000cr (Además te llevas el maestro inversor)
    ############################################################################

    # NOTE: Dar licencia
    def asign_license(self, ctx):
        # calcula el siguiente nivel
        user_level = io.open(f"profile/{ctx.author.id}_profile/level.txt", 'r')
        actual_level = user_level.readlines()
        user_level.close()

        level = actual_level[0]
        next_level = int(level) + 1

        # aplica la mejora de nivel
        user_level = io.open(f"profile/{ctx.author.id}_profile/level.txt", 'w')

        # si el nivel al que sube es 5 debe reiniciar todo y dar prestigio
        if next_level != 5:

            # siguiente nivel
            user_level.write(str(next_level))
            user_level.close()

            # transacciones a cero
            '''reset_user_transac = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'w')
            reset_user_transac.write("0")
            reset_user_transac.close()'''

        else:

            user_level.write("0")
            user_level.close()

            # reinicia la cuenta
            # credit
            reset_user_credits = io.open(f"profile/{ctx.author.profile}_profile/credit.txt", 'w')
            reset_user_credits.write("30")
            reset_user_credits.close()

            # transac
            '''reset_user_transac = io.open(f"profile/{ctx.author.id}_profile/transac.txt", 'w')
            reset_user_transac.write("0")
            reset_user_transac.close()'''

            # prestigio
            new_prestige = io.open(f"profile/{ctx.author.id}_profile/prestige.txt", 'a')
            new_prestige.write("*")
            new_prestige.close()

    # NOTE: Quita un nivel
    def remove_license(self, ctx):
        # lee el nivel
        user_level = io.open(f"profile/{ctx.author.id}_profile/level.txt", 'r')
        actual_level = user_level.readlines()
        user_level.close()

        level = int(actual_level[0])

        # si el nivel es cero no hace nada
        if level == 0:
            return

        else:
            # en caso de no serlo resta uno
            user_level = io.open(f"profile/{ctx.author.id}_profile/level.txt", 'w')
            user_level.write( str( int(level) - 1 ) )
            user_level.close()
