import tkinter
import math
N = int(input("number of charges:"))
RADIUS=2
CHARGES=[]
CONST = 0.05
for i in range(N):
	CHARGES.append([int(input("input x-coordinate:")), int(input("input y-coordinate:")), int(input("input quantity (quantity must be an integer):"))])
def Count_min_distance(charges, x, y):
	DISTANCES = []
	for i in range(len(charges)):
		DISTANCES.append(math.sqrt(((x-charges[i][0])**2) + (y-charges[i][1])**2))
		print (DISTANCES[i])
	return min(DISTANCES)

def Calc_one_force(x_c, y_c, q_x, q_y, q_s):
	return [(q_s/((q_x-x_c)**2 + (q_y-y_c)**2))*(q_x-x_c), (q_s/((q_x-x_c)**2 + (q_y-y_c)**2))*(q_y-y_c)]
def Calc_vectors(force1, force2):
	return force1[0]+force2[0], force1[1]+force2[1]
def Sum_forces(forces):
	for i in range(1,len(forces)):
		forces[i]=Calc_vectors(forces[i-1],forces[i])
	return forces[len(forces)-1]
def Calc_point_force(x, y):
	FORCES = []
	for charge in CHARGES:
		FORCES.append(Calc_one_force(x, y, charge[0], charge[1], charge[2]))
	return Sum_forces(FORCES)

def Count_line(x, y):
	POINTS = []
	while x<=1000 and y<=1000 and Count_min_distance(CHARGES, x, y)>=RADIUS:
		POINTS.append([x, y])
		x = x + Calc_point_force(x, y)[0]*CONST
		y = y + Calc_point_force(x, y)[1]*CONST
	return POINTS	
def Round(n, r, x, y):
	POINTS = []
	for i in range(n):
		POINTS.append([math.cos(2*math.pi*i/n)*r + x), math.sin(2*math.pi*i/n)*r + y)]
	return POINTS
c = tkinter.Canvas(width=1000, height = 1000)
c.pack()
BEGINNING_POINTS=[]
for charge in CHARGES:
	BEGINNING_POINTS.append(Round(10, RADIUS, charge[0], charge[1]))
for massive in BEGINNING_POINTS:
	for i in range(len(massive)):
		Count_line(massive[i])
c.mainloop()
