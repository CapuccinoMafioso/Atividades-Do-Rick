class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, data):
        novo_no = Node(data)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.next = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        else:
            temp = self.inicio
            self.inicio = self.inicio.next
            if self.inicio is None:
                self.fim = None
            return temp.data

    def esta_vazia(self):
        return self.inicio is None

    def olhar(self):
        if self.esta_vazia():
            return None
        else:
            return self.inicio.data

    def exibir_fila(self):
        if self.esta_vazia():
            print("A fila está vazia")
        else:
            atual = self.inicio
            while atual:
                print(atual.data, end=" ")
                atual = atual.next
            print()

fila = Fila()
#
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
#


print("Fila após enfileiramento inicial:")
fila.exibir_fila()
fila.enfileirar(4)
fila.enfileirar(5)
fila.enfileirar(6)
#


print("Fila após novos enfileiramentos:")
fila.exibir_fila()
#


fila.desenfileirar()
fila.desenfileirar()
#


print("Fila após desenfileiramentos:")
fila.exibir_fila()
#


print("Primeiro elemento da fila:", fila.olhar())

if fila.esta_vazia():
    print("A fila está vazia")
else:
    print("A fila não está vazia")

# Código feito por Rick José
