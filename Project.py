import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from sklearn.linear_model import LinearRegression
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

import csv

entries = [[5,5],
           [15,20], 
    [25,14],
    [35,32], 
    [45,22],
    [55,38]]

points=[[5,5],
           [15,20], 
    [25,14],
    [35,32], 
    [45,22],
    [55,38]]


Datapionts=[]

file=False
    
class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self, "Linear Regresssion")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.refresh()
        self.container.bind()
        self.show_frame(Homepage)
        
        
        
    def show_frame(self,cont):
        frame =self.frames[cont]
        frame.tkraise()
        

    def refresh(self):
        self.frames.clear()
        for Fra in (Homepage,addpionts,Graph,Graphpionts):
            frame = Fra(self.container,self)
            self.frames[Fra] = frame
            frame.grid(row=0,column=0,sticky="nsew")
    def refreshpage(self,page):
        self.refresh()
        self.show_frame(page)
        
    def refreshgraph(self):
        self.refresh()
        self.show_frame(Graph)
        
    
        
class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Home page")
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Manula pionts", 
                            command= lambda: controller.show_frame(addpionts))
        
        button2 = ttk.Button(self, text="Graph from a file", 
                            command= lambda: controller.show_frame(Graphpionts))
        button1.pack()
        button2.pack()

