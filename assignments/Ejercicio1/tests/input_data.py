# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["3","gato", "perro", "jabali", "ardilla", "perro", "oso", 5],
    ["Cuántas palabras por lista: ","Ingresa los datos para la lista 1",">>> ", ">>> ", ">>> ", "['gato', 'perro', 'jabali']",
    "Ingresa los datos para la lista 2", ">>> ", ">>> ", ">>> ", "['ardilla', 'perro', 'oso']", "Número de caracteres: ", "['perro']"],
    ["La salida no cumple con el caso de prueba."]
    ),
    # Test case 2
    (
     ["2","gato", "perro", "gato", "ardilla",3],
    ["Cuántas palabras por lista: ","Ingresa los datos para la lista 1",">>> ", ">>> ", "['gato', 'perro']", "Ingresa los datos para la lista 2",
    ">>> ", ">>> ", "['gato', 'ardilla']", "Número de caracteres: ", "[]"],
    ["La salida no cumple con el caso de prueba."]
    )
    ]
