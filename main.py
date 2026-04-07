import ttkbootstrap as ttk
from views.login import View_login
from views.dashboard import View_dashboard
from views.calculadora_view import View_calculadora
from 

VISTAS={
    "login":View_login,
    "dashboard":View_dashboard,
    "Calculadora":View_calculadora,
    "adivinar_numero":View_adivinar_numero

}
class Main: 
    def __init__(self):
        self.app=ttk.Window(themename="superhero")
        self.app.title("capibara")
        self.app.geometry("800x600")
        self.contenedor=ttk.Frame(self.app)
        self.contenedor.pack(expand=True)
        self.manager("login")
        self.app.mainloop()
    def manager(self,vista):
        manager_view(vista,self.contenedor,self.manager)
        
    
def manager_view(clave,contenedor,manager):
    if clave not in VISTAS:
        raise ValueError("Vista no encontrada")
    vista=VISTAS[clave]
    vista(contenedor,manager)
    

if __name__=="__main__":
    Main()