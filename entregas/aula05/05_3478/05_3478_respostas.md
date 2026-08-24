# Respostas - Aula Prática 5

## Questão 1: Identifique relações de herança entre as classes.
Na modelagem apresentada, podemos identificar três grupos principais de hierarquia de herança:
* **Pessoas e Profissões:** A classe base é `Pessoa` (que transmite os atributos `nome` e `idade`). A classe `Funcionário` é subclasse de Pessoa (herdando seus dados e adicionando `salario` e `carga_horaria`). Por fim, `Garçom`, `Chefe de cozinha` e `Gerente` são subclasses de `Funcionário`, herdando tudo acima e adicionando seus métodos específicos.
* **Comidas:** A classe base é `Iguaria` (com `nome` e `preco`). Suas subclasses são `Bolo` e `Pizza`, que herdam os atributos base e adicionam suas especificidades (`formato` e `borda_recheada`).
* **Estabelecimentos:** A classe base é `Restaurante` (`nome`, `endereco`, `telefone`). Sua subclasse é `Pizzaria`, que herda esses dados e adiciona a característica `rodizio`.

## Questão 2: Como você modelaria a relação entre a classe Restaurante e a classe Iguaria?
A relação entre Restaurante e Iguaria é que um restaurante possui várias Iguarias. Um restaurante possui um conjunto de iguarias que formam o seu menu/cardápio. Para implementar isso, a classe `Restaurante` precisaria de um novo atributo, por exemplo, chamado `cardapio`, que seria uma lista de objetos do tipo `Iguaria` (`cardapio: list[Iguaria]`).

## Questão 3: Indique os tipos que você atribuiria para os argumentos: argumento1, argumento2 e argumento3.
Com base na lógica de negócio do restaurante, os tipos apropriados para os argumentos seriam:
* **argumento1 (em Garçom.anotar_pedido):** Deve ser do tipo `list[Iguaria]` ou uma classe nova chamada `Pedido`, pois o garçom anota uma lista de itens que o cliente quer comer.
* **argumento2 (em Chefe de cozinha.preparar):** Deve ser do tipo `Iguaria` (ou `Pedido`), pois o chefe recebe a instrução para preparar uma comida específica.
* **argumento3 (em Gerente.demitir):** Deve ser uma instância da classe `Funcionário`, pois a ação de demitir recai sobre um funcionário da equipe.