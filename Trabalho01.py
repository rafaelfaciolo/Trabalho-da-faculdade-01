#----------TRABALHO--------------
print('Programa de controle de atendimento de um salão de beleza, feito por Rafael Faciolo')
total = 0
contador = 0
while True:
    atendimento = input('Qual procedimento será realizado?\n'
                      '0001 - Unhas Mão \n'
                      '0002 - Cabelo \n'
                      '0003 - Sobrancelha \n'
                      '>>')

    if atendimento == '0001':
        valor = 50
    elif atendimento == '0002':
        valor = 75
    elif atendimento == '0003':
        valor = 55
    else:
        print('OPÇÃO INVÁLIDA!')
        continue
    print("Total do atendimento até o momento: R${:.2f}".format(total+valor))
    contador = contador + 1
    total = total + valor
    resposta = input('Deseja inserir mais algum procedimento?\n'
                     'Digite (Y) para continuar ou (N) para finalizar\n'
                     '>>')
    if resposta.upper() == 'Y':
        continue
    else:
        pgto = input('Qual será a forma de pagamento? \n'
                         '1 - Cartão \n'
                         '2 - Dinheiro \n'
                         '3 - Pix \n'
                         '4 - Fiado \n'
                         '>>')
        if pgto == '1':
                    taxa = 5 / 100
        elif pgto == '2':
                    taxa = 0
        elif pgto == '3':
                    taxa = 0
        elif pgto == '4':
                    taxa = 10/100
        else:
            print('Forma de pagamento inválida.')
            continue
    taxa = total * taxa
    totalfinal = total + taxa
    print("Descrição do atendimento:\n"
                "Quantidade de procedimentos realizados: {}\n"
                "Forma de pagamento: {}\n"
                "Taxa: R$ {:.2f}\n"
                "Total final: R${:.2f}".format(contador, pgto, taxa,totalfinal))
    break
