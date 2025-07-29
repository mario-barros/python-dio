#email = input().strip()
email = "mariobarrosoutlook.com"

verify = 0

verify_list = []

for e in email:
    verify_list += e

check1 = " " in verify_list
check2 = verify_list[0] == "@" or verify_list[-1] == "@"


if "@" in email:
    verify += 1

    if "gmail.com" in email or "outlook.com":
        verify += 1

        if check1 == False:
            verify += 1

            if check2 == False:
                verify += 1


if verify == 4:
    print("E-mail válido")

else:
    print("E-mail inválido")