from flask import Flask, render_template
import json
import pymysql.cursors

app = Flask(__name__)
conn = pymysql.connect(host='localhost',
                             user='thallis',
                             password='teste123',
                             db='dbteste',
                             cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/produtos', methods=['GET'])
def produtos():
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps(result)
    finally:
        conn.close()


@app.route('/listas')
def listas():
    response = 'Bool!'
    list = ['Gabriel', 'Heloisa', 'Thallis', 'Will', 'Marcinho', 'Cleiison']
    nomes = []
    for nome in list:
        nomes.append(nome)
        for letra in nome:
            print(letra)
        print(nome)
    print(nomes)
    return json.dumps(list, indent=4)


if __name__ == '__main__':
    app.run()
