# Este es el fichero principal del programa. 

# Se importa el fichero funciones.py que se ha creado anteriormente con todas las funciones. 
import funciones
archivo = "partidos.txt"

# Menú del programa:  
def mostrar_menu():
    print("""
    1. Añade partido
    2. Muestra en cuántos partidos ha jugado un equipo como local y en cuántos como visitante
    3. Elimina un partido
    4. Lista los nombres de los equipos participantes
    5. Listado de clasificación de los equipos
    6. Salir (Para guardar cambios)
    """)


def main():
    partidos = funciones.leer_partidos(archivo)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            codigo = input("Código del partido: ")
            local = input("Equipo local: ")
            visitante = input("Equipo visitante: ")
            goles_local = int(input("Goles del equipo local: "))
            goles_visitante = int(input("Goles del equipo visitante: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            jornada = input("Jornada: ")
            nuevo_partido = {
                "codigo": codigo,
                "local": local,
                "visitante": visitante,
                "goles_local": goles_local,
                "goles_visitante": goles_visitante,
                "fecha": fecha,
                "jornada": jornada
            }
            funciones.añadir_partido(partidos, nuevo_partido)
            print("Partido añadido correctamente.")

        elif opcion == "2":
            equipo = input("Nombre del equipo: ")
            local, visitante = funciones.contar_partidos_equipo(partidos, equipo)
            if local + visitante == 0:
                print("Error: el equipo no existe.")
            else:
                print(f"El equipo {equipo} ha jugado {local} partidos como local y {visitante} como visitante.")

        elif opcion == "3":
            codigo = input("Código del partido a eliminar: ")
            if funciones.eliminar_partido(partidos, codigo):
                print("Partido eliminado correctamente.")
            else:
                print("Error: partido no encontrado.")

        elif opcion == "4":
            equipos = funciones.listar_equipos(partidos)
            print("Equipos participantes:")
            for equipo in equipos:
                print(f"- {equipo}")

        elif opcion == "5":
            tabla = funciones.clasificacion(partidos)
            print("Clasificación:")
            print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Equipo", "Ganados", "Perdidos", "Empatados", "Puntos"))
            for equipo, stats in sorted(tabla.items(), key=lambda x: x[1]['puntos'], reverse=True):
                print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(equipo, stats["ganados"], stats["perdidos"], stats["empatados"], stats["puntos"]))

        elif opcion == "6":
            funciones.escribir_partidos(archivo, partidos)
            print("Datos guardados. ¡Adiós!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
