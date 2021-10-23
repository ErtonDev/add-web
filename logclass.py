################################################################################
# Project by: ErtonDev
# Info: Clase log para bot de discord.
################################################################################

## MODULES / LIBRARIES
################################################################################
import colorama
from colorama import Fore, Back, Style

## SETUP
################################################################################
colorama.init(autoreset = True)

## LOG
################################################################################
class Log():
    def __init__(self):
        self.output = ""

    # NOTE: calls de comandos satisfechas
    def logCall(self, command = str("x"), author = str("x"), details = bool(False), detailed_info = str("x")):

        # call detallada
        if details == True:
            self.output = f"#{command} " + Style.DIM + "call " + Style.NORMAL + Fore.LIGHTBLUE_EX + f"by {author} " + Fore.WHITE + f"= {detailed_info}"

        # call no detallada
        else:
            self.output = f"#{command} " + Style.DIM + "call " + Style.NORMAL + Fore.LIGHTBLUE_EX + f"by {author}"

        # to print
        print(self.output)

    # NOTE: calls de comandos fallidas
    def logFail(self, command, author, error_type = str("x")):

        # call por error
        self.output = f"#{command} " + Style.DIM + "call " + Style.NORMAL + Fore.LIGHTBLUE_EX + f"by {author} " + Fore.RED + f"! {error_type}"

        # error types
        ########################################################################
        # NotAllowedError : el author no cumple con los requisitos para usar el comando
        # AccountNotFoundError : el author no tiene una cuenta de .banco
        # ArgumentNotFoundError : el author ha usado un argumento no contemplado
        # CommandNotFoundError : el comando no está registrado
        # AccountExistsError : ya tiene una cuenta
        # LimitError : Algo no se puede hacer más
        # IndexError : Los valores no se ajustan a la realidad
        ########################################################################

        # to print
        print(self.output)

    # NOTE: events como cuando se detecta una palabra clave
    def logEvent(self, event_type = str("x")):

        # event
        self.output = "/Event: " + Fore.LIGHTGREEN_EX + f"{event_type}"

        # to print
        print(self.output)
