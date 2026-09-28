# Entrada de dados

qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

print(" Olá, somos a empresa TudoWeb e gostaríamos de saber sua opinião sobre o nosso atendimento.")

for i in range( 1 , 11 ):
    nome_cliente = input(" \n Digite seu nome: ")
    idade_cliente = int(input(" Digite sua idade: "))
    print(" Digite uma nota de 1 a 3 para avaliar nosso atendimento: ")

    alternativa_errada = True
    while alternativa_errada == True :

        nota = input("\n[1]Excelente \n[2]Bom \n[3]Ruim \n")

        match nota:
            case "1" :
                qtd_excelente = (qtd_excelente + 1)
                alternativa_errada = False

            case "2" :
                qtd_bom = (qtd_bom + 1)
                alternativa_errada = False
            
            case "3" :
                qtd_ruim = (qtd_ruim + 1)
                alternativa_errada = False

            case _:
                print(" opcao inválida ")
                alternativa_errada = True

    
print(f" Quantidade de nota Excelente: {qtd_excelente} ")
print(f" Quantidade de nota Boa: {qtd_bom} ")
print(f" Quantidade de nota ruim: {qtd_ruim} ")

