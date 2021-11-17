# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:18:58 2021

@author: Eier
"""


class Spørsmål:
    def __init__(self, spørsmål, alternativ, korrekt_svar):
        self.spørsmål=spørsmål
        self.alternativ=alternativ
        self.korrekt_svar=korrekt_svar
        
    def __str__(self):
        res=self.spørsmål + "\n"
        for i, alt in enumerate(self.alternativ):
            res += f"{i+1}: {alt} \n"
        return res
    def sjekk_svar(self):
        svar=int(input("Skriv ditt svar som et tall: "))
        if svar== self.korrekt_svar:
            return "Ditt svar er korrekt!"
        elif svar>3:t
            return "Skriv inn et tall mellom 1 og 3."
        else:
            return "Feil svar."
spm1=Spørsmål("Er denne koden riktig?", ["Nei", "Kanskje", "Ja"], 3)
print(spm1)
print(spm1.sjekk_svar())
spm2=Spørsmål("Hvordan er vestlandsværet?", ["Regnfylt", "Varmt", "Tørt"], 1)
print(spm2)
print(spm2.sjekk_svar())



#Forenklet svar på oppgaven
#print("Er denne koden skrevet riktig?")
#print("1.Ja")
#print("2.Nei")
#print("3.Kanskje")
#b=input("Skriv ditt svar som tallet foran ønsket svar: ")
#a=int(b)
#if a==3 :
#    print("Svaret ditt er korrekt.")
#else:
#    print("Svaret ditt er feil.")