import urllib.request, json

with urllib.request.urlopen("http://127.0.0.1:5000") as url:
    try:
        data = url.read()
        if data:
            print(json.loads(data))
            # print(data)
    except Exception as error:
        print('Ha ocurrido un problema al consultar el servicio')
        
