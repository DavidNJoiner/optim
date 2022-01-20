import tkinter as tk
import ezdxf

class MainApp(tk.Frame):

    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.root = root
        
        toolbox = Toolbox(self.root)
        #toolbox.pack(side="left", fill="y")

        self.title = ('Autocad Helper')
        self.geometry = ('400x400')

        self.dxf_dat = None
        self.doc = ezdxf.new(dxfversion='R2010')
        self.msp = self.doc.modelspace()

    def exportDXF(self):
        
        self.doc.layers.new('AH_Layer', dxfattribs={'color': 2})
        self.msp.add_circle([0,9], radius=3)
        self.doc.saveas('template.dxf')

   
class Toolbox(tk.Toplevel):

    def __init__(self, parent):

        self.wallA = 0
        self.wallB = 0

    def onReturn(storageVal, entry):  
        storageVal = entry.get()
        print(storageVal+' was stored')

    def clrEntries(self):

        for entry in filter(lambda w : isinstance(w,entry), self.children.itervalues()):
            entry.delete(0, 'end')

        

    

    