#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import *
#import sys
#sys.path.insert(1, "C:\Users\kawta\OneDrive\Documents\GitHub\c04-ch6-exercices")
#from exercice2 import frequence
# TODO: Définissez vos fonction ici
def volume_masse(a=2, b=9, c=3, masse_volumique=8):
    volume = (4/3)*pi*a*b*c
    masse = masse_volumique * volume
    return volume, masse

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volume_masse())
#print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__))[-1]("ceci est une phrase"))


