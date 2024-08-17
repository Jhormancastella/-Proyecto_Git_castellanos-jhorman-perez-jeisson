import modules.corefiles as cf
import funciones.globales as gf
import funciones.especialistas as fsp
import funciones.iraconsulta as fic
import main

def MenuRegistro(op: int):
    title = """
    ➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️
   ⚕️  🧑‍⚕️  MODULO ADMIN De Registro de sucursal  👩‍⚕️  ⚕️
    ➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️
    """
    MenuRegistroOp = '1. Agregar\n2. Salir'
    gf.borrar_pantalla()
    if op != 5:  # Reemplazado 4 con 5 para salir en la opción 5
        print(title)
        print(MenuRegistroOp)
        while True:
            try:
                op = int(input(":) "))
                if op not in range(1, 6):
                    raise ValueError("La opción ingresada no está en el rango válido")
                break
            except ValueError as e:
                print("Error:", e)
                gf.pausar_pantalla()
                MenuRegistro(0)

        match op:
            case 1:
                try:
                    fsp.NewEspecialista()
                except Exception as e:
                    print("Error al agregar especialista:", e)
                else:
                    print("Especialista agregado exitosamente")
                gf.pausar_pantalla()
                MenuRegistro(0)
            case 2:
                main.mainMenu(0)

            case _:
                print("La opción ingresada no está disponible en las opciones")
                gf.pausar_pantalla()
                MenuRegistro(0)
