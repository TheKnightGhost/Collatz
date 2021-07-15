from flask import Flask, request, jsonify, session
import json

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'esto-es-una-clave-muy-secreta'

@app.route('/')
def server_info():

    try:

        bd = open("bd.txt", "r")

        if bd:
            bd = open("bd.txt")
            contenido = bd.read()

            if contenido != "":
                bd.close()
                return contenido
            else:
                return 'no se ha ingresado ningun dato'

        else:
            print('Error')
            return 'Hubo un problemas al consultar la informacion'

    except Exception as error:
        print(error)
        return 'ha ocurrido un error'

    # if 'data' in session:
    #     return "se guardo la siguiente secuencia: " + session['data']
    # else:
    #     return "no se ha ingresado ningun dato"


@app.route('/secuencia/<int:n>', methods=["GET", "POST"])
def entrada(n):
    try:

        collatz = list()
        lista = []

        while n != 1 :
            collatz.append(n) 
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        collatz.append(1)  
        l = len(collatz)
        contador = 0

        for i in range(0, l):
            lista.append({
                f'{contador}' : collatz[i]
            })
            contador += 1

        x = {
            'secuencia' : lista
        }

        vl_json = json.dumps(str(x))
        # session['data'] = vl_json

        bd = open("bd.txt", "w")

        if bd:

            bd.write(vl_json)
            bd = open("bd.txt")
            # contenido = bd.read()

            bd.close()
            # print(contenido)

            return vl_json

        else:
            print('Error')
            return 'Hubo un problemas de conexion con la BD'

    except Exception as error:
        print(error)
        print("Ha ocurrido un problema al ejecutar la peticion")

if __name__ == "__main__":
    app.run(debug = True)

    
