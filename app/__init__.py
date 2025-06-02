from flask import Flask, render_template, request

app = Flask(__name__)

# Rota da Home
@app.route('/')
def home():
    return render_template('home.html')

# Rota Sobre + Depoimentos (juntas numa página)
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota Conteúdo do Curso
@app.route('/curso')
def curso():
    return render_template('curso.html')

# Rota Contato

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        # Dados do formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')

        # Aqui você processa o que quiser (ex: enviar e-mail real, salvar no banco, etc.)
        print(f"Nome: {nome}, Email: {email}, Mensagem: {mensagem}")

        # Depois pode retornar um HTML de sucesso ou a mesma página com mensagem
        return render_template('contato.html', sucesso=True)

    # Se for GET (primeiro acesso à página)
    return render_template('contato.html')
