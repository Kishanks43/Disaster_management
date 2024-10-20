                                                    

import tkinter as tk
from tkinter import *
from PIL import ImageTk , Image
import csv
import random
from tkinter import messagebox
import string
import os
import time
p=''
inc=''
place=''
p_i_c=''
ph1=''
ph2=''
def tr():
    s9.withdraw()
    s13.deiconify()
    he=s13.winfo_screenheight()
    wi=s13.winfo_screenwidth()
    s13.geometry("%dx%d"%(wi,he))
    s13['bg']='light green'

    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\report.png")
    lab=Label(s13, image=im)
    lab.place(x=0,y=0)
    
    l1=Label(s13,text=" Training Session Report ",font=("Eras Medium ITC",60),bg="#c6bfac", fg="Black")
    l1.place(x=50,y=20)
    a=50
    b=150
    Label(s13,text='Admin no.',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a,y=b)
    a=a+200
    Label(s13,text='Name',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a,y=b)
    a=a+200
    Label(s13,text='Phone Number',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a,y=b)
    a=a+200
    Label(s13,text='Email ID',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a+50,y=b)
    a=a+300
    Label(s13,text='Package',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a,y=b)
    a=a+200
    
    f=open("training.csv",'r')
    cr=csv.reader(f)
    
    for i in cr:
        
        adm_no=i[0]
        name=i[1]
        ph_no=i[2]
        eid=i[3]
        pack=i[4]
        
        a=50
        b=b+100
        Label(s13,text=adm_no,font=("Monotype corsiva",25),bg="#886c43", fg="Black").place(x=a,y=b)
        a=a+200
        Label(s13,text=name,font=("Monotype corsiva",25),bg="#886c43", fg="Black").place(x=a,y=b)
        a=a+200
        Label(s13,text=ph_no,font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a,y=b)
        a=a+200
        Label(s13,text=eid,font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a+30,y=b)
        a=a+300
        Label(s13,text=pack,font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a,y=b)
        
        
    f.close()
    b1=Button(s13,text="BACK TO PREVIOUS MENU",font=('Times New Roman',25),fg='#886c43',bg='White',command=psc_odr,relief='solid',borderwidth=2)
    b1.place(x=800,y=b+100)

    s13.attributes('-fullscreen', True)

    s13.mainloop()

def psc_gi():
    s12.withdraw()
    s9.deiconify()
def gi():
    s9.withdraw()
    s12.deiconify()
    he=s12.winfo_screenheight()
    wi=s12.winfo_screenwidth()
    s12.geometry("%dx%d"%(wi,he))

    im1=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\pic15.png")
    lab1=Label(s12, image=im1)
    lab1.place(x=0,y=0)
    #im2=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\report.png")
    #lab2=Label(s12, image=im2)
    #lab2.place(x=0,y=0)

    b1=Button(s12,text="BACK TO PREVIOUS MENU",font=('Times New Roman',25),fg='#886c43',bg='White',command=psc_gi,relief='solid',borderwidth=2)
    b1.place(x=970,y=700)
    s12.attributes('-fullscreen', True)
    
    s12.mainloop()
    
def psc_odr():
    s10.withdraw()
    s9.deiconify()
def odr():
    s9.withdraw()
    s10.deiconify()
    he=s10.winfo_screenheight()
    wi=s10.winfo_screenwidth()
    s10.geometry("%dx%d"%(wi,he))
    s10['bg']='light green'

    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\report.png")
    lab=Label(s10, image=im)
    lab.place(x=0,y=0)

    
    l1=Label(s10,text=" On Duty Report ",font=("Eras Medium ITC",60),bg="#c6bfac", fg="Black")
    l1.place(x=50,y=20)
    a=50
    b=150
    Label(s10,text='Admin no.',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a,y=b)
    a=a+170
    Label(s10,text='Name',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a,y=b)
    a=a+170
    Label(s10,text='Incident',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a,y=b)
    a=a+170
    Label(s10,text='Place',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a+50,y=b)
    a=a+370
    Label(s10,text='Person-in-charge',font=("Monotype corsiva",25),bg="#c6bfac", fg="Black").place(x=a,y=b)
    a=a+200
    Label(s10,text='''Primary
contact number''',font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a,y=b)
    a=a+200
    Label(s10,text='''Secondary
contact number''',font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a,y=b)
    a=a+200
    f=open("onduty.csv",'r')
    cr=csv.reader(f)
    
    for i in cr:
        
        adm_no=i[0]
        name=i[1]
        inc=i[2]
        place=i[3]
        p_i_c=i[4]
        ph1=i[5]
        ph2=i[6]
        a=50
        b=b+100
        Label(s10,text=adm_no,font=("Monotype corsiva",25),bg="#886c43", fg="Black").place(x=a,y=b)
        a=a+150
        Label(s10,text=name,font=("Monotype corsiva",25),bg="#886c43", fg="Black").place(x=a,y=b)
        a=a+150
        Label(s10,text=inc,font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a,y=b)
        a=a+200
        Label(s10,text=place,font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a+30,y=b)
        a=a+400
        Label(s10,text=p_i_c,font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a,y=b)
        a=a+200
        Label(s10,text=ph1,font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a,y=b)
        a=a+200
        Label(s10,text=ph2,font=("Monotype corsiva",25),bg="#e9e5da", fg="Black").place(x=a,y=b)
        
    f.close()
    b1=Button(s10,text="BACK TO PREVIOUS MENU",font=('Times New Roman',25),fg='#886c43',bg='White',command=psc_odr,relief='solid',borderwidth=2)
    b1.place(x=800,y=b+100)

    s10.attributes('-fullscreen', True)
    
    s10.mainloop()
def p5_mm():
    s9.withdraw()
    w.deiconify()
    
    

def p5():
    w.withdraw()
    s9.deiconify()
    he=s9.winfo_screenheight()
    wi=s9.winfo_screenwidth()
    s9.geometry("%dx%d"%(wi,he))
    s9['bg']='light green'

    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\pic7.png")
    lab=Label(s9, image=im)
    lab.place(x=0,y=0)

    l1=Label(s9,text="Report",font=("Eras Medium ITC",60),bg="White", fg="Black",relief='solid',borderwidth=2)
    l1.place(x=50,y=20)
    a=500
    b=150
    b1=Button(s9, text="General Instructions", command=gi,font=("Times New Roman",25),bg="White",fg="Black",width=20)
    b1.place(x=a,y=b)
    b=b+100
    #b2=Button(s9, text="Incident Report", command=ir,font=("Times New Roman",25),bg="White",fg="Black",width=20)
    #b2.place(x=a,y=b)
    b=b+100
    b3=Button(s9, text="Training Session Report", command=tr,font=("Times New Roman",25),bg="White",fg="Black",width=20)
    b3.place(x=a,y=b)
    b=b+100
    b4=Button(s9, text="On Duty report ", command=odr,font=("Times New Roman",25),bg="White",fg="Black",width=20)
    b4.place(x=a,y=b)
    b=b+100
    b5=Button(s9, text="Back to main menu ", command=p5_mm,font=("Times New Roman",25),bg="White",fg="Black",width=20)
    b5.place(x=a,y=b)
    b=b+100

    s9.attributes('-fullscreen', True)

    s9.mainloop()
def od_withdraw():
    s11.withdraw()
    w.deiconify()


def od_commit():
    global p,inc,ph1,ph2,p_i_c,place
    ph1=ri.get()
    c=otx1.get()
    f=open('onduty.csv','a',newline='')
    cw=csv.writer(f)
    f1=open("incident.csv",'r')
    cr=csv.reader(f1)
    for i in cr:
        if i[12]==ph1:
            inc=i[3]
            ph2=i[13]
            p_i_c=i[11]
            place="%s,%s,%s"%(i[0],i[1],i[2])
    
    cw.writerow([c,p,inc,place,p_i_c,ph1,ph2])
    f.close()
    messagebox.showinfo("on duty",'registered')
    s11.deiconify()
    s8.withdraw()
    he=s11.winfo_screenheight()
    wi=s11.winfo_screenwidth()
    s11.geometry("%dx%d"%(wi,he))
    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\REPORT12.png")
    
    pic=Button(s11,width=1600,height=900,command=od_withdraw,image=im).place(x=0,y=0)
    #while True:
    #   Canvas.move(pic,1600,900)
    s11.attributes('-fullscreen', True)
    
    s11.mainloop()
