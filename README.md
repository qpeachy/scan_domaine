# scan_domaine

function get_domaine(tab): GET the domain list from a github repository(modul requests) then save the result domain by domain into str in a list
function get_tld(tab): GET the tld list from a git hub repository(modul request) then save the tld only(.exemple)(line by line then word by word) in a list into str
function verification_domaine(domaine): verificate if the domain synthax input by the user is comfrom
function main(): tell th user to enter a domain, this domain is then verified then we add get_domain list to the domain and ping it, save the ping domain(==0) to a domain.txt file
