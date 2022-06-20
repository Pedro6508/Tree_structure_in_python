Esse projeto consiste na criação de uma estrutura do tipo arvore
usando python. Seguem aqui informações importantes:

1 - setting: 
    1.1 - Na linha com o comentário "Name the first node", vá 
    até a string "Name the first node here" e a altere para 
    colocar o id desejado nesse primeiro nó. 

    1.2 - A partir da linha com o comentário "User space below"
    é possível que o usuário  digite seu código livremente sem
    afetar a estrutura pré-pronta.

2 - Como usar:
    2.1 - Por padrão todos os elementos da arvore ficam
    guardados em uma lista chamada majorList, mas nada impede 
    que o usuário acesse os nós de outra forma.

    2.2 - Por padrão o primeiro elemento da arvore já está na
    majorList e para definir alguém como Raiz da estrutura é 
    preciso defini-lo como majorList[0].
        2.2.EX: {
            source = majorList[0] 
        }

    2.3 - Atualmente só existe uma forma de adcionar nós a
    arvore, que é usando o metodo addSon do nó pai e passando
    o argumento id para ele.
        2.3.EX: {
            Dad = majorList[0] # Dad se torna o elemento Raiz

            Filho = Dad.addSon( "son" )

            # A partir de agora o objeto Filho, que possui o 
            # id "son", é filho do objeto Dad.
        }
    
    2.4 - Os metodos e atributos que iniciam com "__" são
    privativos ao funcionamento da estrutura e não devem ser
    usados pelos usuarios.

3 - Detalhes: 
    - Como funciona a estrutura de armazenamento de irmãos 
    de um nó específico:
        - Todo elemento possui uma lista com seus filhos e 
        outra com seus irmãos, mas isso gera um problema:
            - Para cada filho novo de um pai surgira uma 
            nova lista de irmãos desse filho que possuirá 
            tamanho N - 1, sendo N o número de filhos do 
            pai. Logo, chegamos a conclusão que para N
            filhos de um pai haverá um armazenamento 
            ocupado de N*( N - 1 ) posições, que é um
            valor exponencial.
        - Para solucionar esse problema foi implementado um
        metodo de lista dinâmica: 
            - Analisando um pouco é fácil perceber que a 
            lista de irmãos de um certo elemento é a lista
            de filhos do pai desse elemento menos ele mesmo. 
            Usando esse lógica foi construida a seguinte 
            estrutura:{
                Todo elemento possui, dentro do seu objeto chields
                uma lista auxiliar, que é chamada de stack e a lista princiapal que é chamada de list;

                Quando um dos filhos do objeto chama sua lista de irmãos oque é chamado na verdade é um metodo que:{ 
                    Definições:{
                        objeto filho: aquele que requisitou a lista de irmãos
                        objeto pai: o pai do objeto filho
                        list: lista de filhos do objeto pai
                        stack: lista auxilar do objeto pai
                    }

                    Esse metodo acessa a list retira dela o objeto filho e o insere na stack, juntamente com o seu antigo index em list. Depois list é retornada ao objeto filho.

                    Caso já exista algum objeto na stack:{ 
                        O elemento no topo da stack é acessado, obtendo tanto o objeto filho que foi colocado lá quanto seu antigo index em list, e objeto filho é inserido em list 
                        na posição index guardada na stack. 
                        Depois a stack é esvaziada e o algoritmo do methodo segue, agora com list completa.
                    }
                }

                Caso o elemento pai chame sua lista de filhos, algo análogo ocorre:{
                    Definições:{
                        objeto: aquele que requisitou a lista de irmãos
                        objeto filho: um filho de objeto
                        list: lista de filhos do objeto
                        stack: lista auxilar do objeto
                    }

                    list é retornada ao objeto. 

                    Caso já exista algum objeto na stack:{ 
                        O elemento no topo da stack é acessado, obtendo tanto o objeto filho que foi colocado lá quanto seu antigo index em list, e objeto filho é inserido em list na posição index guardad na stack. 
                        Depois a stack é esvaziada e list é retornada a quem a chamou.
                    }
                }
                

            }
    
    



