from distutils.log import error
from itertools import count
from multiprocessing.connection import wait
from operator import length_hint
from sys import stdout
from tracemalloc import DomainFilter
from wsgiref import validate
import requests
import subprocess

def get_domaine(tab):
    try:
        url='https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-10000.txt'    
        req=requests.get(url, allow_redirects=True)
    except:
        print("error")
    i=0

    while i < 9985:
        tab.append(req.text.splitlines()[i])
        i+=1
    return (tab)



def get_tld(tab):
    try:
        url='https://raw.githubusercontent.com/datasets/top-level-domain-names/master/top-level-domain-names.csv'    
        req=requests.get(url, allow_redirects=True)
    except:
        print("error")
    
    temp=[]
    i=0
    while i < 920:
        temp.append(req.text.splitlines()[i])
        i+=1

    a=1
    while a<(length_hint(temp)):
        b=0
        c=str(temp[a])
        d=""
        while c[b] != ",":
            d+=c[b]
            b+=1
        #print(d)
        tab.append(d)
        a+=1

    return(tab)


def verification_domaine(domaine):
    tdl=""
    indice=0
    tab=[]
    get_tld(tab)
    while domaine[indice]!=".":
            indice+=1
    while indice < length_hint(domaine):
        tdl+=domaine[indice]
        indice+=1

    if tdl in tab:
        return True
    return False


def main():
    tab=[]
    get_domaine(tab)
    domaine=input("Entrez un nom de domaine: ")
    if verification_domaine(domaine)==False:
        print("format de domaine non valable ex: exemple.fr")
    else:
        resultat=open("domaine.txt", "a")
        i=0
        while i < length_hint(tab):
            trial= str(tab[i]) + "." + domaine
            var="ping -c 3 " + trial
            cmd= subprocess.run(var, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if cmd.returncode==0:
                resultat.write(trial)
                resultat.write('\n')
                print(var)
            else:
                print("domaine non existant")
            i+=1
        resultat.close()
    
main()

 