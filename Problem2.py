from math import sqrt
print('Note: Add spaces after typing a single coordinate and press enter.')
x1,y1 = map(int,input('Please input the first 2 coordinates of the circle: ').split())
x2,y2 = map(int,input('Please input the second 2 coordinates of the circle: ').split())
x3,y3 = map(int,input('Please input the third 2 coordinates of the circle: ').split())
#Asks for user input of the 3 x and y points of the circle

x12 = x1 - x2                   #Code Block for all of the computation
x13 = x1 - x3                   #necessary for finding the center(h,k),
x31 = x3 - x1                   #radius r and the vectors DEF
x21 = x2 - x1
y12 = y1 - y2
y13 = y1 - y3
y31 = y3 - y1
y21 = y2 - y1   
px13 = pow(x1, 2) - pow(x3, 2)
py13 = pow(y1, 2) - pow(y3, 2)
px21 = pow(x2, 2) - pow(x1, 2)
py21 = pow(y2, 2) - pow(y1, 2)
F = ((px13*x12 + py13*x12 + px21*x13 + py21*x13) // (2 * (y31*x12 - y21*x13)))
G = ((px13*y12 + py13*y12 + px21*y13 + py21*y13) // (2 * (x31*y12 - x21*y13)))
C = (-pow(x1, 2) - pow(y1, 2) - 2 * G* x1 - 2 * F* y1);      
h = -G;
k = -F;
sqr = h**2 + k**2 - C;
r = round(sqrt(sqr), 5);
l=[2*G,2*F,C]

print("Center = (", h, ",", k, ")");        #Outputs the center,radius and vector DEF
print("Radius is equal to: ", r);
print("vector[D,E,F] is : ",l)