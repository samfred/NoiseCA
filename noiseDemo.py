from tkinter import *
from random import *
from functools import partial


#map stuff
################################################################
root = Tk()#master runtime guy
root.title('Noise Thing')

#map sizing stuff
w=800
h=500
cellsize=10
rows=int(h/cellsize)
cols=int(w/cellsize)

#boring gui stuff
canvas=Canvas(root, width=w, height=h, bg='white')
canvas.pack()


#noise function
################################################################
    
#noise parameters
minvalue=0
maxvalue=99
noise_density=50
iterations=0
tilemap=[]

#generate empty tilemap
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append(None)
    tilemap.append(col)

#assign each square a value
def noise(tilemap,noise_density):
    for i in range(rows):
        for j in range(cols):
            randvalue=randint(minvalue,maxvalue)
            if randvalue <= noise_density:
                value=minvalue
            else:
                value=maxvalue
            tilemap[i][j]=value


#cellular automata
################################################################
def cell_auto(tilemap,iterations):
    for its in range(iterations):
        newtilemap=[]
        for i in range(rows):
            col=[]
            for j in range(cols):
                value=maxvalue
                wallneighbors=0
                for n in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if is_in_map(m,n):
                            if n!=i or m!=j:
                                if tilemap[n][m]<=noise_density:
                                    wallneighbors+=1
                        else:
                            wallneighbors+=1
                if wallneighbors > 4:
                    value=minvalue
                col.append(value)
            newtilemap.append(col)

        for i in range(rows):
            for j in range(cols):
                tilemap[i][j]=newtilemap[i][j]


#draw the tilemap
####################################################################
def draw_tilemap(tilemap):

    #clear the canvas
    canvas.delete('all')
    
    #gridlines
    for i in range(0,w,cellsize):
        canvas.create_line(i,0,i,h,fill='gray')
    for i in range(0,h,cellsize):
        canvas.create_line(0,i,w,i,fill='gray')

    #tiles
    for i in range(rows):
        for j in range(cols):
            if tilemap[i][j] <= noise_density:
                x1=j*cellsize
                y1=i*cellsize
                x2=x1+cellsize
                y2=y1+cellsize
                canvas.create_rectangle(x1,y1,x2,y2,fill='black')

#button methods
########################################################################
def generate(tilemap,iterations,noise_density):
    noise(tilemap,noise_density)
    cell_auto(tilemap,iterations)
    draw_tilemap(tilemap)

def change_iterations(change):
    global iterations
    iterations+=change
    print(iterations)

def change_noise_density(change):
    global noise_density
    noise_density+=change
    print(noise_density)


#helper mathods
########################################################################

#return bool of whether or not (x,y) is a valid space
def is_in_map(x,y):
    return x>=0 and x<cols and y>=0 and y<rows


#do all the actions
########################################################################

noise(tilemap,noise_density)
cell_auto(tilemap,iterations)
draw_tilemap(tilemap)

#make the buttons
generate_button=Button(root, text='Generate', command=lambda: generate(tilemap,iterations,noise_density))
generate_button.pack()

increase_iterations_button=Button(root,text='Iterations++',command=lambda: change_iterations(1))
increase_iterations_button.pack()
decrease_iterations_button=Button(root,text='Iterations--',command=lambda: change_iterations(-1))
decrease_iterations_button.pack()

increase_noise_density_button=Button(root,text='Noise Density++',command=lambda: change_noise_density(1))
increase_noise_density_button.pack()
decrease_noise_density_button=Button(root,text='Noise Density--',command=lambda: change_noise_density(-1))
decrease_noise_density_button.pack()

#have the master do all the things
root.mainloop()

















