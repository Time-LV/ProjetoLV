import numpy as np
from flask import Flask, render_template
import CalculoLotkaVolterra as clv

app = Flask(__name__)


@app.route('/')
def index():
    # Parâmetros do modelo de Lotka-Volterra
    alpha = 0.1
    beta = 0.02
    delta = 0.01
    gamma = 0.1

    # Condições iniciais
    initial_conditions = [40, 9]

    # Tempo de simulação
    t_start = 0
    t_end = 200
    t_step = 0.1  # ou outro valor positivo, dependendo da sua lógica
    t_values = np.arange(t_start, t_end, t_step)

    # Simular o modelo de Lotka-Volterra usando o método de Euler
    result = clv.euler_method(clv.lotka_volterra, initial_conditions, t_values, args=(alpha, beta, delta, gamma))

    # Renderizar a página HTML com os resultados
    return render_template('index.html', t_values=t_values, result=result)


if __name__ == '__main__':
    app.run(debug=True)