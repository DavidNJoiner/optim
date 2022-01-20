import tkinter as tk
from gui_classes import *

x = 5319
y = 3758

start = 400
end = 1200
step = 100

def main():
    root = tk.Tk()
    root.title('Autocad Helper')
    root.geometry('{}x{}'.format(800, 600))
    MainApp(root)
    root.mainloop()
     
main()

    

