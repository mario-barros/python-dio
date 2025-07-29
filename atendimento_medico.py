# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def ordena_fila(pessoas):
    urgente = []
    idosos = []
    demais = []

    for nome, idade, status in pessoas:
        if status.lower() == "urgente":
            urgente.append((nome, idade, status))
        elif idade >= 60:
            idosos.append((nome, idade, status))
        else:
            demais.append((nome, idade, status))
    
    urgente.sort(key=lambda pessoa: pessoa[1], reverse=True)
    idosos.sort(key=lambda pessoa: pessoa[1], reverse=True)
    
    return urgente + idosos + demais

fila_ordenada = []

for nome, idade, status in ordena_fila(pacientes):
    fila_ordenada.append(nome)

fila_apresentada = ", ".join(fila_ordenada)

# TODO: Exiba a ordem de atendimento com título e vírgulas:
print(f"Ordem de Atendimento: {fila_apresentada}")