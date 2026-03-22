cardapio = {
    'salgados: ':{         
        1: {'nome': 'pastel 5 - sabor 1', 'preco': 5.0},
        2: {'nome': 'pastel 5 - sabor 2', 'preco': 5.0},
        3: {'nome': 'pastel 5 - sabor 3', 'preco': 5.0},
        4: {'nome': 'pastel 8 - sabor 1', 'preco': 8.0},
        5: {'nome': 'pastel 8 - sabor 2', 'preco': 8.0}
    },

    'Doces: ':{
        1: {'nome': 'doce 1', 'preco': 1.0},
        2: {'nome': 'doce 2', 'preco': 1.0},
        3: {'nome': 'doce 3', 'preco': 3.0},
        4: {'nome': 'doce 4', 'preco': 3.5}
    },
        
    'Bebidas: ':{
        1: {'nome': 'suco - sabor 1', 'preco': 5.0},
        2: {'nome': 'suco - sabor 2', 'preco': 5.0},
        3: {'nome': 'refri 1', 'preco': 4.0},
        4: {'nome': 'a.coco', 'preco': 4.0}
    }
}

pedido = []
total = 0

while True:

    print('\n--- CATEGORIAS ---')

    categorias = list(cardapio.keys())

    for i, categoria in enumerate(categorias, 1):
        print(f'{i} - {categoria}')

    print('0 - Finalizar pedido')

    try:
        escolha_categoria = int(input('escolha uma categoria: '))
    except:
        print('Digite apenas números!')
        continue

    if escolha_categoria == 0:
        break

    if escolha_categoria < 1 or escolha_categoria > len(categorias):
        print('Categoria inválida!')
        continue

    categoria = categorias[escolha_categoria - 1]
    produtos = cardapio[categoria]

    print(f'\n--- {categoria} ---')

    for codigo, item in produtos.items():
        print(f'{codigo} - {item["nome"]} - R${item["preco"]}')

    escolha_produto = int(input('Escolha o produto: '))

    if escolha_produto in produtos:

        quantidade = int(input('Quantidade: '))

        item = produtos[escolha_produto]
        subtotal = item['preco']*quantidade

        pedido.append({
            'nome': item['nome'],
            'quantidade': quantidade,
            'subtotal': subtotal
        })

        total +=subtotal

        print('Item adcionado ao pedido!')

    else:
        print('Opção invalida!')

print('\n--- RESUMO O PEDIDO---')

for item in pedido:
    print(f'{item['nome']} x{item['quantidade']} - R${item['subtotal']:.2f}')

print(f'\nTotal: R${total:.2f}')
print('Agradecemos a preferencia!')