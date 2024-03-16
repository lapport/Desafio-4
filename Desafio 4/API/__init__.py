from flask import Flask, jsonify, request
import webbrowser

app = Flask(__name__)

lista = []


def adcicionar(nome, descrição, link, programa, animador):
    personagem = {'Nome': nome,
                  'descrição': descrição,
                  'link': link,
                  'programa': programa,
                  'animador': animador}
    lista.append(personagem)


def mostrar():
    return jsonify(lista)


def web(url):
    navegador = webbrowser.get()
    navegador.open(url)


@app.route('/characters/', methods=['POST'])
def adicionar_personagem():
    data = request.get_json()
    adcicionar(data['nome'], data['descrição'], data['link'], data['programa'], data['animador'])
    return jsonify({"message": "Personagem adicionado com sucesso."}), 201


@app.route('/characters/', methods=['GET'])
def listar_personagens():
    return mostrar()


@app.route('/characters/<int:index>/', methods=['GET'])
def ver_personagem(index):
    if index >= len(lista) or index < 0:
        return jsonify({"error": "Personagem não encontrado."}), 404
    else:
        url = lista[index]['link']
        web(url)
        return jsonify(lista[index])


@app.route('/characters/<int:index>/', methods=['DELETE'])
def deletar_personagem(index):
    if index >= 0 and index < len(lista):
        del lista[index]
        return jsonify({"message": "Personagem deletado com sucesso."}), 200
    else:
        return jsonify({"error": "Personagem não encontrado."}), 404


if __name__ == '__main__':
    app.run(debug=True)