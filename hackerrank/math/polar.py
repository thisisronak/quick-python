import cmath
import math

a = raw_input()
b = cmath.phase(complex(a))
r = abs(complex(a))

print ("{0}\n{1}".format(r,b))