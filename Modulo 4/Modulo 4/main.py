import redis
import json

# Conexión a KeyDB
client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Función para agregar una receta
def agregar_receta():
    nombre = input("Introduce el nombre de la receta: ")

    receta = {
        "nombre": nombre,
        "ingredientes": [],
        "pasos": []
    }

    print("\n--- Ingredientes ---")
    while True:
        ingrediente = input("Introduce un ingrediente (deja vacío para terminar): ")
        if ingrediente == "":
            break
        receta["ingredientes"].append(ingrediente)

    print("\n--- Pasos ---")
    while True:
        paso = input("Introduce un paso (deja vacío para terminar): ")
        if paso == "":
            break
        receta["pasos"].append(paso)

    # Guardar la receta en KeyDB
    # Usamos el nombre de la receta como la clave y el valor como el JSON serializado
    client.set(nombre, json.dumps(receta))
    print("Receta agregada con éxito.")

# Función para ver las recetas
def ver_recetas():
    # Obtener todas las claves (recetas) almacenadas
    recetas_keys = client.keys()

    if recetas_keys:
        print("\n--- Listado de recetas ---")
        for key in recetas_keys:
            receta = json.loads(client.get(key))
            print(f"Nombre: {receta['nombre']}")
            print("Ingredientes:")
            for ingrediente in receta['ingredientes']:
                print(f"  - {ingrediente}")
            print("Pasos:")
            for paso in receta['pasos']:
                print(f"  - {paso}")
            print("\n")
    else:
        print("No hay recetas registradas.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("a) Agregar nueva receta")
        print("b) Ver listado de recetas")
        print("f) Salir")

        opcion = input("Selecciona una opción: ").lower()

        if opcion == 'a':
            agregar_receta()
        elif opcion == 'b':
            ver_recetas()
        elif opcion == 'f':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()
