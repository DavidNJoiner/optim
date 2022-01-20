import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
import ezdxf
import partitioning

class MainApp():

    def __init__(self, master):

        self.dxf_dat = None
        self.doc = ezdxf.new(dxfversion='R2010')
        self.msp = self.doc.modelspace()

        mainframe = ttk.Frame(master)

        toolbox = Toolbox(mainframe)
        toolbox2 = Toolbox(mainframe)

        toolbox.grid(column = 0, row = 0)
        toolbox2.grid(column = 1, row = 0)

    def exportDXF(self):
        
        self.doc.layers.new('AH_Layer', dxfattribs={'color': 2})
        self.msp.add_circle([0,9], radius=3)
        self.doc.saveas('template.dxf')

   
class Toolbox(tk.Frame):

    def __init__(self, parent):

        super(Toolbox, self).__init__()

        toolBoxframe = ttk.Frame(parent)
        
        #Create all the toolbox widgets
        self.wallA_lbl = ttk.Label(toolBoxframe, text='Wall A : ')
        self.wallB_lbl = ttk.Label(toolBoxframe, text='Wall B : ')
        self.wallA_entry = ttk.Entry(toolBoxframe, text='')
        self.wallB_entry = ttk.Entry(toolBoxframe, text='')
        self.processBtn = ttk.Button(toolBoxframe, text='PROCESS', command=self.onReturn)

        #Layout all the toolbox widgets
        self.wallA_lbl.grid(column = 0, row = 0)
        self.wallB_lbl.grid(column = 0, row = 1)
        self.wallA_entry.grid(column = 1, row = 0)
        self.wallB_entry.grid(column = 1, row = 1)
        self.processBtn.grid(column = 0, row = 2)

        self.wallA = 0
        self.wallB = 0

    def onReturn(self):  
        print('something was stored')

    def clrEntries(self):

        for entry in filter(lambda w : isinstance(w,entry), self.children.itervalues()):
            entry.delete(0, 'end')

        

    

    