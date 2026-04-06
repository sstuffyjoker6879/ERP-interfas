import ttkbootstrap as ttk
class View_dashboard:
    def __init__(self,contenedor,manager):
        self.contenedor=contenedor
        self.manager=manager
        self.view_dashboard()
    
    
    def view_dashboard(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()
        contenedor_dashboard=ttk.Frame(self.contenedor,padding=20,relief="solid",borderwidth=2)
        contenedor_dashboard.pack(expand=True)
        ttk.Label(contenedor_dashboard,text="dashboard",font=("Arial",20)).pack(pady=20)
        ttk.Button(contenedor_dashboard,text="Calculadora",command=lambda:self.manager("Calculadora")).pack(pady=10)
        ttk.Button(contenedor_dashboard,text="Back",command=lambda:self.manager("login")).pack(pady=10)
        return contenedor_dashboard