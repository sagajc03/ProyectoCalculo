from decimal import Decimal
from random import gauss
from sqlite3 import Row
from tkinter import *
import tkinter
from PIL import ImageTk,Image
import numpy as np 
import os

from gauss import gaussjordan
from segundoGrado import formula_Gen
from Metodonewton import newthon_r
from signosdescartes_copy import descartes
from coeficientesEnteros import CoeficioentesEnteros
from BinomioNewton import BinomioNewton
from derivada import derivada


current_path = os.path.dirname(r'C:\Users\sagaj\OneDrive\Documentos\purebasCodigo\ProyectoCalculo\guiLap.py') #LAP
# current_path = os.path.dirname(r'C:\Users\ThinkCentre M910s\OneDrive\Documentos\purebasCodigo\ProyectoCalculo\gui.py') #PC
img_path = os.path.join(current_path, 'img')


root = Tk()
root.title('Proyecto Cálculo')
root.iconphoto(True,PhotoImage(file=os.path.join(img_path,'unknown.png')))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN MENU
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def button_gauss():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()

    frameGauss.grid(row=0,column=1,padx=15,pady=15)
    l_gauss.grid(row=0,column=0)
    l_gauss_ins.grid(row=1,column=0)
    e_gauss.grid(row=2,column=0)
    b_gauss_aceptar.grid(row=3,column=0)

def button_for_gen():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()
    
    frameF_G.grid(row=0,column=1,padx=15,pady=15)
    l_f_g.grid(row=0,column=0)

    l_a_f_g.grid(row=1,column=0)
    l_b_f_g.grid(row=2,column=0)
    l_c_f_g.grid(row=3,column=0)

    e_a_f_g.grid(row=1,column=1)
    e_b_f_g.grid(row=2,column=1)
    e_c_f_g.grid(row=3,column=1)
    
    l_x1r_f_g.grid(row=0,column=2)
    l_x2r_f_g.grid(row=1,column=2)
    l_x1i_f_g.grid(row=2,column=2)
    l_x2i_f_g.grid(row=3,column=2)

    e_x1r_f_g.grid(row=0,column=3)
    e_x2r_f_g.grid(row=1,column=3)
    e_x1i_f_g.grid(row=2,column=3)
    e_x2i_f_g.grid(row=3,column=3)

    b_f_g_aceptar.grid(row=4,column=5)

def button_n_r():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()
    
    frameN_R.grid(row=0,column=1,padx=15,pady=15)
    l_n_r.grid(row=0,column=0)

    e_n_r_grado.grid(row=1,column=0)
    b_n_r_aceptar.grid(row=2,column=0)

def button_ley_signos():
    frameGauss.grid_remove()    
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()
    
    frameLey_Signos.grid(row=0,column=1,padx=15,pady=15)
    l_ley_signos.grid(row=0,column=0)
    e_ley_signos.grid(row=1,column=0)
    b_ley_signos_aceptar.grid(row=2,column=0)

def button_p_q():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()
    
    frameP_Q.grid(row=0,column=1,padx=15,pady=15)
    l_p_q.grid(row=0,column=0)

    l_p.grid(row=1,column=0)
    e_p.grid(row=1,column=1)
    l_q.grid(row=2,column=0)
    e_q.grid(row=2,column=1)
    b_p_q_aceptar.grid(row=3,column=1)
    t_p_q_res.grid(row=2,column=3)
def button_division_sintetica():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()
    
    frameDivision_Sintetica.grid(row=0,column=1,padx=15,pady=15)
    l_division_sintetica.grid(row=0,column=0)
    e_div_sin_n.grid(row=1,column=0)
    l_division_sintetica2.grid(row=2,column=0)
    e_div_sin_x.grid(row=3,column=0)

    b_div_sin_aceptar.grid(row=4,column=0)

