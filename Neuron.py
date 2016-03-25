"""
A Study Neuron Process Object
"""

gate_input = [[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
x = [0,0,0]
w = [0,0,0]
c = [0,0,0]
z = 0
s = 0
n = 0
d = 0
t = 0
r = 0.1


def print_values():
    """ this function print all the class values - DEBUG function """
    counter = 0
    print "----------------------------"
    print "Gate Inputs:"
    for i in gate_input:
        print i
    print "~~~~~~~~~~~~"

    print "x values:"
    for i in x:
        print "x" + str(counter) + ": " + str(i)
        counter += 1
    print "~~~~~~~~~~~~"

    counter = 0
    print "w values:"
    for i in w:
        print "w" + str(counter) + ": " + str(i)
        counter += 1
    print "~~~~~~~~~~~~"

    counter = 0
    print "c values:"
    for i in c:
        print "c" + str(counter) + ": " + str(i)
        counter += 1

    print "~~~~~~~~~~~~"
    print "z:" + str(z) + "; s:" + str(s) + "; t:" + str(t) + "; n:" + str(n) + "; r:" + str(r) + "; d:" + str(d)

    print "----------------------------"
