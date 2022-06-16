from operator import length_hint
import requests
import subprocess

def get_sub_domain(tab):
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


def domain_verification(domain):
    tdl=""
    index=0
    tab=[]
    get_tld(tab)
    while domain[index]!=".":
            index+=1
    while index < length_hint(domain):
        tdl+=domain[index]
        index+=1

    if tdl in tab:
        return True
    return False


def main():
    tab=[]
    get_sub_domain(tab)
    domain=input("Enter a domain name(ex: exemple.ex): ")
    if domain_verification(domain)==False:
        print("domain format invalid ex: exemple.com")
    else:
        resultat=open("domain.txt", "a")
        i=0
        while i < length_hint(tab):
            trial= str(tab[i]) + "." + domain
            var="ping -c 3 " + trial
            cmd= subprocess.run(var, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if cmd.returncode==0:
                resultat.write(trial)
                resultat.write('\n')
                print(var)
            else:
                print("non existant domain")
            i+=1
        resultat.close()
    
main
