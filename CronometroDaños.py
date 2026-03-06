import pandas as pd
import time

# Función para formatear el tiempo
def formatear_tiempo(segundos):
    minutos = int(segundos // 60)
    segundos_restantes = segundos % 60
    return f"{minutos:02d}:{segundos_restantes:05.2f}"

# Variables
tiempo_inicio_dano = None
en_reparacion = False
danos = []
tiempo_total_danos = 0
piloto = ""

print("\n== Cronómetro de daños ==")
print("Comandos:")
print("[1] Registrar daño")
print("[2] Daño arreglado")
print("[3] Salir y guardar CSV")

while True:

    comando = input(">> ")

    # Registrar daño
    if comando == "1":

        if not en_reparacion:

            # Empieza a contar inmediatamente
            tiempo_inicio_dano = time.time()
            en_reparacion = True

            print("Cronómetro de daño iniciado.")

            # Luego pide el piloto
            piloto = input("Nombre del piloto cuando ocurrió el daño: ")

        else:
            print("Ya hay un daño en reparación.")

    # Finalizar daño
    elif comando == "2":

        if en_reparacion:

            tiempo_fin = time.time()
            tiempo_total = tiempo_fin - tiempo_inicio_dano

            numero_dano = len(danos) + 1

            tiempo_total_danos += tiempo_total

            danos.append((
                numero_dano,
                piloto,
                formatear_tiempo(tiempo_total),
                formatear_tiempo(tiempo_total_danos)
            ))

            print(f"\nDaño {numero_dano} arreglado.")
            print(f"Piloto: {piloto}")
            print(f"Tiempo reparación: {formatear_tiempo(tiempo_total)}")
            print(f"Tiempo total acumulado de daños: {formatear_tiempo(tiempo_total_danos)}")

            en_reparacion = False

        else:
            print("No hay daño registrado.")

    # Salir
    elif comando == "3":
        break

    else:
        print("Comando no reconocido.")


# Guardar CSV
if danos:

    data = []

    for d in danos:
        data.append([d[0], d[1], d[2], d[3]])

    df = pd.DataFrame(
        data,
        columns=[
            "Número de daño",
            "Piloto",
            "Tiempo reparación",
            "Tiempo total acumulado daños"
        ]
    )

    nombre_archivo = "registro_danos.csv"

    df.to_csv(nombre_archivo, index=False)

    print(f"\nDatos exportados exitosamente a '{nombre_archivo}'")
    print(f"Tiempo total acumulado de daños: {formatear_tiempo(tiempo_total_danos)}")

else:
    print("No se registraron daños.")