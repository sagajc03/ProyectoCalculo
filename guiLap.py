from decimal import Decimal
from random import gauss
from sqlite3 import Row
from tkinter import *
import tkinter
from PIL import ImageTk,Image
import numpy as np 
import os
import matplotlib.pyplot as plt
from sympy import *
import re

from gauss import gaussjordan
from segundoGrado import formula_Gen
from Metodonewton import newthon_r
from signosdescartes_copy import descartes
from coeficientesEnteros import CoeficioentesEnteros
from BinomioNewton import BinomioNewton
from derivada import derivada
from integrales import integrales as inte
from minicuadra import minicuadra
from utilidades import utilidades as util


# current_path = os.path.dirname(r'C:\Users\sagaj\OneDrive\Documentos\purebasCodigo\ProyectoCalculo\guiLap.py') #PC
current_path = os.path.dirname(r'C:\Users\ThinkCentre M910s\OneDrive\Documentos\purebasCodigo\ProyectoCalculo\gui.py') #PC
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
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
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
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
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
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
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
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
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
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
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
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
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
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
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
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
    frameAutor.grid_remove()

    frameDerivada.grid(row=0,column=1,padx=15,pady=15)
    l_derivada.grid(row=0,column=0)
    e_derivada.grid(row=1,column=0)
    b_derivadas_aceptar.grid(row=2,column=0)

def button_integral():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
    frameAutor.grid_remove()

    frameIntegral.grid(row=0,column=1,padx=15,pady=15)
    l_integral_ins.grid(row=0,column=0)
    l_integral_tot.grid(row=1,column=0)
    b_integral_aniadir.grid(row=0,column=5)
    b_integral_aceptar.grid(row=0,column=6)

    l_integral_ecuacion.grid(row=0,column=1)
    l_integral_lim_inf.grid(row=0,column=2)
    l_integral_lim_sup.grid(row=0,column=3)
    l_integral_area.grid(row=0,column=4)
    l_integral_total.grid(row=0,column=7)


    e_integral_ecuacion.grid(row=1,column=1)
    e_integral_lim_inf.grid(row=1,column=2)    
    e_integral_lim_sup.grid(row=1,column=3)
    e_integral_area.grid(row=1,column=4)
    e_integral_area_total.grid(row=1,column=7)

    #---Simple---
    l_integral_simple.grid(row=15,column=0)
    e_integral_simple.grid(row=15,column=1)
    b_integral_simple.grid(row=15,column=2)
    e_integral_simple_res.grid(row=15,column=3)

    if len(inter_array_ex) == 0:
        inter_array_in.append(e_integral_ecuacion)
        inter_array_in.append(e_integral_lim_inf)
        inter_array_in.append(e_integral_lim_sup)
        inter_array_in.append(e_integral_area)
        inter_array_ex.append(inter_array_in)



    
def button_igualacion():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
    frameAutor.grid_remove()
    


    frameIgualar.grid(row=0,column=1,padx=15,pady=15)

    l_instruc_igualar.grid(row=0,column=5)

    l_igualacion_x0.grid(row=1,column=0)
    l_igualacion_x1.grid(row=1,column=1)
    l_igualacion_x2.grid(row=1,column=2)
    l_igualacion_x3.grid(row=1,column=3)
    l_igualacion_x4.grid(row=1,column=4)

    l_igualacion_espacio.grid(row=1,column=5)

    l_igualacionx0.grid(row=1,column=6)
    l_igualacionx1.grid(row=1,column=7)
    l_igualacionx2.grid(row=1,column=8)
    l_igualacionx3.grid(row=1,column=9)
    l_igualacionx4.grid(row=1,column=10)
    
    e_igualacion_x0.grid(row=2,column=0)
    e_igualacion_x1.grid(row=2,column=1)
    e_igualacion_x2.grid(row=2,column=2)
    e_igualacion_x3.grid(row=2,column=3)
    e_igualacion_x4.grid(row=2,column=4)

    e_igualacionx0.grid(row=2,column=6)
    e_igualacionx1.grid(row=2,column=7)
    e_igualacionx2.grid(row=2,column=8)
    e_igualacionx3.grid(row=2,column=9)
    e_igualacionx4.grid(row=2,column=10)

    l_igualacion_resultado.grid(row=3,column=5)
    l_igualacion_inst.grid(row=3,column=11)
    b_aceptar_igualacion.grid(row=1,column=11)

    e_igualacion_y0.grid(row=3,column=6)
    e_igualacion_y1.grid(row=3,column=7)
    e_igualacion_y2.grid(row=3,column=8)
    e_igualacion_y3.grid(row=3,column=9)
    e_igualacion_y4.grid(row=3,column=10)



