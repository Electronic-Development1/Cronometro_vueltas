import pandas as pd
import time
import CronometroMetaMeta as meta
import CronometroDaños as danos 
import CronometroCambioPilotoPits as pits

vueltas = []
datos_incidentes = []
tiempo_vuelta_inicio = 0
tiempo_total_acumulado = 0
en_carrera = False
piloto_actual = ""

print("\n== CRONOMETRO SQUALO VTH ==")
print("Comandos: [1] Iniciar | [ENTER] Vuelta | [D] Registrar Daño | [P] Cambiar Piloto | [3] Salir")

while True:
    comando = input(">> ").lower()

    # 1. INICIAR CARRERA
    if comando == '1':
        if not en_carrera:
            piloto_actual = input("Nombre del piloto que inicia: ")
            tiempo_vuelta_inicio = time.time()
            en_carrera = True
            print(f">>> Carrera Iniciada. Piloto: {piloto_actual}")
        else:
            print("Ya está en ejecución.")

    # 2. REGISTRAR VUELTA
    elif comando == '' and en_carrera:
        registro, tiempo_vuelta_inicio, tiempo_total_acumulado = meta.registrar_vuelta(
            vueltas, 
            tiempo_vuelta_inicio, 
            tiempo_total_acumulado,
            piloto_actual
        )
        vueltas.append(registro)

        signo = "+" if registro[2] > 0 else "-"
        print(f"Vuelta {registro[0]} [{piloto_actual}]: {registro[1]} ({signo}{abs(registro[2]):.2f}s)")

    # 3. REGISTRAR DAÑO
    elif comando == 'd' and en_carrera:
        v_actual = len(vueltas) + 1
        resultado_danio = danos.registrar_daño(v_actual, piloto_actual)
        datos_incidentes.append(resultado_danio)
        print(f">>> Incidente guardado en Vuelta {v_actual}")

    # 4. CAMBIO DE PILOTO
    elif comando == 'p' and en_carrera:
        v_actual = len(vueltas) + 1
        resultado_cambio = pits.cambio_piloto(v_actual)
        piloto_actual = resultado_cambio["Piloto"]
        datos_incidentes.append(resultado_cambio)
        print(f">>> Cambio registrado. Piloto actual: {piloto_actual}")

    # 5. SALIR
    elif comando == '3':
        if vueltas:
            mensaje = meta.guardar_excel(vueltas, "Reporte_Final.csv")
            print(f"\n{mensaje}")

            if datos_incidentes:
                df_danos = pd.DataFrame(datos_incidentes)
                df_danos.to_csv("Reporte_Danos.csv", index=False)
                print("\nReporte incidentes guardado")

        break