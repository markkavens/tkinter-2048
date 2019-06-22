import tkinter as tk
from tkinter import messagebox
import random

arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
score = 0
rec = []
nums = []
def showText():
     y=70
     j=0
     for row in arr:
          x=70
          for i in range(4):
               if row[i]==0:
                    canvas.itemconfig(rec[j],fill="white")
                    canvas.itemconfig(nums[j],text="")
               else:
                    canvas.itemconfig(rec[j],fill=colorpicker(row[i]))
                    canvas.itemconfig(nums[j],text=row[i])
               x=x+120
               j=j+1
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
     else:
          gameover()
                

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

def colorpicker(val):
     if val == 2:
          return "#71f289"
     elif val==4:
          return "#5eed79"
     elif val==8:
          return "#3ee05d"
     elif val==16:
          return "#2bff35"
     elif val==32:
          return "#33e054"
     elif val==64:
          return "#2ee851"
     elif val==128:
          return "#3df762"
     elif val==256:
          return "#2ff957"
     elif val==512:
          return "#29f250"
     elif val==1024:
          return "#1eff4a"
     elif val==2048:
          return "#0cf967"  

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

def gameover():
     lost = True
     for i in range(4):
          for j in range(4):
               if i-1 > 0:
                    if arr[i-1][j]==arr[i][j]:
                         lost = False
               if i+1 < 4:
                    if arr[i+1][j]==arr[i][j]:
                         lost = False
               if j-1 > 0:
                    if arr[i][j-1]==arr[i][j]:
                         lost = False
               if j+1 < 4:
                    if arr[i][j+1]==arr[i][j]:
                         lost = False
     if lost == True :
          messagebox.showinfo("Game Over","Your Score : "+str(score))
               

def draw():
     y=70
     for i in range(4):
          x=70
          for j in range(4):
               rec.append(canvas.create_rectangle(x-50,y-50,x+50,y+50,fill="white"))
               nums.append(canvas.create_text((x,y),font = ("arial", 30),text=""))
               x=x+120
          y=y+120


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
draw()
game()

wind.bind('<Up>', up)
wind.bind('<Down>', down)
wind.bind('<Left>', left)
wind.bind('<Right>', right)
wind.mainloop()





