#Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos, como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

#Leitura de arquivos
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#Escrita de arquivos
arquivo = open("dados.txt", "w")
arquivo.write("Olá Mundo!")
arquivo.close()

#Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)