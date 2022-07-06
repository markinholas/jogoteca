from flask import Flask, render_template

class jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = jogo("God of War", "Ação", "Playstation")
jogo2 = jogo("Cs:Go","Tiro", "PC")
jogo3 = jogo("Minecraft", "Construção", "PC")

lista1 =  (jogo1, jogo2, jogo3)

app = Flask(__name__)

lista = ['God of War', 'LoL', 'Batman']

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista1)

app.run()