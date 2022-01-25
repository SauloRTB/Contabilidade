import numpy as np
import os
import pandas as pd
import PySimpleGUI as sg
import csv

class Demonstrativo_cartao:
    def __init__(self, nome, validade, lista_devedores, lista_compras, valores=None):
        self.nome = nome
        self.validade = validade
        self.lista_devedores = lista_devedores
        self.lista_compras = lista_compras
        self.valores = valores
    
    def criar_valores(self):
        valores = []
        linha = []
        linha.append('A')
        
        for i in (range(len(self.lista_compras))):
            linha.append(0.0)

        for i in range(len(self.lista_devedores)):
            valores.append(linha[:])
        cont = 0
        for i in range(len(self.lista_devedores)):
            valores[cont][0] = self.lista_devedores[cont]
            cont += 1
            print(cont)
        return valores

def criar_dataframe(nome, vencimento, ano,mes_referencia, lista_devedores, lista_compras):
    if not os.path.exists(os.getcwd() + '/tabelas/'): 
         os.makedirs(os.getcwd() + '/tabelas/')
    lista_devedores_final = ['PARCELA ATUAL','TOTAL DE PARCELAS']
    for i in lista_devedores:
        lista_devedores_final.append(i)
    print(lista_devedores_final)
    print(lista_compras)

    tabela = pd.DataFrame(columns=lista_compras, index=lista_devedores_final)
    tabela.index.name = 'DEVEDORES' 
    for col in tabela.columns:
        tabela[col].values[:] = 0.0
    tabela.to_csv(os.getcwd() + '/tabelas/' + ano + '_' + mes_referencia + '_' + vencimento +'_' + nome + '.csv', sep=',', encoding='utf-8')
    return True

def criar_planilha(filename):
    # --- populate table with file contents --- #
    if filename == '':
        return
    data = []
    header_list = []
    if filename is not None:
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            header_list = next(reader)
            data = list(reader) 
            
    return header_list, data

def lista_pagadores(valores):
    pagadores = ''
    for i in valores:
        pagadores = pagadores + '-' + i[0]
    pagadores = pagadores.replace('-PARCELA ATUAL-TOTAL DE PARCELAS-','')
    return pagadores

def atualizar_compra(arquivo, opção, texto):
    planilha = pd.read_csv(arquivo)
    if opção == 'Alterar':
        nomeantigo, nomenovo = texto.split()
        planilhanova = planilha.rename(columns={nomeantigo: nomenovo})
        planilha = pd.DataFrame(planilhanova)
    elif opção == 'Remover':
        planilha = pd.DataFrame(planilha) 
        del planilha[texto]
    elif opção == 'Adicionar':
        planilha = planilha.assign(novo=0.0)
        nomecolunanova = 'novo'
        planilha = planilha.rename(columns={nomecolunanova: texto})
    planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
    os.remove(arquivo)
    os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', arquivo)

def atualizar_devedor(arquivo, opção, indice, nomenovo):
    planilha = pd.read_csv(arquivo) 
    if opção == 'Alterar':      
        planilha.loc[indice, 'DEVEDORES'] = nomenovo

    elif opção == 'Remover':
        planilha = planilha.drop(planilha.index[[indice]])
    elif opção == 'Adicionar':
        planilha = pd.DataFrame(planilha)
        print(planilha)
        lista = list(planilha)
        print(lista)
        valor = planilha.columns
        print(valor)
        valor = (len(valor)-1)
        print(valor)
        valor = valor
        lista = [nomenovo]
        print(lista)
        for i in range(valor):
            lista.append(0)
        print(lista)
        planilha.loc[len(planilha)]= lista
    planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
    os.remove(arquivo)
    os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', arquivo)

