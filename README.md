# scan_domaine
Scan domaine is a python script that will, from an input domaine, ping all the possible sub_domains and save the ones that are valid in a domaine.txt file

## Installation
```bash
python -m pip install requests
```
python 3
```bash
python3 -m pip install requests
```

## Start
import the modules
```bash
from operator import length_hint
import requests
import subprocess
```
## First function: get_sub_domain
from a github file get the sub_domain list with request.get(take the informations via the link)
```bash
def get_sub_domain(tab):
    try:
        url='https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-10000.txt'    
        req=requests.get(url, allow_redirects=True)
    except:
        print("error")
    i=0
```
then save every single sub_domain line by line(req.text.splitLines) in a list(listName.append)
```bash
    while i < 9985:
        tab.append(req.text.splitlines()[i])
        i+=1
    return (tab)
```
## Second function: get_tld
from a github file get the tld(Top-Level domain) list with request.get(take the informations via the link)
```bash
def get_tld(tab):
    try:
        url='https://raw.githubusercontent.com/datasets/top-level-domain-names/master/top-level-domain-names.csv'    
        req=requests.get(url, allow_redirects=True)
    except:
        print("error")
```
then save every single tld line by line(req.text.splitLines) in a temporary list(listName.append)
```bash
    temp=[]
    i=0
    while i < 920:
        temp.append(req.text.splitlines()[i])
        i+=1
```
extract only the tld from the line and save them in the list(listName.append)
```bash
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
```

## Third function: domain_verification
It's a boolean function that will verify the domain input validity.
```bash
def domain_verification(domain):
    tdl=""
    index=0
    tab=[]
```
Using the function get_tld saved in a list
```bash
    get_tld(tab)
```
And extracting the tld from the domain input
```bash
    while domain[index]!=".":
            index+=1
    while index < length_hint(domain):
        tdl+=domain[index]
        index+=1
```
it will compare the list with the tld extracted from the domain input (3)(2)
```bash
    if tdl in tab:
        return True
    return False
```


## Main function
After saving get_sub_domain in a list 
```bash
def main():
    tab=[]
    get_sub_domain(tab)
```
Asking the user to enter a domain, then in function of the return value of domain_verification(False or True):
Ether printing an invalid syntax message
```bash
    domain=input("Enter a domain name(ex: exemple.ex): ")
    if domain_verification(domain)==False:
        print("domain format invalid ex: exemple.com")
```
Or else opening a txt file(open("fileName.txt", "a") a: Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.),
 ```bash
    else:
        resultat=open("domain.txt", "a")
 ```
 Until reaching the end of the lenght of the file(while), concatening a sub_domain with the input domain in a variable 
 ```bash
        i=0
        while i < length_hint(tab):
            trial= str(tab[i]) + "." + domain
 ```
 Ping it
 ```bash
            var="ping -c 3 " + trial
            cmd= subprocess.run(var, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 ```
 Depending on the result (0 means the cmd worked otherwise there's an error) ether save the ones that worked in the file(fileName.write()) or print that the domain doesn't work
 ```bash
            if cmd.returncode==0:
                resultat.write(trial)
                resultat.write('\n')
            else:
                print("non existant domain")
            i+=1
        resultat.close()
    
main()
```
