import csv
import random

# Campos fijos
sexos = ["Mujer", "Hombre", "Intersexual"]
generos = ["Femenino", "Masculino", "No binario"]
orientaciones = ["Heterosexual", "Homosexual", "Bisexual"]
tipos_identificacion = ["Cédula de ciudadanía", "Pasaporte", "Cédula de extranjería"]
zonas = ["Urbano", "Rural"]
discapacidades = ["Visual", "Intelectual", "Auditiva"]

departamentos = {
    "20": ["20032", "20060", "20175", "20178"], # Cesar
    "41": ["41001", "41306", "41319", "41349"], # Huila
    "19": ["19001", "19022", "19050", "19075"], # Cauca
    "52": ["52683", "52685", "52560", "52573"], # Nariño
    "25": ["25019", "25123", "25126", "25168"], # Cundinamarca
    "27": ["27615", "27001", "27006", "27025"] # Chocó

}

primer_nombres = [
    "Juan", "Ana", "Carlos", "Laura", "Sofía", "Miguel", "Camila", "Daniel", "Valentina", "Julián",
    "Natalia", "Andrés", "Paula", "Sebastián", "María", "Felipe", "Lucía", "Mateo", "Isabella",
    "Tomás", "Gabriela", "Diego", "Samuel", "Juliana", "David", "Mariana", "Alejandro", "Daniela", "Nicolás", "Sara",
    "Esteban", "Luisa", "Martín", "Renata", "Emilio", "Victoria", "Emilia", "Agustín", "Antonia", "Emmanuel",
    "Ariana", "Bruno", "René", "Diana", "Pablo", "Mónica", "Cristian", "Lorena", "Francisco", "Carolina",
    "Jorge", "Patricia", "Iván", "Beatriz", "Ramiro", "Fabiola", "Alfredo", "Leticia", "Oscar", "Teresa",
    "Gustavo", "Silvia", "Rocío", "Clara", "Roberto", "Cecilia", "Mauricio", "Verónica", "Raúl", "Javier",
    "Camilo", "Ricardo", "Elena", "Manuela", "Ignacio", "Alberto", "Valeria", "Nicolás", "Sofía", "Alonso"
]
segundo_nombres = [
    "Carlos", "María", "Andrés", "Isabel", "Paola", "Ángel", "Andrea", "Esteban", "Lucía", "David",
    "Carolina", "Felipe", "Alexander", "José", "Santiago", "Estefanía", "Alonso", "Sofía", "Nicolás",
    "Valeria", "Alberto", "Ignacio", "Manuela", "Elena", "Ricardo", "Patricia", "Camilo", "Fernanda", "Javier",
    "Raúl", "Verónica", "Mauricio", "Patricia", "Jorge", "Cecilia", "Roberto", "Clara", "Hugo", "Rocío",
    "Gustavo", "Silvia", "Oscar", "Teresa", "Iván", "Beatriz", "Ramiro", "Fabiola", "Alfredo", "Leticia",
    "Martina", "Emiliano", "Valentina", "Agustina", "Emilio", "Renata", "Bruno", "Ariadna", "Cristina", "Leonardo",
    "Lorena", "Francisco", "Diana", "Pablo", "Mónica", "Cristian", "Antonia", "Emmanuel", "Ariana", "Gabriel"
]
apellidos = [
    "Pérez", "López", "Martínez", "Rodríguez", "Hernández", "Gómez", "Moreno", "Jiménez", "Ramírez", "Suárez",
    "García", "Ortiz", "Mendoza", "Cruz", "Castro", "Salazar", "Peña", "Álvarez", "Montoya", "Rivera",
    "Cardona", "Londoño", "Herrera", "Bermúdez", "Chávez", "Mejía", "Castaño", "Morales", "Ríos", "Torres",
    "Vargas", "Serrano", "Pineda", "Reyes", "Navarro", "Molina", "Soto", "Delgado", "Campos", "Vega",
    "Aguilar", "Silva", "Fuentes", "Escobar", "Pacheco", "Maldonado", "Arias", "Córdoba", "Sánchez", "Ruiz",
    "Castillo", "Márquez", "Ramón", "Villalba", "Guzmán", "Solano", "Palacios", "Rangel", "Barrios", "Córdoba",
    "Vallejo", "Benítez", "Cortés", "Rueda", "Mora", "Sarmiento", "Buitrago", "Castañeda", "Cárdenas", "Salinas"
]

