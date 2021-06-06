Pilhas:
    -> LIFO - (Last in first out) - o último elemento inserido é o primeiro a ser removido 

Quando utilizar listas?
    -> As vezes, pela da natureza do problema precisamos guardar dados apenas na primeira ou na última posição, aí que entra a pilha, por ser mais eficiente para este problema 

Pilhas apaarecem em diversos contexto na computação:
    Ex: 
    -> Ao navegar na internet as pilhas são utilizadas no browser para gerenciar no fluxo de navegação permitindo que consigamos retornar à página anterior.
    -> O mesmo vale para o VScode (a medida em que codificamos ele vai empilhando e por conta disso, o último código digitado é o que sai, ao utilizar o camando - CTRL + Z) 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Minimamente devemos saber: 
    Inserir: 
        -> Para inserirmos algo na pilha devemos saber o que vai ser inserido.

    Remover: 
        -> Para remover algo da pilha não precisamos de um id ou passar um elemento a ser removido, pois necessariamente sempre irá ser o último

    Saber o topo da pilha:
        -> Iremos utilizar o __repr__ que serve para representar um objeto como uma string