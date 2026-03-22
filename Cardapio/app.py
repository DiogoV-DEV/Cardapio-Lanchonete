from flask import Flask, render_template

app = Flask(__name__)

cardapio = {
    "Salgados": [
        {"nome": "Pastel de Carne", "preco": 8},
        {"nome": "Pastel de Queijo", "preco": 7},
        {"nome": "Coxinha", "preco": 6}
    ],
    "Doces": [
        {"nome": "Brigadeiro", "preco": 3},
        {"nome": "Pudim", "preco": 5}
    ],
    "Bebidas": [
        {"nome": "Coca-Cola", "preco": 6},
        {"nome": "Guaraná", "preco": 5},
        {"nome": "Suco", "preco": 5}
    ]
}

@app.route("/")
def cardapio_page():
    return render_template("cardapio.html", cardapio=cardapio)

if __name__ == "__main__":
    app.run(debug=True)