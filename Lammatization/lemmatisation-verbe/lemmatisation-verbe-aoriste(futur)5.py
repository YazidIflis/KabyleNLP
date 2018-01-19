#-------------------------------------------------------------------------------
# Name:        lemmatize aoriste futur (dexième pluriel masculin et féminin)
# Purpose:     Lemmatization for Kabyle
#
# Author:      Muḥend Belqasem
#
# Created:     15/01/2018
# Copyright:   (c) Belkacem Mohammed 2018
# Licence:     <MIT>
#-------------------------------------------------------------------------------
def sekyed_asekkil (asekkil,tighra):
    yella=False
    for i in tighra:
        if asekkil==i:
            yella= True

    return yella

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
for line in open("C:/tal/corpus-aoriste5.txt"):
    #Aoriste 1 ière personne
        i = line.split()
        i= i[0]
        a=''
        if (i.endswith('emt') or  i.endswith('ent')):
             a=i[0:len(i)-3].decode('utf8')
        else:
                if (i.endswith('mt') or  i.endswith('nt')):
                   a=i[0:len(i)-2].decode('utf8')
                else:
                    if (i.endswith('et') or  i.endswith('en')):
                       a=i[0:len(i)-2].decode('utf8')
                       #print a,'ici'
                    else:
                        if (i.endswith('t') or  i.endswith('n')):
                         a=i[0:len(i)-1].decode('utf8')



        #print a
        if(len(a) >=3):
            if not sekyed_asekkil(a[len(a)-2:len(a)-1], voyelles) and not sekyed_asekkil(a[len(a)-1:len(a)], voyelles):

                if(a[len(a)-3:len(a)-2]<>'e') and a[len(a)-2:len(a)-1] != a[len(a)-1:len(a)]:

                    a=a[0:len(a)-1]+'e'+a[len(a)-1:len(a)]
                    #print a


        if (len (a)==2 ) and (a[0] not in voyelles and a[1] not in voyelles):

                          if(a[0] not in['ɣ'.decode('utf8'),'m','z','s','g','d','ẓ'.decode('utf8')]):
                           a='e'+a[len(a)-2:len(a)]

                          else:
                            a=a[0]+'e'+a[1]
                            #print a


        # traietement des cas de déplacement de e
        if (amasal(a)=='cecec') :
            a=a[0]+a[2:len(a)]
        if (amasal(a)=='ccccecec'):
            a=a[0:4]+a[5:len(a)]
        if (amasal(a)=='cccecec'):
            a=a[0:3]+a[4:len(a)]
        if (amasal(a)=='ccecec'):
            a=a[0:1]+'e'+a[1:2]+a[len(a)-3:len(a)]
        if (amasal(a)=='ccececec'):
            a=a[0:4]+a[len(a)-3:len(a)]
        print i.decode('utf8'), '->', a
        a=""
