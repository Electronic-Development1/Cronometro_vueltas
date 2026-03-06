import time
import csv

def formatear(seg):
    m = int(seg // 60)
    s = seg % 60
    return f"{m:02d}:{s:05.2f}"

cambios = []

inicio = None
piloto_entra = ""
piloto_sale = ""

tiempo_total_cambios = 0

print("\n== Cronómetro Cambio de Piloto ==")
print("1 Registrar pilotos (entra / sale)")
print("2 Iniciar cronómetro de cambio")
print("3 Terminar cambio")
print("4 Finalizar carrera")

while True:

    cmd = input(">> ")

    # Registrar pilotos antes del cambio
    if cmd == "1":

        piloto_entra = input("Piloto que entra a pits: ")
        piloto_sale = input("Piloto que sale a pista:  ")
        print('\n')

        print(f"Registro listo: {piloto_entra} -> {piloto_sale}")
        print("Usa la opción 2 cuando empiece el cambio.  ")

    # Iniciar cronómetro
    elif cmd == "2":

        if piloto_entra == "" or piloto_sale == "":
            print("Primero debes registrar los pilotos con opción 1.")
        else:
            inicio = time.time()
            print("Cronómetro de cambio iniciado.")

    # Terminar cronómetro
    elif cmd == "3":

        if inicio is None:
            print("Primero debes iniciar el cronómetro.")
        else:

            tiempo = time.time() - inicio
            tiempo_total_cambios += tiempo

            cambios.append([
                piloto_entra,
                piloto_sale,
                len(cambios) + 1,
                formatear(tiempo)
            ])

            print(f"Cambio completado {piloto_entra} -> {piloto_sale}")
            print("Tiempo de cambio:", formatear(tiempo))

            inicio = None
            piloto_entra = ""
            piloto_sale = ""

    # Finalizar programa
    elif cmd == "4":
        break

    else:
        print("Comando inválido")


# Guardar CSV
with open("cambio_pilotos.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Piloto que entra",
        "Piloto que sale",
        "Numero de cambio",
        "Tiempo"
    ])

    for c in cambios:
        writer.writerow(c)

    # Fila final con el tiempo total (4 columnas para evitar errores)
    writer.writerow(["TOTAL CAMBIOS", "", "", formatear(tiempo_total_cambios)])

print("\nDatos guardados en cambio_pilotos.csv")
print("Tiempo total en cambios:", formatear(tiempo_total_cambios))