class Graphpionts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        canvas = tk.Canvas(self,width=500, height=700)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas,width=200,height=200)
        
        ttk.Label(scrollable_frame, text="Pionts from Graph",).grid(row=0,column=2)
        
        ttk.Label(scrollable_frame, text = "New piont:").grid(row=1,column=0)
        x = tk.IntVar()
        y = tk.IntVar()
        
        ttk.Label(scrollable_frame, text = "X:").grid(row=2,column=0)
        e=tk.Entry(scrollable_frame,textvariable=x).grid(row=2,column=1)
        
        ttk.Label(scrollable_frame, text = "Y:").grid(row=3,column=0)
        e=tk.Entry(scrollable_frame,textvariable=y).grid(row=3,column=1)
        
        Add= ttk.Button(scrollable_frame, text="ADD Piont",command=lambda:self.Addpoi(x,y))
        Graph = ttk.Button(scrollable_frame, text="Graph pionts", command= lambda: self.graph())
        Add.grid(row=3,column=3)
        Graph.grid(row=3,column=4)
        
        ttk.Label(scrollable_frame, text = " ").grid(row=4,column=1)
        ttk.Label(scrollable_frame, text = "Pionts already in the array:").grid(row=7,column=1)
        self.controller = controller
        lab = ttk.Label(scrollable_frame, text="X").grid(row=8,column=0)
        lab = ttk.Label(scrollable_frame, text="Y").grid(row=8,column=1)
        lab = ttk.Label(scrollable_frame, text="Remove piont").grid(row=8,column=3)
        

        
        scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
        )
        
        canvas.create_window((0, 13), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        labelsX = []
        labelsY = []
        buttons = []
        for i in range(len(Datapionts)):
            labelsX.append(ttk.Label(scrollable_frame, width=15, text=Datapionts[i][0], anchor='w'))
            labelsY.append(ttk.Label(scrollable_frame, width=15, text=Datapionts[i][1], anchor='w'))
            buttons.append(ttk.Button(scrollable_frame, text="-",
                                      command=lambda IO=i: self.remove(IO)))
            
            labelsX[i].grid(row=i+13,column=0)
            labelsY[i].grid(row=i+13,column=1)
            buttons[i].grid(row=i+13,column=3)
        
        
        canvas.grid(row=0,column=19,sticky="nsew")
        scrollable_frame.grid_rowconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollbar.grid(row=0,column=20,sticky="nsew")
        
    def Addpoi(self,n1,n2):
        x = (n1.get())  
        y = (n2.get())  
        Datapionts.append([x,y])
        self.controller.refreshpage(Graphpionts)
    
    
    def remove(self,y):
        del Datapionts[y]
        self.controller.refreshpage(Graphpionts)
    
    def graph(self):
        entries.clear()
        for i in Datapionts:
            points.append(i)
        self.controller.refreshgraph()
    
        
        

class addpionts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        file=False
        canvas = tk.Canvas(self,width=500, height=700)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas,width=200,height=200)
        
        ttk.Label(scrollable_frame, text="Pionts",).grid(row=0,column=2)
        
        ttk.Label(scrollable_frame, text = "New piont:").grid(row=1,column=0)
        x = tk.IntVar()
        y = tk.IntVar()
        
        ttk.Label(scrollable_frame, text = "X:").grid(row=2,column=0)
        e=tk.Entry(scrollable_frame,textvariable=x).grid(row=2,column=1)
        
        ttk.Label(scrollable_frame, text = "Y:").grid(row=3,column=0)
        e=tk.Entry(scrollable_frame,textvariable=y).grid(row=3,column=1)
        
        Add= ttk.Button(scrollable_frame, text="ADD Piont",command=lambda:self.Addpoi(x,y))
        Graph = ttk.Button(scrollable_frame, text="Graph pionts", command= lambda: self.graph())
        Add.grid(row=3,column=3)
        Graph.grid(row=3,column=4)
        
        ttk.Label(scrollable_frame, text = " ").grid(row=4,column=1)
        ttk.Label(scrollable_frame, text = "Pionts already in the array:").grid(row=7,column=1)
        self.controller = controller
        lab = ttk.Label(scrollable_frame, text="X").grid(row=8,column=0)
        lab = ttk.Label(scrollable_frame, text="Y").grid(row=8,column=1)
        lab = ttk.Label(scrollable_frame, text="Remove piont").grid(row=8,column=3)
        

        
        scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
        )
        
        canvas.create_window((0, 13), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        labelsX = []
        labelsY = []
        buttons = []
        for i in range(len(entries)):
            labelsX.append(ttk.Label(scrollable_frame, width=15, text=entries[i][0], anchor='w'))
            labelsY.append(ttk.Label(scrollable_frame, width=15, text=entries[i][1], anchor='w'))
            buttons.append(ttk.Button(scrollable_frame, text="-",
                                      command=lambda IO=i: self.remove(IO)))
            
            labelsX[i].grid(row=i+13,column=0)
            labelsY[i].grid(row=i+13,column=1)
            buttons[i].grid(row=i+13,column=3)
        
        
        canvas.grid(row=0,column=19,sticky="nsew")
        scrollable_frame.grid_rowconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollbar.grid(row=0,column=20,sticky="nsew")
        
    def Addpoi(self,n1,n2):
        x = (n1.get())  
        y = (n2.get())  
        entries.append([x,y])
        self.controller.refreshpage(addpionts)
    
    
    def remove(self,y):
        del entries[y]
        self.controller.refreshpage(addpionts)
        
    def graph(self):
        entries.clear()
        for i in entries:
            points.append(i)
        self.controller.refreshgraph()
        
    
    

        



class Graph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Graph")
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Home", 
                            command= lambda: controller.show_frame(Homepage))
        button1.pack()
        x=[]
        y=[]
        for i in points:
            x.append(i[0])
            y.append(i[1])
        print()
        xo,yo = regresssion(x,y)
        f = Figure(figsize=(5,5),dpi=100)
        a = f.add_subplot(111)
        a.plot(x,y,"ob") 
        a.plot(xo,yo)
    
        canvas = FigureCanvasTkAgg( f ,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
        
        
    
def ConfigPionts():
    x = np.array(5, 15, 25, 35, 45, 55)
    y = np.array(5, 20, 14, 32, 22, 38)
    xo,yo= regresssion(x, y)
    f = Figure(figsize=(5,5),dpi=100)
    a = f.add_subplot(111)
    a.plot(x,y,"ob") 
    a.plot(xo,yo)
    plt.show()
        
def regresssion(x,y):
    n= np.size(x)
    meanx= np.mean(x)
    meany= np.mean(y)
    SS_xy=0
    SS_xx=0
    for i in range(np.size(x)):
            SS_xy+= (x[i]-meanx)*(y[i]-meany)
            SS_xx+= (x[i]-meanx)**2
        
    slope= SS_xy/SS_xx
    Y_intercept = meany-(slope*meanx)
    xo = np.arange(0,max(x)+1) 
    yo = (slope*xo)+Y_intercept
    return xo,yo


      

def main():  
    with open('Datapionts.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            count= 0
            for row in csv_reader:
                if count == 0:
                    count+= 1
                else:
                    Datapionts.append([int(row[0]),int(row[1])])
    root = Window()
    #draw_button = tk.Button(root,text="Graph", command=drawplots)
    #draw_button.pack()
    root.mainloop()

    
    
    
main()