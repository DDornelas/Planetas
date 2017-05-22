import matplotlib.pyplot as plt

periodo={"Mercurio": 0.241, "Venus": 0.615, "Terra": 1, "Marte": 1.88, "Jupiter": 11.86, "Saturno": 29.5, "Urano": 84, "Plutao": 248}

raio={"Mercurio": 0.387, "Venus": 0.723, "Terra": 1, "Marte": 1.523, "Jupiter": 5.202, "Saturno": 9.539, "Urano": 19.18, "Plutao": 39.44}

p=[]
r=[]

for i in periodo:
	p.append(periodo.get(i)**2)

for i in raio:
	r.append(raio.get(i)**3)

plt.figure(figsize=(6,5), dpi=96)
#plt.axis([-0.5,60,-1,30])

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Raio ao Cubo ($(UA)^{3}$)')
plt.ylabel(r'Per\'{i}odo ao Quadrado ($Ano^{2}$)')

plt.title(r'Verifica\c{c}\~{a}o Experimental Lei de Kepler', fontsize=12)
plt.grid()
plt.yscale('log')
plt.xscale('log')
plt.plot(r,p,'r-', linewidth=1)
#plt.legend(loc='upper right') 
plt.savefig("LK.pdf", dpi=96)
plt.show()
