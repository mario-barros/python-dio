descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

preco = float(input())
cupom = input().strip()

if preco and cupom:
    if cupom == "DESCONTO10":
        preco_desconto = preco - (preco * 0.10)

        print(f"{preco_desconto:.2f}")

    elif cupom == "DESCONTO20":
        preco_desconto = preco - (preco * 0.20)

        print(f"{preco_desconto:.2f}")

    elif cupom == "SEM_DESCONTO":
        print(f"{preco:.2f}")
else:
    print("Erro! Informe o preço e o cupom.")