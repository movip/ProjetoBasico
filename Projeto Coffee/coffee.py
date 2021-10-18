from coffee_object import Small_Coffee, Regular_Coffee, Big_Coffee


cafe1 = Small_Coffee()
cafe2 = Regular_Coffee()
cafe3 = Big_Coffee()




while True:
            cardapio = int(input(f"Escolha o número do seu pedido abaixo:\n1 [1] - {cafe1.nome} = R${cafe1.valor}0\n2 [2] - {cafe2.nome} = R${cafe2.valor}0\n3 [3] - {cafe3.nome} = R${cafe3.valor}0\n4 [4] - Sair do Cardápio\n5 Digite aqui: "))

            if cardapio == 1:
                valor_cliente = float(input("Qual o valor entregue para a compra?\n1 Digite aqui: "))

                if valor_cliente >= cafe1.valor:
                    troco = valor_cliente - cafe1.valor
                    print(f"Compra realizada com sucesso!\n1 Pedido selecionado: Small Coffee\n2 Valor do pedido: R${cafe1.valor}0\n3 Valor entregue: R${valor_cliente}0\n4 Troco: R${troco}0")
                    menu = int(input("Deseja realizar mais alguma compra?\n1 [1] - Sim\n2 [2] - Não\n3 Digite aqui: "))
                    if menu == 1:
                        pass
                    elif menu == 2:
                        print("Obrigado pela sua preferência! Até mais :)")
                        break
                    else:
                        print("Favor digitar apenas o número mencionado..")
                        break

                else:
                    dinheiro_insuficiente = int(input("Dinheiro insuficiente, favor colocar valor equivalente ao pedido\n1 [1] - Tentar novamente\n2 [2] - Sair do Sistema\n3 Digite aqui: "))
                    if dinheiro_insuficiente == 1:
                        pass
                    elif dinheiro_insuficiente == 2:
                        print("Obrigado pela sua preferência! Até mais :)")
                        break
                    else:
                        print("Favor digitar apenas o número mencionado..")
                        break

            elif cardapio == 2:
                valor_cliente = float(input("Qual o valor entregue para a compra?\n1 Digite aqui: "))

                if valor_cliente >= cafe2.valor:
                    troco = valor_cliente - cafe2.valor
                    print(f"Compra realizada com sucesso!\n1 Pedido selecionado: Regular Coffee\n2 Valor do pedido: R${cafe2.valor}0\n3 Valor entregue: R${valor_cliente}0\n4 Troco: R${troco}0")
                    menu = int(input("Deseja realizar mais alguma compra?\n1 [1] - Sim\n2 [2] - Não\n3 Digite aqui: "))
                    if menu == 1:
                        pass
                    elif menu == 2:
                        print("Obrigado pela sua preferência! Até mais :)")
                        break
                    else:
                        print("Favor digitar apenas o número mencionado..")

                else:
                    dinheiro_insuficiente = int(input("Dinheiro insuficiente, favor colocar valor equivalente ao pedido\n1 [1] - Tentar novamente\n2 [2] - Sair do Sistema\n3 Digite aqui: "))
                    if dinheiro_insuficiente == 1:
                        pass
                    elif dinheiro_insuficiente == 2:
                        print("Obrigado pela sua preferência! Até mais :)")
                        break
                    else:
                        print("Favor digitar apenas o número mencionado..")
                        break

            elif cardapio == 3:
                valor_cliente = float(input("Qual o valor entregue para a compra?\n1 Digite aqui: "))

                if valor_cliente >= cafe3.valor:
                    troco = valor_cliente - cafe3.valor
                    print(f"Compra realizada com sucesso!\n1 Pedido selecionado: Regular Coffee\n2 Valor do pedido: R${cafe3.valor}0\n3 Valor entregue: R${valor_cliente}0\n4 Troco: R${troco}0")
                    menu = int(input("Deseja realizar mais alguma compra?\n1 [1] - Sim\n2 [2] - Não\n3 Digite aqui: "))
                    if menu == 1:
                        pass
                    elif menu == 2:
                        print("Obrigado pela sua preferência! Até mais :)")
                        break
                    else:
                        print("Favor digitar apenas o número mencionado..")

                else:
                    dinheiro_insuficiente = int(input("Dinheiro insuficiente, favor colocar valor equivalente ao pedido\n1 [1] - Tentar novamente\n2 [2] - Sair do Sistema\n3 Digite aqui: "))
                    if dinheiro_insuficiente == 1:
                        pass
                    elif dinheiro_insuficiente == 2:
                        print("Obrigado pela sua preferência! Até mais :)")
                        break
                    else:
                        print("Favor digitar apenas o número mencionado..")
                        break                

            elif cardapio == 4:
                print("Obrigado pela sua preferência! Até mais :)")
                break

            else:
                print("Favor digitar apenas o número mencionado..")
                for x in range(3):
                    try:
                        

                    #print("Fechando Sistema por insistência do erro.")
                    


#     except:
#         print("Favor digitar apenas o número mencionado..")
#     else:
#         break
# else:
#     print("Fechando Sistema..")   
                            