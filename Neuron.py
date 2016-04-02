"""
A Study Process Of A Neuron Object - Train Nand Gates
"""

import matplotlib.pyplot as plt
import numpy as np

"""
the gate inputs (x) need to be Constant - Don't change values!.
x0 - is a DC - direct current as '1' all the time.
z - is the desired outputs for Nand gate

|---------------------------------------------------------------------------------------------------------------------|
|----------------------------------| x0*w0 | x1*w1 | x2*w2 | s=c0+c1+c2 | if s>t n=1 | z-n | r*e | x0*d | x1*d | x2*d |
| x0 | x1 | x2 | z  | w0 | w1 | w2 |   c0  |   c1  |   c2  |      s     |      n     |  e  |  d  |  w0  |  w1  |  w2  |
|--------------|----|--------------|-----------------------|------------|------------|-----|-----|------|------|------|
| 1  | 0  | 0  | 1  | 0  | 0  | 0  |       |       |       |            |            |     |     |      |      |      |
| 1  | 0  | 1  | 1  |    |    |    |       |       |       |            |            |     |     |      |      |      |
| 1  | 1  | 0  | 1  |    |    |    |       |       |       |            |            |     |     |      |      |      |
| 1  | 1  | 1  | 0  |    |    |    |       |       |       |            |            |     |     |      |      |      |
|---------------------------------------------------------------------------------------------------------------------|

"""

x = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

w = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]          # weights

c = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]          # c0=x0*w0 ; c1=x1*w1 ; c2=x2*w2

output = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]     # output: w0=x0*d ; w1=x1*d ; w2=x2*d

z = [1, 1, 1, 0]  # desired outputs for Nand gate - Don't change values!

s = [0, 0, 0, 0]  # sum: s = c0 + c1 + c2
n = [0, 0, 0, 0]  # if s > t then n=1 else n=0
e = [0, 0, 0, 0]  # error: e = z - n
d = [0, 0, 0, 0]  # Correction: d = r * e

t = 0.5           # threshold
r = 0.1           # delta

def calculate_values():
    # TO IMPLEMENT
    print("")

def print_matrix(arr):
    for i in arr:
        print(i)

def print_transpose(arr, name):
    counter = 0;
    for i in arr:
        print(name + str(counter) + ": " + str(i))
        counter += 1

def print_seperator():
    print("~~~~~~~~~~~~")

def print_values():
    """ this function print all the class values - DEBUG function """
    counter = 0
    print("----------------------------")
    print("x0 x1 x2:")
    print_matrix(x)
    print_seperator()
    print("w0 w1 w2:")
    print_matrix(w)
    print_seperator()
    print("c0 c1 c2:")
    print_matrix(c)

    print_seperator()

    print_transpose(z, "z")
    print_seperator()
    print_transpose(n, "n")
    print_seperator()
    print_transpose(s, "s")
    print_seperator()
    print_transpose(d, "d")
    print_seperator()
    print_transpose(e, "e")
    print_seperator()
    print("----------------------------")


def plot_graph():
    plt.plot([0, 0, 1, 1], [0, 1, 0, 1], 'ro')
    plt.plot([-0.5, 1.5], [-0.5, 1.5])
    plt.plot([-0.5, 1.5], [1.5, -0.5])
    plt.axis([-1, 2, -1, 2])
    plt.show()