def p4_mm():
    s8.withdraw()
    w.deiconify()
          
def check_vo():
    global p,inc,ph1,ph2,p_i_c,place
    f1=open('volunteer.csv','r')
    f2=open('incident.csv','r')

    

    
    cr1=csv.reader(f1)
    cr2=csv.reader(f2)
    c=otx1.get()
    a=300
    b=150
    t1=Entry(s8,font=('Monotype Corsiva',20),textvariable=otx1,state='disabled')
    t1.place(x=a,y=b)
    a=50
    b=250
    h1=Label(s8,text='Incident',font=("Monotype Corsiva",25),bg="#0aa8ab",fg="Black")
    h1.place(x=a,y=b)
    a=a+200
    h2=Label(s8,text='Place of Incident',font=("Monotype Corsiva",25),bg="#0aa8ab",fg="Black")
    h2.place(x=a+30,y=b)
    a=a+350
    h3=Label(s8,text='Person-in-charge',font=("Monotype Corsiva",25),bg="#0aa8ab",fg="Black")
    h3.place(x=a+150,y=b)
    a=a+450
    h4=Label(s8,text='''Primary contact
number''',font=("Monotype Corsiva",25),bg="#0aa8ab",fg="Black")
    h4.place(x=a-3,y=b)
    a=a+250
    '''h5=Label(s8,text=''Secondary contact
number'',font=("Monotype Corsiva",25),bg="#0aa8ab",fg="Black")
    h5.place(x=a,y=b)'''
    b=b+25
    for i in cr1:
        p=i[1]
        
        if i[0]==c:
            for j in cr2:
                inc=j[3]
                ph1=j[12]
                ph2=j[13]
                #nv=j[4]
                p_i_c=j[11]
                place="%s,%s,%s"%(j[0],j[1],j[2])
                otx2.set(inc)
                otx3.set(place)
                otx4.set(p_i_c)
                otx5.set(ph1)
                otx6.set(ph2)
                a=30
                b=b+50
                
                
                la=Label(s8,text=inc,font=("Monotype corsiva",25),bg="#0aa8ab", fg="White")
                la.place(x=a,y=b)
                a=a+230
                l1 = Label(s8,text = place,font=("Monotype corsiva",25),bg='#0aa8ab',fg='White')
                l1.place(x=a+20,y=b)
                a=a+500
                l2 = Label(s8,text = p_i_c,font=("Monotype corsiva",25),bg='#0aa8ab',fg='White')
                l2.place(x=a,y=b)
                a=a+300
                l3 = Label(s8,text = ph1,font=("Monotype corsiva",25),bg='#0aa8ab',fg='White')
                l3.place(x=a,y=b)
                a=a+250
                '''l4 = Label(s8,text = ph2,font=("Monotype corsiva",25),bg='#0aa8ab',fg='White')
                l4.place(x=a,y=b)'''
            break
                

    f1.close()
    f2.close()
    
    a=50
    b=b+75
    la1=Label(s8, text="Enter Primary Phone Number ",font=("Monotype corsiva",25),bg='#0aa8ab',fg='Black')
    la1.place(x=a, y=b)
    a=a+400
    te1=Entry(s8,font=("Monotype corsiva",25),textvariable=ri)
    te1.place(x=a,y=b)
    a=a+400
    b1=Button(s8,command=od_commit,text='Register',font=('Monotype Corsiva',25),bg="#ab0d0a",fg='White')
    b1.place(x=a,y=b)
    def clear():
        te1.delete(0,END)
    b2=Button(s8,command=clear,text='CLEAR',font=('Monotype Corsiva',25),bg='#ab0d0a',fg='White')
    b2.place(x=a+300,y=b)
    b3=Button(s8,command=p4_mm,text='BACK TO THE MAIN MENU ',font=('Monotype Corsiva',25),bg='#ab0d0a',fg='White')
    b3.place(x=a+50,y=b+80)
                
                    

#On Duty/Ready to goo
def p4():
    w.withdraw()
    s8.deiconify()
    he=s8.winfo_screenheight()
    wi=s8.winfo_screenwidth()
    s8.geometry("%dx%d"%(wi,he))
    s8['bg']='light green'
    f1=open('volunteer.csv','r')
    f2=open('incident.csv','r')
    im1=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\image21.png")
    lab1=Label(s8, image=im1)
    lab1.place(x=0,y=0)

    im2=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\images.png")
    lab2=Label(s8, image=im2)
    lab2.place(x=1240,y=0)
    
    cr1=csv.reader(f1)
    cr2=csv.reader(f2)
    
    l1=Label(s8,text="Ready To Goo !!",font=("Eras Medium ITC",60),bg="#0aa8ab", fg="Black",relief='solid',borderwidth=2)
    l1.place(x=50,y=20)
    a=50
    b=150
    l2=Label(s8,text="Enter your admin no. :",font=('Monotype Corsiva',20),bg='#0aa8ab',fg='Black',relief='solid',borderwidth=2)
    l2.place(x=a,y=b)
    a=a+250
    t1=Entry(s8,font=('Monotype Corsiva',20),textvariable=otx1)
    t1.place(x=a,y=b)
    a=a+250
    b1=Button(s8,text='Check',bg='#ab0d0a',fg="White",command=check_vo,font=('Times New Roman ',20),relief='solid',borderwidth=2)
    b1.place(x=a,y=b-10)

    s8.attributes('-fullscreen', True)
    
    s8.mainloop()
   
def done():
    global y 
    f = open("training.csv","a",newline="")
    cw = csv.writer(f)
    a1 = t1.get()
    a2 = t2.get()
    a3 = t3.get()
    a4 = t4.get()
    a5 = rp.get()
    cw.writerow([a1,a2,a3,a4,a5])
    messagebox.showinfo("Training Session","Done")
    f.close()
    


def p3_mm():
    s7.withdraw()
    w.deiconify()
    

    
def check_adm():
    global y
    f = open("volunteer.csv","r")
    cr = csv.reader(f)
    x = admch.get()
    flag = 1
    for i in cr:
        a1 = i[0]
        a2 = i[1]
        a3 = i[7]
        a4 = i[9]
        
        if i[0] == x:
            flag=-1
            Label(s7,text="Admin No",font=("Monotype corsiva",18),bg="#97acef", fg="Black",relief='solid',borderwidth=2).place(x=50,y=300)
            Label(s7,text="Name",font=("Monotype corsiva",20),bg="#97acef", fg="Black",relief='solid',borderwidth=2).place(x=50,y=350)
            Label(s7,text="Phone Number ",font=("Monotype corsiva",20),bg="#97acef", fg="Black",relief='solid',borderwidth=2).place(x=50,y=400)
            Label(s7,text="Email ID ",font=("Monotype corsiva",20),bg="#97acef", fg="Black",relief='solid',borderwidth=2).place(x=50,y=450)
            t1.set(a1)
            t2.set(a2)
            t3.set(a3)
            t4.set(a4)
            te1 = Entry(s7,width = 20,textvariable = t1,state="disabled",font=("Monotype corsiva",18)).place(x=250,y=300)
            te2 = Entry(s7,width = 20,textvariable = t2,state="disabled",font=("Monotype corsiva",18)).place(x=250,y=350)
            te3 = Entry(s7,width = 20,textvariable = t3,state="disabled",font=("Monotype corsiva",18)).place(x=250,y=400)
            te4 = Entry(s7,width = 20,textvariable = t4,state="disabled",font=("Monotype corsiva",18)).place(x=250,y=450)
            Label(s7,text='''Flood
Management''',font=("Monotype corsiva",22),bg="#97acef", fg="Black",relief='solid',borderwidth=2).place(x=600,y=300)
            Label(s7,text="Landslide",font=("Monotype corsiva",22),bg="#97acef", fg="Black",relief='solid',borderwidth=2).place(x=850,y=300)
            Label(s7,text="""Fire
Based""",font=("Monotype corsiva",22),bg="#97acef", fg="Black",relief='solid',borderwidth=2).place(x=1080,y=300)
            Radiobutton(s7,text="Package 1",variable = rp,value="Flood Management",bg='#97acef',fg="Black",font=("Monotype corsiva",18),relief='solid',borderwidth=2).place(x=600,y=400)
            Radiobutton(s7,text="Package 2",variable = rp,value="Landslide",bg='#97acef',fg="Black",font=("Monotype corsiva",18),relief='solid',borderwidth=2).place(x=850,y=400)
            Radiobutton(s7,text="Package 3",variable = rp,value="Fire Based",bg='#97acef',fg="Black",font=("Monotype corsiva",18),relief='solid',borderwidth=2).place(x=1075,y=400)

            a = 50
            b = 520
            Label(s7,text="Note: ",font=("Monotype corsiva",18),bg="White", fg="Black").place(x=a,y=b)
            b = b+25
            Label(s7,text="1. On week ends                                  ",font=("Monotype corsiva",18),bg="White", fg="Black").place(x=a,y=b)
            b = b+25
            Label(s7,text="2. Minimum Amount for Refreshment - Rs.300/day   ",font=("Monotype corsiva",18),bg="White", fg="Black").place(x=a,y=b)
            b = b+25
            Label(s7,text="3. Select only one package at a time             ",font=("Monotype corsiva",18),bg="White", fg="Black").place(x=a,y=b)
            b = b+33
            Label(s7,text="4. No. of classes vary based on your performance ",font=("Monotype corsiva",18),bg="White", fg="Black").place(x=a,y=b)

            Button(s7,text="Done",font=("Times New Roman",20),command = done,width=10,height=1).place(x=850,y=580)
            Button(s7,text="Back To Menu",font=("Times New Roman",20),command = p3_mm,width=10,height=1).place(x=850,y=680)
            y = a1
    if flag==1:
         messagebox.showerror("Training Session","Admin No not registered")
         s7.withdraw()
         w.deiconify()

    f.close()  

    
