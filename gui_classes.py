from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style, Label, Entry
import ezdxf
import partitioning

class MainApp(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.dxf_data = None
        self.doc = ezdxf.new(dxfversion='R2010')
        self.msp = self.doc.modelspace()

    def initUI(self):
        self.master.title('Autocad Helper')
        self.style = Style()
        self.style.theme_use("default")

        mainframe = Frame(self, relief=RAISED, borderwidth=1,)
        mainframe.pack(fill=BOTH, expand=True)

        toolbox = Toolbox(mainframe)
        toolbox.pack(fill="both", expand=True)

        self.pack(fill=BOTH, expand=True)

    def exportDXF(self):
        
        self.doc.layers.new('AH_Layer', dxfattribs={'color': 2})
        self.msp.add_circle([0,9], radius=3)
        self.doc.saveas('template.dxf')

   
class Toolbox(Frame):

    def __init__(self, parent):

        super(Toolbox, self).__init__()
        
        #Create all the toolbox widgets
        self.result_lbl = Label(self)
        self.wallA_lbl = Label(self, text='Wall A : ')
        self.wallB_lbl = Label(self, text='Wall B : ')
        self.minWidth_lbl = Label(self, text='Min : ')
        self.maxWidth_lbl = Label(self, text='Max : ')
        self.wallA_entry = Entry(self, text='')
        self.wallB_entry = Entry(self, text='')
        self.minWidth_entry = Entry(self, text='')
        self.maxWidth_entry = Entry(self, text='')
        self.processBtn = Button(self, text='PROCESS', command=self.onSearch)
        

        #Layout all the toolbox widgets
        self.result_lbl.grid(column=0, row=6)
        self.wallA_lbl.grid(column = 0, row = 0)
        self.wallB_lbl.grid(column = 0, row = 1)
        self.minWidth_lbl.grid(column = 0, row = 3)
        self.maxWidth_lbl.grid(column = 0, row = 4)
        self.wallA_entry.grid(column = 1, row = 0)
        self.wallB_entry.grid(column = 1, row = 1)
        self.minWidth_entry.grid(column = 1, row= 3)
        self.maxWidth_entry.grid(column = 1, row = 4)
        self.processBtn.grid(column = 0, row = 5)


    def onSearch(self): 
        try:
            widthInterval = [int(self.minWidth_entry.get()), int(self.maxWidth_entry.get())]
            partitioning.search(float(self.wallA_entry.get()), float(self.wallB_entry.get()), widthInterval, True)
        except:
            self.result_lbl.configure(text='Please fill all datas')

    def clrEntries(self):
        for entry in filter(lambda w : isinstance(w,entry), self.children.itervalues()):
            entry.delete(0, 'end')

    

        

    

    