#Newton Gregory
#Written by Yusuf Hani Almoadhen

import pandas as pd
from sympy import *

t = [0,1,2,3,4,5,6]
I = [176,185,194,203,212,220,229]

diff1_col=[]
diff2_col=['']
diff3_col=['','']
diff4_col=['','']
diff5_col=['','','']
diff6_col=['','','']

h = t[1]-t[0]

for i in range(0,len(I)-1):
    diff1 = I[i+1]-I[i]
    diff1_col.append(diff1)

for i in range(0,len(diff1_col)-1):
    diff2 = diff1_col[i+1]-diff1_col[i]
    diff2_col.append(diff2)

for i in range(1,len(diff2_col)-1):
    diff3 = diff2_col[i+1]-diff2_col[i]
    diff3_col.append(diff3)

for i in range(2,len(diff3_col)-1):
    diff4 = diff3_col[i+1]-diff3_col[i]
    diff4_col.append(diff4)

for i in range(2,len(diff4_col)-1):
    diff5 = diff4_col[i+1]-diff4_col[i]
    diff5_col.append(diff5)

for i in range(3,len(diff5_col)-1):
    diff6 = diff5_col[i+1]-diff5_col[i]
    diff6_col.append(diff6)

diff1_col.append('')
diff2_col.append('')
diff3_col.append('')
diff4_col.extend(['',''])
diff5_col.extend(['',''])
diff6_col.extend(['','',''])

table = pd.DataFrame({
    't': t,
    'I': I,
    '1st': diff1_col,
    '2nd': diff2_col,
    '3rd': diff3_col,
    '4th': diff4_col,
    '5th': diff5_col,
    '6th': diff6_col
})

a0 = float("{:.3g}".format(I[0]))
a1 = float("{:.3g}".format(diff1_col[0]/h))
a2 = float("{:.3g}".format(diff2_col[1]/(2*h**2)))
a3 = float("{:.3g}".format(diff3_col[2]/(6*h**3)))
a4 = float("{:.3g}".format(diff4_col[2]/(24*h**4)))
a5 = float("{:.3g}".format(diff5_col[3]/(120*h**5)))
a6 = float("{:.3g}".format(diff6_col[3]/(720*h**6)))

print("h =",h,'\n')
print(table.to_markdown(index=False),'\n')
print("a0 =",a0)
print("a1 =",a1)
print("a2 =",a2)
print("a3 =",a3)
print("a4 =",a4)
print("a5 =",a5)
print("a6 =",a6,'\n')

x = Symbol('x')
Eq = a0 + a1*(x-t[0]) + a2*(x-t[0])*(x-t[1]) + a3*(x-t[0])*(x-t[1])*(x-t[2]) + a4*(x-t[0])*(x-t[1])*(x-t[2])*(x-t[3]) + a5*(x-t[0])*(x-t[1])*(x-t[2])*(x-t[3])*(x-t[4]) + a6*(x-t[0])*(x-t[1])*(x-t[2])*(x-t[3])*(x-t[4])*(x-t[5])
print("P(x) = ",simplify(Eq))

print("At x = 0.2")
print("y =","{:.5g}".format(float(Eq.subs({x:0.2}))))
