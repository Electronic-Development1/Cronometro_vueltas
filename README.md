CRONOMETROS TELEMETRIA VTH 2026

Sistema modular en Python diseñado para la captura, procesamiento y exportación de datos en tiempo real durante pruebas de pista y competencias.

Este sistema permite gestionar múltiples cronómetros paralelos para monitorear el desempeño del vehículo y el equipo. Se enfoca en medir los tiempos por vuelta, el registro de incidentes y los tiempos en Pits (tránsito y parada).


Guía de Comandos Rápidos
Comando     Momento de Ejecución    Resultado

1           Inicio de Carrera       Setea el piloto inicial y arranca el reloj global.
ENTER       Paso por Meta           Registra la vuelta, calcula la diferencia vs. anterior y tiempo global.
D           Daño o incidente        Abre el log de reparaciones (pide descripción y mide duración).
P           Entrada a Pits          Activa la secuencia completa de telemetría de boxes (ver abajo).
3           Fin de Sesión           Detiene el sistema y exporta los resultados.


Protocolo de Pits (Comando P)
El comando P es el más crítico y debe ejecutarse siguiendo este orden para no perder datos:

En la Meta: Presiona P justo cuando el coche cruce la línea para entrar a boxes. El sistema registrará la vuelta automáticamente.

En Pits: Presiona ENTER cuando el coche se detenga. Se guardará el Tiempo Meta-Pits.

Durante la Parada: El sistema pedirá el nombre del Nuevo Piloto.

Salida a Pista: Presiona ENTER cuando el coche salga de pits. Se guardará el Tiempo de Parada y el cronómetro de la nueva vuelta iniciará automáticamente.


Reportes
Al presionar 3, se generarán dos archivos en la carpeta raíz:

Reporte_Final.csv: Tabla detallada con todas las vueltas, tiempos, diferencias y el piloto asignado a cada una.

Reporte_Danos.csv: Diario cronológico de cada incidente, descripción del daño y desglose de tiempos en pits.

Nota para el operador: Mantén la calma. Si te equivocas en un comando, el sistema está diseñado para no cerrarse bruscamente. Prioriza siempre el registro en la línea de meta.