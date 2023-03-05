import matplotlib.pyplot as plt
import math

# Pedimos el número de vectores a graficar
n = int(input("Ingrese el número de vectores a graficar: "))

# Lista de colores
colors = ["b", "g", "r", "c", "m", "y", "k", "w"]

# Listas para guardar las coordenadas de los puntos
x1_list = []
y1_list = []
x2_list = []
y2_list = []

# Pedimos las coordenadas de los puntos P y Q de cada vector
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

    # Guardamos las coordenadas del vector en su forma canónica
    x1_list.append(0)
    y1_list.append(0)
    x2_list.append(vx)
    y2_list.append(vy)

# Dibujamos los vectores
for i in range(n):
    x1 = x1_list[i]
    y1 = y1_list[i]
    x2 = x2_list[i]
    y2 = y2_list[i]

    # Dibujamos el vector
    plt.arrow(x1, y1, x2, y2, head_width=0.1, head_length=0.2, fc=colors[i], ec=colors[i],
              label=f"vector {i + 1}: <{x2:.2f}, {y2:.2f}>")

# Mostramos el título y la leyenda
plt.title("Vectores en el plano")
plt.xlabel("Coordenada x")
plt.ylabel("Coordenada y")
plt.legend()

# Mostramos la gráfica
plt.grid()
plt.show()
