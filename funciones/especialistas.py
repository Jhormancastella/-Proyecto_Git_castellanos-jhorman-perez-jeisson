import json
import funciones.globales as gf
import modules.corefilesP as cfp
import ui.uiMenuSpecialistas as uipc

def NewEspecialista():
    title = """
    *****************************
    * REGISTRO DE sucursales *
    *****************************
    """
    gf.borrar_pantalla()
    print(title)
    
    identificacion = input("Ingrese el Nombre de la sucurla: ")
    codEspecialista = input("Ingrese Dirrecion completa: ")
    nombreEspecialista = input("Ingrese telefono : ")
    correoElectronico = input("Ingrese Correo Electrónico: ")
    telefono = input("Ingrese numero  del celular : ")
    especialista = {
        'identificacion': identificacion,
        'codEspecialista': codEspecialista,
        'nombreEspecialista': nombreEspecialista,
        'correoElectronico': correoElectronico,
        'telefono': telefono,
    }
    cfp.AddData('data', identificacion, especialista)
    gf.centroClinico.get('data').update({identificacion: especialista})
    if bool(input('Desea registrar otro especialista (Sí) o Enter (No): ')):
        NewEspecialista()
    else:
        uipc.MenuEspecialista(0)

def SearchData():
    criterio = input('Ingrese el Nro de Identificacion del especialista: ')
    data = gf.centroClinico.get('data').get(criterio)
    return data

def ModifyData():
    dataEspecialista = SearchData()
    if dataEspecialista:
        identificacion, codEspecialista, nombreEspecialista, correoElectronico, telefono, especialidad, jornada, consultas = dataEspecialista.values()
        for key in dataEspecialista.keys():
            if key not in ['identificacion', 'consultas']:
                if bool(input(f'Desea modificar {key} (sí) o Enter (No): ')):
                    if key == 'especialidad':
                        print("Seleccione nueva Especialización:")
                        print("1. Pediatría")
                        print("2. Ginecología")
                        print("3. Dermatología")
                        print("4. Endocrinología")
                        print("5. Optometría")
                        especializacion = input("Ingrese el número correspondiente a la especialización: ")
                        especializaciones = ["Pediatría", "Ginecología", "Dermatología", "Endocrinología", "Optometría"]
                        dataEspecialista[key] = especializaciones[int(especializacion) - 1]
                    elif key == 'jornada':
                        print("Seleccione nuevo Horario:")
                        print("1. Mañana")
                        print("2. Tarde")
                        horario = input("Ingrese el número correspondiente al horario: ")
                        horarios = ["Mañana", "Tarde"]
                        dataEspecialista[key] = horarios[int(horario) - 1]
                    else:
                        dataEspecialista[key] = input(f'Ingrese el nuevo valor para {key}: ')
        gf.centroClinico.get('data').update({identificacion: dataEspecialista})
        cfp.UpdateFile(gf.centroClinico)
        uipc.MenuEspecialista(0)
    else:
        print("Especialista no encontrado.")
        
def DeleteData():
    identificacion = input('Ingrese el Nro de Identificacion del especialista a eliminar: ')
    if identificacion in gf.centroClinico.get('data'):
        del gf.centroClinico.get('data')[identificacion]
        cfp.UpdateFile(gf.centroClinico)
        print("Especialista eliminado correctamente.")
        uipc.MenuEspecialista(0)
    else:
        print("Especialista no encontrado.")

