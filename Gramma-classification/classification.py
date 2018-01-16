#-------------------------------------------------------------------------------
# Name:        Tokeznization & Classification
# Purpose:     Lemmatization & Stemming
#
# Author:      Muhend Belqasem - belkacem77@gmail.com
#
# Created:     03/01/2018
# Copyright:   (c) Muhend belqasem 2018
# Licence:     <Tisiragt ttunefkent i wid ara d-yesnernin alguritm-a s deg annar n tussna -
#alguritm-a ur yettwaseqdac ara i usuffeɣ n tizrawin di tisdawiyin neɣ anida-nniḍen,
#alguritm-a ur yettwaseqdac ara deg idlisen neɣ yal afari-s nniḍen ama batel neɣ s tedrimt -
#alguritm(a ad yettwaseqdec kan i timerna-yines ar iseɣẓanen n batel yellan di Internet
#ugar n telɣut, nermes ameskar-is ar belkacem77@gmail.com>
#-------------------------------------------------------------------------------

def main():
    stop_words={'win','tin','din','akken','deg','ɣef','ten','nsen','nniḍen','nneɣ','werǧin','aṭas','akked','tid','wid','kan','acu','ala','ara','ur','ihi','ayagi','amzun','ula','wagi','d','ad','ulac','nsen','nezzeh','akken','ayen','ugar','drus','ulac','yiwen','ama'}

    verbs=[]
    nouns=[]
    others={}
    asenqedh={'.','?','!',':'}
    tizdit={'-'}
    nounprefixes1={'a','i'}
    nounprefixes2={'ta','ti'}
    nounsuffixes={'an','en','in'}
    verbsprefixes={'ttwa','tettwa','tettu','ttu'}
    for line in open("C:/tal/text2.txt"):
        line=line.decode('utf8')
        precedent=''
        line=line.lower()
        line=line.replace('.','')
        line=line.replace(',','')
        line=line.replace(';','')
        line=line.replace('?','')
        line=line.replace(':','')
        line=line.replace('!','')
        line=line.replace('-',' ')
        line=line.replace('  ',' ')

        for awal in line.split():
             awal = awal.strip()
             if (awal not in stop_words and len(awal)>2):
             #ette ligne c'est pour chercher les noms et adjectifs commençant par a, i, te et ti, et ta. ou bien les noms ayant subis un état d'annexion
                if (awal.startswith('tu') or (awal.startswith('ta') or awal.startswith('te') or awal.startswith('ti')) and precedent!='ad') or (((awal.startswith('a') or awal.startswith('i') or awal.startswith('u')  ) and (not awal.endswith('i') and not awal.endswith('u')  and not awal.endswith('a') and len (awal)<=3)) or ((awal.startswith('yi') or awal.startswith('u') or awal.startswith('a') or awal.startswith('i')) and len(awal)>3 and (awal not in stop_words) and  precedent!='ad')):
                 nouns.append(awal)
                else:
                 if (awal not in stop_words):
                  if (precedent=='ad'or precedent=='d' or precedent=='t' or precedent=='id') or (awal.startswith('tt') or awal.startswith('ye') or awal.startswith('ye') or awal.startswith('te') or awal.endswith('an') or awal.endswith('ant') or (awal.endswith('iɣ'.decode('utf8')) or awal.endswith('in'))) :
                   verbs.append (awal)
             precedent=awal

    print "\nImyagen:\n"
    for verb in verbs:
        print verb

    print "\nIsmawen d yirbiben:\n"
    for noun in nouns:
        if (noun.startswith('a') or noun.startswith('i') or noun.startswith('u')):
            print noun, ' amalay'
        else:
            print noun, ' unti'
    pass

if __name__ == '__main__':
    main()
