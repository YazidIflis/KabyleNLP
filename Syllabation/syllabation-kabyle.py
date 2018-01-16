tirgalin=['a','e','i','u']
tighra=['ɛ'.decode('utf8'),'b','c','č'.decode('utf8'),'d','ḍ'.decode('utf8'),'f','g','ɣ'.decode('utf8'),'ǧ'.decode('utf8'),'h','ḥ'.decode('utf8'),'j','k','l','m','n','p','q','r','ṛ'.decode('utf8'),'s','ṣ'.decode('utf8'),'t','ṭ'.decode('utf8'),'v','w','x','y','z','ẓ'.decode('utf8')]
syllabe=['v','vc','vcc','cv','cvc','cvcc']

#for taghret in tighra:
#    print taghret.decode('utf8')
def sekyed (azrir):
    a=""
    for i in azrir:
        if i in tighra:
            a=a+'c'
        else:
            a=a+'v'
    return a

text= "Seg wasmi yebda umdan yesnulfuy-d tasekla, yeɛreḍ kan akken amek aratt-id yessefhem. Yebɣa ad yegzu dacu id-yesnulfuy ed wacimittid yesnulfuy ed wamek itt-id yesnulfuy."
text=text.replace('-','')
text=text.replace(',','')
text=text.replace('.',' ')
#text=text.replace(' ','')
text=text.lower()
text=text.decode('utf8')

for awal in text.split():
 while (len(awal)>0):
  if len(awal)>=4 and sekyed (awal[0:4]) in syllabe:
            print awal[0:4],"->",sekyed (awal[0:4])
            awal=awal[4:len(awal)]
  else:
    if len(awal)>=3 and sekyed (awal[0:3]) in syllabe:
                print awal[0:3],"->",sekyed (awal[0:3])
                awal=awal[3:len(awal)]
    else:
        if len(awal)>=2 and sekyed (awal[0:2]) in syllabe:
                    print awal[0:2],"->",sekyed (awal[0:2])
                    awal=awal[2:len(awal)]
        else:
            if len(awal)>=1 and sekyed (awal[0:1]) in syllabe:
                        print awal[0:1],"->",sekyed (awal[0:1])
                        awal=awal[1:len(awal)]
