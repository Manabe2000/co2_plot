import math
import matplotlib.pyplot as plt

# mg = 100
# k = 20
# v_e = 400
# v_0 = 600

mg = 200
k = 20
v_e = 800
v_0 = 600
v_02 = 800

v_list = []
v_2list = []
t_list = []

fig,ax = plt.subplots()

for t in range(1,500):
    t = t / 1000
    v = (mg/k)*(1 - math.exp((-k)*t)) + v_e*(1 - math.exp((-k)*t)) + v_0*(math.exp((-k)*t))
    v_2 = (mg/k)*(1 - math.exp((-k)*t)) + v_e*(1 - math.exp((-k)*t)) + v_02*(math.exp((-k)*t))
    v_list.append(v)
    v_2list.append(v_2)
    t_list.append(t)

ax.plot(t_list,v_list)
ax.plot(t_list,v_2list)
 
plt.show()
