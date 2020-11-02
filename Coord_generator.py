import random
coords_x=[]
coords_y=[]
New_Coords=[]
NumTurbs = int(input('How many turbines?'))
for i in range(NumTurbs):
    got = 0
    xcoord=random.randint(-3000,3000)
    ycoord=random.randint(-2000,2000)
    for j in range(0,len(coords_x)):
        if xcoord == coords_x[j] and ycoord == coords_y[j]:
            got = 1
    if got < 1:   
        coords_x.append(xcoord)
        coords_y.append(ycoord)
mid_Coords = [coords_x , coords_y]
coordsfile = open('start_coords.txt', 'w')
for element in range(NumTurbs):
     New_Coords.append(str(mid_Coords[0][element]) + '  ' + str(mid_Coords[1][element]) + '\n\n')
print (New_Coords)
for els in New_Coords:
    coordsfile.write(els)
coordsfile.close()
