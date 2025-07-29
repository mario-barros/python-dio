# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
nomes_temas = []

for _ in range(n):
    # Recebe o nome do participante e o tema
    linha = input().strip()

    # Procura a primeira ocorrencia de virgula
    virgula = linha.rfind(",")

    # Faz o fatiamento para armazenar o nome e o tema
    nome = linha[:virgula]
    tema = linha[virgula + 2:]
    
    # Cria os temas na variavel eventos
    if tema in eventos:
        pass
    else:
        eventos[tema] = []

    # Armazena o nome e o tema em uma lista
    nomes_temas.append((nome, tema))

for nome_tema in nomes_temas:
    if nome_tema[1] in eventos:
        eventos[nome_tema[1]].append(nome_tema[0])

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
