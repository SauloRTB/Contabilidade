import PySimpleGUI as sg
import os
import funcoes
import os

sg.theme('DarkBrown')

def PaginainIcial():
    
    flayout = [
        [],
        [sg.Text('CONTABILIDADE MENSAL 2.0')],
        [sg.Text('Bem-vindo!! :D')],
        [sg.Button('1 - Criar planilha mensal por cartão')], 
        [sg.Button('2 - Reutilizar planilha')],
        [sg.Button('3 - Editar planilha existente')], 
        [sg.Button('4 - Relatorio Geral')],
        [sg.Button('5 - Relatorio Resumido')], 
        [sg.Button('Sair')]
    ]

    return sg.Window('CONTABILIDADE MENSAL', flayout, size=(500,300), element_justification='center',finalize=True)
def Criar_cartao():
    flayout = [
    [sg.Text('Por favor, Preencha os campos abaixo:')],
    [sg.Text('Obs: separa devedores e compras por um espaço em branco')],
    [sg.Text('Nome:'), sg.InputText('', size=50, key='-nomecartao-')],
    [sg.Text('Devedores:'), sg.InputText('', size=50, key='-devedores-')],
    [sg.Text('Compras:'), sg.InputText('', size=50, key='-compras-')],
    [sg.Text('Ano:'), sg.InputText('', size=50, key='-ano-')],    
    [sg.Text('Vencimento:',size=10), sg.InputCombo(['5','10','15','20','25','30'], size=5,key='-vencimento-'), sg.Text('Mês:',size=5), sg.InputCombo(['01','02','03','04','05','06','07','08','09','10','11','12'], size=5,key='-mesreferencia-'),],
    [sg.Button('Criar Demonstrativo')],
    [sg.Text('', key='-textosucesso-')]
    ]

    return sg.Window('CRIAR DEMONSTRATIVO MENSAL', flayout, size=(400,260), element_justification='center',finalize=True)
