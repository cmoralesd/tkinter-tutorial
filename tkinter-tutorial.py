#!/usr/bin/env python
"""
Ejenplo básico del uso de Tkinter
Basado en: https://pythonbasics.org/tkinter/
Autor: cmoralesd (http://github.com/cmoralesd)
"""

from tkinter import *
import time

class Window(Frame):
    clock_on = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # se crea menú principal
        main_menu = Menu(self.master)
        self.master.config(menu=main_menu)

        # se crea un menú secundario
        menu_config = Menu(main_menu)
        menu_config.add_command(label='Opción 1')
        menu_config.add_command(label='Salir', command=self.exit_window)
        # se agrega al menú principal
        main_menu.add_cascade(label='Opciones', menu=menu_config)

        # creamos un contenedor para otros widgets
        self.pack(fill=BOTH, expand=1)

        # se agrega botón
        self.exitButton = Button(self, text='Cerrar', command=self.exit_window)
        self.exitButton.place(x=130, y=300)

        # se agrega botón
        self.clockButton = Button(self, text='Activar reloj', command=self.clock)
        self.clockButton.place(x=130, y=200)

        # se agregan etiquetas
        self.label1 = Label(master, text='hora actual:')
        self.label1.place(x=70, y=110)
        self.label2 = Label(master, text=self.get_time(), fg='Green', font=('Helvetica', 18))
        self.label2.place(x=70, y=150)
    
    # método salir
    def exit_window(self):
        exit()

    # método get_time
    def get_time(self):
        now = time.strftime('%H:%M:%S')
        return now
    
    # método update_clock
    def update_clock(self):
        self.label2.configure(text=self.get_time())
        if self.clock_on:
            self.after(1000, self.update_clock)
    
    # método clock
    def clock(self):
        if self.clock_on == False:
            self.clock_on = True
            self.clockButton.configure(text='Desactivar reloj')
            self.update_clock()
        else:
            self.clock_on = False
            self.clockButton.configure(text='Activar reloj')



# main code
# inicializa una ventana
root = Tk()
app = Window(root)

# agrega título
root.wm_title("ventana principal")
root.geometry('320x400-0-0')

# muestra la ventana
root.mainloop()