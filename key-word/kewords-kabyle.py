#-------------------------------------------------------------------------------
# Name:        Test Mining & Indexation
# Purpose:     Analyse de textes et extraction de mots clés
#
# Author:      Muhend Belqasem - belkacem77@gmail.com
#
# Created:     05/01/2018
# Copyright:   (c) Muhend belqasem 2018
# Licence:     <Tisiragt ttunefkent i wid ara d-yesnernin alguritm-a s deg annar n tussna -
#alguritm-a ur yettwaseqdac ara i usuffeɣ n tizrawin di tisdawiyin neɣ anida-nniḍen,
#alguritm-a ur yettwaseqdac ara deg idlisen neɣ yal afari-s nniḍen ama batel neɣ s tedrimt -
#alguritm(a ad yettwaseqdec kan i timerna-yines ar iseɣẓanen n batel yellan di Internet
#ugar n telɣut, nermes ameskar-is ar belkacem77@gmail.com>
#-------------------------------------------------------------------------------

import rake
import operator
rake_object = rake.Rake("C:/tal/stopwords.txt")
text=""
for line in open("C:/tal/amagrad.txt"):
        line=line
        text=text+' '+line
text=text.decode('utf8')
keywords = rake_object.run(text)
print "Tisura: \n"
for keyword in keywords:
    print 'tasarutt: ', keyword[0],' ->',  str(keyword[1])
