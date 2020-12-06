import socket as sk

arquivo = open('ips', 'r')
lista_IP_val = []
lista_IP_inval = []

for IP in arquivo:
    try:
        if sk.inet_aton(IP):
            lista_IP_val.append(IP)
    except sk.error:
        lista_IP_inval.append(IP)

arquivo.close()

print('Endereços válidos:')
for IP_val in lista_IP_val:
    print(IP_val, end='')

print('\nEndereços inválidos:')
for IP_inval in lista_IP_inval:
    print(IP_inval, end='')
    
