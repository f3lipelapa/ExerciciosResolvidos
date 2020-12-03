import exerc_6_part1 as c6
from time import sleep

while True:
    try:
        canal_desejado = int(input('CANAL: '))
    except (ValueError):
        print('Digite o canal novamente.')
    else:
        if 1 <= canal_desejado <= 184:
            break
        else:
            print('Digite o canal novamente.')
while True:
    try:
        volume_desejado = int(input('VOLUME: '))
    except (ValueError):
        print('Digite o volume novamente.')
    else:
        if 0 <= volume_desejado <= 100:
            break
        else:
            print('Digite o volume novamente.')

tele = c6.TV(canal_desejado, volume_desejado)
tele.Mostrar()

while True:
    print(
        'Deseja mudar o canal ou aumentar/diminuir o volume?',
        '\n1 - Trocar volume',
        '\n2 - Trocar de canal',
        '\n3 - Não quero aumentar/diminuir'
    )
    try:
        escolha = int(input('Escolha: '))
    except (ValueError):
        print('Digite sua escolha novamente.')
    else:
        if escolha < 1 or escolha > 3:
            print('Digite sua escolha novamente.')
        if escolha == 1:
            while True:
                try:
                    novo_volume = int(input('VOLUME: '))
                except (ValueError):
                    print('Digite o volume novamente.')
                else:
                    if 0 <= novo_volume <= 100:
                        tele.TrocarVolume(novo_volume)
                        tele.Mostrar()
                        break
                    if novo_volume < 0 or novo_volume > 100:
                        print('Digite o volume novamente.')
        if escolha == 2:
            while True:
                try:
                    novo_canal = int(input('CANAL: '))
                except (ValueError):
                    print('Digite o canal novamente.')
                else:
                    if 1 <= novo_canal <= 184:
                        tele.TrocarCanal(novo_canal)
                        tele.Mostrar()
                        break
                    else:
                        print('Digite o canal novamente.')
        if escolha == 3:
            print('Obrigado por assistir!')
            sleep(2)
            break
