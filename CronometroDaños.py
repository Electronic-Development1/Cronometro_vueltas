import time

def registrar_daño(numero_vuelta, nombre_piloto):
    print(f"\n--- CRONÓMETRO DE DAÑO ACTIVO (Vuelta {numero_vuelta}) ---")
    inicio_reparacion = time.time()
    descripcion = input("¿Qué se está reparando?: ")
    
    input(">> Presiona ENTER cuando la reparación esté terminada...")
    fin_reparacion = time.time()
    duracion = fin_reparacion - inicio_reparacion

    minutos = int(duracion // 60)
    segundos = duracion % 60
    tiempo_fmt = f"{minutos:02d}:{segundos:05.2f}"
    
    print(f"Reparación finalizada en: {tiempo_fmt}")
    
    return {
        "Vuelta": numero_vuelta,
        "Evento": f"DAÑO: {descripcion}",
        "Tiempo": tiempo_fmt,
        "Segundos": duracion,
        "Piloto": nombre_piloto
    }
