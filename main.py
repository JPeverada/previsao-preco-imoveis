import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

codificador_tabela = LabelEncoder()
modelo = LinearRegression()
modelo_tree = RandomForestRegressor()

historico_novos_imoveis = []
tabela = pd.read_excel('Docs/Imoveis.xlsx')

tabela['Acabamento'] = codificador_tabela.fit_transform(tabela['Acabamento'])
tabela['Localizacao'] = codificador_tabela.fit_transform(tabela['Localizacao'])
tabela['Piscina'] = codificador_tabela.fit_transform(tabela['Piscina'])
tabela['Garagem'] = codificador_tabela.fit_transform(tabela['Garagem'])
tabela['Tipo'] = codificador_tabela.fit_transform(tabela['Tipo'])

data_frame= pd.DataFrame(tabela)

y = data_frame['Preco']
x = data_frame.drop('Preco', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

modelo_tree.fit(x_train, y_train)
modelo.fit(x_train, y_train)

previsao_tree = modelo_tree.predict(x_test)
previsao_linear = modelo.predict(x_test)

while True:
    metros_quadrados = int(input('Digite a metragem do imóvel (ou 0 para sair): '))
    if metros_quadrados == 0:
        break
    acabamento = input('Digite o acabamento do imóvel (Ruim, Regular, Bom, Impecável): ')
    localizacao = input('Digite a localização do imóvel (Bairro, Centro, Praia): ')
    piscina = input('Digite se o imóvel possui piscina (Sim/Não): ')
    garagem = input('Digite se o imóvel possui garagem (Sim/Não): ')
    tipo = input('Digite o tipo do imóvel (Apartamento/Casa): ')

    match acabamento:
        case 'Ruim': 
            acabamento = 3
        case 'Regular': 
            acabamento = 2
        case 'Bom': 
            acabamento = 0
        case 'Impecável': 
            acabamento = 1

    match localizacao:
        case 'Bairro': 
            localizacao = 0
        case 'Centro': 
            localizacao = 1
        case 'Praia': 
            localizacao = 2

    if piscina == 'Sim': 
        piscina = 1
    else: 
        piscina = 0

    if garagem == 'Sim': 
        garagem = 1
    else: 
        garagem = 0

    match tipo:
        case 'Apartamento': 
            tipo = 0
        case 'Casa': 
            tipo = 1
            
    df_temporario = pd.DataFrame([{
        "Tamanho": metros_quadrados,
        "Acabamento": acabamento,
        "Localizacao": localizacao,
        "Piscina": piscina,
        "Garagem": garagem,
        "Tipo": tipo
    }])

    nova_previsao_tree = modelo_tree.predict(df_temporario)[0]
    nova_previsao_linear = modelo.predict(df_temporario)[0]
    
    novo_imovel = {
        "Tamanho": metros_quadrados,
        "Acabamento": acabamento,
        "Localizacao": localizacao,
        "Piscina": piscina,
        "Garagem": garagem,
        "Tipo": tipo,
        "Preco_tree": nova_previsao_tree,
        "Preco_linear": nova_previsao_linear
    }
    
    historico_novos_imoveis.append(novo_imovel)
    
if historico_novos_imoveis:
    df_historico = pd.DataFrame(historico_novos_imoveis)
    print("\nHistórico de novos imóveis:")
    print(df_historico)
else:
    print("Nenhum imóvel foi adicionado ao histórico.")
