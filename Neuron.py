"""
A Study Process Of A Neuron Object - Train Nand Gates
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Neuron(object):

    condition = 'New'

    """
        the gate inputs (x) need to be Constant - Don't change values!.
        x0 - is a DC - direct current as '1' all the time.
        z - is the desired outputs for Nand gate

        |---------------------------------------------------------------------------------------------------------------------|
        |----------------------------------| x0*w0 | x1*w1 | x2*w2 | s=c0+c1+c2 | if s>t n=1 | z-n | r*e | x0*d | x1*d | x2*d |
        | x0 | x1 | x2 | z  | w0 | w1 | w2 |   c0  |   c1  |   c2  |      s     |      n     |  e  |  d  |  w0  |  w1  |  w2  |
        |--------------|----|--------------|-----------------------|------------|------------|-----|-----|------|------|------|
        | 1  | 0  | 0  | 1  | 0  | 0  | 0  |       |       |       |            |            |     |     |  ??  |  ??  |  ??  |
        | 1  | 0  | 1  | 1  | ?? | ?? | ?? |       |       |       |            |            |     |     |      |      |      |
        | 1  | 1  | 0  | 1  |    |    |    |       |       |       |            |            |     |     |      |      |      |
        | 1  | 1  | 1  | 0  |    |    |    |       |       |       |            |            |     |     |      |      |      |
        |---------------------------------------------------------------------------------------------------------------------|

    """


    def __init__(self, name):
        """ constructor """
        self.name = name

        self.x = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
        self.w = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  # weights
        self.c = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  # c0=x0*w0 ; c1=x1*w1 ; c2=x2*w2
        self.output = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  # output: w0=x0*d ; w1=x1*d ; w2=x2*d

        self.w_outputs = [0, 0, 0]

        self.z = [1, 1, 1, 0]  # desired outputs for Nand gate - Don't change values!

        self.s = [0, 0, 0, 0]  # sum: s = c0 + c1 + c2
        self.n = [0, 0, 0, 0]  # if s > t then n=1 else n=0
        self.e = [0, 0, 0, 0]  # error: e = z - n
        self.d = [0, 0, 0, 0]  # Correction: d = r * e

        self.t = 0.5  # threshold
        self.r = 0.1  # delta

    def calculate_values(self):
        xyz=0
        while xyz < 4:
            for i in range(4):
                temp_sum = 0
                for j in range(3):
                    if i != 0:
                        self.w[i][j] = self.w[i-1][j] + self.w_outputs[j]

                    self.c[i][j] = self.x[i][j] * self.w[i][j]
                    temp_sum += self.c[i][j]

                self.s[i] = temp_sum
                if self.s[i] > self.t:
                    self.n[i] = 1
                else:
                    self.n[i] = 0

                self.e[i] = self.z[i] - self.n[i]

                self.d[i] = self.r * self.e[i]

                for k in range(3):
                    self.w_outputs[k] = self.d[i] * self.x[i][k]
                    if i == 0:
                        self.output[i][k] = self.w_outputs[k]
                    else:
                        self.output[i][k] = self.output[i-1][k] + self.w_outputs[k]

                xyz += 1
                print("xyz: " + str(xyz))

    def print_matrix(self):
        """ this function print all the class values - DEBUG function """

        temp_str = ""

        print("""\n |---------------------------------------------------------------------------------------------------------------------|
 |----------------------------------| x0*w0 | x1*w1 | x2*w2 | s=c0+c1+c2 | if s>t n=1 | z-n | r*e | x0*d | x1*d | x2*d |
 | x0 | x1 | x2 | z  | w0 | w1 | w2 |   c0  |   c1  |   c2  |      s     |      n     |  e  |  d  |  w0  |  w1  |  w2  |
 |--------------|----|--------------|-----------------------|------------|------------|-----|-----|------|------|------|""")

        for i in range(4):
            for j in range(3):
                temp_str += " |" + "%0.1f"% self.x[i][j]

            temp_str += " | " + str("%0.1f"% self.z[i])

            for j in range(3):
                temp_str += "| " + "%0.1f"% self.w[i][j]

            for j in range(3):
                temp_str += " |\t" + "%0.1f"% self.c[i][j]

            temp_str += " |\t " + str("%0.1f"% self.s[i]) + "\t"
            temp_str += " |\t " + str("%0.1f"% self.n[i]) + "\t"
            temp_str += "  | " + str("%0.1f"% self.e[i])
            temp_str += " | " + str("%0.1f"% self.d[i])

            for j in range(3):
                temp_str += " |  " + "%0.1f"% self.output[i][j]

            temp_str += " | \n"

        print(temp_str + " |---------------------------------------------------------------------------------------------------------------------|\n")


    def plot_graph(self):
        fig, ax = plt.subplots()
        ax.plot([0, 0, 1, 1], [0, 1, 0, 1], 'ro')
        ax.set_ylim(-1, 2)
        ax.set_xlim(-1, 2)

        x = np.arange(-1, 2 * np.pi, 0.1)
        line, = ax.plot(x, np.sin(x))

        def animate(i):
            line.set_ydata(np.sin(x + i ))
            return line,

        def init():
            line.set_ydata(np.ma.array(x, mask=True))
            return line,

        ani = animation.FuncAnimation(fig, animate, np.arange(-1, 200), init_func=init, interval=100, blit=True)
        plt.show()

