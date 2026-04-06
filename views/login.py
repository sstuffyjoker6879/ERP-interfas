import ttkbootstrap as ttk
class View_login:
    def __init__(self,contenedor,manager):
        self.contenedor=contenedor
        self.manager=manager
        self.view_login()
    def view_login(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()
        contenedor_login=ttk.Frame(self.contenedor,padding=20,relief="solid",borderwidth=2)
        contenedor_login.pack(expand=True)
        ttk.Label(contenedor_login,text="login",font=("Arial",20)).pack(pady=20)
        ttk.Entry(contenedor_login,width=30).pack(pady=10)
        ttk.Entry(contenedor_login,width=30).pack(pady=10)
        ttk.Button(contenedor_login,text="login",command=lambda:self.manager("dashboard")).pack(pady=10)
        return contenedor_login