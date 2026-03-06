# CRÓNOMETRO INCLUYENDO EL PRIMER TIEMPO DE META A PITS 
# (el primer piloto hace un recorido más largo. sale en meta y llega a pits)

import pandas as pd
import time

def formatear(seg):
    m = int(seg // 60)
    s = seg % 60
    return f"{m:02d}:{s:05.2f}"

inicio_vuelta = None
en_carrera = False
piloto = ""
vueltas = []

esperando_pits = False
inicio_meta_pits = None

print("\n== Cronómetro de Vueltas ==")

piloto = input("Nombre del primer piloto: ")

print("\nComandos rápidos:")
print("1  → Iniciar carrera")
print("Enter → Registrar vuelta")
print("2 → Última vuelta (va a pits)")
print("3 → Llegó a pits")
print("4 → Nuevo piloto desde pits")
print("5 → Guardar y salir\n")

while True:

    cmd = input()

    # INICIAR CARRERA
    if cmd == "1":

        inicio_vuelta = time.time()
        en_carrera = True
        print("Carrera iniciada")

    # REGISTRAR VUELTA NORMAL
    elif cmd == "":

        if not en_carrera:
            print("No hay piloto corriendo.")
            continue

        ahora = time.time()
        tiempo_vuelta = ahora - inicio_vuelta

        num = len(vueltas) + 1

        vueltas.append([
            piloto,
            num,
            formatear(tiempo_vuelta),
            "",
            ""
        ])

        print(f"{piloto} - Vuelta {num}: {formatear(tiempo_vuelta)}")

        inicio_vuelta = time.time()

    # ÚLTIMA VUELTA HACIA PITS
    elif cmd == "2":

        ahora = time.time()
        tiempo_vuelta = ahora - inicio_vuelta

        num = len(vueltas) + 1

        vueltas.append([
            piloto,
            num,
            formatear(tiempo_vuelta),
            "PITS",
            ""
        ])

        print(f"{piloto} última vuelta: {formatear(tiempo_vuelta)}")
        print("Piloto va hacia pits...")

        inicio_meta_pits = time.time()
        esperando_pits = True

    # LLEGÓ A PITS
    elif cmd == "3":

        if not esperando_pits:
            print("No hay piloto en camino a pits.")
            continue

        tiempo_meta_pits = time.time() - inicio_meta_pits

        vueltas[-1][4] = formatear(tiempo_meta_pits)

        print("Tiempo META → PITS:", formatear(tiempo_meta_pits))

        esperando_pits = False
        en_carrera = False

    # NUEVO PILOTO DESDE PITS
    elif cmd == "4":

        piloto = input("Nombre del nuevo piloto: ")

        inicio_vuelta = time.time()
        en_carrera = True

        print(f"{piloto} salió de pits.")

    # GUARDAR
    elif cmd == "5":
        break


# GUARDAR ARCHIVO
if vueltas:

    df = pd.DataFrame(
        vueltas,
        columns=[
            "Piloto",
            "Vuelta",
            "Tiempo vuelta",
            "Evento",
            "Meta → Pits"
        ]
    )

    archivo = "vueltas_carrera.csv"
    df.to_csv(archivo, index=False)

    print("\nArchivo guardado:", archivo)

else:

    print("No se registraron vueltas.")