barrios = ["Las Margaritas", "San Fernando", "La Esperanza", "Villa Nueva", "El Prado", "Bosque Popular",
           "Las Flores", "San José", "El Refugio", "Los Álamos", "La Castellana", "San Antonio", "Altos del Bosque",
           "Villa Luz", "San Luis", "El Jardín", "La Candelaria", "Los Laureles", "El Porvenir", "Villa del Prado",
           "Bella Vista", "La Estrella", "Los Rosales", "El Recreo", "Villa María", "San Cristóbal", "Villa Clara",
           "San Carlos", "El Mirador", "Villa Diana"]

# Control de unicidad
usados_identificacion = set()
usados_celular = set()
usados_correos = set()
usados_celular_tercero = set()
usados_correos_tercero = set()

with open("datos.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "primer_nombre","segundo_nombre","primer_apellido","segundo_apellido",
        "sexo","tipo_identificacion","numero_identificacion",
        "departamento_domicilio","municipio_domicilio","zona_domicilio",
        "numero_via","numero_uno","letra","numero_dos","barrio_sector",
        "celular_uno","correo","genero","orientacion_sexual",
        "personas_cargo","discapacidad",
        "nombre_tercero","apellido_tercero","celular_uno_tercero","correo_tercero"
    ])

    for i in range(1500):
        primer_nombre = primer_nombres[i % len(primer_nombres)]
        segundo_nombre = random.choice(segundo_nombres)
        primer_apellido = apellidos[i % len(apellidos)]
        segundo_apellido = random.choice(apellidos)
        sexo = random.choice(sexos)
        genero = random.choice(generos)
        orientacion = random.choice(orientaciones)

        # Tipo y número de identificación
        tipo_identificacion = random.choice(tipos_identificacion)
        while True:
            numero_identificacion = random.randint(1000000000, 9999999999)
            if numero_identificacion not in usados_identificacion:
                usados_identificacion.add(numero_identificacion)
                break

        # Departamento y municipio coherentes
        departamento = random.choice(list(departamentos.keys()))
        municipio = random.choice(departamentos[departamento])
        zona = random.choice(zonas)

        # Celular único
        while True:
            celular = "3" + str(random.randint(100000000, 999999999))
            if celular not in usados_celular:
                usados_celular.add(celular)
                break

        # Correo único
        while True:
            correo = f"{primer_nombre.lower()}.{primer_apellido.lower()}{i}@ejemplo.com"
            if correo not in usados_correos:
                usados_correos.add(correo)
                break

        # Dirección
        numero_via = random.randint(1, 99)
        numero_uno = random.randint(1, 99)
        letra = random.choice(["a", "b", "c"])
        numero_dos = random.randint(1, 50)
        barrio = random.choice(barrios)

        # Personas a cargo y discapacidad
        personas_cargo = random.randint(1, 10)
        discapacidad = random.choice(discapacidades)

        # Datos del tercero
        nombre_tercero = random.choice(primer_nombres)
        apellido_tercero = random.choice(apellidos)

        while True:
            celular_tercero = "3" + str(random.randint(100000000, 999999999))
            if celular_tercero not in usados_celular_tercero:
                usados_celular_tercero.add(celular_tercero)
                break

        while True:
            correo_tercero = f"{nombre_tercero.lower()}.{apellido_tercero.lower()}{i}@ejemplo.com"
            if correo_tercero not in usados_correos_tercero:
                usados_correos_tercero.add(correo_tercero)
                break

        writer.writerow([
            primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
            sexo, tipo_identificacion, numero_identificacion,
            departamento, municipio, zona,
            numero_via, numero_uno, letra, numero_dos, barrio,
            celular, correo, genero, orientacion,
            personas_cargo, discapacidad,
            nombre_tercero, apellido_tercero, celular_tercero, correo_tercero
        ])