def p3():
    w.withdraw()
    s7.deiconify()
    he=s7.winfo_screenheight()
    wi=s7.winfo_screenwidth()
    s7.geometry("%dx%d"%(wi,he))
    s7['bg']='light green'

    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\pic5.png")
    lab=Label(s7, image=im)
    lab.place(x=-100,y=0)
    
    l1=Label(s7,text="Training Session",font=("Eras Medium ITC",60),bg="#ffffff", fg="Black",relief='solid',borderwidth=2)
    l1.place(x=50,y=20)
    Label(s7,text = "Enter your Admin No: ",font=("Monotype corsiva",20),bg="#99afff", fg="Black",relief='solid',borderwidth=2).place(x=50,y=150)
    Entry(s7,width = 20,textvariable = admch,font=("Monotype corsiva",18)).place(x=300,y=150)
    Button(s7,text="Check",bg="#8194cd",fg="Black",font=("Times New Roman",20),command = check_adm,width=10,height=1).place(x=550,y=150)

    s7.attributes('-fullscreen', True)

    s7.mainloop()




def m_di():
    c=del_ph.get()
    f1=open('incident.csv','r')
    f2=open('temp.csv','w',newline='')
    cw=csv.writer(f2)
    cr=csv.reader(f1)
    mg=messagebox.askquestion('Caution','Are you sure u want to delete the disaster details / disaster has been addressed???',icon='warning')
    if mg=='yes':
        flag=-1
        for i in cr:
            if i[12]!=c:
                cw.writerow(i)
            else:
                flag=1
        if flag==1:
            messagebox.showinfo("Admin","DELETED SUCCESSFULLY")
        else:
            messagebox.showerror("Admin","Invalid Phone Number")
    
        
          
    f1.close()
    f2.close()
    os.remove('incident.csv')
    os.rename('temp.csv','incident.csv')
        
def del_i():
    a=900
    b=500
    l1=Label(s3,text="Enter primary contact number :",font=("Monotype corsiva",20),bg="#6270a5", fg="White")
    l1.place(x=a,y=b)
    a=a+310
    t1=Entry(s3,textvariable=del_ph,font=('Monotype Corsiva',20))
    t1.place(x=a,y=b)
    a=a-100
    b=b+75
    b1=Button(s3,text='Delete',bg='#0c3b62',fg='White',font=('Times New Roman',20),command=m_di)
    b1.place(x=a,y=b)
    def clear():
        t1.delete(0,END)
    a=a+100
    
    b2=Button(s3,text='Clear',command=clear,font=('Times New Roman',20),bg="#0c3b62",fg="White")
    b2.place(x=a,y=b)

def modify_i():
    r1=itx1.get()
    r2=itx2.get()
    r3=itx3.get()
    r4=itx4.get()
    r5=itx5.get()
    r6=itx6.get()
    r7=itx7.get()
    r8=itx8.get()
    r9=itx9.get()
    r10=itx10.get()
    r11=itx11.get()
    r12=itx12.get()
    r13=itx13.get()
    r14=itx14.get()
    
    f1=open('incident.csv','r')
    f2=open('temp.csv','w',newline='')
    cw=csv.writer(f2)
    cr=csv.reader(f1)
    flag=-1
    for i in cr:
        flag=1
        if i[12]==r13:
            cw.writerow([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14])
        else:
            cw.writerow(i)
    
    if flag==1:
        messagebox.showinfo('modify incident','Your incident details have been modified successfully!!!')

    f1.close()
    f2.close()
    os.remove('incident.csv')
    os.rename('temp.csv','incident.csv')
    
def psc_im():
    s6.withdraw()
    s3.deiconify()
    
