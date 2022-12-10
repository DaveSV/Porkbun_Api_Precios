

import json
  
# Opening JSON file
f = open('porkbun_domain_pricing.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
valor = ""
  
# Iterating through the json
# list

for d in data['pricing']['xp']['registration']:
    valor = valor + d


print(valor)


print(data['pricing']['xp']['registration'])

for x in data['pricing']:

    ext = x
    result = "data['pricing']['" + ext + "']['registration']"
    print("Extensión '",ext, "' \nRegistro:", data['pricing'][ext]['registration'])
    print("Renovación:", data['pricing'][ext]['renewal'])
    print("Transferencia:", data['pricing'][ext]['transfer'],"\n")
  
# Closing file
f.close()