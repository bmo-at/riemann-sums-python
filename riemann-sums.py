# Author: Jan-Robin Aumann
# 17.04.2019

import sys
import math as math
import numpy as numpy

f = lambda x : numpy.sin(x)*numpy.cos(x-(math.pi/5))

a = int(sys.argv[1])
b = int(sys.argv[2])
N = int(sys.argv[3])

roundTo = int(sys.argv[4])

dx = (b-a)/N

x = numpy.around(numpy.linspace(a, b, N + 1),roundTo)

minima = []
maxima = []

for i in range(N):

    res_min = dx * min(round(f(x[i]),roundTo), round(f(x[i+1]),roundTo))
    minima.append(res_min)
    print("$\\frac{b-a}{n}*m_n = ",
        "\\frac{",
        x[i],
        "-",
        x[i+1],
        "}{",
        N,
        "} * ",
        min(round(f(x[i]),roundTo), round(f(x[i+1]),roundTo)),
        " = ",
        round(res_min,roundTo),
        "$",
        sep='')

    res_max = dx * max(round(f(x[i]),roundTo), round(f(x[i+1]),roundTo))
    maxima.append(res_max)
    print("$\\frac{b-a}{n}*M_n = ",
        "\\frac{",
        x[i],
        "-",
        x[i+1],
        "}{",
        N,
        "} * ",
        max(round(f(x[i]),roundTo), round(f(x[i+1]),roundTo)),
        " = ",
        round(res_max,roundTo),
        "$",
        sep='', end= '\n\n')

print("$\\displaystyle\\sum^{n = 50}_{k=1}{\\frac{b-a}{n}*m_n}$",round(numpy.sum(minima),roundTo))
print("$\\displaystyle\\sum^{n = 50}_{k=1}{\\frac{b-a}{n}*M_n}$",round(numpy.sum(maxima),roundTo))

print("$\\displaystyle\\sum^{n = 50}_{k=1}{\\frac{b-a}{n}*mittel_n}$",round((numpy.sum(minima) + numpy.sum(maxima))/2,roundTo))
