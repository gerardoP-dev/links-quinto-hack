"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    lista_vacia=[]
    texto_cambiado = ['F', '0', '0', 'Z', '1', 'M', '@', 'N']
    for i in range(len(result)):
        lista_vacia.append(texto_cambiado[i])

    result = lista_vacia
    return result  

print(fn_hack_10())