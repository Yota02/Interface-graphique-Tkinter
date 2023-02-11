# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:15:40 2021

@author: Alexis
"""
from tkinter import * 

def calculer():
    """
    Permet de calculer la somme alterné d'un tableau
    """
    longeur1 = int(longueurentry.get())
    reponse = 0 
    if longeur1 == 1 :
        valeur1 = int(texte1.get())
        reponse = valeur1
        champ_label2.configure(text = "la réponse est : " + str(reponse))
    if longeur1 == 2 :
        valeur1 = int(texte1.get())
        valeur2 = int(texte2.get())
        reponse = valeur1 - valeur2 
        champ_label2.configure(text = "la réponse est : " + str(reponse))
    if longeur1 == 3 :
         valeur1 = int(texte1.get())
         valeur2 = int(texte2.get())
         valeur3 = int(texte3.get())
         reponse = valeur1 - valeur2 + valeur3 
         champ_label2.configure(text = "la réponse est :" + str(reponse))
    if longeur1 ==  4 :
         valeur1 = int(texte1.get())
         valeur2 = int(texte2.get())
         valeur3 = int(texte3.get())
         valeur4 = int(texte4.get())
         reponse = valeur1 - valeur2 + valeur3 - valeur4 
         champ_label2.configure(text = "la réponse est : " + str(reponse))
    if longeur1 == 5 :
        valeur1 = int(texte1.get())
        valeur2 = int(texte2.get())
        valeur3 = int(texte3.get())
        valeur4 = int(texte4.get())
        valeur5 = int(texte5.get())
        reponse = valeur1 - valeur2 + valeur3 - valeur4 + valeur5
        champ_label2.configure(text = "la réponse est : " + str(reponse))
    if longeur1 == 6 :
        valeur1 = int(texte1.get())
        valeur2 = int(texte2.get())
        valeur3 = int(texte3.get())
        valeur4 = int(texte4.get())
        valeur5 = int(texte5.get())
        valeur6 = int(texte6.get())
        reponse = valeur1 - valeur2 + valeur3 - valeur4 + valeur5 - valeur6
        champ_label2.configure(text = "la réponse est : " + str(reponse))
    if longeur1 == 7 :
         valeur1 = int(texte1.get())
         valeur2 = int(texte2.get())
         valeur3 = int(texte3.get())
         valeur4 = int(texte4.get())
         valeur5 = int(texte5.get())
         valeur6 = int(texte6.get())
         valeur7 = int(texte7.get())
         reponse = valeur1 - valeur2 + valeur3 - valeur4 + valeur5 - valeur6 + valeur7
         champ_label2.configure(text = "la réponse est : " + str(reponse))
    if longeur1 == 8 :
        valeur1 = int(texte1.get())
        valeur2 = int(texte2.get())
        valeur3 = int(texte3.get())
        valeur4 = int(texte4.get())
        valeur5 = int(texte5.get())
        valeur6 = int(texte6.get())
        valeur7 = int(texte7.get())
        valeur8 = int(texte8.get())
        reponse = valeur1 - valeur2 + valeur3 - valeur4 + valeur5 - valeur6 + valeur7 - valeur8
        champ_label2.configure(text = "la réponse est : " + str(reponse))
    if longeur1 == 9 :
        valeur1 = int(texte1.get())
        valeur2 = int(texte2.get())
        valeur3 = int(texte3.get())
        valeur4 = int(texte4.get())
        valeur5 = int(texte5.get())
        valeur6 = int(texte6.get())
        valeur7 = int(texte7.get())
        valeur8 = int(texte8.get())
        valeur9 = int(texte9.get())
        reponse = valeur1 - valeur2 + valeur3 - valeur4 + valeur5 - valeur6 + valeur7 - valeur8 + valeur9
        champ_label2.configure(text = "la réponse est : " + str(reponse))
    if longeur1 == 10 :
        valeur1 = int(texte1.get())
        valeur2 = int(texte2.get())
        valeur3 = int(texte3.get())
        valeur4 = int(texte4.get())
        valeur5 = int(texte5.get())
        valeur6 = int(texte6.get())
        valeur7 = int(texte7.get())
        valeur8 = int(texte8.get())
        valeur9 = int(texte9.get())
        valeur10 = int(texte10.get())
        reponse = valeur1 - valeur2 + valeur3 - valeur4 + valeur5 - valeur6 + valeur7 - valeur8 + valeur9 - valeur10
        champ_label2.configure(text = "la réponse est : " + str(reponse))
    return()

def calculer2():
    """
    Permet de calculer la sommes des lignes
    """
    repligne1 = 0 
    repligne2 = 0 
    repligne3 = 0 
    valeur11 = int(texte11.get())
    valeur12 = int(texte12.get())
    valeur13 = int(texte13.get())
    valeur14 = int(texte14.get())
    valeur15 = int(texte15.get())
    valeur16 = int(texte16.get())
    valeur17 = int(texte17.get())
    valeur18 = int(texte18.get())
    valeur19 = int(texte19.get())
    repcolonne1 = valeur11 + valeur14 + valeur17
    repcolonne2 = valeur12 + valeur15 + valeur18
    repcolonne3 = valeur13 + valeur16 + valeur19
    repligne1 = valeur11 + valeur12 + valeur13
    repligne2 = valeur14 + valeur15 + valeur16
    repligne3 = valeur17 + valeur18 + valeur19
    repdiago = valeur11 + valeur12 + valeur13 + valeur14 + valeur15 + valeur16 + valeur17 + valeur18 + valeur19
    ligne1.configure(text = "" + str(repligne1))
    ligne2.configure(text = "" + str(repligne2))
    ligne3.configure(text = "" + str(repligne3))
    diagonal.configure(text = "" + str(repdiago))
    colonne1.configure(text = "" + str(repcolonne1)) 
    colonne2.configure(text = "" + str(repcolonne2))
    colonne3.configure(text = "" + str(repcolonne3))
    
    
    return()

def ausuivant1(event):
    """
    Met le focus (le curseur) sur le champ de saisie suivant
    """
    texte2.focus_set()
    return()

def ausuivant2(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte3.focus_set()
    return()

def ausuivant3(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte4.focus_set()
    return()

def ausuivant4(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte5.focus_set()
    return()

def ausuivant5(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte6.focus_set()
    return()

def ausuivant6(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte7.focus_set()
    return()

def ausuivant7(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte8.focus_set()
    return()

def ausuivant8(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte9.focus_set()
    return()

def ausuivant9(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte10.focus_set()
    return()

def ausuivant11(event):
    """
    Met le focus (le curseur) sur le champ de saisie suivant
    """
    texte12.focus_set()
    return()

def ausuivant12(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte13.focus_set()
    return()

def ausuivant13(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte14.focus_set()
    return()

def ausuivant14(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte15.focus_set()
    return()

def ausuivant15(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte16.focus_set()
    return()

def ausuivant16(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte17.focus_set()
    return()

def ausuivant17(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte18.focus_set()
    return()

def ausuivant18(event):
    """
    Met le focus (le curseur) sur le champ de saisie du nombre de jets
    """
    texte19.focus_set()
    return()

fenetre = Tk()

#structure :
champ_label1 = Label(fenetre, text="Exercice 1 : ")
champ_label1.grid(row = 0, column = 0)
champ_label1 = Label(fenetre, text="Exercice 2 : ")
champ_label1.grid(row = 7, column = 0)
champ_label2 = Label(text="la réponse est : ")
champ_label2.grid(row= 3, column = 0)
longueurtexte = Label(fenetre, text="longeur textes : ")
longueurtexte.grid(row = 4, column = 0) 
longueurentry  = Spinbox(fenetre, from_=0, to=10, width = 2)
longueurentry.grid(row = 4, column = 1)   
#texte ex 1 :
texte1 = Entry(fenetre, width=2)
texte1.bind("<Return>", ausuivant1)  
texte1.grid(row = 1,column = 2)
texte1.focus_set()
texte2 = Entry(fenetre, width=2)
texte2.bind("<Return>", ausuivant2)     
texte2.grid(row = 1,column = 3)
texte3 = Entry(fenetre, width=2)
texte3.bind("<Return>", ausuivant3)     
texte3.grid(row = 1,column = 4)
texte4 = Entry(fenetre, width=2)
texte4.bind("<Return>", ausuivant4)     
texte4.grid(row = 1,column = 5)
texte5 = Entry(fenetre, width=2)
texte5.bind("<Return>", ausuivant5)  
texte5.grid(row = 1,column = 6)   
texte6 = Entry(fenetre, width=2)
texte6.bind("<Return>", ausuivant6)     
texte6.grid(row = 1,column = 7)
texte7 = Entry(fenetre, width=2)
texte7.bind("<Return>", ausuivant7)     
texte7.grid(row = 1,column = 8)
texte8 = Entry(fenetre, width=2)
texte8.bind("<Return>", ausuivant8)     
texte8.grid(row = 1,column =9)
texte9 = Entry(fenetre, width=2)
texte9.bind("<Return>", ausuivant9)     
texte9.grid(row = 1,column = 10)
texte10 = Entry(fenetre, width=2)
texte10.bind("<Return>")     
texte10.grid(row = 1,column = 11)
#texte ex 2 :
texte11 = Entry(fenetre, width=2)
texte11.bind("<Return>", ausuivant11)  
texte11.grid(row = 8,column = 1)
texte11.focus_set()
texte12 = Entry(fenetre, width=2)
texte12.bind("<Return>", ausuivant12)     
texte12.grid(row = 8,column = 2)
texte13 = Entry(fenetre, width=2)
texte13.bind("<Return>", ausuivant13)     
texte13.grid(row = 8,column = 3)
texte14 = Entry(fenetre, width=2)
texte14.bind("<Return>", ausuivant14)     
texte14.grid(row = 9,column = 1)
texte15 = Entry(fenetre, width=2)
texte15.bind("<Return>", ausuivant15)  
texte15.grid(row = 9,column = 2)   
texte16 = Entry(fenetre, width=2)
texte16.bind("<Return>", ausuivant16)     
texte16.grid(row = 9,column = 3)
texte17 = Entry(fenetre, width=2)
texte17.bind("<Return>", ausuivant17)     
texte17.grid(row = 10,column = 1)
texte18 = Entry(fenetre, width=2)
texte18.bind("<Return>", ausuivant18)     
texte18.grid(row = 10,column =2)
texte19 = Entry(fenetre, width=2)
texte19.bind("<Return>")        
texte19.grid(row = 10,column = 3)
#ligne :
colonne1 = Label(fenetre, text="c")
colonne1.grid(row = 11, column = 1)
colonne2 = Label(fenetre, text="c")
colonne2.grid(row = 11, column = 2)
colonne3 = Label(fenetre, text="c")
colonne3.grid(row = 11, column = 3)     
#colone :
ligne1 = Label(fenetre, text="l")
ligne1.grid(row = 8, column = 4)
ligne2 = Label(fenetre, text="l")
ligne2.grid(row = 9, column = 4)
ligne3 = Label(fenetre, text="l")
ligne3.grid(row = 10, column = 4)
#diagonal :
diagonal = Label(fenetre, text="d")
diagonal.grid(row = 11, column = 4)
#bouton :
calculer = Button(fenetre, text= "Calculer", command=calculer) 
calculer.grid(row = 6, column = 0)
calculer = Button(fenetre, text= "Calculer", command=calculer2) 
calculer.grid(row = 12, column = 0)
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.grid(row = 100,column = 0)

fenetre.mainloop()