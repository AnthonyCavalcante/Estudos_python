'''class ArquiveDocs:
    def __init__(self):
        self.folder = []
    
    def add_file(self, filename):
        self.folder.insert(0, filename)
    
    def remove_file(self):
        return self.folder.pop(0)
    
    def qtd_files(self):
        self.folder == []
    
    def print_files(self):
        print(self.folder)
        print(len(self.folder))
    



docs = ArquiveDocs()
docs.add_file('arquivo 1')
docs.add_file('arquivo 2')
docs.add_file('arquivo 3')
folder = docs.print_files()
print(docs.remove_file())
print('nova lista')
docs.print_files()
if len(docs.folder) == 2:
    print('deu certo')
'''
'''class car:
    def __init__(self, marca, cor, modelo):
        self.marca = marca
        self.cor = cor 
        self.modelo = modelo
    
    def ignite_on(self):
        print('carro ligado')
    
    def ignite_off(self):
        print('carro desligado')
        

carro1= car('chevrolet', 'preto', 'corsa')

print(carro1.modelo)
ligar= carro1.ignite_off()
ligar
ignicao = input('ligar carro?\n')
if ignicao == 'sim':
    ligar = carro1.ignite_on()
else:
    ligar = carro1.ignite_off()

ligar'''
