# **CRONOMETRO PITS A PITS INCLUYENDO LOS NOMBRES- (diferente a CronometroPitsPits.py)**
import pandas as pd
import time

# Función para formatear tiempo mm:ss.ms
def formatear_tiempo(segundos):
    minutos = int(segundos // 60)
    segundos_restantes = segundos % 60
    return f"{minutos:02d}:{segundos_restantes:05.2f}"

# Variables
tiempo_inicio = None
tiempo_vuelta_inicio = None
tiempo_vuelta_acumulado = 0
tiempo_total_acumulado = 0
en_ejecucion = False

piloto_actual = ""

# Lista para guardar vueltas
vueltas = []

# Menú
print("\n== Cronómetro para registrar vueltas (Pits - Pits) ==")
print("Comandos:")
print("  [1] Registrar piloto")
print("  [2] Iniciar")
print("  [ENTER] Registrar vuelta")
print("  [3] Salir y guardar archivo")

# Bucle principal
while True:

    comando = input(">> ")

    # REGISTRAR PILOTO
    if comando == '1':

        nombre = input("Nombre del piloto: ").strip()

        if nombre == "":
            print("Debes ingresar un nombre válido.")
        else:
            piloto_actual = nombre
            print(f"Piloto registrado: {piloto_actual}")

    # INICIAR
    elif comando == '2':

        if piloto_actual == "":
            print("Primero debes registrar el piloto con '0'.")
            continue

        if not en_ejecucion:

            if tiempo_inicio is None:
                tiempo_inicio = time.time()

            tiempo_vuelta_inicio = time.time()
            en_ejecucion = True

            print(f"Cronómetro iniciado para {piloto_actual}.")

        else:
            print("El cronómetro ya está en marcha.")

    # REGISTRAR VUELTA CON ENTER
    elif comando == "":

        if en_ejecucion:

            tiempo_actual = time.time()

            tiempo_vuelta_acumulado += tiempo_actual - tiempo_vuelta_inicio
            tiempo_total_acumulado += tiempo_vuelta_acumulado

            vuelta_segundos = tiempo_vuelta_acumulado

            # Diferencia con la vuelta anterior
            if vueltas:

                ultima_vuelta = vueltas[-1][2]

                ult_min, ult_sec = map(float, ultima_vuelta.split(":"))
                ultimos_segundos = ult_min * 60 + ult_sec

                diferencia = vuelta_segundos - ultimos_segundos

            else:
                diferencia = 0

            vuelta_num = len(vueltas) + 1

            vueltas.append((
                piloto_actual,
                vuelta_num,
                formatear_tiempo(vuelta_segundos),
                diferencia,
                formatear_tiempo(tiempo_total_acumulado)
            ))

            signo = "+" if diferencia > 0 else "-"

            print(
                f"{piloto_actual} | Vuelta {vuelta_num}: {formatear_tiempo(vuelta_segundos)} "
                f"({signo}{abs(diferencia):.2f}s) | Tiempo global: {formatear_tiempo(tiempo_total_acumulado)}"
            )

            tiempo_vuelta_acumulado = 0
            tiempo_vuelta_inicio = time.time()

        else:
            print("Debes iniciar el cronómetro primero con '1'.")

    # SALIR
    elif comando == '3':
        break

    else:
        print("Comando no reconocido.")

# Exportar archivo
if vueltas:

    data = []
    mejor_vuelta = None
    mejor_tiempo = float("inf")

    for v in vueltas:

        data.append([v[0], v[1], v[2], f"{v[3]:.2f}s", v[4]])

        min_, sec_ = map(float, v[2].split(":"))
        segundos_vuelta = min_ * 60 + sec_

        if segundos_vuelta < mejor_tiempo:
            mejor_tiempo = segundos_vuelta
            mejor_vuelta = v[1]

    df = pd.DataFrame(
        data,
        columns=["Piloto", "Número de vuelta", "Tiempo por vuelta", "Diferencia", "Tiempo global"]
    )

    nombre_archivo = "vueltasPitsPits.csv"
    df.to_csv(nombre_archivo, index=False)

    print(f"\nDatos exportados exitosamente a '{nombre_archivo}'")
    print(f"La mejor vuelta fue la {mejor_vuelta} con tiempo {formatear_tiempo(mejor_tiempo)}")

else:
    print("No se registraron vueltas.")