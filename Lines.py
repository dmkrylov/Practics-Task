import tkinter
import math
N = int(input("number of charges:"))
CHARGES=[]
for i in range(3*N):
	CHARGES.append(int(input("input coordinates, then quantity of each charge:")))
def calc_vectors(dx1, dy1, dx2, dy2):
	return dx1+dx2, dy1+dy2
def calc_one_force(x_c, y_c, q_x, q_y, q_s):
	return (q_s/((q_x-x_c)**2 + (q_y-y_c)**2))*(q_x-x_c), (q_s/((q_x-x_c)**2 + (q_y-y_c)**2))*(q_y-y_c)
def calc_many_forces(forces):
	for i in range(1,len(forces)):
		forces[i]=calc_vectors(forces[i-1],forces[i])
	return forces[len(forces)-1]


def Round(n, r, x, y):
	POINTS = []
	for i in range(n):
		POINTS.append(math.cos(2*math.pi*i/n)*r + x)
		POINTS.append(math.sin(2*math.pi*i/n)*r + y)
	return POINTS