def button_lineal():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
    frameAutor.grid_remove()
    
    frameLineal.grid(row=0,column=1,padx=15,pady=15)

    l_lineal_a.grid(row=0,column=0)
    e_lineal_n.grid(row=1,column=0)
    b_lineal_aceptar.grid(row=2,column=0)
    l_lineal_b.grid(row=5,column=0)
    

def button_polinomica():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
    frameAutor.grid_remove()
    
    framePolinomica.grid(row=0,column=1,padx=15,pady=15)

    l_polinomica_a.grid(row=0,column=0)
    e_polinomica_n.grid(row=1,column=0)
    b_polinomica_aceptar.grid(row=2,column=0)
    l_polinomica_b.grid(row=5,column=0)


def button_financiero():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
    frameAutor.grid_remove()

    frameFinan.grid(row=0,column=1,padx=15,pady=15)

    l_finan1.grid(row=0,column=0)
    e_finan1.grid(row=1,column=0)
    l_finan2.grid(row=2,column=0)
    e_finan2.grid(row=3,column=0)
    b_finan_c.grid(row=4,column=0)
    l_finan_e.grid(row=5,column=0)
    l_finan_m.grid(row=6,column=0)
    l_finan_p.grid(row=7,column=0)
    e_finan_e.grid(row=5,column=1)
    e_finan_m.grid(row=6,column=1)
    e_finan_p.grid(row=7,column=1)

def button_autor():
    frameGauss.grid_remove()
    frameF_G.grid_remove()
    frameN_R.grid_remove()
    frameLey_Signos.grid_remove()
    frameP_Q.grid_remove()
    frameDivision_Sintetica.grid_remove()
    frameBinomios.grid_remove()
    frameDerivada.grid_remove()
    frameIntegral.grid_remove()
    frameIgualar.grid_remove()
    frameLineal.grid_remove()
    framePolinomica.grid_remove()
    frameFinan.grid_remove()
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
b_integral = Button(frameMenu, text="Integral", command=button_integral,width=30)
b_ingualar = Button(frameMenu,text="Igualación",command=button_igualacion,width=30)
b_lineal = Button(frameMenu,text="Formula Lineal",command=button_lineal,width=30)
b_polinomica = Button(frameMenu,text="Formula Polinomica",command=button_polinomica,width=30)
b_finan = Button(frameMenu,text="Financiero",command=button_financiero,width=30)
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
b_integral.grid(row=8,column=0)
b_ingualar.grid(row=9,column=0)
b_lineal.grid(row=10,column=0)
b_polinomica.grid(row=11,column=0)
b_finan.grid(row=12,column=0)
b_autor.grid(row=13,column=0)
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
    dfx = derivada.scardfxalt(a,n,float(e_derivada_x.get()))
    e_derivada_4.grid(row=5,column=5)
    e_derivada_4.delete(0,END)
    e_derivada_4.insert(0,dfx)


