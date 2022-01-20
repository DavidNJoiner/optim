import tkinter as tk
from gui_classes import *

x = 5319
y = 3758

start = 400
end = 1200
step = 100

def main():
    root = Tk()
    root.geometry("300x200+300+300")
    App = MainApp()
    root.mainloop()
     
if __name__ == '__main__':
    main()

    

