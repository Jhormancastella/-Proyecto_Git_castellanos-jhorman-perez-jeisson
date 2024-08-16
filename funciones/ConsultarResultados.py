import os
import json
import funciones.globales as gf
from datetime import datetime, timedelta
import ui.uiConsultas as uc

def SearchData():
    criterio = input('Ingrese el Nro de Identificacion del paciente: ')
    data = gf.sucursal.get('data').get(criterio)
    return data

def nuwsucursal():
    title = """
    ***************************
    * REGISTRO de sucursal *
    ***************************
    """
    gf.borrar_pantalla()
    print(title)

    # Ruta al archivo pacientes.json dentro de la carpeta "data"
    modules_file = os.path.join("data", "sucursales.json")

    # Verificar si el archivo pacientes.json existe
    if not os.path.exists(modules_file):
        print("El archivo pacientes.json no se encuentra en la carpeta 'data'. Por favor, asegúrese de que el archivo esté presente.")
        return

    while True:
        mudulos = SearchData()
        if mudulos:
            fecha_registro = datetime.now().strftime("%Y-%m-%d")  # Fecha de registro
            print(f"Fecha de registro de la consulta: {fecha_registro}")

            motivo = input("Ingrese el motivo de la sucursal: ")
            direccion = input("Ingrese los antecedentes del direccion: ")
            telefono = input("Ingrese otros medios telefono: ")
            
            print("Seleccione el sucursal:")
            print("1. telefono")
            print("2. direccion")
            print("3. ID")
            print("4. gerente")
            print("5. contatos")
            sucursales = input("Ingrese el número correspondiente al especialista: ")
            
            horario_inicio = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)  # Horario inicio
            if input("¿Prefiere la cita por la mañana? (Sí/No): ").lower() == 'sí':
                horario_inicio = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
            else:
                horario_inicio = datetime.now().replace(hour=14, minute=0, second=0, microsecond=0)
            
            # Calcular fecha de la cita (2 días después de la fecha de registro)
            fecha_cita = datetime.now() + timedelta(days=2)
            fecha_cita_str = fecha_cita.strftime("%Y-%m-%d")

            # Calcular horario de la cita (20 minutos por consulta)
            horario_fin = horario_inicio + timedelta(minutes=20)
            horario_str = f"{horario_inicio.strftime('%I:%M %p')} - {horario_fin.strftime('%I:%M %p')}"

            modulo = ""
            if sucursales == '1':
                modulo = "modulo 101"
            elif sucursales == '2':
                modulo = "modulo 201"
            elif sucursales == '3':
                modulo = "modulo 301"
            elif sucursales == '4':
                modulo = "modulo 401"
            elif sucursales == '5':
                modulo = "modulo 501"
            else:
                print("sucursal no válido.")
            
            if sucursales:
                print(f"Su cita ha sido programada con la sucursal en {modulo} para el {fecha_cita_str} a las {horario_str}.")
                print("Por favor, asegúrese de llegar al consultorio 20 minutos antes de la cita.")
                
                # Guardar los datos de la consulta en el paciente
                sucursales['direciones'] = sucursales.get('direciones', [])
                sucursales['direcciones'].append({
                    'fecha_cita': fecha_cita_str,
                    'horario_cita': horario_str,
                    'especialista': sucursales,
                    'motivo': motivo,
                    'antecedentes': direccion,
                    'alergias': telefono,
                    'direccion': direccion
                })

                # Actualizar el archivo sucursaless.json con los nuevos datos
                with open(sucursales, "w") as file:
                    json.dump(gf.sucursal, file, indent=4)

                if input("¿Desea agregar otra consulta? (Sí/No): ").lower() != 'sí':
                    break  # Salir del bucle si no se desea agregar otra consulta
            else:
                print("Cita no programada debido a una selección de sucursales inválida.")
        else:
            print("Paciente no encontrado.")
            if input("¿Desea volver al menú de direcciones? (Sí/No): ").lower() != 'sí':
                break  # Salir del bucle si no se desea agregar otra consulta
            else:
                continue  # Volver al inicio del bucle para ingresar otro número de identificación
