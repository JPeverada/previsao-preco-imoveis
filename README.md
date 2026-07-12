# Property Price Predictor 🏠💰

Este projeto consiste em um script Python que utiliza técnicas de Machine Learning para prever o preço de imóveis com base em suas características (tamanho, acabamento, localização, presença de piscina, garagem e tipo do imóvel). 

O modelo compara duas abordagens distintas de regressão para encontrar as melhores estimativas.

---

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **Pandas**: Para manipulação e tratamento dos dados de treino.
* **Scikit-Learn**: Para a criação, treino e avaliação dos modelos de Machine Learning.
  * `LinearRegression`
  * `RandomForestRegressor`
  * `LabelEncoder` (Pré-processamento de variáveis categóricas)

---

## 🧠 Modelos Implementados

Para garantir uma análise comparativa, o projeto treina e utiliza simultaneamente dois algoritmos:
1. **Regressão Linear**: Modelo matemático que assume uma relação linear entre as variáveis independentes e a variável alvo.
2. **Random Forest Regressor**: Modelo baseado em múltiplas árvores de decisão (ensemble), ideal para capturar relações não-lineares complexas nos dados.

---

## 🛠️ Como Funciona

1. **Carga e Tratamento:** O script lê uma base de dados histórica (`Docs/Imoveis.xlsx`).
2. **Encoding:** Transforma os dados de texto (ex: "Bom", "Centro", "Sim") em valores numéricos utilizando o `LabelEncoder`.
3. **Treino:** Divide a base em dados de treino e teste (70/30) e ajusta ambos os modelos.
4. **Interatividade:** Abre um menu interativo no terminal para o usuário simular as características de um novo imóvel.
5. **Histórico:** Ao encerrar as consultas, gera e exibe um DataFrame com o histórico de todos os imóveis consultados e suas respectivas previsões.

---

## 📋 Pré-requisitos e Como Executar

Certifique-se de ter as bibliotecas necessárias instaladas antes de rodar o script:

```bash
pip install pandas scikit-learn openpyxl
