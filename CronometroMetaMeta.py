import pandas as pd
import time

def formatear_tiempo(segundos):
    minutos = int(segundos // 60)
    segundos_restantes = segundos % 60
    return f"{minutos:02d}:{segundos_restantes:05.2f}"

def registrar_vuelta(vueltas_lista, tiempo_vuelta_inicio, tiempo_total_acumulado, piloto):
    tiempo_actual = time.time()
    
    vuelta_segundos = tiempo_actual - tiempo_vuelta_inicio
    nuevo_tiempo_total = tiempo_total_acumulado + vuelta_segundos

    if vueltas_lista:
        ultima_vuelta_str = vueltas_lista[-1][1] 
        ult_min, ult_sec = map(float, ultima_vuelta_str.split(":"))
        ultimos_segundos = ult_min * 60 + ult_sec
        diferencia = vuelta_segundos - ultimos_segundos
    else:
        diferencia = 0

    vuelta_num = len(vueltas_lista) + 1
    
    registro = (
        vuelta_num,
        formatear_tiempo(vuelta_segundos),
        diferencia,
        formatear_tiempo(nuevo_tiempo_total),
        piloto
    )

    return registro, tiempo_actual, nuevo_tiempo_total

def guardar_excel(vueltas, nombre_archivo="vueltasMetaMeta.csv"):
    if not vueltas:
        return "No se registraron vueltas."

    data = []
    mejor_tiempo = float("inf")
    mejor_vuelta = None

    for v in vueltas:
        data.append([v[0], v[1], f"{v[2]:.2f}s", v[3], v[4]]) 
        
        min_, sec_ = map(float, v[1].split(":"))
        segundos_v = min_ * 60 + sec_
        if segundos_v < mejor_tiempo:
            mejor_tiempo = segundos_v
            mejor_vuelta = v[0]

    df = pd.DataFrame(
        data,
        columns=["Número de vuelta", "Tiempo por vuelta", "Diferencia", "Tiempo global", "Piloto"]
    )
    df.to_csv(nombre_archivo, index=False)
    return f"Exportado a {nombre_archivo}. Mejor vuelta: {mejor_vuelta} ({formatear_tiempo(mejor_tiempo)})"