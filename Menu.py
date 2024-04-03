from tkinter import *
import tkinter as tk
from Tooltip import *
from tkinter import messagebox



class Menu():
   def mostrarAyuda(self,event):
        messagebox.showinfo("ayuda","debe diligenciar todos los campos marcados con *\nluego presione el boton Registrarse")
   def crearVentanaM(self):
        self.ventana=tk.Toplevel()
        self.ventana.geometry("400x400")
        self.menu = tk.Menu(self.ventana)
        self.ventana.resizable(0,0)
        self.lblTitulo =tk.Label(self.ventana, text="Bienvenido usuario")
        self.lblTitulo.place(x=150, y=100)
        self.gestionarCliente = tk.Menu(self.menu,tearoff=0)
        self.gestionarCliente.add_command(label="crear cliente ",command=self.crearCliente )
        self.gestionarCliente.add_command(label="eliminar cliente", command=self.eliminarCliente)
        self.gestionarCliente.add_command(label="modificar cliente ", command=self.modificarCliente)
        self.gestionarCuenta = tk.Menu(self.menu,tearoff=0)
        self.gestionarTrans = tk.Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="gestionar Clientes", menu=self.gestionarCliente)
        self.menu.add_cascade(label="gestionar Cuenta", menu=self.gestionarCuenta)
        self.menu.add_cascade(label="gestionar Transaccion", menu=self.gestionarTrans)
        self.ventana.config(menu=self.menu)
   def crearCliente(self):
      self.ventana=tk.Tk()
      self.ventana.geometry("300x300")
      self.lblTitulo =tk.Label(self.ventana,text="Crear Cliente")
      self.lblTitulo.place(x=100, y=20)
      self.lblusuario1=tk.Label(self.ventana,text="Cédula* ")
      self.lblusuario1.place(x=25,y=40)
      self.txtusuario1=Entry(self.ventana)
      self.txtusuario1.place(x=25,y=60)
      self.lblNombre=tk.Label(self.ventana,text="Nombre*")
      self.lblNombre.place(x=25,y=80)
      self.txtNombre=Entry(self.ventana)
      self.txtNombre.place(x=25,y=100)
      self.lblApellido=tk.Label(self.ventana,text="apellido*")
      self.lblApellido.place(x=25,y=120)
      self.txtapellido=Entry(self.ventana)
      self.txtapellido.place(x=25,y=140)
      self.lbltelefono=tk.Label(self.ventana,text="Telefono*")
      self.lbltelefono.place(x=25,y=160)
      self.txtTelefono=Entry(self.ventana)
      self.txtTelefono.place(x=25,y=180)
      self.lblEmail=tk.Label(self.ventana,text="Email*")
      self.lblEmail.place(x=25,y=200)
      self.txtEmail=Entry(self.ventana)
      self.txtEmail.place(x=25,y=220)
      self.btnguardar=Button(self.ventana,text="guardar")
      self.btnguardar.place(x=90,y=250)
      self.btnlimpiar=Button(self.ventana,text="limpiar")
      self.btnlimpiar.place(x=25,y=250)
    
      #imagenAyuda = tk.PhotoImage(file=r"icons\help.png")
      #self.btnAyuda = Button(self.ventana, image=imagenAyuda)
      #self.btnAyuda.place(relx=1, rely=1, width=25)
      #Tooltip(self.btnAyuda,"presione para obtener ayuda!\nALT+a")
      #self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)
      #self.ventana.bind('<Alt-a>', self.mostrarAyuda)
      ##Este código es el botón de ayuda, con el cual presente problemas
      self.btnsalir=Button(self.ventana,text="salir")
      self.btnsalir.place(x=150,y=250)
     
   def eliminarCliente(self):
      self.ventana=tk.Tk()
      self.ventana.geometry("300x300")
      self.lblTitulo =tk.Label(self.ventana,text="Eliminar Cliente")
      self.lblTitulo.place(x=100, y=20)
      self.lblusuario1=tk.Label(self.ventana,text="Cédula* ")
      self.lblusuario1.place(x=25,y=40)
      self.txtusuario1=Entry(self.ventana)
      self.txtusuario1.place(x=25,y=60)
      self.lblNombre=tk.Label(self.ventana,text="Nombre*")
      self.lblNombre.place(x=25,y=80)
      self.txtNombre=Entry(self.ventana, state="disabled")
      self.txtNombre.place(x=25,y=100)
      self.lblApellido=tk.Label(self.ventana,text="apellido*")
      self.lblApellido.place(x=25,y=120)
      self.txtapellido=Entry(self.ventana, state="disabled")
      self.txtapellido.place(x=25,y=140)
      self.lbltelefono=tk.Label(self.ventana,text="Telefono*")
      self.lbltelefono.place(x=25,y=160)
      self.txtTelefono=Entry(self.ventana, state="disabled")
      self.txtTelefono.place(x=25,y=180)
      self.lblEmail=tk.Label(self.ventana,text="Email*")
      self.lblEmail.place(x=25,y=200)
      self.txtEmail=Entry(self.ventana, state="disabled")
      self.txtEmail.place(x=25,y=220)
      self.btneliminar=Button(self.ventana,text="eliminar")
      self.btneliminar.place(x=90,y=250)
      self.btnlimpiar=Button(self.ventana,text="limpiar")
      self.btnlimpiar.place(x=25,y=250)
      self.btnsalir=Button(self.ventana,text="salir")
      self.btnsalir.place(x=150,y=250)
      self.btnBuscar =Button(self.ventana, text="Buscar")
      self.btnBuscar.place(x=250, y=25)
      
      #imagenAyuda = tk.PhotoImage(file=r"icons\help.png")
      #self.btnAyuda = tk.Button(self.ventana, image=imagenAyuda)
      #self.btnAyuda.place(x=20, y=25, width=20, height=20)
      #Tooltip(self.btnAyuda,"presione para obtener ayuda!\nALT+a")
      #self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)

      #self.ventana.bind('<Alt-a>', self.mostrarAyuda)
      # ##Este código es el botón de ayuda, con el cual presente problemas
      
     
   def modificarCliente(self):
      self.ventana=tk.Tk()
      self.ventana.geometry("300x300")
      self.lblTitulo =tk.Label(self.ventana,text="Modificar Cliente")
      self.lblTitulo.place(x=100, y=20)
      self.lblusuario1=tk.Label(self.ventana,text="Cédula* ")
      self.lblusuario1.place(x=25,y=40)
      self.txtusuario1=Entry(self.ventana)
      self.txtusuario1.place(x=25,y=60)
      self.lblNombre=tk.Label(self.ventana,text="Nombre*")
      self.lblNombre.place(x=25,y=80)
      self.txtNombre=Entry(self.ventana)
      self.txtNombre.place(x=25,y=100)
      self.lblApellido=tk.Label(self.ventana,text="apellido*")
      self.lblApellido.place(x=25,y=120)
      self.txtapellido=Entry(self.ventana)
      self.txtapellido.place(x=25,y=140)
      self.lbltelefono=tk.Label(self.ventana,text="Telefono*")
      self.lbltelefono.place(x=25,y=160)
      self.txtTelefono=Entry(self.ventana)
      self.txtTelefono.place(x=25,y=180)
      self.lblEmail=tk.Label(self.ventana,text="Email*")
      self.lblEmail.place(x=25,y=200)
      self.txtEmail=Entry(self.ventana)
      self.txtEmail.place(x=25,y=220)
      self.btnguardar=Button(self.ventana,text="guardar")
      self.btnguardar.place(x=90,y=250)
      self.btnlimpiar=Button(self.ventana,text="limpiar")
      self.btnlimpiar.place(x=25,y=250)
      self.btnsalir=Button(self.ventana,text="salir")
      self.btnsalir.place(x=150,y=250)
      self.btnBuscar =Button(self.ventana, text="Buscar")
      self.btnBuscar.place(x=250, y=25)
      
      #imagenAyuda = tk.PhotoImage(file=r"icons\help.png")
      #self.btnAyuda = tk.Button(self.ventana, image=imagenAyuda)
      #self.btnAyuda.place(x=20, y=25, width=20, height=20)
      #Tooltip(self.btnAyuda,"presione para obtener ayuda!\nALT+a")
      #self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)
      #self.ventana.bind('<Alt-a>', self.mostrarAyuda)
      ##Este código es el botón de ayuda, con el cual presente problemas parece que hay problemas con la ruta del icono
      self.ventana.mainloop()