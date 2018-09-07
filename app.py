from flask import Flask, render_template
import requests
import json
app = Flask(__name__)



@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

url = "https://www.pokeapi.co/api/v2/pokemon/"

@app.route('/pokemon/<int:id>', methods=['GET', 'POST'])
def ider(id):
    #get name
    urlid = ''.join([url,str(id)])
    r = requests.get(urlid)
    data = r.json()
    name = data["name"]
    return render_template("templateid.html",id=id, name = name)

@app.route('/pokemon/<name>', methods=['GET', 'POST'])
def namer(name):
    #get id 
    urln = ''.join([url,str(name)])
    r = requests.get(urln)
    data = r.json()
    id = data["id"]
    return render_template("templatename.html",id=id, name = name)



if __name__ == '__main__':
    app.run()

