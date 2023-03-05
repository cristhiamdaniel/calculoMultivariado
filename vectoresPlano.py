import math

# Pedimos el número de vectores a evaluar
n = int(input("Ingrese el número de vectores a evaluar: "))

# Pedimos las coordenadas de los puntos P y Q de cada vector y calculamos su módulo y dirección
for i in range(n):
    # Pedimos las coordenadas de P
    px = float(input(f"Ingrese la coordenada x de P del vector {i + 1}: "))
    py = float(input(f"Ingrese la coordenada y de P del vector {i + 1}: "))

    # Pedimos las coordenadas de Q
    qx = float(input(f"Ingrese la coordenada x de Q del vector {i + 1}: "))
    qy = float(input(f"Ingrese la coordenada y de Q del vector {i + 1}: "))

    # Calculamos las coordenadas del vector
    vx = qx - px
    vy = qy - py

    # Calculamos el módulo del vector
    mod = math.sqrt(vx ** 2 + vy ** 2)

    # Calculamos la dirección del vector en radianes y en grados
    dir_rad = math.atan2(vy, vx)
    dir_deg = math.degrees(dir_rad)

    # Imprimimos los resultados
    print(f"Vector {i + 1}: módulo={mod:.2f}, dirección={dir_deg:.2f} grados")
    print()
