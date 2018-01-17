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
for line in open("C:/tal/corpus-aoriste3.txt"):
    #Aoriste 1 ière personne
        i = line.split()
        i= i[0]
        a=""
        #print i

        if i.startswith('i') or i.startswith('ya') or i.startswith('yi'):
             a=i[1:len(i)].decode('utf8')



            #print i.decode('utf8')
        else:
            if i.startswith('ye'):
                a=i[2:len(i)].decode('utf8')
            #print a, 'ici'
            if (len (a)<=2)  :
                a='e'+a[len(a)-2:len(a)] # si plus de deux consonnes




        print i.decode('utf8'), '->', a
        a=""
