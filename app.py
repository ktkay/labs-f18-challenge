from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<string:query>', methods=['GET'])
def pokemon(query):
    response = requests.get('http://pokeapi.co/api/v2/pokemon/'+str(query)+'/')
    return render_template('pokemon.html', response = response.json(), query = query)

if __name__ == '__main__':
    app.run()
