import numpy as np
import matplotlib.pyplot as plt


# Definir equações diferenciais do modelo Lotka-Volterra
def lotka_volterra(t, y, alpha, beta, delta, gamma):
    prey, predator = y
    dydt = [alpha * prey - beta * prey * predator, delta * prey * predator - gamma * predator]
    return dydt


# Método de Euler para resolver equações diferenciais
def euler_method(func, y0, t, args):
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        y[i] = y[i - 1] + np.multiply(func(t[i - 1], y[i - 1], *args), dt)
    return y


#Parametros do modelo Lotka-Volterra
alpha = 0.1  # Taxa de crecimiento de presas
beta = 0.02  # Taxa de depredação de presas por predadores
delta = 0.01  # Taxa de reprodução de predadores por presas
gamma = 0.1  # Taxa de mortalidade de predadores

# Condições iniciais
initial_conditions = [40, 9]  # Número inicial de presas e predadores

# Tempo de simulação
t_start = 0  # fixo
t_end = 200  # input
t_step = 0.1
t_values = np.arange(t_start, t_end, t_step)

# Simular o modelo de Lotka-Volterra usando o método de Euler
result = euler_method(lotka_volterra, initial_conditions, t_values, args=(alpha, beta, delta, gamma))

# print(result)

# Graficar os resultados
plt.plot(t_values, result[:, 0], label='Presas (Presa)')
plt.plot(t_values, result[:, 1], label='Depredadores (Predador)')
plt.xlabel('Tempo (Dias)')
plt.ylabel('População')
plt.title('Modelo de Lotka-Volterra')
plt.legend()

plt.savefig('lotka_volterra_simulation.png')

# Mostrar a gráfica
plt.show()
