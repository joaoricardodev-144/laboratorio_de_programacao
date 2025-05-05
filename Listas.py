listaDeCompras = ["cereja", "maçã", "banana", "abacaxi", "uva", "laranja"] # lista de frutas

listaDeCompras.insert(1, "kiwi") # Irá inserir o "kiwi" na segunda posição

print("o terceiro elemento é:", listaDeCompras[2]) # Irá exibir qual é o terceiro elemento da lista

listaDeCompras.remove("banana") # Irá remover o elemento "banana"

listaDeCompras.remove(listaDeCompras[-1]) # Irá remover o último elemento da lista

listaDeCompras.insert(0, "abacate") # Irá inserir o elemento "abacate" na última posição

for itens in listaDeCompras:
    print(itens)
listaDeCompras.sort()
print(listaDeCompras)
    