def b_limpiar_derivadas():
    for i in range(0,len(derivadaEntry)):
        derivadaOut[i].destroy()
        derivadaEntry[i].destroy()
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
#FUNCIONES DE LOS BOTONES EN INTEGRAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_integrales():
    for i in range(len(inter_array_ex)):
        ecuacion = inter_array_ex[i][0].get()
        a = inter_array_ex[i][1].get()
        b = inter_array_ex[i][2].get()
        area = inte.integrales.integral(ecuacion,a,b)
        areas_inte.append(area)
        inter_array_ex[i][3].delete(0,END)
        inter_array_ex[i][3].insert(0,str(area))
        if i == 0:
            cuenta = area
            e_integral_area_total.delete(0,END)
            e_integral_area_total.insert(0,str(area))
        else:
            cuenta = cuenta - area
            e_integral_area_total.delete(0,END)
            e_integral_area_total.insert(0,str(cuenta))



def b_aniadir_integral():
    inter_array_in = []
    e_integral_ecuacion = Entry(frameIntegral,width=15)
    e_integral_lim_inf = Entry(frameIntegral,width=15)
    e_integral_lim_sup = Entry(frameIntegral,width=15)
    e_integral_area = Entry(frameIntegral,width=15)
    inter_array_in.append(e_integral_ecuacion)
    inter_array_in.append(e_integral_lim_inf)
    inter_array_in.append(e_integral_lim_sup)
    inter_array_in.append(e_integral_area)
    inter_array_ex.append(inter_array_in)
    tam = len(inter_array_ex)
    for i in range(0,4):
        inter_array_ex[tam-1][i].grid(row=tam,column=i+1)

def b_int_sim():
    e = e_integral_simple.get()
    res = inte.integrales.integral2(e)
    e_integral_simple_res.delete(0,END)
    e_integral_simple_res.insert(0,res)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME INTEGRAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameIntegral = LabelFrame(root,text="Integrales",padx=10,pady=10)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME INTEGRAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cadena_integrales = """
Instrucciones:
Escribir la ecuación de la recta, el limite inferior 
y el limite superior en los cuadros siguientes:
Usa el signo de multiplicacion '*'
"""

cadena_integrales2 = """
Total es el primero menos los siguientes
"""
l_integral_ins = Label(frameIntegral,text=cadena_integrales)
l_integral_tot = Label(frameIntegral,text=cadena_integrales2)
global inter_array_ex,inter_array_in, areas_inte
inter_array_ex, inter_array_in, areas_inte = [],[],[]
b_integral_aceptar = Button(frameIntegral,text="Aceptar",command=b_aceptar_integrales)
b_integral_aniadir = Button(frameIntegral,text="Añadir",command=b_aniadir_integral)

l_integral_simple = Label(frameIntegral,text="Integracion indefinida")
e_integral_simple = Entry(frameIntegral,width=20)
b_integral_simple = Button(frameIntegral,text="Aceptar | Resultado =>",command=b_int_sim)
e_integral_simple_res = Entry(frameIntegral,width=20)

l_integral_ecuacion = Label(frameIntegral,text="Ecuación")
l_integral_lim_inf = Label(frameIntegral,text="Limite inferior")
l_integral_lim_sup = Label(frameIntegral,text="Limite superior")
l_integral_area = Label(frameIntegral,text="Area")
l_integral_total = Label(frameIntegral,text="TOTAL")