def atualizar_valores(arquivo,opcao, nome, valores):
    coluna = nome
    planilha = pd.read_csv(arquivo)
    planilha = pd.DataFrame(planilha)
    indice = 0
    if opcao == 'Fixa':
        for linha in range(len(planilha)):
            if indice == 0:
                planilha.at[indice, coluna] = 0
                indice += 1
                planilha = planilha.round(2)
                planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
                os.remove(arquivo)
                os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', arquivo)
            elif indice == 1:
                planilha.at[indice, coluna] = 0
                indice += 1
                planilha = planilha.round(2)
                planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
                os.remove(arquivo)
                os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', arquivo)
            else:
                valor = valores[indice -2]
                valor = valor.replace(',','.')
                planilha.at[indice, coluna] = float(valor)
                indice += 1
                planilha = planilha.round(2)
                planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
                os.remove(arquivo)
                os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', arquivo)
    elif opcao == 'Parcelada':
        for linha in range(len(planilha)):
            if indice == 0:
                
                valor = valor = valores[indice]
                valor = valor.replace(',','.')
                planilha.at[indice, coluna] = float(valor)
                indice += 1
                planilha = planilha.round(2)
                planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
                os.remove(arquivo)
                os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', arquivo)

            elif indice == 1:
                valor = valores[indice]
                valor = valor.replace(',','.')
                planilha.at[indice, coluna] = float(valor)
                indice += 1
                planilha = planilha.round(2)
                planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
                os.remove(arquivo)
                os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', arquivo)

            else:
                valor = valores[indice]
                valor = valor.replace(',','.')
                planilha.at[indice, coluna] = float(valor)
                indice += 1
                planilha = planilha.round(2)
                planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
                os.remove(arquivo)
                os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', arquivo)

def atualizar_planilha(arquivo, nome_novo):
    planilha = pd.read_csv(arquivo)
    planilha = pd.DataFrame(planilha)
    planilha.to_csv(nome_novo, sep=',', encoding='utf-8', index= False)
    planilha = pd.read_csv(nome_novo)
    pd.DataFrame(planilha)
    lista_colunas = []
    for coluna in planilha.columns:
        lista_colunas.append(coluna)
    indice = 1
    for coluna in range(len(lista_colunas)-1):
        parcelaatual = planilha[lista_colunas[indice]][0]
        totalparcela = planilha[lista_colunas[indice]][1]
        if not parcelaatual == 0:
            if parcelaatual == totalparcela:
                del planilha[lista_colunas[indice]]
        indice += 1
    lista_colunas = []
    for coluna in planilha.columns:
        lista_colunas.append(coluna)  
    indice = 1
    for coluna in range(len(lista_colunas)-1):
        valoratual = planilha[lista_colunas[indice]][0]
        if not valoratual == 0:
            novovalor = int(valoratual) + 1
            planilha.loc[0,lista_colunas[indice]] = novovalor
        indice += 1
    planilha = planilha.round(2)
    planilha.to_csv(os.getcwd() + '/tabelas/' + 'novo.csv', sep=',', encoding='utf-8', index= False)
    os.remove(nome_novo)
    os.rename(os.getcwd() + '/tabelas/' + 'novo.csv', os.getcwd() + '/tabelas/' + nome_novo)
    return 'sucesso', str(os.getcwd()) + '/tabelas/' + nome_novo

def soma_totais(arquivo):

    planilha = pd.read_csv(arquivo)
    planilha = pd.DataFrame(planilha)
    lista_colunas = []
    for coluna in planilha.columns:
        lista_colunas.append(coluna)
    lista_colunas.remove(lista_colunas[0])
    planilha['TOTAL'] = planilha[lista_colunas].sum(axis=1)
    lista_valores = []
    indice = 0
    lista_colunas.append('TOTAL')
    for coluna in range(len(lista_colunas)):
        valor = planilha[lista_colunas[indice]].sum()
        valor = valor - (planilha.at[0, lista_colunas[indice]] + planilha.at[1, lista_colunas[indice]])
        lista_valores.append(valor)
        indice += 1
    lista_valores.insert(0, 'TOTAL')
    planilha.loc[len(planilha)] = lista_valores
    planilha = planilha.round(2)
    planilha.to_csv(os.getcwd() + '/tabelas/' + 'temp.csv', sep=',', encoding='utf-8', index= False)
    return str(os.getcwd() + '/tabelas/' + 'temp.csv')

def resume_totais(arquivo):
    planilha = pd.read_csv(arquivo)
    planilha = pd.DataFrame(planilha)
    lista_colunas = []
    for coluna in planilha.columns:
        lista_colunas.append(coluna)
    lista_colunas.remove(lista_colunas[0])
    indice = 0
    lista_valores = []
    for coluna in range(len(lista_colunas)):
        valor = planilha.at[len(planilha)-1, lista_colunas[indice]]
        lista_valores.append(valor)
        indice += 1
    planilha2 = pd.DataFrame(list(zip(lista_colunas,lista_valores)), columns = ['COMPRAS','VALOR'])
    planilha2 = planilha2.round(2)
    planilha2.to_csv(os.getcwd() + '/tabelas/' + 'temp.csv', sep=',', encoding='utf-8', index= False)
    return str(os.getcwd() + '/tabelas/' + 'temp.csv')




