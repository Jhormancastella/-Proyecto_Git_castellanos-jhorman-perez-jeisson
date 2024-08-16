import json
from datetime import date

import modules.corefiles as cf
import modules.corefilesP as cfp
import funciones.globales as fg
import ui.uiMenuSpecialistas as uiSp
import ui.uiMenuPacientes as uiPt
import ui.uiConsultas as uiC

def mainMenu(op):
    fg.borrar_pantalla()
    title = """
    🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩
    🟥 🏣🚑👨‍⚕️👩‍⚕️🏥 Modulo de Sucursales 🏣🚑👨‍⚕️👩‍⚕️🏥  🟥
    🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩
    """
    mainMenuOp = "1. Registro de nueva sucursal\n2. Editar sucursal\n3. Salir"
    if op != 4:
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print('Error en la opcion ingresada')
            fg.pausar_pantalla()
            mainMenu(0)
        else:
            if opcion == 1:
                uiSp.MenuEspecialista(0)
            elif opcion == 2:
                uiPt.MenuPacientes(0)
            else:
                print('Opcion ingresada no pertenece al menu de opciones')
                fg.pausar_pantalla()
                mainMenu(0)

if __name__ == '__main__':
    cf.MY_DATABASE = 'data/sucursales.json'
    cfp.MY_DATABASEP = 'data/especialistas.json'
    cf.checkFile(fg.centroClinico)
    cfp.checkFile(fg.centroClinico)
    mainMenu(0)