e_integral_ecuacion = Entry(frameIntegral,width=15)
e_integral_lim_inf = Entry(frameIntegral,width=15)
e_integral_lim_sup = Entry(frameIntegral,width=15)
e_integral_area = Entry(frameIntegral,width=15)
e_integral_area_total = Entry(frameIntegral,width=15)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN IGUALACION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def button_igualacion_acep():
    if (e_igualacion_x0.get() != ''):
        x0 = float(e_igualacion_x0.get())
    else:
        x0 = 0

    if (e_igualacion_x1.get() != ''):
        x1 = float(e_igualacion_x1.get())
    else:
        x1 = 0
    
    if (e_igualacion_x2.get() != ''):
        x2 = float(e_igualacion_x2.get())
    else:
        x2 = 0

    if (e_igualacion_x3.get() != ''):
        x3 = float(e_igualacion_x3.get())
    else:
        x3 = 0

    if (e_igualacion_x4.get() != ''):
        x4 = float(e_igualacion_x4.get())
    else:
        x4 = 0
    
    if (e_igualacionx0.get() != ''):
        y0 = float(e_igualacionx0.get())
    else:
        y0 = 0
    if (e_igualacionx1.get() != ''):
        y1 = float(e_igualacionx1.get())
    else:
        y1 = 0
    if (e_igualacionx2.get() != ''):
        y2 = float(e_igualacionx2.get())
    else:
        y2 = 0
    if (e_igualacionx3.get() != ''):
        y3 = float(e_igualacionx3.get())
    else:
        y3 = 0
    if (e_igualacionx4.get() != ''):
        y4 = float(e_igualacionx4.get())
    else:
        y4 = 0

    z0 = x0 + (y0*-1)
    z1 = x1 + (y1*-1)
    z2 = x2 + (y2*-1)
    z3 = x3 + (y3*-1)
    z4 = x4 + (y4*-1)

    e_igualacion_y0.delete(0,END)
    e_igualacion_y0.insert(0,str(z0))
    e_igualacion_y1.delete(0,END)
    e_igualacion_y1.insert(0,str(z1))
    e_igualacion_y2.delete(0,END)
    e_igualacion_y2.insert(0,str(z2))
    e_igualacion_y3.delete(0,END)
    e_igualacion_y3.insert(0,str(z3))
    e_igualacion_y4.delete(0,END)
    e_igualacion_y4.insert(0,str(z4))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME IGUALACION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameIgualar = LabelFrame(root,text="Igualación",padx=10,pady=10)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME IGUALACION
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_instruc_igualar = Label(frameIgualar,text="Escribe la igualdad")

l_igualacion_x0 = Label(frameIgualar,text="x4")
l_igualacion_x1 = Label(frameIgualar,text="x3")
l_igualacion_x2 = Label(frameIgualar,text="x2")
l_igualacion_x3 = Label(frameIgualar,text="x1")
l_igualacion_x4 = Label(frameIgualar,text="x0")

l_igualacion_espacio = Label(frameIgualar,text="=",width=10)

l_igualacionx0 = Label(frameIgualar,text="x4")
l_igualacionx1 = Label(frameIgualar,text="x3")
l_igualacionx2 = Label(frameIgualar,text="x2")
l_igualacionx3 = Label(frameIgualar,text="x1")
l_igualacionx4 = Label(frameIgualar,text="x0")

b_aceptar_igualacion = Button(frameIgualar,text="Aceptar",command=button_igualacion_acep)

e_igualacion_x0 = Entry(frameIgualar,width=10)
e_igualacion_x1 = Entry(frameIgualar,width=10)
e_igualacion_x2 = Entry(frameIgualar,width=10)
e_igualacion_x3 = Entry(frameIgualar,width=10)
e_igualacion_x4 = Entry(frameIgualar,width=10)

e_igualacionx0 = Entry(frameIgualar,width=10)
e_igualacionx1 = Entry(frameIgualar,width=10)
e_igualacionx2 = Entry(frameIgualar,width=10)
e_igualacionx3 = Entry(frameIgualar,width=10)
e_igualacionx4 = Entry(frameIgualar,width=10)

l_igualacion_resultado = Label(frameIgualar,text="Resultado",pady=15)
l_igualacion_inst = Label(frameIgualar,text="Copiar a Newton-Rapson o conveniente")

