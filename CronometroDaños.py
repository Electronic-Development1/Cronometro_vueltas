import time

def registrar_daño(numero_vuelta, nombre_piloto):
    print(f"\n--- CRONÓMETRO DE DAÑO ACTIVO (Vuelta {numero_vuelta}) ---")
    inicio_reparacion = time.time()

    input(">> Presiona ENTER cuando el daño esté reparado...")
    fin_reparacion = time.time()
    duracion = fin_reparacion - inicio_reparacion

    minutos = int(duracion // 60)
    segundos = duracion % 60
    tiempo_fmt = f"{minutos:02d}:{segundos:05.2f}"
    
    print(f"Reparación finalizada en: {tiempo_fmt}")
    
    return {
        "Vuelta": numero_vuelta,
        "Tipo": "DAÑO",
        "Piloto": nombre_piloto,
        "Duracion": tiempo_fmt,
        "Segundos": duracion
    }
