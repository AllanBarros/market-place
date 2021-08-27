# market-place
Backend simples para market place.


### Instruções

Para rodar o projeto é necessário ter o Python3 instalado e rodar o comando

- pip install -r requirements.txt

Após isso iniciar o servidor de testes, indo até a pasta root do projeto

- python manage.py runserver

### Endpoints

O projeto contém alguns endpoints para uso:

- http://localhost:8000/buscar/

    Esse endpoint espera um GET que trará todos os produtos cadastrados se vazio ou:
        
        '?name=Racao'

    Para uma busca especifica.


- http://localhost:8000/adicionar/

    Espera um POST com os seguintes dados em json: 
        
        {
            "id_produto":1,
            "quantidade_produto":2
        }
    
    Informando qual o produto a ser adicionado ao carrinho e sua quantidade.

- http://localhost:8000/quantidade/

    Espera um PATCH com os seguintes dados em json: 
        
        {
            "id_produto":1,
            "id_produto_carrinho":1,
            "quantidade_produto":2
        }
    
    Informando qual o produto, sua quantidade para ser atualizado, o id da relação entre carrinho e produto. 


- http://localhost:8000/remover/

    Espera um DELETE com os seguintes dados em json: 
        
        {
            "id_produto":1,
            "id_carrinho":1,
        }
    
    Informando qual o produto e o id do carrinho é o necessário para remoção.


- http://localhost:8000/exibir/

    Espera um GET com os seguintes dados na url:

         '?id_carrinho=1' 

    Caso encontre o id passado ele trará todos os dados no carrinho.


- http://localhost:8000/comprar/

    Espera um POST com os seguintes dados em json:

        {
            "id_carrinho":1,
        }

    Caso encontre ele finalizará a compra com o conteúdo do carrinho.


### Testes

Para rodar os testes no projeto é necessário usar o comando:

- python manage.py test

Caso queria ver a cobertura de testes é só rodar o comando:

- coverage run --source='.' manage.py test

e depois aplicar:

- coverage html

Para melhor visualização no navegador.

Foram feitos testes de integração devido a baixa complexidade do projeto.
