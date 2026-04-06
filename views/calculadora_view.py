import ttkbootstrap as ttk
from tkinter import StringVar
class View_calculadora:
    def __init__(self,contenedor,manager):
        self.contenedor=contenedor
        self.manager=manager
        self.operaciones=StringVar()
        self.operaciones.set("0")
    
        self.view_calculadora(self.operaciones.get())

    def view_calculadora(self, operaciones=""):
        for widget in self.contenedor.winfo_children():
            widget.destroy()
        #contenedores
        contenedor_header=ttk.Frame(self.contenedor,padding=20)
        contenedor_header.pack(expand=True)
        contenedor_display=ttk.Frame(self.contenedor,padding=20)
        contenedor_display.pack(expand=True)
        contenedor_button=ttk.Frame(self.contenedor,padding=20,relief="solid",borderwidth=2)
        contenedor_button.pack(expand=True)
        #widgets
        ttk.Label(contenedor_header,text="calculadora",font=("Arial",20)).pack(pady=20)
        ttk.Label(contenedor_display,text=operaciones,font=("Arial",12)).pack(fill="y",pady=20)
        ttk.Entry(contenedor_display,width=25,textvariable=self.operaciones,font=("Arial",12)).pack(fill="y",pady=10)
        #botones
        ttk.Button(contenedor_button,text="1",command=lambda:self.evento_boton("1")).grid(row=0,column=0,pady=10,padx=10)
        ttk.Button(contenedor_button,text="2",command=lambda:self.evento_boton("2")).grid(row=0,column=1,pady=10,padx=10)
        ttk.Button(contenedor_button,text="3",command=lambda:self.evento_boton("3")).grid(row=0,column=2,pady=10,padx=10)
        ttk.Button(contenedor_button,text="4",command=lambda:self.evento_boton("4")).grid(row=1,column=0,pady=10,padx=10)
        ttk.Button(contenedor_button,text="5",command=lambda:self.evento_boton("5")).grid(row=1,column=1,pady=10,padx=10)
        ttk.Button(contenedor_button,text="6",command=lambda:self.evento_boton("6")).grid(row=1,column=2,pady=10,padx=10)
        ttk.Button(contenedor_button,text="7",command=lambda:self.evento_boton("7")).grid(row=2,column=0,pady=10,padx=10)
        ttk.Button(contenedor_button,text="8",command=lambda:self.evento_boton("8")).grid(row=2,column=1,pady=10,padx=10)
        ttk.Button(contenedor_button,text="9",command=lambda:self.evento_boton("9")).grid(row=2,column=2,pady=10,padx=10)
        ttk.Button(contenedor_button,text="0",command=lambda:self.evento_boton("0")).grid(row=3,column=1,pady=10,padx=10)
        ttk.Button(contenedor_button,text=".",command=lambda:self.evento_boton(".")).grid(row=3,column=0,pady=10,padx=10)
        ttk.Button(contenedor_button,text="+",command=lambda:self.evento_boton("+")).grid(row=0,column=3,pady=10,padx=10)
        ttk.Button(contenedor_button,text="-",command=lambda:self.evento_boton("-")).grid(row=1,column=3,pady=10,padx=10)
        ttk.Button(contenedor_button,text="*",command=lambda:self.evento_boton("*")).grid(row=2,column=3,pady=10,padx=10)
        ttk.Button(contenedor_button,text="/",command=lambda:self.evento_boton("/")).grid(row=3,column=3,pady=10,padx=10)
        ttk.Button(contenedor_button,text="=",command=lambda:self.evento_boton("=")).grid(row=3,column=2,pady=10,padx=10)
        ttk.Button(contenedor_display,text="C",command=lambda:self.evento_boton("C")).pack(pady=10,side="left")
        

        ttk.Button(self.contenedor,text="Back",command=lambda:self.manager("dashboard")).pack(pady=10)
        return self.contenedor
    
    def evento_boton(self,boton):
        if boton=="=":
            self.view_calculadora(self.operaciones.get())
            self.operaciones.set(eval(self.operaciones.get()))
        elif boton=="C":
            self.operaciones.set("0")
        else:
            if self.operaciones.get()=="0":
                self.operaciones.set(boton)
            else:
                self.operaciones.set(self.operaciones.get()+boton)