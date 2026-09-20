def classificar_consumo():
    while True:
        # Solicita os dados ao usuário
        tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
        
        # Validação básica para garantir que o tipo foi digitado corretamente
        if tipo_imovel not in ["comercial", "casa", "apartamento"]:
            print("Tipo de imóvel inválido. Por favor, escolha entre 'comercial', 'casa' ou 'apartamento'.\n")
            continue

        try:
            consumo = float(input("Digite o consumo mensal de água em m³: "))
        except ValueError:
            print("Por favor, digite um número válido para o consumo.\n")
            continue

        # Implementação das regras de negócio
        if tipo_imovel == "comercial":
            print("Tarifa comercial aplicada - consulte o plano corporativo.")
        elif tipo_imovel == "apartamento" and consumo < 10:
            print("Consumo econômico - excelente controle de água!")
        elif tipo_imovel == "apartamento" or (tipo_imovel == "casa" and consumo <= 25):
            print("Consumo moderado - dentro do padrão residencial.")
        else:
            print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")

        # Pergunta se deseja continuar ou finalizar
        continuar = input("\nDeseja fazer outro cálculo? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nEncerrando o sistema de conscientização. Até logo!")
            break
        print("-" * 40) # Linha separadora para a próxima consulta

# Executa a função
classificar_consumo()