#Checking for incident modification     
def check_i():
    f=open('incident.csv','r')
    cr=csv.reader(f)
    ph=itx13.get()
    flag=-1
    for i in cr:
        if i[12]==ph:
            flag=1
            a=50
            b=200
            l2=Label(s6,text="Name of the place ",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l2.place(x=a,y=b)
            b=b+50
            l3=Label(s6,text="Name of City/district/village ",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l3.place(x=a,y=b)
            b=b+50
            l4=Label(s6,text="Name of state",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l4.place(x=a,y=b)
            b=b+50
            l5=Label(s6,text="Type of Natural Disaster",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l5.place(x=a,y=b)
            b=b+50
            l6=Label(s6,text="Expected no. of volunteers",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l6.place(x=a,y=b)
            b=b+50
            l7=Label(s6,text="Blood Donors required (Approx)",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l7.place(x=a,y=b)
            b=b+50
            l8=Label(s6,text="Funds required(expected)",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l8.place(x=a,y=b)
            a=850
            b=150
            l9=Label(s6,text="Date of incident ",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l9.place(x=a,y=b)
            b=b+50
            l10=Label(s6,text="Reporting Date ",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l10.place(x=a,y=b)
            b=b+50
            l11=Label(s6,text="Exit date",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l11.place(x=a,y=b)
            b=b+50
            l12=Label(s6,text="No. of camp days (approx) ",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l12.place(x=a,y=b)
            b=b+50
            l13=Label(s6,text="Person in-charge ",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l13.place(x=a,y=b)
            b=b+50
           
            l15=Label(s6,text="Secondary Contact Number ",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
            l15.place(x=a,y=b)
            b=b+50

            a=480
            b=150
            t13=Entry(s6,textvariable=itx13,state='disabled',bg='white',font=('Monotype Corsiva',25),width=15)
            t13.place(x=a,y=b)
            b=b+50
            t1=Entry(s6,textvariable=itx1,bg='white',font=('Monotype Corsiva',25))
            t1.place(x=a,y=b)
            b=b+50
            t2=Entry(s6,textvariable=itx2,bg='white',font=('Monotype Corsiva',25))
            t2.place(x=a,y=b)
            b=b+50
            t3=Entry(s6,textvariable=itx3,bg='white',font=('Monotype Corsiva',25))
            t3.place(x=a,y=b)
            b=b+50
            t4=Entry(s6,textvariable=itx4,bg='white',font=('Monotype Corsiva',25))
            t4.place(x=a,y=b)
            b=b+50
            t5=Entry(s6,textvariable=itx5,bg='white',font=('Monotype Corsiva',25))
            t5.place(x=a,y=b)
            b=b+50
            t6=Entry(s6,textvariable=itx6,bg='white',font=('Monotype Corsiva',25))
            t6.place(x=a,y=b)
            b=b+50
            t7=Entry(s6,textvariable=itx7,bg='white',font=('Monotype Corsiva',25))
            t7.place(x=a,y=b)
            b=150
            a=1200
            t8=Entry(s6,textvariable=itx8,bg='white',font=('Monotype Corsiva',25))
            t8.place(x=a,y=b)
            b=b+50
            t9=Entry(s6,textvariable=itx9,bg='white',font=('Monotype Corsiva',25))
            t9.place(x=a,y=b)
            b=b+50
            t10=Entry(s6,textvariable=itx10,bg='white',font=('Monotype Corsiva',25))
            t10.place(x=a,y=b)
            b=b+50
            t11=Entry(s6,textvariable=itx11,bg='white',font=('Monotype Corsiva',25))
            t11.place(x=a,y=b)
            b=b+50
            t12=Entry(s6,textvariable=itx12,bg='white',font=('Monotype Corsiva',25))
            t12.place(x=a,y=b)
            b=b+50
            
            t14=Entry(s6,textvariable=itx14,bg='white',font=('Monotype Corsiva',25))
            t14.place(x=a,y=b)
            b=b+200
            a=400

            t1.insert(0,i[0]) 
            t2.insert(0,i[1]) 
            t3.insert(0,i[2]) 
            t4.insert(0,i[3]) 
            t5.insert(0,i[4]) 
            t6.insert(0,i[5]) 
            t7.insert(0,i[6]) 
            t8.insert(0,i[7]) 
            t9.insert(0,i[8]) 
            t10.insert(0,i[9]) 
            t11.insert(0,i[10]) 
            t12.insert(0,i[11]) 
            t14.insert(0,i[13]) 

            b2=Button(s6,text='BACK TO PREVIOUS MENU',fg='Green',bg='#f7ac03',font=('Times New Roman',20),width=25,command=psc_im)
            b2.place(x=a,y=b)
            a=a+400
            b1=Button(s6,text='MODIFY',fg='Green',bg="#f7ac03",font=('Times New Roman',20),width=25,command=modify_i)
            b1.place(x=a,y=b)
    else:
        flage=-1

    if flag==-1:
        messagebox.showinfo('Incident Details','No existing record found')
        s6.withdraw()
        s3.deiconify()
        
#Modify Incident details
def p1_im():
    s3.withdraw()
    s6.deiconify()
    he=s6.winfo_screenheight()
    wi=s6.winfo_screenwidth()
    s6.geometry("%dx%d"%(wi,he))
    s6['bg']='light green'

    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\pic10.png")
    lab=Label(s6, image=im)
    lab.place(x=0,y=0)
    
    l1=Label(s6,text="Modify Details ",font=("Eras Medium ITC",60),bg="#dfd1c5", fg="Black")
    l1.place(x=50,y=20)

    a=50
    b=150
    l14=Label(s6,text="Enter your primary contact number : ",font=("Monotype corsiva",25),bg="#dfd1c5", fg="Black")
    l14.place(x=a,y=b)
    a=480
    
    t13=Entry(s6,textvariable=itx13,bg='white',font=('Monotype Corsiva',25),width=15)
    t13.place(x=a,y=b)
    a=a+250
    ch=Button(s6,text='Check',bg='#dfd1c5',fg='Green',command=check_i,font=('Times New Roman',20),relief='solid',borderwidth=2)
    ch.place(x=a,y=b-5)

    
    s6.attributes('-fullscreen', True)

    s6.mainloop()



def ia_commit():
    f=open('incident.csv','a',newline='')
    cw=csv.writer(f)
    
    r1=itx1.get()
    r2=itx2.get()
    r3=itx3.get()
    r4=itx4.get()
    r5=itx5.get()
    r6=itx6.get()
    r7=itx7.get()
    r8=itx8.get()
    r9=itx9.get()
    r10=itx10.get()
    r11=itx11.get()
    r12=itx12.get()
    r13=itx13.get()
    r14=itx14.get()
    cw.writerow([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14])
    f.close()
    messagebox.showinfo('Incident','Incident Details successfully added!!!')
        
def psc_ia():
    s5.withdraw()
    s3.deiconify()
    
#Add Incident details
def p1_ia():
    s3.withdraw()
    s5.deiconify()
    he=s5.winfo_screenheight()
    wi=s5.winfo_screenwidth()
    s5.geometry("%dx%d"%(wi,he))
    s5['bg']='light green'

    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\pic9.png")
    lab=Label(s5, image=im)
    lab.place(x=0,y=0)

    l1=Label(s5,text="Incident Details ",font=("Eras Medium ITC",60),bg="#e9d8c6", fg="Black")
    l1.place(x=50,y=20)

    a=50
    b=150
    l2=Label(s5,text="Name of the place ",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l2.place(x=a,y=b)
    b=b+75
    l3=Label(s5,text="Name of City/district/village ",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l3.place(x=a,y=b)
    b=b+75
    l4=Label(s5,text="Name of state",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l4.place(x=a,y=b)
    b=b+75
    l5=Label(s5,text="Type of Natural Disaster",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l5.place(x=a,y=b)
    b=b+75
    l6=Label(s5,text="Expected no. of volunteers",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l6.place(x=a,y=b)
    b=b+75
    l7=Label(s5,text="Blood Donors required (Approx)",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l7.place(x=a,y=b)
    b=b+75
    l8=Label(s5,text="Funds required(expected)",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l8.place(x=a,y=b)
    a=850
    b=150
    l9=Label(s5,text="Date of incident ",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l9.place(x=a,y=b)
    b=b+75
    l10=Label(s5,text="Reporting Date ",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l10.place(x=a,y=b)
    b=b+75
    l11=Label(s5,text="Exit date",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l11.place(x=a,y=b)
    b=b+75
    l12=Label(s5,text="No. of camp days (approx) ",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l12.place(x=a,y=b)
    b=b+75
    l13=Label(s5,text="Person in-charge ",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l13.place(x=a,y=b)
    b=b+75
    l14=Label(s5,text="Primary Contact Number ",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l14.place(x=a,y=b)
    b=b+75
    l15=Label(s5,text="Secondary Contact Number ",font=("Monotype corsiva",25),bg="#e9d8c6", fg="Black")
    l15.place(x=a,y=b)
    b=b+75

    a=475
    b=150
    t1=Entry(s5,textvariable=itx1,bg='white',font=('Monotype Corsiva',25))
    t1.place(x=a,y=b)
    b=b+75
    t2=Entry(s5,textvariable=itx2,bg='white',font=('Monotype Corsiva',25))
    t2.place(x=a,y=b)
    b=b+75
    t3=Entry(s5,textvariable=itx3,bg='white',font=('Monotype Corsiva',25))
    t3.place(x=a,y=b)
    b=b+75
    t4=Entry(s5,textvariable=itx4,bg='white',font=('Monotype Corsiva',25))
    t4.place(x=a,y=b)
    b=b+75
    t5=Entry(s5,textvariable=itx5,bg='white',font=('Monotype Corsiva',25))
    t5.place(x=a,y=b)
    b=b+75
    t6=Entry(s5,textvariable=itx6,bg='white',font=('Monotype Corsiva',25))
    t6.place(x=a,y=b)
    b=b+75
    t7=Entry(s5,textvariable=itx7,bg='white',font=('Monotype Corsiva',25))
    t7.place(x=a,y=b)
    b=150
    a=1200
    t8=Entry(s5,textvariable=itx8,bg='white',font=('Monotype Corsiva',25))
    t8.place(x=a,y=b)
    b=b+75
    t9=Entry(s5,textvariable=itx9,bg='white',font=('Monotype Corsiva',25))
    t9.place(x=a,y=b)
    b=b+75
    t10=Entry(s5,textvariable=itx10,bg='white',font=('Monotype Corsiva',25))
    t10.place(x=a,y=b)
    b=b+75
    t11=Entry(s5,textvariable=itx11,bg='white',font=('Monotype Corsiva',25))
    t11.place(x=a,y=b)
    b=b+75
    t12=Entry(s5,textvariable=itx12,bg='white',font=('Monotype Corsiva',25))
    t12.place(x=a,y=b)
    b=b+75
    t13=Entry(s5,textvariable=itx13,bg='white',font=('Monotype Corsiva',25))
    t13.place(x=a,y=b)
    b=b+75
    t14=Entry(s5,textvariable=itx14,bg='white',font=('Monotype Corsiva',25))
    t14.place(x=a,y=b)
    b=b+100
    a=150

    def clear_i():
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        t6.delete(0,END)
        t7.delete(0,END)
        t8.delete(0,END)
        t9.delete(0,END)
        t10.delete(0,END)
        t11.delete(0,END)
        t12.delete(0,END)
        t13.delete(0,END)
        t14.delete(0,END)

    b2=Button(s5,text='BACK TO PREVIOUS MENU',fg='Green',bg='#f4a905',font=('Times New Roman',20),width=25,command=psc_ia,relief='solid',borderwidth=2)
    b2.place(x=a,y=b)
    a=a+400
    b3=Button(s5,text='CLEAR',fg='Green',bg='#f4a905',font=('Times New Roman',20),width=25,command=clear_i,relief='solid',borderwidth=2)
    b3.place(x=a,y=b)
    a=a+400
    b1=Button(s5,text='SUBMIT',fg='Green',bg="#f4a905",font=('Times New Roman',20),width=25,command=ia_commit,relief='solid',borderwidth=2)
    b1.place(x=a,y=b)

    s5.attributes('-fullscreen', True)

    s5.mainloop()


def p1_incident():
    a=1000
    b=200
    b_a=Button(s3, text="ADD INCIDENT", command=p1_ia,font=("Times New Roman",20),bg="#425a90",fg="White",width=30,relief='raised',borderwidth=2)
    b_a.place(x=a,y=b)
    b=b+100
    b_m=Button(s3, text="MODIFY INCIDENT DETAILS", command=p1_im,font=("Times New Roman",20),bg="#6374ac",fg="White",width=30,relief='raised',borderwidth=2)
    b_m.place(x=a,y=b)
    b=b+100
    b_d=Button(s3, text="DELETE INCIDENT", command=del_i,font=("Times New Roman",20),bg="#795c8e",fg="White",width=30,relief='raised',borderwidth=2)
    b_d.place(x=a,y=b)








def psc_vm():
    s4.withdraw()
    s3.deiconify()
    
#commit modify volunteers
def modify_v():
    a=adm.get()
    r1=mtx1.get()
    r2=mtx2.get()
    r3=rg.get()
    r4=mtx4.get()
    r5=mtx5.get()
    r6=mtx6.get()
    r7=mtx7.get()
    r8=mtx8.get()

    r9=mtx9.get()
    r10=mtx10.get()
    r11=rb.get()

    r12=mtx12.get()
    r13=mtx13.get()
    r14=mtx14.get()
    r15=mtx15.get()
    r16=mtx16.get()
    r17=mtx17.get()

    r18=rc.get()
    r19=mtx19.get()
    r20=mtx20.get()
    r21=mtx21.get()
    r22_1=mtx22_1.get()
    r22_2=mtx22_2.get()
    r22_3=mtx22_3.get()
    f1=open('volunteer.csv','r')
    f2=open('temp.csv','a',newline='')
    cw=csv.writer(f2)
    cr=csv.reader(f1)

    flag=1

    for i in cr :
        if i[0]!=a:
            cw.writerow(i)
        else:
            cw.writerow([a,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22_1,r22_2,r22_3])
    else:
        flag=-1
    if flag==-1:
        messagebox.showinfo('Admin','Modified Successfully')
        

    f1.close()
    f2.close()
    os.remove('volunteer.csv')
    os.rename('temp.csv','volunteer.csv')
    


    
#modify volunteers
def check_v():
    f=open('volunteer.csv','r')
    cr=csv.reader(f)
    a=adm.get()
    flag=-1
    for i in cr:
        n=i[0]
        
        if n==a:
            flag=1
            a=50
            b=200
            l2=Label(s4,text="Name",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l2.place(x=a,y=b)
            b=b+50
            l3=Label(s4,text="Age",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l3.place(x=a,y=b)
            b=b+50
            l4=Label(s4,text="Gender",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l4.place(x=a,y=b)
            b=b+50
            l5=Label(s4,text="Qualification",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l5.place(x=a,y=b)
            b=b+50
            l6=Label(s4,text="Address",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l6.place(x=a,y=b)
            b=b+50
            l7=Label(s4,text="Area",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l7.place(x=a,y=b)
            b=b+50
            l8=Label(s4,text="Phone Number",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l8.place(x=a,y=b)
            b=b+50
            l9=Label(s4,text="Emergency Contact Number",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l9.place(x=a,y=b)
            b=b+50
        

            l10=Label(s4,text="Email Id",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l10.place(x=a,y=b)
            b=b+50
            l11=Label(s4,text="Aadhar No",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l11.place(x=a,y=b)
            b=b+50
            
            l12=Label(s4,text="Blood donor",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l12.place(x=a,y=b)
            b=b+50
            l13=Label(s4,text="Blood group",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l13.place(x=a,y=b)
            b=b+50
            
            a=750
            b=150
            
            l14=Label(s4,text="Any allegies?",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l14.place(x=a,y=b)
            b=b+50
            #l15=Label(s4,text="How can you help? ",font=("Monotype corsiva",20),bg="Light Green", fg="Black")
            #l15.place(x=a,y=b)
            b=b+50
            l16=Label(s4,text="Nature of Job",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l16.place(x=a,y=b)
            b=b+50
            l17=Label(s4,text="How amny days leave can be taken(approx)?",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l17.place(x=a,y=b)
            b=b+50
            l18=Label(s4,text="How many kms can you walk per day ",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l18.place(x=a,y=b)
            b=b+50
            l19=Label(s4,text="Any previous camp experience ",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l19.place(x=a,y=b)
            b=b+50
            l20=Label(s4,text="No. of camps attended ",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l20.place(x=a,y=b)
            b=b+50
            l21=Label(s4,text="Location in words ",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l21.place(x=a,y=b)
            b=b+50
            l22=Label(s4,text="Ready to travel any location? ",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l22.place(x=a,y=b)
            b=b+50
            l23=Label(s4,text="Enter three places : ",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
            l23.place(x=a,y=b)
            b=b+50

            a=320
            b=150
            t1=Entry(s4,textvariable=adm,state='disabled',bg='white',font=('Monotype Corsiva',20))
            t1.place(x=a,y=b)
            b=b+50
            
            t2=Entry(s4,textvariable=mtx1,bg='white',font=('Monotype Corsiva',20))
            t2.place(x=a,y=b)
            b=b+50
            t3=Entry(s4,textvariable=mtx2,bg='white',font=('Monotype Corsiva',20))
            t3.place(x=a,y=b)
            b=b+50
            t4m=Radiobutton(s4,text='Male',variable=rg,value='male',bg='#cce9d8',font=('Times New Roman',20))
            t4m.place(x=a,y=b)
            
            t4f=Radiobutton(s4,text='Female',variable=rg,value='female',bg='#cce9d8',font=('Times New Roman',20))
            t4f.place(x=a+100,y=b)
            b=b+50
            t5=Entry(s4,textvariable=mtx4,bg='white',font=('Monotype Corsiva',20))
            t5.place(x=a,y=b)
            b=b+50
            t6=Entry(s4,textvariable=mtx5,bg='white',font=('Monotype Corsiva',20))
            t6.place(x=a,y=b)
            b=b+50
            t7=Entry(s4,textvariable=mtx6,bg='white',font=('Monotype Corsiva',20))
            t7.place(x=a,y=b)
            b=b+50
            t8=Entry(s4,textvariable=mtx7,bg='white',font=('Monotype Corsiva',20))
            t8.place(x=a,y=b)
            b=b+50
            t9=Entry(s4,textvariable=mtx8,bg='white',font=('Monotype Corsiva',20))
            t9.place(x=a,y=b)
            b=b+50
            t10=Entry(s4,textvariable=mtx9,bg='white',font=('Monotype Corsiva',20))
            t10.place(x=a,y=b)
            b=b+50
            t11=Entry(s4,textvariable=mtx10,bg='white',font=('Monotype Corsiva',20))
            t11.place(x=a,y=b)
            b=b+50
            t12y=Radiobutton(s4,text='Yes',variable=rb,value='yes',bg='#cce9d8',font=('Times New Roman',20))
            t12y.place(x=a,y=b)
            t12n=Radiobutton(s4,text='No',variable=rb,value='no',bg='#cce9d8',font=('Times New Roman',20))
            t12n.place(x=a+100,y=b)
            b=b+50
            t13=Entry(s4,textvariable=mtx12,bg='white',font=('Monotype Corsiva',20))
            t13.place(x=a,y=b)
            b=b+50
            
            a=1250
            b=150
            t14=Entry(s4,textvariable=mtx13,bg='white',font=('Monotype Corsiva',20))
            t14.place(x=a,y=b)
            b=b+50
            #t15=Entry(s4,textvariable=mtx14,bg='white',font=('Monotype Corsiva',20))
            #t15.place(x=a,y=b)
            b=b+50
            t16=Entry(s4,textvariable=mtx15,bg='white',font=('Monotype Corsiva',20))
            t16.place(x=a,y=b)
            b=b+50
            t17=Entry(s4,textvariable=mtx16,bg='white',font=('Monotype Corsiva',20))
            t17.place(x=a,y=b)
            b=b+50
            t18=Entry(s4,textvariable=mtx17,bg='white',font=('Monotype Corsiva',20))
            t18.place(x=a,y=b)
            b=b+50
            t19y=Radiobutton(s4,text='Yes',variable=rc,value='yes',bg='#cce9d8',font=('Times New Roman',20))
            t19y.place(x=a,y=b)
            t19n=Radiobutton(s4,text='No',variable=rc,value='no',bg='#cce9d8',font=('Times New Roman',20))
            t19n.place(x=a+100,y=b)
            b=b+50
            t20=Entry(s4,textvariable=mtx19,bg='white',font=('Monotype Corsiva',20))
            t20.place(x=a,y=b)
            b=b+50
            t21=Entry(s4,textvariable=mtx20,bg='white',font=('Monotype Corsiva',20))
            t21.place(x=a,y=b)
            b=b+50
            t22=Entry(s4,textvariable=mtx21,bg='white',font=('Monotype Corsiva',20))
            t22.place(x=a,y=b)
            b=b+50
            t23_1=Entry(s4,textvariable=mtx22_1,bg='white',font=('Monotype Corsiva',20),width=15)
            t23_1.place(x=a-300,y=b)
            t23_2=Entry(s4,textvariable=mtx22_2,bg='white',font=('Monotype Corsiva',20),width=15)
            t23_2.place(x=a-100,y=b)
            t23_3=Entry(s4,textvariable=mtx22_3,bg='white',font=('Monotype Corsiva',20),width=15)
            t23_3.place(x=a+100,y=b)
            
            t2.insert(0,i[1])
            t3.insert(0,i[2])
            
            
            t5.insert(0,i[4])
            t6.insert(0,i[5])
            t7.insert(0,i[6])
            t8.insert(0,i[7])
            t9.insert(0,i[8])
            t10.insert(0,i[9])
            t11.insert(0,i[10])
            
            t13.insert(0,i[12])
            
            t14.insert(0,i[13])
            t16.insert(0,i[15])
            t17.insert(0,i[16])
            t18.insert(0,i[17])
            
            t20.insert(0,i[19])
            t21.insert(0,i[20])
            t22.insert(0,i[21])
            t23_1.insert(0,i[22])
            t23_2.insert(0,i[23])
            t23_3.insert(0,i[24])

            a=650
            b=b+100
            b1=Button(s4,text='UPDATE',font=("Monotype Corsiva",20),bg='#f2ebce',fg='Green',command=modify_v,relief='raised',borderwidth=2)
            b1.place(x=a,y=b)
            a=a+200
            b2=Button(s4,text='BACK TO PREVIOUS SCREEN',font=("Monotype Corsiva",20),bg='#f2ebce',fg='Green',command=psc_vm,relief='raised',borderwidth=2)
            b2.place(x=a,y=b)
            a=a+200
            
                



            
    if flag==-1:
    
            messagebox.showinfo("Invalid","Adm no. not found")
            s4.withdraw()
            s3.deiconify()
            

#modify checking
def p1_m():
    s3.withdraw()
    s4.deiconify()
    he=s4.winfo_screenheight()
    wi=s4.winfo_screenwidth()
    s4.geometry("%dx%d"%(wi,he))
    s4['bg']='light green'

    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\image20.png")
    lab=Label(s4, image=im)
    lab.place(x=0,y=0)

    
    l1=Label(s4,text="Modify :",font=("Eras Medium ITC",60),bg="#cce9d8", fg="Black")
    l1.place(x=50,y=20)
    
    
    a=50
    b=150

    
    ch=Label(s4,text="Enter admin no. :",font=("Monotype corsiva",20),bg="#cce9d8", fg="Black")
    ch.place(x=a,y=b)
    
    a=320
    t1=Entry(s4,textvariable=adm,bg='white',font=('Monotype Corsiva',20))
    t1.place(x=a,y=b)
    b1=Button(s4,text='Check',command=check_v,font=("Times New Roman",20),bg='#f2ebce',fg="Green",relief='raised',borderwidth=2)
    b1.place(x=a+250,y=b)

    s4.attributes('-fullscreen', True)
    
    s4.mainloop()

def m_dv():
    f1=open('volunteer.csv','r')
    cr=csv.reader(f1)
    f2=open('temp.csv','w',newline='')
    cw=csv.writer(f2)
    c=del_adm.get()
    mg=messagebox.askquestion('Caution','Are you sure you want delete the volunteer detail ???',icon='warning')
    if mg=='yes':
        flag=-1
        for i in cr:
            if i[0]!=c:
                
                cw.writerow(i)
            else:
                flag=1
        if flag==-1:
            messagebox.showinfo('Caution',"Invalid admin no.!!!")
        else:
            messagebox.showinfo('Completed','Deleted Successfully')

    f1.close()
    f2.close()
    os.remove('volunteer.csv')
    os.rename('temp.csv','volunteer.csv')
            
                
        
def del_v():
    a=100
    b=610
    l1=Label(s3,text='Enter Your Admin no. : ',font=('Monotype Corsiva',20),bg='#012041',fg='White')
    l1.place(x=a,y=b)
    a=a+250
    t1=Entry(s3,textvariable=del_adm,font=('Monotype Corsiva',20))
    t1.place(x=a,y=b)
    a=a-100
    b=b+75
    b1=Button(s3,text='Delete',command=m_dv,font=('Times New Roman',20),bg="#02152c",fg="White",relief='raised',borderwidth=2)
    b1.place(x=a,y=b)
    def clear():
        t1.delete(0,END)
    a=a+100
    
    b2=Button(s3,text='Clear',command=clear,font=('Times New Roman',20),bg="#02152c",fg="White",relief='raised',borderwidth=2)
    b2.place(x=a,y=b)
def p1_mm():
    s3.withdraw()
    w.deiconify()
    
#Admin()    
def p1():
    w.withdraw()
    s3.deiconify()
    he=s3.winfo_screenheight()
    wi=s3.winfo_screenwidth()
    s3.geometry("%dx%d"%(wi,he))
    s3['bg']='light green'
    
    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\pic4.png")
    lab=Label(s3, image=im)
    lab.place(x=0,y=0)
    
    l1=Label(s3,text="Administration Page :",font=("Eras Medium ITC",60),bg="#0d4778", fg="White",relief='solid',borderwidth=2)
    l1.place(x=50,y=20)

    a=100
    b=200
    b1=Button(s3, text="Modify", command=p1_m,font=("Times New Roman",20),bg="#11578f",fg="White",width=20,relief='raised',borderwidth=2)
    b1.place(x=a,y=b)
    a=a+400
    b2=Button(s3, text="Delete", command=del_v,font=("Times New Roman",20),bg="#11578f",fg="White",width=20,relief='raised',borderwidth=2)
    b2.place(x=a,y=b)
    b=b+100
    b4=Button(s3, text="BACK TO MAIN MENU", command=p1_mm,font=("Times New Roman",20),bg="#11578f",fg="White",width=20,relief='raised',borderwidth=2)
    b4.place(x=300,y=b)
    a=900
    b=100
    b3=Button(s3, text="INCIDENT DETAILS  ", command=p1_incident,font=("Times New Roman",20),bg="#3580b6",fg="White",width=40,relief='raised',borderwidth=2)
    b3.place(x=a,y=b)

    s3.attributes('-fullscreen', True)
    
    s3.mainloop()

def p2_commit():
    f=open('volunteer.csv','a',newline='')
    cw=csv.writer(f)
    r1=tx1.get()
    r2=tx2.get()
    r3=rg.get()
    r4=tx4.get()
    r5=tx5.get()
    r6=tx6.get()
    r7=tx7.get()
    r8=tx8.get()

    r9=tx9.get()
    r10=tx10.get()
    r11=rb.get()

    r12=tx12.get()
    r13=tx13.get()
    r14=tx14.get()
    r15=tx15.get()
    r16=tx16.get()
    r17=tx17.get()

    r18=rc.get()
    r19=tx19.get()
    r20=tx20.get()
    r21=tx21.get()
    r22_1=tx22_1.get()
    r22_2=tx22_2.get()
    r22_3=tx22_3.get()

    adm_no=''.join(str(random.randint(0,9)) for i in range (4))
    
    R=[adm_no,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22_1,r22_2,r22_3]
    cw.writerow(R)

    f.close()
    messagebox.showinfo('Volunteer','Your admin no is '+adm_no)


    
def p2_mm():
    s2.withdraw()
    w.deiconify()


    
#Registration 
def p2():
    
    
    w.withdraw()
    s2.deiconify()
    he=s2.winfo_screenheight()
    wi=s2.winfo_screenwidth()
    s2.geometry("%dx%d"%(wi,he))


    im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\pic3.png")
    lab=Label(s2, image=im)
    lab.place(x=0,y=0)
    
    s2['bg']='light green'
    l1=Label(s2,text="Register yourself",font=("Eras Medium ITC",60),bg="#648284", fg="White",relief='solid',borderwidth=2)
    l1.place(x=50,y=20)
    
    a=50
    b=150
    l2=Label(s2,text="Name",font=("Monotype corsiva",20),bg="#607980", fg="White")
    l2.place(x=a,y=b)
    b=b+50
    l3=Label(s2,text="Age",font=("Monotype corsiva",20),bg="#55717c", fg="White")
    l3.place(x=a,y=b)
    b=b+50
    l4=Label(s2,text="Gender",font=("Monotype corsiva",20),bg="#486671", fg="White")
    l4.place(x=a,y=b)
    b=b+50
    l5=Label(s2,text="Qualification",font=("Monotype corsiva",20),bg="#435e71", fg="White")
    l5.place(x=a,y=b)
    b=b+50
    l6=Label(s2,text="Address",font=("Monotype corsiva",20),bg="#425f71", fg="White")
    l6.place(x=a,y=b)
    b=b+50
    l7=Label(s2,text="Area",font=("Monotype corsiva",20),bg="#436070", fg="White")
    l7.place(x=a,y=b)
    b=b+50    
    l8=Label(s2,text="Phone Number",font=("Monotype corsiva",20),bg="#406474", fg="White")
    l8.place(x=a,y=b)
    b=b+50
    l9=Label(s2,text="Emergency Contact Number",font=("Monotype corsiva",20),bg="#476776", fg="White")
    l9.place(x=a,y=b)
    b=b+50
    l10=Label(s2,text="Email Id",font=("Monotype corsiva",20),bg="#415f72", fg="White")
    l10.place(x=a,y=b)
    b=b+50
    
    l11=Label(s2,text="Aadhar No",font=("Monotype corsiva",20),bg="#455d5e", fg="White")
    l11.place(x=a,y=b)
    b=b+50
    
    l12=Label(s2,text="Blood donor",font=("Monotype corsiva",20),bg="#24343d", fg="White")
    l12.place(x=a,y=b)
    b=b+50
    l13=Label(s2,text="Blood group",font=("Monotype corsiva",20),bg="#24343d", fg="White")
    l13.place(x=a,y=b)
    b=b+50
    l14=Label(s2,text="Any allegies?",font=("Monotype corsiva",20),bg="#24343d", fg="White")
    l14.place(x=a,y=b)
    b=b+50
    a=700
    b=150
    #l15=Label(s2,text="How can you help? ",font=("Monotype corsiva",20),bg="Light Green", fg="White")
    #l15.place(x=a,y=b)
    #b=b+50
    l16=Label(s2,text="Nature of Job",font=("Monotype corsiva",20),bg="#324c5b", fg="White")
    l16.place(x=a,y=b)
    b=b+50
    l17=Label(s2,text="How amny days leave can be taken(approx)?",font=("Monotype corsiva",20),bg="#324c5b", fg="White")
    l17.place(x=a,y=b)
    b=b+50
    l18=Label(s2,text="How many kms can you walk per day ",font=("Monotype corsiva",20),bg="#324c59", fg="White")
    l18.place(x=a,y=b)
    b=b+50
    l19=Label(s2,text="Any previous camp experience ",font=("Monotype corsiva",20),bg="#324c59", fg="White")
    l19.place(x=a,y=b)
    b=b+50
    l20=Label(s2,text="No. of camps attended ",font=("Monotype corsiva",20),bg="#2e4855", fg="White")
    l20.place(x=a,y=b)
    b=b+50
    l21=Label(s2,text="Location in words ",font=("Monotype corsiva",20),bg="#3e5259", fg="White")
    l21.place(x=a,y=b)
    b=b+50
    l22=Label(s2,text="Ready to travel any location? ",font=("Monotype corsiva",20),bg="#3e5259", fg="White")
    l22.place(x=a,y=b)
    b=b+50
    l23=Label(s2,text="Enter three places : ",font=("Monotype corsiva",20),bg="#3e5259", fg="White")
    l23.place(x=a,y=b)
    b=b+50

    a=400
    b=150
    t1=Entry(s2,textvariable=tx1,bg='white',font=('Monotype Corsiva',20))
    t1.place(x=a,y=b)
    b=b+50
    t2=Entry(s2,textvariable=tx2,bg='white',font=('Monotype Corsiva',20))
    t2.place(x=a,y=b)
    b=b+50
    t3m=Radiobutton(s2,text='Male',variable=rg,value='male',bg='#516f79',fg="White",font=('Times New Roman',20))
    t3m.place(x=a,y=b)
    
    t3f=Radiobutton(s2,text='Female',variable=rg,value='female',bg='#516f79',fg="White",font=('Times New Roman',20))
    t3f.place(x=a+100,y=b)
    b=b+50
    t4=Entry(s2,textvariable=tx4,bg='white',font=('Monotype Corsiva',20))
    t4.place(x=a,y=b)
    b=b+50
    t5=Entry(s2,textvariable=tx5,bg='white',font=('Monotype Corsiva',20))
    t5.place(x=a,y=b)
    b=b+50
    t6=Entry(s2,textvariable=tx6,bg='white',font=('Monotype Corsiva',20))
    t6.place(x=a,y=b)
    b=b+50
    t7=Entry(s2,textvariable=tx7,bg='white',font=('Monotype Corsiva',20))
    t7.place(x=a,y=b)
    b=b+50
    t8=Entry(s2,textvariable=tx8,bg='white',font=('Monotype Corsiva',20))
    t8.place(x=a,y=b)
    b=b+50
    t9=Entry(s2,textvariable=tx9,bg='white',font=('Monotype Corsiva',20))
    t9.place(x=a,y=b)
    b=b+50
    t10=Entry(s2,textvariable=tx10,bg='white',font=('Monotype Corsiva',20))
    t10.place(x=a,y=b)
    b=b+50
    t11y=Radiobutton(s2,text='Yes',variable=rb,value='yes',bg='#283a46',fg='White',font=('Times New Roman',20))
    t11y.place(x=a,y=b)
    t11n=Radiobutton(s2,text='No',variable=rb,value='no',bg='#39434c',fg='White',font=('Times New Roman',20))
    t11n.place(x=a+100,y=b)
    b=b+50
    t12=Entry(s2,textvariable=tx12,bg='white',font=('Monotype Corsiva',20))
    t12.place(x=a,y=b)
    b=b+50
    t13=Entry(s2,textvariable=tx13,bg='white',font=('Monotype Corsiva',20))
    t13.place(x=a,y=b)
    b=b+50
    a=1200
    b=150
    #t14=Entry(s2,textvariable=tx14,bg='white',font=('Monotype Corsiva',20))
    #t14.place(x=a,y=b)
    #b=b+50
    t15=Entry(s2,textvariable=tx15,bg='white',font=('Monotype Corsiva',20))
    t15.place(x=a,y=b)
    b=b+50
    t16=Entry(s2,textvariable=tx16,bg='white',font=('Monotype Corsiva',20))
    t16.place(x=a,y=b)
    b=b+50
    t17=Entry(s2,textvariable=tx17,bg='white',font=('Monotype Corsiva',20))
    t17.place(x=a,y=b)
    b=b+50
    t18y=Radiobutton(s2,text='Yes',variable=rc,value='yes',bg='#3b4046',fg="White",font=('Times New Roman',20))
    t18y.place(x=a,y=b)
    t18n=Radiobutton(s2,text='No',variable=rc,value='no',bg='#3b4046',fg="White",font=('Times New Roman',20))
    t18n.place(x=a+100,y=b)
    b=b+50
    t19=Entry(s2,textvariable=tx19,bg='white',font=('Monotype Corsiva',20))
    t19.place(x=a,y=b)
    b=b+50
    t20=Entry(s2,textvariable=tx20,bg='white',font=('Monotype Corsiva',20))
    t20.place(x=a,y=b)
    b=b+50
    t21=Entry(s2,textvariable=tx21,bg='white',font=('Monotype Corsiva',20))
    t21.place(x=a,y=b)
    b=b+50
    t22_1=Entry(s2,textvariable=tx22_1,bg='white',font=('Monotype Corsiva',20),width=15)
    t22_1.place(x=a-300,y=b)
    t22_2=Entry(s2,textvariable=tx22_2,bg='white',font=('Monotype Corsiva',20),width=15)
    t22_2.place(x=a-100,y=b)
    t22_3=Entry(s2,textvariable=tx22_3,bg='white',font=('Monotype Corsiva',20),width=15)
    t22_3.place(x=a+100,y=b)


    def clear_v():
        t1.delete(0,END)
        t2.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        t6.delete(0,END)
        t7.delete(0,END)
        t8.delete(0,END)
        t9.delete(0,END)
        t10.delete(0,END)
        t12.delete(0,END)
        t13.delete(0,END)
        #t14.delete(0,END)
        t15.delete(0,END)
        t16.delete(0,END)
        t17.delete(0,END)
        t19.delete(0,END)
        t20.delete(0,END)
        t21.delete(0,END)
        t22_1.delete(0,END)
        t22_2.delete(0,END)
        t22_3.delete(0,END)

    b=b+100
    a=700
    
    b1=Button(s2,text='SUBMIT',font=("Monotype Corsiva",20),bg='#131d24',fg='White',command=p2_commit,relief='raised',borderwidth=2)
    b1.place(x=a,y=b)
    a=a+200
    b2=Button(s2,text='BACK TO MAIN MENU',font=("Monotype Corsiva",20),bg='#131d24',fg='light green',command=p2_mm)
    b2.place(x=a,y=b)
    a=a+400
    b3=Button(s2,text='CLEAR',fg='Light Green',bg='#131d24',font=('Times New Roman',20),command=clear_v)
    b3.place(x=a,y=b)

    s2.attributes('-fullscreen', True)
    
    s2.mainloop()
    
    
    
    
#Main screen   
w=tk.Tk()
he=w.winfo_screenheight()
wi=w.winfo_screenwidth()
w.geometry("%dx%d"%(wi,he))

w['bg']='light green'
s1=Toplevel()
s2=Toplevel()#Registration_screen
s3=Toplevel()#Admin_screen 
s4=Toplevel()#V_modify_screen
s5=Toplevel()#Add_incident_screen 
s6=Toplevel()#Incident_modify_screen
s7=Toplevel()#Training_screen
s8=Toplevel()#OnDuty_screen
s9=Toplevel()#Report_screen
s10=Toplevel()#OD_Report_screen
s11=Toplevel()#OD_truck_pic(For giving a animation kind of effect but not literally)
s12=Toplevel()#Genr_ins_screen 
s13=Toplevel()#Training_report_screen 
s1.withdraw()
s2.withdraw()
s3.withdraw()
s4.withdraw()
s5.withdraw()
s6.withdraw()
s7.withdraw()
s8.withdraw()
s9.withdraw()
s10.withdraw()
s11.withdraw()
s12.withdraw()
s13.withdraw()
w.deiconify()


#for registration form 
tx1=tk.StringVar()
tx2=tk.StringVar()
#tx3=tk.StringVar()
tx4=tk.StringVar()
tx5=tk.StringVar()
tx6=tk.StringVar()
tx7=tk.StringVar()
tx8=tk.StringVar()
tx9=tk.StringVar()
tx10=tk.StringVar()
#tx11=tk.StringVar()
tx12=tk.StringVar()
tx13=tk.StringVar()
tx14=tk.StringVar()
tx15=tk.StringVar()
tx16=tk.StringVar()
tx17=tk.StringVar()
#tx18=tk.StringVar()
tx19=tk.StringVar()
tx20=tk.StringVar()
tx21=tk.StringVar()
tx22_1=tk.StringVar()
tx22_2=tk.StringVar()
tx22_3=tk.StringVar()
#Radio buttons 
rg=tk.StringVar()
rb=tk.StringVar()
rc=tk.StringVar()


adm=tk.StringVar()
#Vmodify_txtvar
mtx1=tk.StringVar()
mtx2=tk.StringVar()
mtx4=tk.StringVar()
mtx5=tk.StringVar()
mtx6=tk.StringVar()
mtx7=tk.StringVar()
mtx8=tk.StringVar()
mtx9=tk.StringVar()
mtx10=tk.StringVar()
mtx12=tk.StringVar()
mtx13=tk.StringVar()
mtx14=tk.StringVar()
mtx15=tk.StringVar()
mtx16=tk.StringVar()
mtx17=tk.StringVar()
mtx19=tk.StringVar()
mtx20=tk.StringVar()
mtx21=tk.StringVar()
mtx22_1=tk.StringVar()
mtx22_2=tk.StringVar()
mtx22_3=tk.StringVar()

#Inc_modify&add_textvar
itx1=tk.StringVar()
itx2=tk.StringVar()
itx3=tk.StringVar()
itx4=tk.StringVar()
itx5=tk.StringVar()
itx6=tk.StringVar()
itx7=tk.StringVar()
itx8=tk.StringVar()
itx9=tk.StringVar()
itx10=tk.StringVar()
itx11=tk.StringVar()
itx12=tk.StringVar()
itx13=tk.StringVar()
itx14=tk.StringVar()

del_ph=tk.StringVar()
del_adm=tk.StringVar()

admch=tk.StringVar()
t1=tk.StringVar()
t2=tk.StringVar()
t3=tk.StringVar()
t4=tk.StringVar()
rp=tk.StringVar()

otx1=tk.StringVar()
otx2=tk.StringVar()
otx3=tk.StringVar()
otx4=tk.StringVar()
otx5=tk.StringVar()
otx6=tk.StringVar()
ri=tk.StringVar()



def exit():
    w.destroy()



im=PhotoImage(file=r"C:\Users\kisha\Documents\project 2023-24\pic2.png")
lab=Label(w, image=im)
lab.place(x=0,y=0)

l1=Label(w,text=" Disaster Management ", font=("Eras Medium ITC",60), bg="#334144", fg="#cf4934",relief='solid',borderwidth=2)
l1.place(x=200, y=100)
a=1100
b=200
b1=Button(w, text="Admin", command=p1,font=("Times New Roman",20),bg="Light Yellow",fg="#cf4934",width=20,relief='solid',borderwidth=2,activebackground='#cf4934',activeforeground='Black',highlightthickness=0)
b1.place(x=a,y=b)
b=b+100
b2=Button(w, text="Register as volunteer", command=p2,font=("Times New Roman",20),bg="Light Yellow",fg="#cf4934",width=20,relief='solid',borderwidth=2,activebackground='#cf4934',activeforeground='Black',highlightthickness=0)
b2.place(x=a,y=b)
b=b+100
b3=Button(w, text="Training Session", command=p3,font=("Times New Roman",20),bg="Light Yellow",fg="#cf4934",width=20,relief='solid',borderwidth=2,activebackground='#cf4934',activeforeground='Black',highlightthickness=0)
b3.place(x=a,y=b)
b=b+100
b4=Button(w, text="On Duty ", command=p4,font=("Times New Roman",20),bg="Light Yellow",fg="#cf4934",width=20,relief='solid',borderwidth=2,activebackground='#cf4934',activeforeground='Black',highlightthickness=0)
b4.place(x=a,y=b)
b=b+100
b5=Button(w, text="Report ", command=p5,font=("Times New Roman",20),bg="Light Yellow",fg="#cf4934",width=20,relief='solid',borderwidth=2,activebackground='#cf4934',activeforeground='Black',highlightthickness=0)
b5.place(x=a,y=b)
b=b+100
b6=Button(w, text="Exit ", command=exit,font=("Times New Roman",20),bg="Light Yellow",fg="#cf4934",width=20,relief='solid',borderwidth=2,activebackground='#cf4934',activeforeground='Black',highlightthickness=0)
b6.place(x=a,y=b)
b=b+100

w.attributes('-fullscreen', True)

w.mainloop()