def button_binomios():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()
    
    frameBinomios.grid(row=0,column=1,padx=15,pady=15)
    l_binomios.grid(row=0,column=0) 
    e_binomios_n.grid(row=1,column=0)
    b_binomios_aceptar.grid(row=2,column=0)
    e_binomios_r.grid(row=1,column=1)
def button_derivada():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()

    frameDerivada.grid(row=0,column=1,padx=15,pady=15)
    l_derivada.grid(row=0,column=0)
    e_derivada.grid(row=1,column=0)
    b_derivadas_aceptar.grid(row=2,column=0)

    
def button_autor():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameAutor.grid_remove()

    frameAutor.grid(row=0,column=1,padx=15,pady=15)
    l_img.pack()
    l_autor.pack(anchor="w")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME MENU
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

frameMenu = LabelFrame(root,text='Menú',padx=10,pady=10)
frameMenu.grid(row=0,column=0,padx=15,pady=15)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME MENU
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


b_gauss = Button(frameMenu, text="Gauss-Jordan", command=button_gauss,width=30)
b_for_gen = Button(frameMenu, text="Fórmula General", command=button_for_gen,width=30)
b_n_r = Button(frameMenu, text="Newton-Rapshon", command=button_n_r,width=30)
b_ley_signos = Button(frameMenu, text="Ley de Signos de descartes", command=button_ley_signos,width=30)
b_p_q = Button(frameMenu, text="Posibles raices", command=button_p_q,width=30)
b_division_sintetica = Button(frameMenu, text="División Sintetica", command=button_division_sintetica,width=30)
b_binomios = Button(frameMenu, text="Binomios de Newton", command=button_binomios,width=30)
b_derivada = Button(frameMenu, text="Derivada", command=button_derivada,width=30)
b_autor = Button(frameMenu, text="Autor", command=button_autor,width=30)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#HACER LAS COSAS APARECER EN FRAME MENU
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
b_gauss.grid(row=0,column=0)
b_for_gen.grid(row=1,column=0)
b_n_r.grid(row=2,column=0)
b_ley_signos.grid(row=3,column=0)
b_p_q.grid(row=4,column=0)
b_division_sintetica.grid(row=5,column=0)
b_binomios.grid(row=6,column=0)
b_derivada.grid(row=7,column=0)
b_autor.grid(row=8,column=0)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN GUASS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_gauss_siguiente():
    n = int(e_gauss.get())
    m = n + 1
    global gaussEntry
    gaussEntry = []
    aux = 1
    lin = 0
    for i in range(0,n*m):
        if i >= m*aux:
            lin = lin + 1
            aux = aux + 1
        gaussEntry.append(Entry(frameGauss,width=10))
        gaussEntry[i].grid(row=lin,column=i%m+1)

    l_gauss_ins = Label(frameGauss,text="Ingresa los datos de la matriz: ")
    l_gauss_ins.grid(row=1,column=0)
    b_gauss_aceptar2.grid(row=n+1,column=m)
    b_gauss_clear.grid(row=n+1,column=m+1)



def b_gauss_siguiente2():
    n = int(e_gauss.get())
    m = n + 1
    global gauss_a_m
    gauss_a_m = np.zeros((n,m))
    aux = 1
    lin = 0
    for i in range(0,n*m):
        if i >= m*aux:
            lin = lin + 1
            aux = aux + 1
        gauss_a_m[lin,i%m] = int(gaussEntry[i].get())
    print(gauss_a_m)
    gauss_a_m = gaussjordan.gauss(n,m,gauss_a_m)
    aux = 1
    lin = 0
    for i in range(0,n*m):
        if i >= m*aux:
            lin = lin + 1
            aux = aux + 1
        gaussEntry[i].delete(0, END)
        gaussEntry[i].insert(0,(gauss_a_m[lin,i%m]))


