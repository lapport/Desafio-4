cor = {'limpo': '\033[m',
       'branco': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'roxo': '\033[35m',
       'ciano': '\033[36m'}


def leiaint(msg):
    while True:
        try:
            n = int(input(f'{cor["ciano"]}{msg}{cor["verde"]}'))
        except (ValueError, TypeError):
            print(f'{cor["vermelho"]}ERRO, DIGITE UM VALOR INTEIRO VALIDO!!{cor["limpo"]}')
        except KeyboardInterrupt:
            print(f'{cor["vermelho"]}O USUARIO PREFERIU NÃO DIGITAR ESSE NUMERO.{cor["limpo"]}')
            return 0
        else:
            return n


def linha(tam=50):
        return f'—' * tam
    
    
def cabeçalho(txt):
    print(cor['roxo'])
    print(linha())
    print(f'{txt.center(50)}')
    print(linha())
    

def menu(nome, opçoes):
    cabeçalho(nome)
    c = 1
    for item in opçoes:
        print(f'{c}-{item}')
        c+=1
    while True:
        print(cor['roxo'],linha(),cor['limpo'])
        opc = leiaint(f'{cor["ciano"]}Sua opção: {cor["verde"]}')
        if opc > len(opçoes) or opc <= 0:
            print(f'{cor["vermelho"]}ERRO EM:"{opc}",DIGITE UMA OPÇÃO VALIDA{cor["limpo"]}')
        else:
            break
    return opc
