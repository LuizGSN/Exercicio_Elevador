class Elevador:
    def __init__(self, capacidade, total_andares):
        self.capacidade = capacidade
        self.qtd_pessoas = 0
        self.total_andares = total_andares
        self.andar_atual = 0
    
    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print(f"Subiu para o andar {self.andar_atual}")
        else:
            print("Você já está no último andar")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print(f"Desceu para o andar {self.andar_atual}")
        else:
            print("Você já está no térreo")

    def entrar(self):
        if self.qtd_pessoas < self.capacidade:
            self.qtd_pessoas += 1
            print(f"Entrou uma pessoa. Total de pessoas: {self.qtd_pessoas}")
        else:
            print("Elevador lotado")

    def sair(self):
        if self.qtd_pessoas > 0:
            self.qtd_pessoas -= 1
            print(f"Saiu uma pessoa. Total de pessoas: {self.qtd_pessoas}")
        else:
            print("Elevador vazio")

elevador1 = Elevador(capacidade= 6, total_andares= 13)
print(elevador1.capacidade)
print(elevador1.qtd_pessoas)
print(elevador1.total_andares)
print(elevador1.andar_atual)
elevador1.subir()
elevador1.entrar()
elevador1.sair()
elevador1.descer()
