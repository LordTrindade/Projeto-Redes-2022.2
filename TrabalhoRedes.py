# # -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:17:26 2023

@author: filip
"""
#teste

import pandas as pd
#import csv
#from IPython.display import display
#import numpy as np
import matplotlib.pyplot as plt

claronome_pcfilipe = "2804:14c:da80:83a0:e8df:ef3f:3365:c432"
claronome_pctiago =  "2804:14c:da80:83a0:14e3:6b40:a6fb:e02e"

class Limpa_tela:
     def __init__(self):
         self.limpar()
     
     def limpar(self):
         try:
             from IPython import get_ipython
             get_ipython().magic('clear')
             get_ipython().magic('reset -f')
         except:
             pass



    
def plot_grafico1(eixo1,eixo2):
    #fig = plt.subplots(figsize = (10,5))
    #fig.plot(eixo1,eixo2,'o-')
    #fig.xlabel('No')
    #fig.ylabel('Inertia')
    #fig.grid(True)
    #fig.show()
    
    plt.plot(eixo1,eixo2,'o-')
    plt.xlabel('Numero do pacote')
    plt.ylabel('Tamanho do pacote')
    plt.grid(True)
    plt.show()


def plot_grafico2(eixo1,eixo2):
    plt.plot(eixo1,eixo2,'o-')
    plt.xlabel('Segundos')
    plt.ylabel('Tamanho do pacote')
    plt.grid(True)
    plt.show()
    
def plot_grafico3(eixo1,eixo2):
    plt.plot(eixo1,eixo2,'o-')
    plt.xlabel('Segundos')
    plt.ylabel('N pacotes')
    plt.grid(True)
    plt.show()

def plot_grafico_protocolos(dataframe,eixo2):

    
    #nlinhasx =len(dataframe.index)
    #nlinhas = []
    #for x in range(1,len(nlinhas)):
        #nlinhas.append(x)
    
    TCP_value = [None] * len(dataframe); tcp = 0
    QUIC_value = [None] * len(dataframe); quic = 0
    TLSv3_value = [None] * len(dataframe); tls3 = 0
    TLSv2_value = [None] * len(dataframe); tls2 = 0
    DNS_value = [None] * len(dataframe); dns = 0
    UDP_value = [None] * len(dataframe); udp = 0
    outros_valores = [None] * len(dataframe); outros = 0
    for x in range(len(eixo2)): #['Protocol']
        pass
        #if dataframe.iloc[0]['A']
        if (dataframe.iloc[x] == "TCP"):
            TCP_value[x]=tcp; tcp = tcp+1
        elif (dataframe.iloc[x] == "QUIC"):
            QUIC_value[x]=quic ; quic = quic+1
        elif (dataframe.iloc[x] == "TLSv1.3"):
            TLSv3_value[x]=tls3; tls3 = tls3+1
        elif (dataframe.iloc[x] == "TLSv1.2"):
            TLSv2_value[x]=tls2; tls2 = tls2+1
        elif (dataframe.iloc[x] == "DNS"):
            DNS_value[x]=dns; dns = dns+1
        elif (dataframe.iloc[x] == "UDP"):
            UDP_value[x]=udp; udp = udp+1
        else:
            outros_valores[x]=outros; outros= outros+1
    
    plt.xlabel('Segundos')
    plt.ylabel('N pacotes')
    plt.plot(eixo2, TCP_value, 'r',label='TCP')
    plt.plot(eixo2, QUIC_value, 'b', label='QUIC')
    plt.plot(eixo2, TLSv3_value, 'y', label='TLSv1.3')
    plt.plot(eixo2, TLSv2_value, 'g', label='TLSv1.2')
    plt.plot(eixo2, DNS_value, 'c', label='DNS')
    plt.plot(eixo2, UDP_value, 'k', label='UDP')
    plt.plot(eixo2, outros_valores, 'm', label='outros protocolos')
    #plt.grid(True)
    plt.show()
    
    
def plot_grafico_protocolos2(dataframe,eixo2,coluna_tamanho):


    
    TCP_value = [None] * len(dataframe); tcp = 0
    QUIC_value = [None] * len(dataframe); quic = 0
    TLSv3_value = [None] * len(dataframe); tls3 = 0
    TLSv2_value = [None] * len(dataframe); tls2 = 0
    DNS_value = [None] * len(dataframe); dns = 0
    UDP_value = [None] * len(dataframe); udp = 0
    outros_valores = [None] * len(dataframe); outros = 0
    for x in range(len(eixo2)): #['Protocol']
        pass
        #if dataframe.iloc[0]['A']
        if (dataframe.iloc[x] == "TCP"):
            TCP_value[x]=tcp; tcp = tcp + coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "QUIC"):
            QUIC_value[x]=quic ; quic = quic+ coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "TLSv1.3"):
            TLSv3_value[x]=tls3; tls3 = tls3+ coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "TLSv1.2"):
            TLSv2_value[x]=tls2; tls2 = tls2+ coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "DNS"):
            DNS_value[x]=dns; dns = dns+ coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "UDP"):
            UDP_value[x]=udp; udp = udp+ coluna_tamanho.iloc[x]
        else:
            outros_valores[x]=outros; outros= outros+ coluna_tamanho.iloc[x]
    

    plt.xlabel('Segundos')
    plt.ylabel('Tamanho acumulado pacotes')
    plt.plot(eixo2, TCP_value, 'r',label='TCP')
    plt.plot(eixo2, QUIC_value, 'b', label='QUIC')
    plt.plot(eixo2, TLSv3_value, 'y', label='TLSv1.3')
    plt.plot(eixo2, TLSv2_value, 'g', label='TLSv1.2')
    plt.plot(eixo2, DNS_value, 'c', label='DNS')
    plt.plot(eixo2, UDP_value, 'k', label='UDP')
    plt.plot(eixo2, outros_valores, 'm', label='outros protocolos')
    #plt.grid(True)
    plt.show()


def plot_grafico_protocolos3(dataframe,eixo2,coluna_tamanho):

    
    
    TCP_value = [None] * len(dataframe); tcp = 0
    QUIC_value = [None] * len(dataframe); quic = 0
    TLSv3_value = [None] * len(dataframe); tls3 = 0
    TLSv2_value = [None] * len(dataframe); tls2 = 0
    DNS_value = [None] * len(dataframe); dns = 0
    UDP_value = [None] * len(dataframe); udp = 0
    outros_valores = [None] * len(dataframe); outros = 0
    for x in range(len(eixo2)): #['Protocol']
        pass
        #if dataframe.iloc[0]['A']
        if (dataframe.iloc[x] == "TCP"):
            TCP_value[x]=coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "QUIC"):
            QUIC_value[x]=coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "TLSv1.3"):
            TLSv3_value[x]=coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "TLSv1.2"):
            TLSv2_value[x]=coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "DNS"):
            DNS_value[x]=coluna_tamanho.iloc[x]
        elif (dataframe.iloc[x] == "UDP"):
            UDP_value[x]=coluna_tamanho.iloc[x]
        else:
            outros_valores[x]=outros; outros= outros+ coluna_tamanho.iloc[x]
    

    plt.xlabel('Segundos')
    plt.ylabel('Tamanho dos pacotes')
    plt.plot(eixo2, TCP_value, 'r',label='TCP')
    plt.plot(eixo2, QUIC_value, 'b', label='QUIC')
    plt.plot(eixo2, TLSv3_value, 'y', label='TLSv1.3')
    plt.plot(eixo2, TLSv2_value, 'g', label='TLSv1.2')
    plt.plot(eixo2, DNS_value, 'c', label='DNS')
    plt.plot(eixo2, UDP_value, 'k', label='UDP')
    plt.plot(eixo2, outros_valores, 'b', label='outros protocolos')
    #plt.grid(True)
    plt.show()
    
    
def plot_grafico_protocolo(dataframe,eixo2,coluna_tamanho,protocolo,color):

    
    #nlinhasx =len(dataframe.index)
    #nlinhas = []
    #for x in range(1,len(nlinhas)):
        #nlinhas.append(x)
    
    Protocol_value = [None] * len(dataframe); 
    for x in range(len(eixo2)): #['Protocol']
        pass
        #if dataframe.iloc[0]['A']
        if (dataframe.iloc[x] == protocolo):
            Protocol_value[x]=coluna_tamanho.iloc[x]
    

    plt.xlabel('Segundos')
    plt.ylabel('Tamanho dos pacotes')
    plt.plot(eixo2, Protocol_value, color,label=protocolo)

    #plt.grid(True)
    plt.show()
    

def plot_grafico_envio1(dataframe,eixo2):

    
    chess_value = [None] * len(dataframe); chess = 0
    outros_valores = [None] * len(dataframe); outros = 0
    for x in range(len(eixo2)): #['Protocol']
        pass
        #if dataframe.iloc[0]['A']
        if (dataframe.iloc[x] == "amplitude.chess.com.cdn.cloudflare.net"):
            chess_value[x]=chess; chess = chess+1
        else:
            outros_valores[x]=outros; outros= outros+1
    
    plt.xlabel('Segundos')
    plt.ylabel('Numero de pacotes enviados de cada fonte')
    plt.plot(eixo2, chess_value, 'g',label='TCP')
    plt.plot(eixo2, outros_valores, 'r', label='outros protocolos')
    #plt.grid(True)
    plt.show()
    
def plot_grafico_envio2(dataframe,eixo2,coluna_tamanho):

    
    chess_value = [None] * len(dataframe); chess=0
    outros_valores = [None] * len(dataframe);  outros = 0
    for x in range(len(eixo2)): #['Protocol']
        pass
        #if dataframe.iloc[0]['A']
        if (dataframe.iloc[x] == "amplitude.chess.com.cdn.cloudflare.net"):
            chess_value[x]=chess ; chess = chess + coluna_tamanho.iloc[x]
        else:
            outros_valores[x]=outros; outros = outros + coluna_tamanho.iloc[x]
    
    plt.xlabel('Segundos')
    plt.ylabel('Tamanho acumulado de pacotes enviados de cada fonte')
    plt.plot(eixo2, chess_value, 'g',label='TCP')
    plt.plot(eixo2, outros_valores, 'r', label='outros protocolos')
    #plt.grid(True)
    plt.show()
    
    
def plot_grafico_envio2_claro(dataframe,eixo2,coluna_tamanho):

    
    chess_value = [None] * len(dataframe); chess=0
    outros_valores = [None] * len(dataframe);  outros = 0
    for x in range(len(eixo2)): #['Protocol']
        pass
        #if dataframe.iloc[0]['A']
        if (dataframe.iloc[x] == claronome_pctiago):
            chess_value[x]=chess ; chess = chess + coluna_tamanho.iloc[x]
        else:
            outros_valores[x]=outros; outros = outros + coluna_tamanho.iloc[x]
    
    plt.xlabel('Segundos')
    plt.ylabel('Tamanho acumulado de pacotes enviados de cada fonte')
    plt.plot(eixo2, chess_value, 'g',label='TCP')
    plt.plot(eixo2, outros_valores, 'r', label='outros protocolos')
    #plt.grid(True)
    plt.show()

def plot_grafico_pacotes_coluna(valores):
    pass
    #info['Protocol'].value_counts()
    serie = valores.value_counts()
    #serie = valores
    
    #plt.xlabel('Segundos')
    #plt.ylabel('Tamanho acumulado de pacotes enviados de cada fonte')
    
    plt.xlabel('Tipos de pacote')
    plt.ylabel('Quantidade')
    serie.plot.bar()
    plt.show()
    
    #plt.plot(serie.index, serie.values)
    
def plot_grafico_destino_coluna(valores):
    pass
    #info['Protocol'].value_counts()
    serie1 = valores.value_counts()
    
    #serie = valores.value_counts()
    serie = serie1.nlargest(6)
    #serie = valores
    
    plt.xlabel('Destinos dos pacotes')
    plt.ylabel('Quantidade')
    serie.plot.bar()
    plt.show()

def plot_grafico_fonte_coluna(valores):
    pass
    #info['Protocol'].value_counts()
    serie1 = valores.value_counts()
    
    #serie = valores.value_counts()
    serie = serie1.nlargest(6)
    #serie = valores
    
    plt.xlabel('Fontes dos pacote')
    plt.ylabel('Quantidade')
    serie.plot.bar()
    plt.show()    


if __name__ == "__main__":
    print("Hello world")
    limpador = Limpa_tela()
    arquivo = r"xadrez_vs_tiago2.csv"
    info = pd.read_csv(arquivo, index_col=0)
    #display(info.to_string())
    info = info.drop("Info",axis =1)
    #display(info.to_string())
    print ("\n\n")
    print(info.iloc[[0]])
    print(info.dtypes)
    nlinhasx =len(info.index)
    nlinhas = []
    for x in range(1,nlinhasx+1):
        nlinhas.append(x)
    plot_grafico1(nlinhas,info['Length'])
    plot_grafico2(info['Time'],info['Length'])
    plot_grafico3(info['Time'],nlinhas)
    
    print("Quantidades de tipos de protocolos: " + str(info['Protocol'].nunique()))
    tipos_protocolos = info['Protocol'].unique()
    print("Tipos de protocolos:" + str(tipos_protocolos))
    plot_grafico_pacotes_coluna(info['Protocol'])
    print(str(info['Protocol'].value_counts()))
    #x = info['Protocol'].nunique()
    
    plot_grafico_protocolos(info['Protocol'],info['Time'])
    print(str(info['Protocol'].size))
    
    plot_grafico_protocolos2(info['Protocol'],info['Time'],info['Length'])
    #plot_grafico_protocolos3(info['Protocol'],info['Time'],info['Length'])
    
    plot_grafico_protocolo(info['Protocol'],info['Time'],info['Length'],"TCP","r")
    plot_grafico_protocolo(info['Protocol'],info['Time'],info['Length'],"QUIC","b")
    plot_grafico_protocolo(info['Protocol'],info['Time'],info['Length'],"DNS","c")
    plot_grafico_protocolo(info['Protocol'],info['Time'],info['Length'],"UDP","k")
    #display(info['Length'].to_string())
    #print(str(info['Length'].size))
    #print(str(info['Length'].iloc[0]))


    ##################
    ## aqui, ver quanto a quem esta enviando coisas
    print("\n\nQuantidades de tipos de fontes: " + str(info['Source'].nunique()))
    #tipos_fontes = info['Source'].unique()
    #print("Tipos de fontes:" + str(tipos_fontes))
    print(str(info['Source'].value_counts()))    
    plot_grafico_fonte_coluna(info['Source'])
    
    ##################
    ## aqui, ver quanto a quem esta recebendo coisas
    print("\n\nQuantidades de tipos de destinos: " + str(info['Destination'].nunique()))
    #tipos_destinos = info['Destination'].unique()
    #print("Tipos de destinos:" + str(tipos_destinos))
    print(str(info['Destination'].value_counts()))
    plot_grafico_destino_coluna(info['Destination'])
    
    
    #################
    ## aqui, cliente - servidor 
    #dataset_by_cliente = info[info['Source'] == "192.168.0.14"]
    #dataset_to_cliente = info[info['Destination'] == "192.168.0.14"]
    #dataset_eu_chess = (((info[info['Destination'] == "192.168.0.14"])&(info[info['Source'] == "amplitude.chess.com.cdn.cloudflare.net"]))&((info[info['Source'] == "192.168.0.14"])&(info[info['Destination'] == "amplitude.chess.com.cdn.cloudflare.net"])))            
    
    dataset_eu_chess = (info.loc[(info['Destination'] == "192.168.0.10")&(info['Source'] == "amplitude.chess.com.cdn.cloudflare.net")])
    print(str(dataset_eu_chess.shape))
    dataset_eu_chess = (info.loc[((info['Destination'] == "192.168.0.10")&(info['Source'] == "amplitude.chess.com.cdn.cloudflare.net"))|((info['Source'] == "192.168.0.10")&(info['Destination'] == "amplitude.chess.com.cdn.cloudflare.net"))])
    print(str(dataset_eu_chess.shape))
    plot_grafico_envio1(dataset_eu_chess['Source'],dataset_eu_chess['Time'])
    plot_grafico_envio2(dataset_eu_chess['Source'],dataset_eu_chess['Time'],dataset_eu_chess['Length'])
    
    

    dataset_claro = (info.loc[((info['Source'] == claronome_pctiago))|((info['Destination'] == claronome_pctiago))])
    print(str(dataset_claro.shape))
    #plot_grafico_envio1(dataset_claro['Source'],dataset_claro['Time'])
    plot_grafico_envio2_claro(dataset_claro['Source'],dataset_claro['Time'],dataset_claro['Length'])
    
    plot_grafico_pacotes_coluna(dataset_eu_chess['Protocol'])
    plot_grafico_protocolos(dataset_eu_chess['Protocol'],dataset_eu_chess['Time'])
    plot_grafico_protocolos2(dataset_eu_chess['Protocol'],dataset_eu_chess['Time'],dataset_eu_chess['Length'])