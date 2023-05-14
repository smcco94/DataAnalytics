import pandas as pd
import yfinance as yf
from ta.trend import MACD
from ta.volatility import BollingerBands
from ta.momentum import StochasticOscillator

def calcular_indicadores_tecnicos(acao, periodo):
    # Obtém os dados históricos da ação usando a biblioteca yfinance
    dados = yf.download(acao, period=periodo)

    # Calcula os indicadores técnicos
    macd = MACD(dados['Close']).macd()
    bollinger_bands = BollingerBands(dados['Close']).bollinger_mavg()
    stoch = StochasticOscillator(dados['High'], dados['Low'], dados['Close']).stoch()

    dados['MACD'] = macd
    dados['Bollinger_Bands'] = bollinger_bands
    dados['Stochastic_Oscillator'] = stoch

    return dados

def tomar_decisao_investimento(acao):
    # Defina o período para o cálculo dos indicadores técnicos (em dias)
    periodo = "1y"

    # Calcula os indicadores técnicos para a ação
    dados_acao = calcular_indicadores_tecnicos(acao, periodo)

    # Obtém os valores mais recentes dos indicadores técnicos
    ultimo_macd = dados_acao['MACD'].iloc[-1]
    ultimo_bollinger = dados_acao['Bollinger_Bands'].iloc[-1]
    ultimo_stoch = dados_acao['Stochastic_Oscillator'].iloc[-1]

    # Obtém o preço mais recente da ação
    preco_atual = dados_acao['Close'].iloc[-1]

    # Obtém os valores do canal de alta e baixa mais recentes
    ultima_alta = dados_acao['High'].rolling(window=20).max().iloc[-1]
    ultima_baixa = dados_acao['Low'].rolling(window=20).min().iloc[-1]

    # Verifica os sinais de investimento com base nos indicadores técnicos
    if ultimo_macd > 0 and ultimo_stoch > 50 and preco_atual > ultimo_bollinger:
        print(f"Investir na ação {acao}: Sinal de compra")

    elif ultimo_macd < 0 and ultimo_stoch < 50 and preco_atual < ultimo_bollinger:
        print(f"Investir na ação {acao}: Sinal de venda")

    else:
        print(f"Nenhum sinal de investimento na ação {acao} no momento")

# Exemplo de uso
tomar_decisao_investimento("AAPL")  # Substitua "AAPL" pelo símbolo da ação desejada
