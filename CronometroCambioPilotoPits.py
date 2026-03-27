import time

def cambio_piloto(vuelta_actual):
    print(f"\n--- ENTRADA A PITS (Vuelta {vuelta_actual}) ---")
    inicio_pits = time.time()
    
    nuevo_piloto = input("Ingrese el nombre del nuevo piloto: ")
    input(f">> {nuevo_piloto}. Presiona ENTER para salir de Pits...")
    
    fin_pits = time.time()
    duracion = fin_pits - inicio_pits
    
    minutos = int(duracion // 60)
    segundos = duracion % 60
    tiempo_fmt = f"{minutos:02d}:{segundos:05.2f}"
    
    print(f"Tiempo del cambio: {tiempo_fmt}. Nuevo piloto: {nuevo_piloto}")
    
    return {
        "Vuelta": vuelta_actual,
        "Evento": "CAMBIO DE PILOTO",
        "Tiempo": tiempo_fmt,
        "Segundos": duracion,
        "Piloto": nuevo_piloto
    }