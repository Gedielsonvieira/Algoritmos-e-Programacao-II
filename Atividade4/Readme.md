Quando se cria uma variável "privada" em Python o que acontece é: dentro da classe você pode referenciar por __variavel mas fora da classe o Python "esconde" este acesso para lembrar ao desenvolvedor que ele não deveria mexer diretamente naquela variável(pois ela é privada), mas não o impede(como em outras linguagens, como Java). Não impede pois o ato de esconder é simplesmente renomear a variável para _Classe__variavel.

Por este motivo você pode acessar variaveis privadas em Python através da sintaxe _NomeDaClasse__nomeDaVariavel.


#self é sempre o objeto que estiver utilizando o método
#set é para modificar o valor de um atributo
#get é para pegar alguma informação
