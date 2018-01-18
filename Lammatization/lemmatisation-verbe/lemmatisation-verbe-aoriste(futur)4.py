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
for line in open("C:/tal/corpus-aoriste4.txt"):
    #Aoriste 1 ière personne
        i = line.split()
        i= i[0]
        #print i
        a=''

        if (i.endswith('im') or  i.endswith('imt')) and ( i.startswith('ti') or i.startswith('ta') ):
            if(i.endswith('m')):
             a=i[1:len(i)-1].decode('utf8')
            else:
             a=i[1:len(i)-2].decode('utf8')
        if (i.endswith('em') or  i.endswith('emt')) and ( i.startswith('ta')):
            if(i.endswith('m')):
             a=i[1:len(i)-2].decode('utf8')
            else:
             a=i[1:len(i)-3].decode('utf8')
        if (i.endswith('em') or  i.endswith('emt')) and ( i.startswith('ti')):
            if(i.endswith('m')):
             a=i[1:len(i)-2].decode('utf8')
            else:
             a=i[1:len(i)-3].decode('utf8')
        if (i.endswith('em') or  i.endswith('emt')) and ( i.startswith('tu')):
            if(i.endswith('m')):
             a=i[1:len(i)-2].decode('utf8')
            else:
             a=i[1:len(i)-3].decode('utf8')
        if (i.endswith('em') or  i.endswith('emt')) and ( i.startswith('te')):
            if(i.endswith('m')):
             a=i[2:len(i)-2].decode('utf8')
            else:
             a=i[2:len(i)-3].decode('utf8')
        if (i.endswith('em') or  i.endswith('emt')) and ( i.startswith('t')):
            if(i.endswith('m')):
             a=i[1:len(i)-2].decode('utf8')
            else:
             a=i[1:len(i)-3].decode('utf8')
        if (len (a)==2 ) and (a[0] not in voyelles and a[0] not in voyelles):

                          #print a,'ici',len(a),a[len(a)-2:len(a)-1]
                          a='e'+a[len(a)-2:len(a)] # si plus de deux consonnes
                          #print a,'ici', a[len(a)-1]


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
            #print a
            a=a[0:4]+a[len(a)-3:len(a)]

       print i.decode('utf8'), '->', a
        a=""
