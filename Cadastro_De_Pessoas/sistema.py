from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'Cadastro_v1.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu (['Cadastrar Pessoa', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\33[31m3ERRO! Digite uma opção valida!\33[m')
    sleep(2.5)

