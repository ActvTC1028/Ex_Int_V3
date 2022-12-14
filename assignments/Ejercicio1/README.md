![Tec de Monterrey](../../images/logotecmty.png)
# Coinciden en las dos listas y tienen x número de caracteres
## Involucra ciclos, listas, condicionales

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
# Area de funciones aquí

def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Diseña e implementa un programa que recibe datos para conformar dos listas de palabras de n elementos, las despliega a pantalla y posteriormente crea una lista con los datos que coinciden en las dos listas y que tienen x número de caracteres y la despliega. Para lo anterior **DEBES CREAR** las siguientes funciones en tu programa:

Función **crea_lista** la cual recibe como parámetro la cantidad de elementos a recibir para conformar la lista. La función recibe las n palabras o frases del usuario y va creando una lista con ellas. El mensaje para pedirlas será: **">>> "**. La función deberá **regresar** la lista como resultado de la función.

Función **coinciden** la cual recibe como parámetro dos listas y un valor entero, la función crea una lista con las palabras que coinciden (elementos que están en las dos listas) y que ademas tienen x número de caracteres. La función **regresa** la lista creada. TIP: Recorre una lista y ve si sus elementos están en la segunda y tienen además x número de caracteres

En el **main**, pide al usuario cuántas palabras habrá en cada lista con el mensaje **"Cuantas palabras por lista: "**. Despliega el mensaje **"Ingresa los datos para la lista 1"**. Manda a llamar la función correspondiente para recibir esa cantidad de datos y guarda el resultado y despliegalo a pantalla. Luego despliega el mensaje **"Ingresa los datos para la lista 2"**. Manda a llamar la función correspondiente para recibir esa cantidad de datos y guarda el resultado y despliegalo. Ahora pide el número de caracteres y posteriormente usa la función que recibe las dos listas (manda las dos listas creadas anteriormente) y el número de caracteres y despliega a pantalla el resultado de la función.

## Ejemplo de ejecución del programa
```
Cuántas palabras por lista: 3
Ingresa los datos para la lista 1
>>> pelota
>>> carro
>>> juguete
Ingresa los datos para la lista 2
['pelota', 'carro', 'juguete']
>>> carro
>>> pelota
>>> escondidas
['carro', 'pelota', 'escondidas']
Número de caracteres: 5
['carro']
```
.


**Nota:** No cambies ni quites el código `if __name__ == '__main__':` 

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
