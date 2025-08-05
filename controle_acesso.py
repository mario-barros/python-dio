# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",

}

# Entrada do usuário
usuario = input("Digite o nome: ").strip()
senha = input("Digite a senha: ").strip()

# TODO: Verifique se o usuário existe e a senha está correta:
verifica_senha = usuarios.get(usuario)

if usuario in usuarios and verifica_senha == senha:
    print("Acesso permitido")
else:
    print("Usuário ou senha incorretos")
