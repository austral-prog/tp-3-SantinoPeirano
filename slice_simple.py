def slice_simple():
    texto = "Awesome"
  
    texto = texto.lower()
    
    medio = int(len(texto)/2)

    print(texto [0:3])
    print(texto [medio-1:medio+2])
    print(texto)

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
