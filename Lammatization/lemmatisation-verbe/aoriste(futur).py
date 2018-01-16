#-------------------------------------------------------------------------------
# Name:        lemmatize aoriste futur
# Purpose:     Lemmatization for Kabyle
#
# Author:      Muḥend Belqasem
#
# Created:     15/01/2018
# Copyright:   (c) Belkacem Mohammed 2018
# Licence:     <MIT>
#-------------------------------------------------------------------------------
def sekyed_asekkil (asekkil,tighra):
    #yella=False
    for i in tighra:
        if asekkil==i:
            return True

    return False

def amasal (azrir):
    amasal=''
    for i in azrir:
        if i =='e':
            amasal=amasal+'e'
        else:
            amasal = amasal+'c'
    return amasal


voyelles=['a','e','i','u']
imasalen=[{'cecec',0}]# ajouter ici les formes issues des différentes flexions après avoir former le radical sans suppression de la lettre e issue de la flexion verbiale
for line in open("C:/tal/corpus-aoriste.txt"):
    #Aoriste 1 ière personne
        i = line.split()
        i= i[0]
        if (i.endswith('iɣ') or i.endswith('uɣ')):
            a=i[0:len(i)-2]
            #print i.decode('utf8')
        else:
            if (i.endswith('eɣ')):
             a=i[0:len(i)-3].decode('utf8')
            #print a
             if ( a[len(a)-2] not in voyelles): # Si l'avant dernière lettre n'est pas une voyelle
                if (a[len(a)-2]<>a[len(a)-1]): #Si les deux dernière lettre ne sont pas les même
                 #print a[0:len(a)-1], a[len(a)-2], a[len(a)-1]
                 a=a[0:len(a)-1]+'e'+a[len(a)-1] # on insère alors un e
                 #print a , 'ici'
                else:
                    if (len (a)<=2):
                          a='e'+a[len(a)-2:len(a)] # si plus de deux consonnes

        # traietement des cas de déplacement de e
        if (amasal(a)=='cecec') :
            a=a[0]+a[2:len(a)]
        if (amasal(a)=='ccccecec'):
            a=a[0:4]+a[5:len(a)]
        if (amasal(a)=='cccecec'):
            a=a[0:3]+a[4:len(a)]
        print i.decode('utf8'), '->', a
        a=""
