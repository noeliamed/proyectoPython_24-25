# Fichero con las funciones. 

#Función que sirve para leer el fichero y devuelve una lista de diccionarios con los datos:
def leer_partidos(archivo):
    try:
        with open(archivo, "r") as f:
            partidos = []
            for linea in f:
                datos = linea.strip().split(",")
                partidos.append({
                    "codigo": datos[0],
                    "local": datos[1],
                    "visitante": datos[2],
                    "goles_local": int(datos[3]),
                    "goles_visitante": int(datos[4]),
                    "fecha": datos[5],
                    "jornada": datos[6]
                })
            return partidos
    except FileNotFoundError:
        return []


# Función para escribir los datos en el fichero:
def escribir_partidos(archivo, partidos):
    with open(archivo, "w") as f:
        for partido in partidos:
            linea = f"{partido['codigo']},{partido['local']},{partido['visitante']},{partido['goles_local']},{partido['goles_visitante']},{partido['fecha']},{partido['jornada']}\n"
            f.write(linea)

# Función para añadir partidos:
def añadir_partido(partidos, nuevo_partido):
    partidos.append(nuevo_partido)

# Función que cuenta los partidos jugados por un equipo como local y como visitante:
def contar_partidos_equipo(partidos, equipo):
    local = sum(1 for p in partidos if p['local'] == equipo)
    visitante = sum(1 for p in partidos if p['visitante'] == equipo)
    return local, visitante

# Función que elimina un partido por su código: 
def eliminar_partido(partidos, codigo):
    for partido in partidos:
        if partido['codigo'] == codigo:
            partidos.remove(partido)
            return True
    return False

# Función que lista los nombres de los equipos participantes:
def listar_equipos(partidos):
    equipos = set()
    for partido in partidos:
        equipos.add(partido['local'])
        equipos.add(partido['visitante'])
    return sorted(equipos)

# Función genera la clasificación de los equipos: 
def clasificacion(partidos):
    tabla = {}
    for partido in partidos:
        local = partido['local']
        visitante = partido['visitante']
        goles_local = partido['goles_local']
        goles_visitante = partido['goles_visitante']

        if local not in tabla:
            tabla[local] = {"ganados": 0, "perdidos": 0, "empatados": 0, "puntos": 0}
        if visitante not in tabla:
            tabla[visitante] = {"ganados": 0, "perdidos": 0, "empatados": 0, "puntos": 0}

        if goles_local > goles_visitante:
            tabla[local]["ganados"] += 1
            tabla[local]["puntos"] += 3
            tabla[visitante]["perdidos"] += 1
        elif goles_local < goles_visitante:
            tabla[visitante]["ganados"] += 1
            tabla[visitante]["puntos"] += 3
            tabla[local]["perdidos"] += 1
        else:
            tabla[local]["empatados"] += 1
            tabla[local]["puntos"] += 1
            tabla[visitante]["empatados"] += 1
            tabla[visitante]["puntos"] += 1

    return tabla








  
