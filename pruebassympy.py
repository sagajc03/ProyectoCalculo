import re
import utilidades as util


string = "3*x+125"
b = util.utilidades.separarTerminos(string)
print(b)
# for i in range(0,len(b)):
#     s = [float(s) for s in re.findall(r'-?\d+\.?\d*',b[i])]
#     print(s)
ae1 = []
for i in range(0,len(b)):
    s = [float(s) for s in re.findall(r'-?\d+\.?\d*',b[i])]
    ae1.append(s)
print (ae1)
print(len(ae1[0]))