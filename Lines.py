import tkinter
import math
#N = int(input("number of charges:"))
RADIUS=2
#CHARGES=[]
#for i in range(3*N):
#	CHARGES.append(int(input("input coordinates, then quantity of each charge:")))
def Count_min_distance(charges, x, y):
	DISTANCES = []
	for i in range(len(charges)):
		DISTANCES.append(math.sqrt(((x-charges[i][0])**2) + (y-charges[i][1])**2))
		print (DISTANCES[i])
	return min(DISTANCES)

def Calc_one_force(x_c, y_c, q_x, q_y, q_s):
	return (q_s/((q_x-x_c)**2 + (q_y-y_c)**2))*(q_x-x_c), (q_s/((q_x-x_c)**2 + (q_y-y_c)**2))*(q_y-y_c)
def Calc_vectors(force1, force2):
	return force1[0]+force2[0], force1[1]+force2[1]
def Sum_forces(forces):
	for i in range(1,len(forces)):
		forces[i]=calc_vectors(forces[i-1],forces[i])
	return forces[len(forces)-1]
def Calc_point_force(x, y):
	pass#не окончено, эта функция считает напряженность поля в данной точке

def count_line(x, y):
	POINTS = []
	while x<=1000 and y<=1000 and Count_min_distance(CHARGES, x, y)>=RADIUS:
		POINTS.append([x, y])
		x = x + Sum_forces(x, y)
		pass#не окончено, эта функция возвращает массив точек на одной линии


def Round(n, r, x, y):
	POINTS = []
	for i in range(n):
		POINTS.append(math.cos(2*math.pi*i/n)*r + x)
		POINTS.append(math.sin(2*math.pi*i/n)*r + y)
	return POINTS