e_igualacion_y0 = Entry(frameIgualar,width=10)
e_igualacion_y1 = Entry(frameIgualar,width=10)
e_igualacion_y2 = Entry(frameIgualar,width=10)
e_igualacion_y3 = Entry(frameIgualar,width=10)
e_igualacion_y4 = Entry(frameIgualar,width=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN LINEAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_lineal():
    n = int(e_lineal_n.get())
    l_lineal_x.grid(row=0,column=1)
    l_lineal_y.grid(row=0,column=2)
    l_lineal_res.grid(row=0,column=3)
    e_lineal_res.grid(row=1,column=3)
    l_lineal_b.grid(row=n+2,column=0)
    b_lineal_aceptar2.grid(row=n+2,column=2)
    global linealEntry
    linealEntry = []
    
    aux = 0
    lin = 0
    for i in range(0,n*2):
        if aux < n:
            aux += 1
        else:
            aux = 0
            lin += 1
        linealEntry.append(Entry(frameLineal,width=10))
        linealEntry[i].grid(row=i%n+1,column=lin+1)

    

def b_aceptar_lineal2():
    n = int(e_lineal_n.get())
    x = []
    y = []
    for i in range(0,n):
        x.append(float(linealEntry[i].get()))
        y.append(float(linealEntry[i+n].get()))
    a0, a1 = minicuadra.lineal(x,y)
    plt.plot(x,y)
    plt.show()
    resp = str(a1)[:8]  + "*x + " + str(a0)[:8] 
    e_lineal_res.delete(0,END)
    e_lineal_res.insert(0,resp)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME LINEAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameLineal = LabelFrame(root,text="Formula Lineal",padx=10,pady=10)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME LINEAL
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cadenaLin = """
Estima la formula de la recta
escribiendo los puntos que se
encuentran en el plano.
"""
l_lineal_a = Label(frameLineal,text="Escribe la cantidad de puntos")
e_lineal_n = Entry(frameLineal,width=10)
b_lineal_aceptar = Button(frameLineal,text="Aceptar",command=b_aceptar_lineal)

l_lineal_b = Label(frameLineal,text=cadenaLin)

#Siguiente columna

l_lineal_x = Label(frameLineal,text="X")
l_lineal_y = Label(frameLineal,text="Y")
b_lineal_aceptar2 = Button(frameLineal,text="Aceptar",command=b_aceptar_lineal2)

#sig
l_lineal_res = Label(frameLineal,text="Respuesta")
e_lineal_res = Entry(frameLineal,width=40)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN POLINOMICA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_aceptar_polinomica():
    n = int(e_polinomica_n.get())
    l_polinomica_x.grid(row=0,column=1)
    l_polinomica_y.grid(row=0,column=2)
    l_polinomica_res.grid(row=0,column=3)
    e_polinomica_res.grid(row=1,column=3)
    l_polinomica_b.grid(row=n+2,column=0)
    b_polinomica_aceptar2.grid(row=n+2,column=2)
    global polinomicaEntry
    polinomicaEntry = []
    
    aux = 0
    lin = 0
    for i in range(0,n*2):
        if aux < n:
            aux += 1
        else:
            aux = 0
            lin += 1
        polinomicaEntry.append(Entry(framePolinomica,width=10))
        polinomicaEntry[i].grid(row=i%n+1,column=lin+1)

def b_aceptar_polinomica2():
    n = int(e_polinomica_n.get())
    x = []
    y = []
    for i in range(0,n):
        x.append(float(polinomicaEntry[i].get()))
        y.append(float(polinomicaEntry[i+n].get()))
    a0, a1, a2 = minicuadra.polinomica(x,y)
    plt.plot(x,y)
    plt.show()
    resp = str(a2)[:8] + "*x^2 +" + str(a1)[:8] + "*x + " + str(a0)[:8]
    e_polinomica_res.delete(0,END)
    e_polinomica_res.insert(0,resp)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME POLINOMICA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
framePolinomica = LabelFrame(root,text="Formula Polinomica",padx=10,pady=10)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME POLINOMICA
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cadenaLin = """
Estima la formula de la recta
escribiendo los puntos que se
encuentran en el plano.
"""
l_polinomica_a = Label(framePolinomica,text="Escribe la cantidad de puntos")
e_polinomica_n = Entry(framePolinomica,width=10)
b_polinomica_aceptar = Button(framePolinomica,text="Aceptar",command=b_aceptar_polinomica)

l_polinomica_b = Label(framePolinomica,text=cadenaLin)

#Siguiente columna

l_polinomica_x = Label(framePolinomica,text="X")
l_polinomica_y = Label(framePolinomica,text="Y")
b_polinomica_aceptar2 = Button(framePolinomica,text="Aceptar",command=b_aceptar_polinomica2)

#sig
l_polinomica_res = Label(framePolinomica,text="Respuesta")
e_polinomica_res = Entry(framePolinomica,width=40)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE LOS BOTONES EN FINAN
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def b_c_finan():
    e1 = e_finan1.get()
    e2 = e_finan2.get()
    punto_eq = 0
    monto = 0
    punto_re = 0
    grados1 = []
    val1 = []
    max1 = 0
    grados2 = []
    val2 = []
    max2 = 0
    maxt = 0

    be1 = util.separarTerminos(e1)
    ae1 = []
    for i in range(0,len(be1)):
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*',be1[i])]
        ae1.append(s)
    for i in range(0,len(be1)):
        val1.append(float(ae1[i][0]))
        if len(ae1[i]) > 1:
            grados1.append(int(ae1[i][1]))
            if int(ae1[i][1]) > max1:
                max1 = int(ae1[i][1])
        else:
            grados1.append(0)


    be2 = util.separarTerminos(e2)
    ae2 = []
    for i in range(0,len(be2)):
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*',be2[i])]
        ae2.append(s)
    for i in range(0,len(be2)):
        val2.append(float(ae2[i][0]))
        if len(ae2[i]) > 1:
            grados2.append(int(ae2[i][1]))
            if int(ae2[i][1]) > max2:
                max2 = int(ae2[i][1])
        else:
            grados2.append(0)
    

    if max1 > max2:
        maxt = max1
    else:
        maxt = max2

    uax1 = 0
    uax2 = 0
    valt = []
    for i in range(maxt+1):
        if i in grados1:
            uax1 = grados1.index(i)
            valt.append(val1[uax1])
        else:
            valt.append(0)
        if i in grados2:
            uax2 = grados2.index(i)
            valt[i] = valt[i] - val2[uax2]

    
    x = 1
    xe = Decimal(0.0)
    fx = Decimal(0.0)
    maxnr = Decimal(0.0)
    x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = newthon_r.definir2(valt,maxt)
    for i in range(-100,100):
        xe,fx = newthon_r.nwtonrap(x+i*x,x12,x11,x10,x9,x8,x7,x6,x5,x4,x3,x2,x1,x0)
        if xe > maxnr:
            maxnr = xe
    punto_eq = maxnr
    e_finan_e.delete(0,END)
    e_finan_e.insert(0,punto_eq)
    

    p1 = inte.integrales.integral(e1,0,punto_eq)
    p2 = inte.integrales.integral(e2,0,punto_eq)
    monto = p1 - p2
    e_finan_m.delete(0,END)
    e_finan_m.insert(0,monto)
    eq = e1 + "-(" + e2 + ")"

    eq2 = inte.integrales.integral2(eq)
    e_finan_p.delete(0,END)
    e_finan_p.insert(0,eq2)
    
    
    
    
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREACION FRAME FINAN
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frameFinan = LabelFrame(root,text="Punto de equilibrio, Monto de retorno, Punto de retorno")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COSAS DEL FRAME FINAN
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_finan1 = Label(frameFinan,text="Ingresa la primera ecuación")
e_finan1 = Entry(frameFinan,width=10)
l_finan2 = Label(frameFinan,text="Ingresa la segunda ecuación")
e_finan2 = Entry(frameFinan,width=10)
b_finan_c = Button(frameFinan,text="Calcular",command=b_c_finan)

l_finan_e =Label(frameFinan,text="Punto de equilibrio:")
l_finan_m =Label(frameFinan,text="Monto de retorno:")
l_finan_p =Label(frameFinan,text="Llevar a newton-Rapson para sarber el Punto de retorno:")
e_finan_e =Entry(frameFinan,width=15)
e_finan_m =Entry(frameFinan,width=15)
e_finan_p =Entry(frameFinan,width=15)
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