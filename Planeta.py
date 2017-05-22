from numpy import*
import math
import getopt,sys

G=6.67*10**(-11)
MS=1.99*10**30

opcao,valor = getopt.getopt(sys.argv[1:],'w:x:y:n: ')

for opcao,valor in opcao:
	if opcao == '-w':
		w = double (valor)
	if opcao == '-x':
		px = double (valor)
	if opcao == '-y':
		py = double (valor)
	if opcao == '-n':
		name = str(valor)

class Planeta:
	
	def __init__(self, nome, massa, x, y):
		self.nome=nome
		self.m=massa
		self.x=x
		self.y=y
	
	def distancia(self):
		d=math.sqrt((self.x**2)+(self.y**2))
		return d*1.5*10**11
	
	def force(self):
		return G*(MS*self.m/(self.distancia()**2))
	
	def period(self):
		return math.sqrt((self.distancia()/(1.5*10**11))**3)

p1=Planeta(name, w, px, py)
p2=Planeta('Jupiter', 1.9*10**27, 5.202, 0)

print "\nPlaneta: %s\nMassa: %fKg\nPosicao com centro Sol: (%f,%f)UA\nDistancia do Sol: %fUA\nForca Gravitacional: %fN\nPeriodo: %fAno(s)"%(name, w, px, py, p1.distancia()/(1.5*10**11), p1.force(), p1.period())
