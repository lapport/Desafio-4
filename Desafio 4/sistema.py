from Interface.__init__ import *
import requests


API_URL = 'http://localhost:5000/characters/'  # URL da sua API


def adcicionar_api(nome, descricao, link, programa, animador):
    data = {
        'nome': nome,
        'descrição': descricao,
        'link': link,
        'programa': programa,
        'animador': animador
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        print("Personagem adicionado com sucesso à API.")
    else:
        print("Falha ao adicionar personagem à API.")


def ver_personagens_api():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Falha ao recuperar personagens da API.")
        return []


def mostrar_personagens():
        personagens = ver_personagens_api()
        if personagens:
            print("\nLista de Personagens Cadastrados na API:")
            for idx, personagem in enumerate(personagens, start=1):
                print(f"\nPersonagem {idx}:")
                for chave, valor in personagem.items():
                    print(f"{chave}: {valor}")
        else:
            print("Nenhum personagem cadastrado na API.")


def deletar_personagem_api(index):
    url = f"{API_URL}{index}/"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Personagem deletado com sucesso da API.")
    else:
        print("Falha ao deletar personagem da API.")


def ver_link_personagem_api(index):
    url = f"{API_URL}{index}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        link = data.get('link')
        if link:
            print(f"Link do personagem {index + 1}: {link}")
        else:
            print("O personagem não possui um link associado.")
    else:
        print("Falha ao recuperar link do personagem da API.")


def main():
    while True:
        resposta = menu('Menu Principal', ['Adicionar personagem', 'Ver personagens', 'Deletar personagem', 'Ver link do personagem', 'Sair'])
        if resposta == 1:
            nome = input('Nome do personagem: ')
            descricao = input('Descrição do personagem: ')
            link = input('Link: ')
            programa = input('Programa: ')
            animador = input('Animador: ')
            adcicionar_api(nome, descricao, link, programa, animador)

        elif resposta == 2:
           mostrar_personagens()

        elif resposta == 3:
            mostrar_personagens()
            index = int(input("Informe o índice do personagem que deseja deletar: "))
            deletar_personagem_api(index - 1)

        elif resposta == 4:
            mostrar_personagens()
            index = int(input("Informe o índice do personagem que deseja ver o link: "))
            ver_link_personagem_api(index - 1)

        elif resposta == 5:
            print('Finalizado')
            break

print('IMPORTANTE INICIAR A API EM UM SERVIDOR DEDICADO')
if __name__ == "__main__":
    main()