""" Professor mudei o import do numpy só a para o código ficar mais limpo 
Outro detalhe: Por algum motivo não roda no jupyter notebook... 
No VScode rodou normal
No terminal também rodou normal"""

from numpy import pi, sin, cos, arange
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definição das condições básicas
bmax = 1  # Normalize bmax em 1
freq = 60  # 60 Hz
w = 2 * pi * freq  # velocidade angular (rad/s)

# Inicialmente, determine os três campos magnéticos componentes
t = arange(0, 1 / 60, 1 / 6000)
Baa = sin(w * t) * (cos(0) + sin(0) * 1j)
Bbb = sin(w * t - 2 * pi / 3) * (cos(2 * pi / 3) + sin(2 * pi / 3) * 1j)
Bcc = sin(w * t + 2 * pi / 3) * (cos(-2 * pi / 3) + sin(-2 * pi / 3) * 1j)

# Cálculo de B líquida (Bnet)
Bnet = Baa + Bbb + Bcc

# Cálculo de um círculo que representa o valor máximo esperado de B líquida (Bnet)
circulo = 1.5 * (cos(w * t) + sin(w * t) * 1j)

# Função para inicializar a animação


def inicio():
    linha.set_data([], [])
    campo_aa.set_UVC(0, 0)
    campo_bb.set_UVC(0, 0)
    campo_cc.set_UVC(0, 0)
    campo_resultante.set_UVC(0, 0)
    return linha, campo_aa, campo_bb, campo_cc, campo_resultante

# Função para atualizar a animação


def animacao(i):
    linha.set_data(circulo.real, circulo.imag)
    campo_aa.set_UVC(Baa.real[i], Baa.imag[i])
    campo_bb.set_UVC(Bbb.real[i], Bbb.imag[i])
    campo_cc.set_UVC(Bcc.real[i], Bcc.imag[i])
    campo_resultante.set_UVC(Bnet.real[i], Bnet.imag[i])
    return linha, campo_aa, campo_bb, campo_cc, campo_resultante


# Configuração da figura
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Linha para o círculo
linha, = ax.plot([], [], color="purple", linewidth=5.0, label="Círculo")

# Vetores dos campos magnéticos componentes
campo_aa = ax.quiver(0, 0, 0, 0, color='red', angles='xy',
                     scale_units='xy', scale=1, label='Baa')
campo_bb = ax.quiver(0, 0, 0, 0, color='green', angles='xy',
                     scale_units='xy', scale=1, label='Bbb')
campo_cc = ax.quiver(0, 0, 0, 0, color='blue', angles='xy',
                     scale_units='xy', scale=1, label='Bcc')

# Vetor do campo magnético resultante
campo_resultante = ax.quiver(
    0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, label='Bnet')

# Título e legenda
ax.set_title("Gráfico Campo Girante", fontsize=17)
ax.set_xlabel("Eixo X", fontsize=15)
ax.set_ylabel("Eixo Y", fontsize=15)
ax.legend(loc="upper left")

# Criação da animação
ani = animation.FuncAnimation(
    fig, animacao, init_func=inicio, frames=len(t), interval=20, blit=True)

# Mostrar a animação
plt.show()
