from flask import Flask, render_template, request, redirect

class cadfilmes:
    def __init__(self,idfilme, titulo, lancamento , diretor, origem, classificacao):
        self.idfilme = idfilme
        self.titulo = titulo
        self.lancamento = lancamento
        self.diretor = diretor
        self.origem = origem
        self.classificacao = classificacao

lista = []

app = Flask(__name__)



@app.route('/')
def cadastro():
    return render_template('cadastro.html', Titulo='Cadastro de Filmes')

@app.route('/criar', methods=['POST'])
def criar():
    idfilme = request.form['ID-Filmes']
    titulo = request.form['TituloFilme']
    lancamento = request.form['Lancamento']
    diretor = request.form['DiretorFilme']
    origem = request.form['Origem']
    classificacao = request.form['Idade']
    obj = cadfilmes(idfilme, titulo, lancamento , diretor, origem, classificacao)
    lista.append(obj)
    return redirect('/filmes')

@app.route('/filmes')
def filmes():
    return render_template('filmes.html', Titulo='Filmes Cadastrados', ListaFilme=lista)

@app.route('/excluir/<IDfilmes>', methods=['GET', 'DELET'])
def excluir(IDfilmes):
    for i, flm in enumerate(lista):
        if flm.idfilme == IDfilmes:
            lista.pop(i)
            break
    return redirect('/')

@app.route('/editar/<IDfilmes>', methods=['GET'])
def editar(IDfilmes):
    for i, flm in enumerate(lista):
        if flm.idfilme == IDfilmes:
            return render_template("editar.html", Titulo='Editar Filmes', Filmes=flm)

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    id = request.form['ID-Filmes']
    for i, flm in enumerate(lista):
        if flm.idfilme == id:
            flm.titulo = request.form['TituloFilme']
            flm.lancamento = request.form['Lancamento']
            flm.diretor = request.form['DiretorFilme']
            flm.origem = request.form['Origem']
            flm.classificacao = request.form['Idade']
        return redirect('/filmes')

if __name__ == '__main__':
    app.run()
