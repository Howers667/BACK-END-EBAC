def exibir_menu():
    return (
        "\nMenu:\n"
        "1 - SOMA\n"
        "2 - SUBTRAÇÃO\n"
        "3 - DIVISÃO\n"
        "4 - MULTIPLICAÇÃO\n"
        "5 - Sair\n"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "5":
            print("Saindo do programa...")
            break

        try:
            numero1 = int(input("Insira um valor: "))
            numero2 = int(input("Insira um segundo valor: "))
        except ValueError:
            print("Erro: digite um número inteiro válido.")

        except ZeroDivisionError:
            ("ERRO, divisao por zero nao eh possivel!!")
            continue  

        if opcao == "1":
            resultado = (lambda x, y: x + y)(numero1, numero2)
            print("Resultado da soma:", resultado)

        elif opcao == "2":
            resultado = (lambda x, y: x - y)(numero1, numero2)
            print("Resultado da subtração:", resultado)

        elif opcao == "3":
            if numero2 == 0:
                print("Erro: divisão por zero.")
            else:
                resultado = (lambda x, y: x / y)(numero1, numero2)
                print("Resultado da divisão:", resultado)

        elif opcao == "4":
            resultado = (lambda x, y: x * y)(numero1, numero2)
            print("Resultado da multiplicação:", resultado)

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

           








