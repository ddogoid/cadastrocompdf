from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

produtos = []


while True:
    print('1:CADASTRAR PRODUTO')
    print('2:TOTAL DE PRODUTOS')
    print('3:LISTA COM OS PRODUTOS CADASTRADOS')
    print('4:PROCURAR PRODUTO')
    print('5:REMOVER ITEM')
    print('6:GERAR PDF')
    print('7:SAIR')

    op = int(input('Escolha uma opção: '))

    if op == 1:
        p = int(input('Quantos produtos quer cadastrar:'))
        for i in range(p):
            itens = {}
            itens['nome'] = str(input('Nome do Produto: ')).strip().upper()
            while True:
                try:
                    itens['quant'] = int(input('Quantidade de produto: '))
                    break
                except ValueError:
                    print('Digite apenas números inteiros para a quantidade')
            while True:
                try:
                    itens['valor'] = float(input('Valor unitário do produto: '))
                    break
                except ValueError:
                    print('Digite apenas números validos (ex: 1.50) para valor')
            produtos.append(itens)

    if op == 2:
        qt_total = sum(item['quant'] for item in produtos)
        qt_valor = sum(item['quant'] * item['valor'] for item in produtos)
        print(f'Quantidade total de produtos cadastrados: {qt_total}')
        print(f'Total de valor de mercadoria é:R$ {qt_valor:.2f}')

    if op == 3:
        for itens in produtos:
            print(f"Produto {itens['nome']}, Quantidade: {itens['quant']}")

    if op == 4:
        procurar = input('Informe o nome do produto que está procurando: ').strip().upper()
        encontrado = False
        for item in produtos:
            if item['nome'] == procurar:
                print(f"Produto encontrado: {item['nome']}, Quantidade: {item['quant']}, "
                      f"Valor unitário: R$ {item['valor']:.2f}")
                encontrado = True
                break
        else:
            print('PRODUTO NÃO ENCONTRADO')
    if op == 5:
        print('AQUI ESTÁ OS PRODUTOS CADASTRADOS:')
        for item in produtos: print(
            f"Produto: {item['nome']}, Quantidade: {item['quant']}, Valor: R$ {item['valor']:.2f}")
        remover = input('Nome do produto que quer remover: ').strip().upper()
        encontrado = False
        for item in produtos:
            if item['nome'] == remover:
                produtos.remove(item)
                print(f'Produto {remover} removido com sucesso.')
                encontrado = True
                break
        if not encontrado:
            print(f'Produto {remover} não encontrado.')
        print(f'Lista de produtos atualizados: {produtos}')

    if op == 6:
        def gerar_pdf(produtos):
            if not produtos:
                print("Nenhum produto cadastrado para gerar o PDF.")
                return

            try:
                nome_arquivo = "produtos_cadastrados.pdf"
                c = canvas.Canvas(nome_arquivo, pagesize=letter)
                largura, altura = letter

                c.setFont("Helvetica-Bold", 14)
                c.drawString(50, altura - 50, "Relatório de Produtos Cadastrados")
                c.setFont("Helvetica", 12)

                y = altura - 80
                for i, item in enumerate(produtos, start=1):
                    texto = (f"{i}. Produto: {item['nome']} | Quantidade: {item['quant']} "
                             f"| Valor unitário: R$ {item['valor']:.2f}")
                    c.drawString(50, y, texto)
                    y -= 20
                    if y < 50:
                        c.showPage()
                        c.setFont("Helvetica", 12)
                        y = altura - 50
                c.save()
                print(f"PDF '{nome_arquivo}' gerado com sucesso!")
            except Exception as e:
                print(f"Erro ao gerar o PDF: {e}")


        gerar_pdf(produtos)
    if op == 7:
        print('OBRIGADO, VOLTE SEMPRE')
        break

