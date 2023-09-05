import numpy as np
import matplotlib.pyplot as plt

# Dados do problema
Tb = 100 + 273.15  # Temperatura na base da aleta (K)
Tfluidoc = 25 + 273.15  # Temperatura do fluido circundante (K)

Coef_Conv = 20  # Coeficiente de convecção (W/m²·K)
L = 0.15  # Comprimento da aleta (m)
A_c = 0.02 * 0.24  # Área da seção transversal da aleta (m²)
k = 240  # Condutividade térmica do alumínio (W/m·K)


# Cálculo da taxa de transferência de calor
Q = (Coef_Conv * A_c * (Tb - Tfluidoc)) / L

# Cálculo da eficiência da aleta
Q_max = Coef_Conv * A_c * (Tb - Tfluidoc)
eta = Q / Q_max

# Cálculo da efetividade da aleta
P = 2 * (20 + 240) / 1000  # Perímetro da seção transversal da aleta (m)
delta_T = Tb - Tfluidoc
Q_max_infinite = (Coef_Conv * A_c) / P * delta_T
E = Q / Q_max_infinite

# Cálculo do comprimento da aleta para a hpótese de aleta infinita
L_infinite = (k * A_c) / Coef_Conv

# Gráfico da distribuição de temperatura ao longo da aleta
x = np.linspace(0, L, 100)
T_x = Tb - (Q_max / (2 * Coef_Conv * A_c)) * (np.cosh(Coef_Conv * x / (2 * k)) / np.cosh(Coef_Conv * L / (2 * k)))

plt.figure(figsize=(10, 5))
plt.plot(x, T_x)
plt.xlabel('Comprimento da Aleta (m)')
plt.ylabel('Temperatura (K)')
plt.title('Distribuição de Temperatura na Aleta')
plt.grid(True)
plt.show()

# Imprimir resultados
print(f"1. Temperatura na extremidade da aleta: {T_x[-1]:.2f} K. Ou seja, {T_x[-1] - 273.15:.2f} °C.")
print(f"Isso mostra um delta de temperatura de {T_x[-1] - Tb:.2f} K. \n")
print(f"2. Taxa de transferência de calor: {Q:.2f} W")
print(f"3. Eficiência da aleta: {eta:.4f}")
print(f"4. Efetividade da aleta: {E:.4f}")
print(f"5. Taxa de transferência de calor para aleta infinita: {Q_max_infinite:.2f} W")
print(f"6. Comparação com o resultado da aleta infinita: {Q / Q_max_infinite:.4f}")
print(f"7. Comprimento da aleta para a hipótese de aleta infinita: {L_infinite:.2f} m")
