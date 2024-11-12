"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    numeros = 5

    while numeros >= 0:
        result.append(numeros)
        numeros -= 1
    return result  

print(fn_hack_7())