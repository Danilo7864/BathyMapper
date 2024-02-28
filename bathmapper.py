import pandas as pd
import matplotlib.pyplot as plt

def processar_dados():
    # Carregar os dados
    dados_rover = pd.read_csv('manterdados/dados_rover.csv', encoding='latin-1')
    dados_maregrafo = pd.read_csv('manterdados/dados_maregrafo.csv', encoding='latin-1')

    # divir dados /12
    dados_maregrafo['altura_mare'] = pd.to_numeric(dados_maregrafo['altura_mare'], errors='coerce') / 12

    # Arredondar os valores da coluna 'altura_mare' para 2 casas decimais
    dados_maregrafo['altura_mare'] = dados_maregrafo['altura_mare'].round(1)

    # Juntar os dados com base na coluna "tempo"
    dados_complentos = pd.merge(dados_rover, dados_maregrafo, on='tempo')

    # corrigir dados (subtração de Z por tempo)
    dados_complentos['Z'] = pd.to_numeric(dados_complentos['Z'], errors='coerce')
    dados_complentos['altura_mare'] = pd.to_numeric(dados_complentos['altura_mare'], errors='coerce')

    dados_complentos['profundidade_corrigida'] = dados_complentos['Z'] + dados_complentos['altura_mare']

    dados_complentos['profundidade_corrigida'] = dados_complentos['profundidade_corrigida'].round(1)

    # Salvando os dados combinados em um novo arquivo CSV
    dados_complentos.to_csv('manterdados/dados_complentos.csv', index=False)

    # Retornar o DataFrame processado
    return dados_complentos


def plotar_mapa_de_calor(dados):
    x = dados['X']
    y = dados['Y']
    z = dados['profundidade_corrigida']

    # Plotar o mapa de calor
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, c=z, cmap='Spectral')
    plt.title('Mapa de Calor em Relação à Profundidade')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar(scatter, label='Profundidade')
    plt.show()

# Chamada da função para processar os dados
dados_complentos = processar_dados()
# Chamada da função para plotar o mapa de calor
plotar_mapa_de_calor(dados_complentos)