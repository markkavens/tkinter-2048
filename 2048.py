import tkinter as tk
import random

arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
score = 0
def showText():
     y=70
     for row in arr:
          x=70
          for i in range(4):
               if row[i]==0:
                    canvas.create_rectangle(x-50,y-50,x+50,y+50,fill="white")
               else:
                    canvas.create_rectangle(x-50,y-50,x+50,y+50,fill="#60d66e")
                    canvas.create_text((x,y),font = ("arial", 30),text=row[i])
               x=x+120
               wind.update()
          y=y+120
     label.config(text="Score : "+str(score))
                         
def printarr():
     for row in arr:
          print(row)
     print(" ")

def shift(row):
     shiftedList = []
     for i in row:
          if i != 0:
               shiftedList.append(i)

     # doubling ...
     shiftedList = fusion(shiftedList)
     while len(shiftedList) != 4:
          shiftedList.append(0)
     #print(shiftedList)
     return shiftedList


def fusion(shiftedList):
     global score
     i=0
     while i<(len(shiftedList)-1):
          if shiftedList[i+1]==shiftedList[i]:
               if shiftedList[i]!=2048:
                    shiftedList[i] = 2*shiftedList[i]
                    score = score + shiftedList[i]
               j = i+1
               while j<len(shiftedList)-1:
                    shiftedList[j] = shiftedList[j+1]
                    j=j+1
               shiftedList.pop(j)
          i=i+1
     #print(shiftedList)
     return shiftedList

def findEmpty():
     emptyBox = []
     for i in range(4):
          for j in range(4):
               if arr[i][j] == 0:
                    emptyBox.append(i*10+j)
     
     return emptyBox

def gen2():
     emptyBox = findEmpty()
     if emptyBox != []:
          ind = random.choice(emptyBox)
          j = ind%10
          i = (ind//10)%10
          arr[i][j] = 2
                

def up(event):
     for i in range(4):
          row = [arr[0][i],arr[1][i],arr[2][i],arr[3][i]]
          row = shift(row)
          arr[0][i],arr[1][i],arr[2][i],arr[3][i]=row[0],row[1],row[2],row[3]
     gen2()
     showText()
    
def down(event):
     for i in range(4):
          row = [arr[3][i],arr[2][i],arr[1][i],arr[0][i]]
          row = shift(row)
          arr[3][i],arr[2][i],arr[1][i],arr[0][i]=row[0],row[1],row[2],row[3]
     gen2()
     showText()
     
def right(event):
     for i in range(4):
          arr[i].reverse()
          arr[i] = shift(arr[i])
          arr[i].reverse()
     gen2()
     showText()
  
     
def left(event):
     for i in range(4):
          arr[i] = shift(arr[i])
     gen2()
     showText()
  

def game():
     global score
     score = 0
     for i in range(4):
          arr[i] = [0,0,0,0]
     i = random.randint(0,3)
     j = random.randint(0,3)
     arr[i][j] = 2
     i = random.randint(0,3)
     j = random.randint(0,3)
     arr[i][j] = 2
     showText()

wind = tk.Tk()
wind.title("2048")
frame = tk.Frame(wind)
frame.pack()
label = tk.Label(wind,font = ("arial",20),text="Score : "+str(score))
label.pack()
bt = tk.Button(frame,text="Reset",font = ("arial",16),command= game)
bt.pack(side="left")

canvas = tk.Canvas(wind, width = 500, height = 500, bg = 'black')
canvas.pack()
canvas.create_rectangle(20,20,120,120,fill="white")
canvas.create_rectangle(140,20,240,120,fill="white")
canvas.create_rectangle(260,20,360,120,fill="white")
canvas.create_rectangle(380,20,480,120,fill="white")

canvas.create_rectangle(20,140,120,240,fill="white")
canvas.create_rectangle(140,140,240,240,fill="white")
canvas.create_rectangle(260,140,360,240,fill="white")
canvas.create_rectangle(380,140,480,240,fill="white")
     
canvas.create_rectangle(20,260,120,360,fill="white")
canvas.create_rectangle(140,260,240,360,fill="white")
canvas.create_rectangle(260,260,360,360,fill="white")
canvas.create_rectangle(380,260,480,360,fill="white")

canvas.create_rectangle(20,380,120,480,fill="white")
canvas.create_rectangle(140,380,240,480,fill="white")
canvas.create_rectangle(260,380,360,480,fill="white")
canvas.create_rectangle(380,380,480,480,fill="white")
game()

wind.bind('<Up>', up)
wind.bind('<Down>', down)
wind.bind('<Left>', left)
wind.bind('<Right>', right)
wind.mainloop()





