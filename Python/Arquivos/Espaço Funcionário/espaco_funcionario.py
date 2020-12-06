import Func_convert as fc

print('ACME Inc.     Uso do espaço em disco pelos usuários',
      f'\n{"-"*51}')
arquivo = open('nome_espaco_funcionario', 'r')

lista_dados = []
lista_nomes = []
lista_espaco = []

for linha in arquivo:
    lista_dados.append(linha.split(','))

for item in lista_dados:
    lista_nomes.append(item[0])
    item_convertido = int(item[1].strip('\n'))
    lista_espaco.append(item_convertido)

for posicao, espaco in enumerate(lista_espaco):
    espaco_convert = fc.Converter(espaco)
    lista_espaco[posicao] = espaco_convert

print(f'{"ID":<3}{"Usuário":<15}{"Espaço Utilizado":<16}{"% do uso":>10}')
for num, funcionario in enumerate(lista_nomes):
    print(f'{(num+1):<3}{funcionario:<15}',
          f'{lista_espaco[num]:>10.2f}Mb',
          f'{fc.Converter_P(lista_espaco[num]):>10.2f}%')

total = 0
count = 0
for n in range(len(lista_espaco)):
    total += lista_espaco[n]
    count += 1

media = total/count
print(f'\nEspaço total ocupado: {total:.2f}Mb',
      f'\nEspaço médio ocupado: {media:.2f}Mb')