def Editar_planilha():
    filename = sg.popup_get_file('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
    
    try:
        header_list, data = funcoes.criar_planilha(filename)  
        pagadores = funcoes.lista_pagadores(data)
    except:
        header_list = ['erro']
        data = [[0.0]]
        pagadores = 'erro'

    


    
    flayout = [
        [sg.Text('Tabela Selecionada:',size=(15,1)),sg.InputText(filename, key='-arquivo-')],
        [sg.Text('Devedores:',size=(15,1)),sg.InputText(pagadores, key='-devedores-')],
        [sg.Table(values=data,
                            max_col_width=25,
                            auto_size_columns=True,
                            vertical_scroll_only=False,
                            headings=header_list,
                            justification='right',
                            key='-tabeladados-',
                            # alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))],
        [sg.Frame('Adicionar/ Remover/Alterar Compra', layout=[[sg.Text('Selecione a opção e digite o nome a ser removido/adcionado abaixo')],
        [sg.Text('para alterar digite o nome antigo e o novo separados espaço:')],
        [sg.InputCombo(['Adicionar','Remover','Alterar'], size=9,key='-addouremovecompra-'),
        sg.InputText(key='-compra-'),sg.Button('Atualizar Com.')]],border_width=10),
        sg.Frame('Adicionar/ Remover/Alterar Devedor', layout=[[sg.Text('Selecione a opção e digite o nome a ser removido/adcionado abaixo')],
        [sg.Text('para alterar digite o nome antigo e o novo separados espaço:')],
        [sg.InputCombo(['Adicionar','Remover','Alterar'], size=9,key='-addouremovedevedor-'),
        sg.InputText(key='-devedor-'),sg.Button('Atualizar Dev.')]],border_width=10)],
        [sg.Frame('Editar valores de uma compra', layout=[[sg.Text('Selecione a opção e digite o nome da compra, para compras de uma parcela você deve informar que a compra')],
        [sg.Text(f'para compras de uma parcela você deve informar que a compra é a parcela "1" de um total de "1":')],
        [sg.InputCombo(['Fixa', 'Parcelada'], size=9, key='-fixaouparcela-'),
        sg.InputText(key='-nomecompra-'),sg.Button('Atualizar Val.')]],border_width=10)]
     

                            ]

    
    return sg.Window('Editar Planilha', flayout, size=(1130,600),finalize=True)
def Editar_planilha2(filename):
    header_list, data = funcoes.criar_planilha(filename)  
    pagadores = funcoes.lista_pagadores(data)
    
    flayout = [
        [sg.Text('Tabela Selecionada:',size=(15,1)),sg.InputText(filename, key='-arquivo-')],
        [sg.Text('Devedores:',size=(15,1)),sg.InputText(pagadores, key='-devedores-')],
        [sg.Table(values=data,
                            max_col_width=25,
                            auto_size_columns=True,
                            vertical_scroll_only=False,
                            headings=header_list,
                            justification='right',
                            key='-tabeladados-',
                            # alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))],
        [sg.Frame('Adicionar/ Remover/Alterar Compra', layout=[[sg.Text('Selecione a opção e digite o nome a ser removido/adcionado abaixo')],
        [sg.Text('para alterar digite o nome antigo e o novo separados espaço:')],
        [sg.InputCombo(['Adicionar','Remover','Alterar'], size=9,key='-addouremovecompra-'),
        sg.InputText(key='-compra-'),sg.Button('Atualizar Com.')]],border_width=10),
        sg.Frame('Adicionar/ Remover/Alterar Devedor', layout=[[sg.Text('Selecione a opção e digite o nome a ser removido/adcionado abaixo')],
        [sg.Text('para alterar digite o nome antigo e o novo separados espaço:')],
        [sg.InputCombo(['Adicionar','Remover','Alterar'], size=9,key='-addouremovedevedor-'),
        sg.InputText(key='-devedor-'),sg.Button('Atualizar Dev.')]],border_width=10)],
        [sg.Frame('Editar valores de uma compra', layout=[[sg.Text('Selecione a opção e digite o nome da compra, para compras de uma parcela você deve informar que a compra')],
        [sg.Text(f'para compras de uma parcela você deve informar que a compra é a parcela "1" de um total de "1":')],
        [sg.InputCombo(['Fixa', 'Parcelada'], size=9, key='-fixaouparcela-'),
        sg.InputText(key='-nomecompra-'),sg.Button('Atualizar Val.')]],border_width=10)]
     

                            ]


    return sg.Window('Editar Planilha2', flayout, size=(1130,600),finalize=True)
def Editar_planilha3(filename):
    header_list, data = funcoes.criar_planilha(filename)  
    pagadores = funcoes.lista_pagadores(data)
    
    flayout = [
        [sg.Text('Tabela Selecionada:',size=(15,1)),sg.InputText(filename, key='-arquivo-')],
        [sg.Text('Devedores:',size=(15,1)),sg.InputText(pagadores, key='-devedores-')],
        [sg.Table(values=data,
                            max_col_width=25,
                            auto_size_columns=True,
                            vertical_scroll_only=False,
                            headings=header_list,
                            justification='right',
                            key='-tabeladados-',
                            # alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))],
        [sg.Frame('Adicionar/ Remover/Alterar Compra', layout=[[sg.Text('Selecione a opção e digite o nome a ser removido/adcionado abaixo')],
        [sg.Text('para alterar digite o nome antigo e o novo separados espaço:')],
        [sg.InputCombo(['Adicionar','Remover','Alterar'], size=9,key='-addouremovecompra-'),
        sg.InputText(key='-compra-'),sg.Button('Atualizar Com.')]],border_width=10),
        sg.Frame('Adicionar/ Remover/Alterar Devedor', layout=[[sg.Text('Selecione a opção e digite o nome a ser removido/adcionado abaixo')],
        [sg.Text('para alterar digite o nome antigo e o novo separados espaço:')],
        [sg.InputCombo(['Adicionar','Remover','Alterar'], size=9,key='-addouremovedevedor-'),
        sg.InputText(key='-devedor-'),sg.Button('Atualizar Dev.')]],border_width=10)],
        [sg.Frame('Editar valores de uma compra', layout=[[sg.Text('Selecione a opção e digite o nome da compra, para compras de uma parcela você deve informar que a compra')],
        [sg.Text(f'para compras de uma parcela você deve informar que a compra é a parcela "1" de um total de "1":')],
        [sg.InputCombo(['Fixa', 'Parcelada'], size=9, key='-fixaouparcela-'),
        sg.InputText(key='-nomecompra-'),sg.Button('Atualizar Val.')]],border_width=10)]
     

                            ]


    return sg.Window('Editar Planilha3', flayout, size=(1130,600),finalize=True)
def popup_editarvalores(texto):

    return sg.popup_get_text(texto)    
def Reutilizar_planilha(): 
    filename = sg.popup_get_file('Selecione o arquivo', no_window=True, file_types=(("CSV Files","*.csv"),))
    
    flayout = [
        [sg.Text('Tabela Selecionada:',size=(15,1)),sg.InputText(filename, key='-arquivo-')],
        [sg.Text('Por favor, Preencha os campos abaixo:')],
        [sg.Text('Nome:',size=6), sg.InputText('', size=50, key='-nomecartao-')],
        [sg.Text('Ano:',size=6), sg.InputText('', size=50, key='-ano-')],    
        [sg.Text('Vencimento:',size=10), sg.InputCombo(['5','10','15','20','25','30'], size=5,key='-vencimento-'), 
        sg.Text('Mês:',size=5), sg.InputCombo(['01','02','03','04','05','06','07','08','09','10','11','12'], size=5,key='-mesreferencia-'),],
        [sg.Button('Atualizar Demonstrativo'), sg.Button('Sair')],
        [sg.Text('', key='-textosucesso-')]

    ]

    return sg.Window('CRIAR DEMONSTRATIVO MENSAL', flayout, size=(400,200), element_justification='center',finalize=True)
def Relatoriogeral():
    fonte = sg.popup_get_file('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
    try:
        filename = funcoes.soma_totais(fonte)
        header_list, data = funcoes.criar_planilha(filename) 
    except:
        header_list, data = ['erro'], [[0.0]]
    layout = [
        [sg.Table(values=data,
                            max_col_width=25,
                            auto_size_columns=True,
                            vertical_scroll_only=False,
                            headings=header_list,
                            justification='right',
                            key='-tabeladados-',
                            # alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))],
        [sg.Text('Nome:'), sg.InputText('demonstrativomensal',key='-nome-')],
        [sg.Button('Selecionar Pasta')],
        [sg.Text('', key='-textosucesso-')]
        
    ]
    return sg.Window('Relatório Geral', layout,size=(650, 250),finalize=True)
def Relatorioresumido():
    fonte = sg.popup_get_file('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
    try:
        filename = funcoes.resume_totais(funcoes.soma_totais(fonte))
        header_list, data = funcoes.criar_planilha(filename) 
    except:
        header_list, data = ['erro'], [[0.0]]

    layout = [
        [sg.Table(values=data,
                            max_col_width=25,
                            auto_size_columns=True,
                            vertical_scroll_only=False,
                            headings=header_list,
                            justification='right',
                            key='-tabeladados-',
                            # alternating_row_color='lightblue',
                            num_rows=min(len(data), 20)),sg.Text('Nome:'), sg.InputText('demonstrativomensal',key='-nome-'),sg.Button('Selecionar Pasta')],
        [sg.Text('', key='-textosucesso-')]
        
    ]
    return sg.Window('Outros Débitos', layout,size=(850, 250),finalize=True)    

janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10 = PaginainIcial(),None,None,None,None,None, None, None, None, None
while True:
    janelaativa, evento, valor = sg.read_all_windows()

    if janelaativa == janela1 and evento == 'Sair' or janelaativa == janela1 and evento == sg.WIN_CLOSED:
        janela1.close()
        break
    if janelaativa == janela1 and evento == '1 - Criar planilha mensal por cartão':
        janela1.hide()
        janela2 = Criar_cartao() 
        
    if janelaativa == janela1 and evento == '3 - Editar planilha existente':
        janela3 = Editar_planilha()
        janela1.hide()
    if janelaativa == janela1 and evento == '2 - Reutilizar planilha':
        janela7 = Reutilizar_planilha()
        janela1.hide()
    if janelaativa == janela1 and evento == '4 - Relatorio Geral':
        janela8 = Relatoriogeral()
        janela1.hide()
    if janelaativa == janela1 and evento == '5 - Relatorio Resumido':
        janela9 = Relatorioresumido()
        janela1.hide()  
    if janelaativa == janela2 and evento == sg.WIN_CLOSED:
        janela1.un_hide()
        janela2.close() 
        
          
    
    if janelaativa == janela2 and evento == 'Criar Demonstrativo':
        nomecartao = valor['-nomecartao-']
        devedores = valor['-devedores-'].split()
        compras = valor['-compras-'].split()
        vencimento = valor['-vencimento-']
        mesreferencia = valor['-mesreferencia-']
        ano = valor['-ano-']
        if funcoes.criar_dataframe(nomecartao, vencimento, ano, mesreferencia,devedores, compras) == True:
            janela2.find_element('-textosucesso-').Update('Arquivo criado com sucesso! :D')
        else:
            janela2.find_element('-textosucesso-').Update('Erro, verifique os dados preenchidos ous e a tabela já existe! :(')  
    if janelaativa == janela3 and evento == 'Atualizar Com.':
        arquivo = valor['-arquivo-']
        texto = valor['-compra-']
        opcao = valor['-addouremovecompra-']
        funcoes.atualizar_compra(arquivo, opcao, texto)
        janela4 = Editar_planilha2(arquivo)
        janela3.close() 
    if janelaativa == janela4 and evento == 'Atualizar Com.':
        arquivo = valor['-arquivo-']
        texto = valor['-compra-']
        opcao = valor['-addouremovecompra-']
        funcoes.atualizar_compra(arquivo, opcao, texto)
        janela5 = Editar_planilha3(arquivo)
        janela4.close()      
    if janelaativa == janela5 and evento == 'Atualizar Com.':
        arquivo = valor['-arquivo-']
        texto = valor['-compra-']
        opcao = valor['-addouremovecompra-']
        funcoes.atualizar_compra(arquivo, opcao, texto)
        janela4 = Editar_planilha2(arquivo)
        janela5.close()  
    if janelaativa == janela3 and evento =='Atualizar Dev.':
        arquivo = valor['-arquivo-']
        texto = valor['-devedor-']
        opcao = valor['-addouremovedevedor-']
        if opcao == 'Alterar':
            listadevedores = valor['-devedores-'].split('-')
            nomeantigo, nomenovo = texto.split()
            indice = listadevedores.index(nomeantigo)+2
        elif opcao == 'Remover':
            listadevedores = valor['-devedores-'].split('-')
            nomeantigo = texto
            nomenovo = ''
            indice = listadevedores.index(nomeantigo)+2
        else:
            nomenovo = texto
            nomeantigo = ''
            indice = 0
        funcoes.atualizar_devedor(arquivo, opcao,indice, nomenovo)
        janela4 = Editar_planilha2(arquivo)
        janela3.close()
    if janelaativa == janela4 and evento =='Atualizar Dev.':
        arquivo = valor['-arquivo-']
        texto = valor['-devedor-']
        opcao = valor['-addouremovedevedor-']
        if opcao == 'Alterar':
            listadevedores = valor['-devedores-'].split('-')
            nomeantigo, nomenovo = texto.split()
            indice = listadevedores.index(nomeantigo)+2
        elif opcao == 'Remover':
            listadevedores = valor['-devedores-'].split('-')
            nomeantigo = texto
            nomenovo = ''
            indice = listadevedores.index(nomeantigo)+2
        else:
            nomenovo = texto
            nomeantigo = ''
            indice = 0
        funcoes.atualizar_devedor(arquivo, opcao,indice, nomenovo)
        janela5 = Editar_planilha3(arquivo)
        janela4.close()
    if janelaativa == janela5 and evento =='Atualizar Dev.':
        arquivo = valor['-arquivo-']
        texto = valor['-devedor-']
        opcao = valor['-addouremovedevedor-']
        if opcao == 'Alterar':
            listadevedores = valor['-devedores-'].split('-')
            nomeantigo, nomenovo = texto.split()
            indice = listadevedores.index(nomeantigo)+2
        elif opcao == 'Remover':
            listadevedores = valor['-devedores-'].split('-')
            nomeantigo = texto
            nomenovo = ''
            indice = listadevedores.index(nomeantigo)+2
        else:
            nomenovo = texto
            nomeantigo = ''
            indice = 0
        funcoes.atualizar_devedor(arquivo, opcao,indice, nomenovo)
        janela4 = Editar_planilha2(arquivo)
        janela5.close()
    if janelaativa == janela3 and evento == 'Atualizar Val.':
        arquivo = valor['-arquivo-']
        opcao = valor['-fixaouparcela-']
        nome = valor['-nomecompra-']
        listadevedores = valor['-devedores-'].split('-')
        valores = []
        if opcao == 'Fixa':
            for i in listadevedores:
                texto = 'Digite o valor para: ' + str(i)
                valores.append(popup_editarvalores(texto))
        elif opcao == 'Parcelada':
            listatemp = ['PARCELA ATUAL','TOTAL DE PARCELAS']
            listadevedores = listatemp + listadevedores
            for i in listadevedores:
                texto = 'Digite o valor para: ' + str(i)
                valores.append(popup_editarvalores(texto))

        funcoes.atualizar_valores(arquivo,opcao,nome,valores)
        janela4 = Editar_planilha2(arquivo)
        janela3.close()
    if janelaativa == janela4 and evento == 'Atualizar Val.':
        arquivo = valor['-arquivo-']
        opcao = valor['-fixaouparcela-']
        nome = valor['-nomecompra-']
        listadevedores = valor['-devedores-'].split('-')
        valores = []
        if opcao == 'Fixa':
            for i in listadevedores:
                texto = 'Digite o valor para: ' + str(i)
                valores.append(popup_editarvalores(texto))
        elif opcao == 'Parcelada':
            listatemp = ['PARCELA ATUAL','TOTAL DE PARCELAS']
            listadevedores = listatemp + listadevedores
            for i in listadevedores:
                texto = 'Digite o valor para: ' + str(i)
                valores.append(popup_editarvalores(texto))

        funcoes.atualizar_valores(arquivo,opcao,nome,valores)
        janela5 = Editar_planilha3(arquivo)
        janela4.close()
    if janelaativa == janela5 and evento == 'Atualizar Val.':
        arquivo = valor['-arquivo-']
        opcao = valor['-fixaouparcela-']
        nome = valor['-nomecompra-']
        listadevedores = valor['-devedores-'].split('-')
        valores = []
        if opcao == 'Fixa':
            for i in listadevedores:
                texto = 'Digite o valor para: ' + str(i)
                valores.append(popup_editarvalores(texto))
        elif opcao == 'Parcelada':
            listatemp = ['PARCELA ATUAL','TOTAL DE PARCELAS']
            listadevedores = listatemp + listadevedores
            for i in listadevedores:
                texto = 'Digite o valor para: ' + str(i)
                valores.append(popup_editarvalores(texto))

        funcoes.atualizar_valores(arquivo,opcao,nome,valores)
        janela4 = Editar_planilha2(arquivo)
        janela5.close()
    if janelaativa == janela3 and evento == sg.WIN_CLOSED:
        janela3.close()
        janela1.un_hide()
    if janelaativa == janela4 and evento == sg.WIN_CLOSED:
        janela4.close()
        janela1.un_hide()
    if janelaativa == janela5 and evento == sg.WIN_CLOSED:
        janela3.close()
        janela1.un_hide()    
    if janelaativa == janela7 and evento == sg.WIN_CLOSED:
        janela7.close()
        janela1.un_hide()
    if janelaativa == janela8 and evento == sg.WIN_CLOSED:
        janela8.close()
        janela1.un_hide()
    if janelaativa == janela9 and evento == sg.WIN_CLOSED:
        janela9.close()
        janela1.un_hide()
    if janelaativa == janela10 and evento == sg.WIN_CLOSED:
        janela10.close()
        janela1.un_hide()

    if janelaativa == janela7 and evento == 'Sair' or janelaativa == janela7 and evento == sg.WIN_CLOSED:
        janela7.close()
        janela1.un_hide()
    if janelaativa == janela7 and evento == 'Atualizar Demonstrativo':
        nomenovo = valor['-ano-'] + '_' +valor['-mesreferencia-']+ '_' + valor['-vencimento-'] + '_' +valor['-nomecartao-'] + '.csv'
        arquivo = valor['-arquivo-']
        status, arquivonovo = funcoes.atualizar_planilha(arquivo,nomenovo)
        if status == 'sucesso':
            sg.popup('Arquivo salvo com sucesso!')
            janela4 = Editar_planilha2(arquivonovo)
            janela7.close()
        else:
            sg.popup('Algo deu errado!!, verifique se os campos forasm corretamente preenchidos ou se o arquivo já existe :(')
    
    if janelaativa == janela8 and evento == 'Selecionar Pasta':
        caminho = sg.popup_get_folder("",no_window=True)
        nome = valor['-nome-']
        
        try:
            os.rename(os.getcwd() + '/tabelas/' + 'temp.csv', caminho +'//' + '_' + nome + '.csv')
            janela8.find_element('-textosucesso-').Update('Arquivo criado com sucesso! :D')
        except FileExistsError:
            janela8.find_element('-textosucesso-').Update('Arquivo já existe! tente alterar o nome do arquivo :(')
    if janelaativa == janela9 and evento == 'Selecionar Pasta':
        caminho = sg.popup_get_folder("",no_window=True)
        nome = valor['-nome-']
        
        try:
            os.rename(os.getcwd() + '/tabelas/' + 'temp.csv', caminho +'//' + '_' + nome + '.csv')
            janela9.find_element('-textosucesso-').Update('Arquivo criado com sucesso! :D')
        except FileExistsError:
            janela9.find_element('-textosucesso-').Update('Arquivo já existe! tente alterar o nome do arquivo :(')
    if janelaativa == janela10 and evento == 'Selecionar Pasta':
        caminho = sg.popup_get_folder("",no_window=True)
        nome = valor['-nome-']
        
        try:
            os.rename(os.getcwd() + '/tabelas/' + 'temp.csv', caminho +'//' + '_' + nome + '.csv')
            janela9.find_element('-textosucesso-').Update('Arquivo criado com sucesso! :D')
        except FileExistsError:
            janela9.find_element('-textosucesso-').Update('Arquivo já existe! tente alterar o nome do arquivo :(')
    
    
        nome = valor['-conta-']
        valorconta = valor['-valor-']
        tipo = valor['-tipocompra-']
        juros = valor['-juros-']
        arquivo = ['-arquivo-']
        funcoes.add_conta(arquivo, nome, valorconta, tipo, juros)