def b_gauss_limpiar():
    for i in range(0,len(gaussEntry)):
        gaussEntry[i].destroy()
    b_gauss_clear.grid_forget()
    b_gauss_aceptar2.grid_forget()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME GAUSS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameGauss = LabelFrame(root,text='Gauss',padx=10,pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME GAUSS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

l_gauss = Label(frameGauss,text="Realiza lo que se te pide abajo:")
l_gauss_ins = Label(frameGauss,text="Ingresa el tamaño de la matriz: ")
e_gauss = Entry(frameGauss,width=30)
b_gauss_aceptar = Button(frameGauss,text="Aceptar",command=b_gauss_siguiente)
b_gauss_aceptar2 = Button(frameGauss,text="Aceptar",command=b_gauss_siguiente2)
b_gauss_clear= Button(frameGauss,text="Reinicio",command=b_gauss_limpiar)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN FORMULA GENERAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_f_g():
    a = float(e_a_f_g.get())
    b = float(e_b_f_g.get())
    c = float(e_c_f_g.get())
    
    x1r,x2r,x1i,x2i = formula_Gen.segundogrado(a,b,c)
    
    e_x1r_f_g.delete(0, END)
    e_x1r_f_g.insert(0, str(x1r))

    e_x2r_f_g.delete(0, END)
    e_x2r_f_g.insert(0, str(x2r))

    e_x1i_f_g.delete(0, END)
    e_x1i_f_g.insert(0, str(x1i))

    e_x2i_f_g.delete(0, END)
    e_x2i_f_g.insert(0, str(x2i))

    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME FORMULA GENERAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameF_G = LabelFrame(root,text='Fórmula General',padx=10,pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME FORMULA GENERAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_f_g = Label(frameF_G,text="Escribe a, b, c:")

e_a_f_g = Entry(frameF_G,width=10)
e_b_f_g = Entry(frameF_G,width=10)
e_c_f_g = Entry(frameF_G,width=10)

l_a_f_g = Label(frameF_G,text="a")
l_b_f_g = Label(frameF_G,text="b")
l_c_f_g = Label(frameF_G,text="c")

b_f_g_aceptar = Button(frameF_G,text="Aceptar",command=b_aceptar_f_g)

e_x1r_f_g = Entry(frameF_G,width=10)
e_x2r_f_g = Entry(frameF_G,width=10)
e_x1i_f_g = Entry(frameF_G,width=10)
e_x2i_f_g = Entry(frameF_G,width=10)

l_x1r_f_g = Label(frameF_G,text="x1r")
l_x2r_f_g = Label(frameF_G,text="x2r")
l_x1i_f_g = Label(frameF_G,text="x1i")
l_x2i_f_g = Label(frameF_G,text="x2i")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES NEWTHON-RAPSHON
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_n_r():
    global x_n_r,lx_n_r
    x_n_r,lx_n_r = [],[]
    n = int(e_n_r_grado.get())
    for i in range(0,n+1):
        cad = "x" + str(i)
        lx_n_r.append(Label(frameN_R,text=cad))
        lx_n_r[i].grid(row=n-i,column=1)
        x_n_r.append(Entry(frameN_R,width=10))
        x_n_r[i].grid(row=n-i,column=2)
    b_n_r_aceptar2.grid(row=n+1,column=2)
    b_n_r_limpiar.grid(row=n+1,column=3)

def b_aceptar_n_r2():
    xx_n_r = []
    for i in range(0,len(x_n_r)):
        xx_n_r.append(Decimal(x_n_r[(len(x_n_r)-1)-i].get()))
    print(xx_n_r)
    global e_n_r
    e_n_r = []
    x = 1
    xe = Decimal(0.0)
    fx = Decimal(0.0)
    aux = 0
    x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = newthon_r.definir(xx_n_r,int(e_n_r_grado.get()))
    l_n_r_r.grid(row=0,column=4)
    for i in range(-100,100):
        auxstr = str(xe)
        xe,fx = newthon_r.nwtonrap(x+i*x,x12,x11,x10,x9,x8,x7,x6,x5,x4,x3,x2,x1,x0)
        xstr = str(xe)
        if(xstr[0:10] != auxstr[0:10]):            
            e_n_r.append(Entry(frameN_R,width=15))
            e_n_r[aux].grid(row=aux+1,column=4)
            e_n_r[aux].insert(0, xstr)
            aux = aux + 1
            
def b_limpiar_n_r():
    for i in range(0,len(e_n_r)):
        e_n_r[i].destroy()
    for i in range(0,len(x_n_r)):
        x_n_r[i].destroy()
        lx_n_r[i].destroy()
    b_n_r_limpiar.grid_forget()
    b_n_r_aceptar2.grid_forget()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME NEWTHON-RAPSHON
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameN_R = LabelFrame(root,text='Newthon-Rapshon',padx=10,pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME NEWTHON-RAPSHON
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

l_n_r = Label(frameN_R,text="Ingresa el grado de la operación")
l_n_r_r = Label(frameN_R,text="Raices")

e_n_r_grado = Entry(frameN_R,width=10)

b_n_r_aceptar = Button(frameN_R,text="Acpetar",command=b_aceptar_n_r)

b_n_r_aceptar2 = Button(frameN_R,text="Acpetar",command=b_aceptar_n_r2)
b_n_r_limpiar = Button(frameN_R,text="Reiniciar",command=b_limpiar_n_r)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN LEY DE SIGNOS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_ley_signos():
    global x_ley_signos,lx_ley_signos
    x_ley_signos,lx_ley_signos = [],[]
    n = int(e_ley_signos.get())
    for i in range(0,n+1):
        cad = "x" + str(i)
        lx_ley_signos.append(Label(frameLey_Signos,text=cad))
        lx_ley_signos[i].grid(row=n-i,column=1)
        x_ley_signos.append(Entry(frameLey_Signos,width=10))
        x_ley_signos[i].grid(row=n-i,column=2)
    b_ley_signos_aceptar2.grid(row=n+1,column=2)
    b_ley_signos_limpiar.grid(row=n+1,column=3)

def b_aceptar_ley_signos2():
    xx_ley_signos = []
    for i in range(0,len(x_ley_signos)):
        xx_ley_signos.append(float(x_ley_signos[(len(x_ley_signos)-1)-i].get()))
    print(xx_ley_signos)
    cad = descartes.signosdescartesfloat(xx_ley_signos,len(xx_ley_signos))
    e_ley_resultados.grid(row=2,column=3)
    e_ley_resultados.delete(0, END)
    e_ley_resultados.insert(0, cad)


def b_limpiar_ley_signos():
    for i in range(0,len(x_ley_signos)):
        x_ley_signos[i].destroy()
        lx_ley_signos[i].destroy()
    e_ley_resultados.grid_remove()
    b_ley_signos_aceptar2.grid_remove()
    b_ley_signos_limpiar.grid_remove()
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME LEY-SIGNOS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameLey_Signos = LabelFrame(root,text='Ley de signos de Descartes',padx=10,pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME LEY-SIGNOS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

l_ley_signos = Label(frameLey_Signos,text="Escribe el grado")
e_ley_signos = Entry(frameLey_Signos,width=10)
e_ley_resultados = Entry(frameLey_Signos,text="",width=80)

b_ley_signos_aceptar = Button(frameLey_Signos,text="Aceptar",command=b_aceptar_ley_signos)
b_ley_signos_aceptar2 = Button(frameLey_Signos,text="Aceptar",command=b_aceptar_ley_signos2)
b_ley_signos_limpiar = Button(frameLey_Signos,text="Limpiar",command=b_limpiar_ley_signos)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN POSIBLES RAICES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_p_q():
    f1 = CoeficioentesEnteros.factorizar(int(e_q.get()))
    f2 = CoeficioentesEnteros.factorizar(int(e_q.get()))
    a = CoeficioentesEnteros.raices(f1,f2)
    lista = []

    for n in a:
        lista.append(n)
    t_p_q_res.delete("1.0","end")
    t_p_q_res.insert(tkinter.END,lista)
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME POSIBLES RAICES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameP_Q = LabelFrame(root,text='Posibles Raices',padx=10,pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME POSIBLES RAICES
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

l_p_q = Label(frameP_Q,text="Escribe P y Q")

l_p = Label(frameP_Q,text="P")
e_p = Entry(frameP_Q,width=10)

l_q = Label(frameP_Q,text="Q")
e_q = Entry(frameP_Q,width=10)
b_p_q_aceptar = Button(frameP_Q,text="Aceptar",command=b_aceptar_p_q)

t_p_q_res = Text(frameP_Q,width=50,height=10)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN DIVISION SINTETICA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_acepar_div_sin():
    global a_div_sin,la_div_sin
    a_div_sin,la_div_sin = [],[]
    n = int(e_div_sin_n.get())
    for i in range(0,n+1):
        cad = "x" + str(i)
        la_div_sin.append(Label(frameDivision_Sintetica,text=cad))
        la_div_sin[i].grid(row=n-i,column=1)
        a_div_sin.append(Entry(frameDivision_Sintetica,width=10))
        a_div_sin[i].grid(row=n-i,column=2)
    b_div_sin_aceptar2.grid(row=n+1,column=2)
    b_div_sin_limpiar.grid(row=n+1,column=3)

def b_acepar_div_sin2():
    a = [] 
    for i in range(0,len(a_div_sin)):
        a.append(float(a_div_sin[(len(a_div_sin)-1)-i].get()))
    
    b = []
    x = float(e_div_sin_x.get())
    n = int(e_div_sin_n.get()) 
    if n >= 2:
        m = n + 1
        b.append(a[0])
        for i in range(1,m):
            b.append(a[i] + x*b[i-1])
    t_div_sin.grid(row=1,column=3)
    t_div_sin.delete("1.0","end")
    t_div_sin.insert(END,b)

def b_limpiar_div_sin():
    for i in range(0,len(a_div_sin)):
        a_div_sin[i].destroy()
        la_div_sin[i].destroy()
    b_div_sin_aceptar2.grid_forget()
    b_div_sin_limpiar.grid_forget()
    t_div_sin.grid_forget()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME DIVISION SINTETICA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameDivision_Sintetica = LabelFrame(root,text='División Sintetica',padx=10,pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME DIVISION SINTETICA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

l_division_sintetica = Label(frameDivision_Sintetica,text="Grado de la operación")
e_div_sin_n = Entry(frameDivision_Sintetica,width=10)
l_division_sintetica2 = Label(frameDivision_Sintetica,text="Número a evaluar")
e_div_sin_x = Entry(frameDivision_Sintetica,width=10)
b_div_sin_aceptar = Button(frameDivision_Sintetica,text="Aceptar",command=b_acepar_div_sin)
b_div_sin_aceptar2 = Button(frameDivision_Sintetica,text="Aceptar",command=b_acepar_div_sin2)
b_div_sin_limpiar = Button(frameDivision_Sintetica,text="Reiniciar",command=b_limpiar_div_sin)
t_div_sin = Text(frameDivision_Sintetica,width=15,height=3)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN BINOMIOS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_binomios():
    n = int(e_binomios_n.get())
    c = BinomioNewton.binomionew(n)
    e_binomios_r.delete(0,END)
    e_binomios_r.insert(0,str(c))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME BINOMIOS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameBinomios = LabelFrame(root,text='Binomios de Newthon',padx=10,pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME BINOMIOS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

l_binomios = Label(frameBinomios,text="Escribe el grado")
e_binomios_n = Entry(frameBinomios,width=10)
e_binomios_r = Entry(frameBinomios,width=50)
b_binomios_aceptar = Button(frameBinomios,text="Aceptar",command=b_aceptar_binomios)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE DERIVADA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_derivada():
    l_derivada_p.grid(row=0,column=1)
    l_derivada_a.grid(row=1,column=1)
    l_derivada_x.grid(row=2,column=1)
    e_derivada_x.grid(row=3,column=1)
    n = int(e_derivada.get())

    l_derivadas_l.grid(row=1,column=n+2)
    b_derivadas_aceptar2.grid(row=2,column=n)
    b_derivadas_limpiar.grid(row=2,column=n+1)
    
    global derivadaEntry
    derivadaEntry = []
    aux = 0
    lin = 0
    for i in range(0,n*2):
        if aux < n:
            aux = aux + 1
        else: 
            aux = 0
            lin = lin + 1
        derivadaEntry.append(Entry(frameDerivada,width=10))
        derivadaEntry[i].grid(row=lin,column=i%n+2)
    
def b_aceptar2_derivada():
    
    n = int(e_derivada.get())
    a = np.zeros((2,n))
    global derivadaOut
    derivadaOut = []
    for i in range(0,n):
        a[0,i] = int(derivadaEntry[i].get())
        a[1,i] = int(derivadaEntry[i+n].get())
    dfx = 0
    dfx = derivada.scardfxalt(a,n,float(e_derivada_x.get()))
    aux = 0
    lin = 0
    for i in range(0,n*2):
        if aux < n:
            aux = aux + 1
        else: 
            aux = 0
            lin = lin + 1
        derivadaOut.append(Entry(frameDerivada,width=10))
        derivadaOut[i].grid(row=lin,column=i%n+5)
    adfx = derivada.sacarmatdfx(a,n)
    for i in range(0,n):
        derivadaOut[i].delete(0, END)
        derivadaOut[i].insert(0,(adfx[0,i]))
        derivadaOut[i+n].delete(0, END)
        derivadaOut[i+n].insert(0,(adfx[1,i]))
    
    e_derivada_4.grid(row=5,column=5)
    e_derivada_4.delete(0,END)
    e_derivada_4.insert(0,dfx)


def b_limpiar_derivadas():
    for i in range(0,len(derivadaEntry)):
        derivadaEntry[i].destroy()
    for i in ran(0,len(derivadaOut)):
        derivadaOut[i].destroy()
    b_derivadas_aceptar2.grid_forget()
    b_derivadas_limpiar.grid_forget()
    l_derivada_p.grid_forget()
    l_derivada_a.grid_forget()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME DERIVADA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameDerivada = LabelFrame(root,text='Derivadas',padx=10,pady=10)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME DERIVADA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_derivada = Label(frameDerivada,text="Numero de polinomios")
e_derivada = Entry(frameDerivada,width=10)
b_derivadas_aceptar = Button(frameDerivada,text="Aceptar",command=b_aceptar_derivada)
l_derivada_x = Label(frameDerivada,text="Ingresa un punto en x")
e_derivada_x = Entry(frameDerivada,width=10)
l_derivada_4 = Label(frameDerivada,text="Aproximación en x seleccionada")
e_derivada_4 = Entry(frameDerivada,width=10)

l_derivada_p = Label(frameDerivada,text="Potencia")
l_derivada_a = Label(frameDerivada,text="Multplica a X")
b_derivadas_aceptar2 = Button(frameDerivada,text="Aceptar",command=b_aceptar2_derivada)
b_derivadas_limpiar = Button(frameDerivada,text="Reinicio",command=b_limpiar_derivadas)
l_derivadas_l = Label(frameDerivada,text="|")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN AUTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME AUTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameAutor = LabelFrame(root,text='Autor de la aplicación',padx=10,pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME AUTOR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cadena = """
sagajc03@gmail.com
Expediente: 307015
Mi nombre es Juan Carlos
Me gustan los zorros, jugar videojuegos,
los autos y la música.

Me gustan las comidas dulces más que las 
saladas.

Y otras tantas cosas más...
"""
#y dibujar
my_image = PhotoImage(file=os.path.join(img_path,'eifoto.png'))
my_imgsub = my_image.subsample(17)
l_img = Label(frameAutor,image=my_imgsub)
l_autor = Label(frameAutor,text=cadena)


root.mainloop()