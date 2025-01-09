from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #Obriga a passar o nome e a categoria
        self.nome = nome.title() #Transforma a primeira letra em maiúscula
        self.categoria = categoria.upper() #Transforma tudo em maiúscula
        self._status = False #Esse "_" é uma convenção para dizer que o atributo é privado
        self._avaliacao = []
        Restaurante.restaurantes.append(self) #Adiciona o objeto à lista de restaurantes assim que ela é criada
 
    def __str__(self): #Serve para exibir o objeto como string
        return f'{self.nome} | {self.categoria}'
    
    @classmethod #Serve para lembrar que é um método de classe
    def listar_restaurantes(cls):
        print(f'{'RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'AVALIAÇÃO'.ljust(20)} | {'STATUS'.ljust(20)}') #Esse é o cabeçalho
        for restaurante in cls.restaurantes:
            # print(f'{restaurante.nome.ljust(22)} | {restaurante.categoria.ljust(20)} | {restaurante._status}')
            print(f'{restaurante.nome.ljust(22)} | {restaurante.categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} |{"Ativo" if restaurante._status else "Desativado"}')

    @property
    def status(self):
        return 'Ativo' if self._status else 'Desativado'

    def alternar_status(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: #Só aceita notas entre 0 e 5
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if len(self._avaliacao) == 0:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_nota = len(self._avaliacao)
        media = round(soma / quantidade_nota, 1) #O round serve para arredondar o número
        return media
    

# restaurante_nihao = Restaurante('Ni Hao', 'Chinesa')
# restaurante_nihao.alternar_status()
# restaurante_pomodoro = Restaurante('Pomodoro', 'Italiana')

Restaurante.listar_restaurantes()




