
def carregar_dados(arquivo):
    dados = []
    try:
        with open(arquivo, mode='r') as file:
            for line in file:
                dados.append(line.strip().split(';'))
    except FileNotFoundError:
        pass
    return dados


def salvar_dados(arquivo, dados):
    with open(arquivo, mode='w') as file:
        for item in dados:
            file.write(';'.join(item) + '\n')


def main():
    usuarios = carregar_dados('usuarios.txt')
    produtos = carregar_dados('produtos.txt')

    while True:
        print("\nMenu:")
        print("1. Usuários")
        print("2. Produtos")
        print("3. Sair")
        escolha = input("Escolha: ")

        if escolha == '1':
            print("\nUsuários:")
            print("1. Adicionar")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Remover")
            escolha_usuario = input("Escolha: ")

            if escolha_usuario == '1':
                nome = input("Nome: ")
                nivel = input("Nível (admin/user): ")
                senha = input("Senha: ")
                usuarios.append([nome, nivel, senha])
                salvar_dados('usuarios.txt', usuarios)
                print("Usuário adicionado.")
            elif escolha_usuario == '2':
                for usuario in usuarios:
                    print(f'Nome: {usuario[0]}, Nível: {usuario[1]}')
            elif escolha_usuario == '3':
                nome = input("Nome: ")
                for usuario in usuarios:
                    if usuario[0] == nome:
                        novo_nome = input("Novo Nome (deixe vazio se não alterar): ")
                        nivel = input("Novo Nível (admin/user) (deixe vazio se não alterar): ")
                        senha = input("Nova Senha (deixe vazio se não alterar): ")
                        if novo_nome: usuario[0] = novo_nome
                        if nivel: usuario[1] = nivel
                        if senha: usuario[2] = senha
                        salvar_dados('usuarios.txt', usuarios)
                        print("Usuário atualizado.")
                        break
            elif escolha_usuario == '4':
                nome = input("Nome: ")
                usuarios = [usuario for usuario in usuarios if usuario[0] != nome]
                salvar_dados('usuarios.txt', usuarios)
                print("Usuário removido.")

        elif escolha == '2':
            print("\nProdutos:")
            print("1. Adicionar")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Remover")
            print("5. Buscar")
            print("6. Ordenar por Nome")
            print("7. Ordenar por Preço")
            escolha_produto = input("Escolha: ")

            if escolha_produto == '1':
                nome = input("Nome: ")
                preco = input("Preço: ")
                quantidade = input("Quantidade: ")
                produtos.append([nome, preco, quantidade])
                salvar_dados('produtos.txt', produtos)
                print("Produto adicionado.")
            elif escolha_produto == '2':
                for produto in produtos:
                    print(f'Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}')
            elif escolha_produto == '3':
                nome = input("Nome: ")
                for produto in produtos:
                    if produto[0] == nome:
                        novo_nome = input("Novo Nome (deixe vazio se não alterar): ")
                        preco = input("Novo Preço (deixe vazio se não alterar): ")
                        quantidade = input("Nova Quantidade (deixe vazio se não alterar): ")
                        if novo_nome: produto[0] = novo_nome
                        if preco: produto[1] = preco
                        if quantidade: produto[2] = quantidade
                        salvar_dados('produtos.txt', produtos)
                        print("Produto atualizado.")
                        break
            elif escolha_produto == '4':
                nome = input("Nome: ")
                produtos = [produto for produto in produtos if produto[0] != nome]
                salvar_dados('produtos.txt', produtos)
                print("Produto removido.")
            elif escolha_produto == '5':
                nome = input("Nome: ")
                for produto in produtos:
                    if produto[0].lower() == nome.lower():
                        print(f'Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}')
                        break
                else:
                    print('Produto não encontrado.')
            elif escolha_produto == '6':
                produtos_ordenados = sorted(produtos, key=lambda x: x[0])
                for produto in produtos_ordenados:
                    print(f'Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}')
            elif escolha_produto == '7':
                produtos_ordenados = sorted(produtos, key=lambda x: float(x[1]))
                for produto in produtos_ordenados:
                    print(f'Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}')

        elif escolha == '3':
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
