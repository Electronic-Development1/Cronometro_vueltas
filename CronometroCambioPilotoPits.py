import time

def registrar_pits(vuelta_actual, piloto_actual):
    print(f"\n--- INGRESO A PITS (Vuelta {vuelta_actual}) ---")
    print(f"[{piloto_actual}] cruzo la meta y va a parar en pits")
    
    # 1. CRONÓMETRO META-PITS
    inicio_transito = time.time()
    input(">> Presiona ENTER cuando el carro llegue a pits")
    fin_transito = time.time()
    
    tiempo_transito = fin_transito - inicio_transito
    min_t, sec_t = int(tiempo_transito // 60), tiempo_transito % 60
    fmt_transito = f"{min_t:02d}:{sec_t:05.2f}"
    print(f"Tiempo de tránsito: {fmt_transito}")
    
    # 2. CRONÓMETRO DE PARADA
    inicio_parada = time.time()
    nuevo_piloto = input(">> Ingrese el nombre del NUEVO piloto: ")
    input("Presiona ENTER cuando el carro arranque")
    fin_parada = time.time()
    
    tiempo_parada = fin_parada - inicio_parada
    min_p, sec_p = int(tiempo_parada // 60), tiempo_parada % 60
    fmt_parada = f"{min_p:02d}:{sec_p:05.2f}"
    
    # 3. CÁLCULOS FINALES
    tiempo_total_pits = tiempo_transito + tiempo_parada
    min_tot, sec_tot = int(tiempo_total_pits // 60), tiempo_total_pits % 60
    fmt_total = f"{min_tot:02d}:{sec_tot:05.2f}"
    
    print(f"Parada en pits: {fmt_parada} | Tiempo total perdido: {fmt_total}")
    
    return {
        "Vuelta": vuelta_actual,
        "Evento": f"PITS (Meta-Pits: {fmt_transito} | Parada: {fmt_parada})",
        "Tiempo": fmt_total,
        "Segundos": tiempo_total_pits,
        "Piloto": nuevo_piloto
    }