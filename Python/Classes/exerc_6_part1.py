class TV:

    def __init__(self, canal, volume):

        self.canal = canal
        self.volume = volume

    def TrocarVolume(self, novo_volume):

        self.volume = novo_volume

    def TrocarCanal(self, novo):

        self.canal = novo

    def Mostrar(self):

        print('+-----------------------+')
        for i in range(3):
            print(f'{"|"}{"|":>24}')
        if self.canal <= 9:
            print(f'|CANAL: {self.canal}{"|":>16}')
        if 10 <= self.canal <= 99:
            print(f'|CANAL: {self.canal}{"|":>15}')
        if self.canal >= 100:
            print(f'|CANAL: {self.canal}{"|":>14}')
        if self.volume <= 9:
            print(f'|VOLUME: {self.volume}{"|":>15}')
        if 10 <= self.volume <= 99:
            print(f'|VOLUME: {self.volume}{"|":>14}')
        if self.volume == 100:
            print(f'|VOLUME: {self.volume}{"|":>13}')
        print('+-----------------------+')
        print('|======-o-o-o-o-o-======|')
        print('+-----------------------+')
