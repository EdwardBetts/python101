#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

liczba = random.randint(1, 10)
#print "Wylosowana liczba:",liczba

for i in range(3):
    odp = raw_input("Jaką liczbę od 1 do 10 mam na myśli? ")
    #print "Podałeś liczbę: ",odp

    if liczba == int(odp):
        print "Zgadłeś! Dostajesz długopis!"
        break
    else:
        print "Nie zgadłeś. Spróbuj jeszcze raz."
        print
