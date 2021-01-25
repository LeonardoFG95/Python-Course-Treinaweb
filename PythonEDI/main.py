from array import array
from vetores import vetor
from listas import lista_ligada, listaDuplamenteLigada
from pilhas import pilha
from filas import fila
from conjuntos import  conjunto
from mapas import mapa
from arvores import arvore, no_arvore_inteiro

#vetorInteiros = array('b', [1, 2, 3])
#print(vetorInteiros)
# 1 / 2 / 3 / 4
#vetorInteiros.insert(3, 4)
#print(vetorInteiros)
#print(vetorInteiros.index(2))

print(30 * "-", "Menu", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")
print("3. Listas Duplamente Ligadas")
print("4. Pilhas")
print("5. Filas")
print("6. Conjuntos")
print("7. Mapas")
print("8. Arvores")

menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetorTeste = vetor.Vetor(0)
    vetorTeste.inserirElementoPosicao(1, 0)
    vetorTeste.inserirElementoPosicao(2, 1)
    vetorTeste.inserirElementoPosicao(3, 2)
    vetorTeste.inserirElementoPosicao(4, 2)
    vetorTeste.inserirElementoPosicao(5, 2)
    vetorTeste.inserirElementoFinal(1)
    print(vetorTeste.tamanhoVetor())
    print(vetorTeste)
    #print(vetorTeste.contem(4))
    print(vetorTeste.indice(4))
    vetorTeste.removerElementoIndice(3)
    print(vetorTeste)
    vetorTeste.removerElemento(5)
    print(vetorTeste)
elif menu == 2:
    listaTeste = lista_ligada.ListaLigada()
    listaTeste.inserir(1)
    listaTeste.inserir(4)
    listaTeste.inserir(5)
    listaTeste.inserirPosicao(1, 10)
    print(listaTeste)
    print(listaTeste.removerElemento(10))
    print(listaTeste)
    #print(listaTeste.contem(5))
    #print(listaTeste.indice(5))
    #print(listaTeste.recuperarElementoNo(0))

elif menu == 3:
    listaTeste = listaDuplamenteLigada.ListaDuplamenteLigada()
    listaTeste.inserir(1)
    listaTeste.inserir(4)
    listaTeste.inserir(5)
    listaTeste.inserirPosicao(2, 10)
    print(listaTeste)
    #print(listaTeste.removerElemento(10))
    listaTeste.removerPosicao(1)
    print(listaTeste)
    #print(listaTeste.contem(5))
    #print(listaTeste.indice(5))
    #print(listaTeste.recuperarElementoNo(0))

elif menu == 4:
    pilhaTeste = pilha.Pilha()
    pilhaTeste.empilhar(5)
    pilhaTeste.empilhar(6)
    pilhaTeste.empilhar(7)
    print(pilhaTeste.desempilhar())

elif menu == 5:
    filaTeste = fila.Fila()
    filaTeste.enfileirar(1)
    filaTeste.enfileirar(2)
    filaTeste.enfileirar(3)
    filaTeste.enfileirar(4)
    print(filaTeste)
    print(filaTeste.desenfileirar())
    print(filaTeste)

elif menu == 6:

    conjuntoTeste = conjunto.Conjunto()
    conjuntoTeste.inserir(1)
    conjuntoTeste.inserir(2)
    conjuntoTeste.inserir(3)
    print(conjuntoTeste.inserir(3))
    #print(conjuntoTeste.inserirPosicao(1, 4))
    print(conjuntoTeste)
    print(conjuntoTeste.removerElemento(3))
    print(conjuntoTeste)
    print(conjuntoTeste.inserir(3))
    print(conjuntoTeste.inserir("Python"))
    print(conjuntoTeste.inserir("TreinaWeb"))
    print(conjuntoTeste.inserir(4))
    print(conjuntoTeste)

elif menu == 7:
    mapaTeste = mapa.Mapa()
    print(mapaTeste)
    mapaTeste.adicionar("par", 10)
    mapaTeste.adicionar("impar", 5)
    mapaTeste.adicionar("par", 2)
    print(mapaTeste)
    print(mapaTeste.contemChave("par"))
    print(mapaTeste.recuperar("par"))

elif menu == 8:
    arvoreTeste = arvore.Arvore()
    print(arvoreTeste)
    arvoreTeste.inserirElemento(no_arvore_inteiro.NoArvoreInteiro(5))
    print(arvoreTeste)
    arvoreTeste.inserirElemento(no_arvore_inteiro.NoArvoreInteiro(4))
    arvoreTeste.inserirElemento(no_arvore_inteiro.NoArvoreInteiro(6))
    arvoreTeste.inserirElemento(no_arvore_inteiro.NoArvoreInteiro(8))
    arvoreTeste.inserirElemento(no_arvore_inteiro.NoArvoreInteiro(7))
    #print(arvoreTeste)
    #print(arvoreTeste.buscar(no_arvore_inteiro.NoArvoreInteiro(7)))
    print("Em ordem.")
    print(arvoreTeste.emOrdem())
    print("Pre Ordem.")
    print(arvoreTeste.preOrdem())
    print("Pos Ordem.")
    print(arvoreTeste.posOrdem())
    print("Altura")
    print(arvoreTeste.altura())
else:
    print("Opção inválida.")

