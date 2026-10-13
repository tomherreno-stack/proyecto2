# Calculadora y Clasificador de IMC 
# determina su clasificación y muestra una recomendación general.
# Autor: Thomas Alejandro Herreno Sanchez
# Fecha: 2026-10-09


# Función para calcular el IMC
def calcular_imc(peso, estatura) -> float:
    imc = peso / (estatura ** 2)
    return round(imc, 2)


# Función para determinar la clasificación del IMC
def clasificar_imc(imc) -> str:
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25.0:
        return "Peso saludable"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidad"


# Función para obtener una recomendación general
def obtener_recomendacion(clasificacion) -> str:
    if clasificacion == "Bajo peso":
        return "Procure mantener una alimentación equilibrada y consulte a un profesional de la salud."

    elif clasificacion == "Peso saludable":
        return "Mantenga una alimentación equilibrada y realice actividad física regularmente."

    elif clasificacion == "Sobrepeso":
        return "Mejore sus hábitos de alimentación y aumente la actividad física con orientación profesional."

    else:
        return "Consulte a un profesional de la salud para recibir una valoración y orientación adecuada."


# Función para ingresar el peso y la estatura
def ingresar_datos() -> tuple:
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        estatura = float(input("Ingrese su estatura en metros: "))
        return peso, estatura
    except ValueError:
        # Si ingresan texto, retornamos ceros para que validar_datos() se encargue del resto
        return 0.0, 0.0


# Función para validar que el peso y la estatura sean mayores que cero
def validar_datos(peso, estatura) -> bool:
    if peso <= 0 or estatura <= 0:
        print("DATOS INVÁLIDOS: el peso y la estatura deben ser mayores que cero.")
        return False

    return True


# Función para mostrar el IMC, la clasificación y la recomendación
def mostrar_resultado(peso, estatura) -> None:
    imc = calcular_imc(peso, estatura)
    clasificacion = clasificar_imc(imc)
    recomendacion = obtener_recomendacion(clasificacion)

    print("\n--- Resultado del IMC ---")
    print(f"Peso: {peso:.2f} kg")
    print(f"Estatura: {estatura:.2f} m")
    print(f"IMC: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")
    print(f"Recomendación: {recomendacion}")


# Función principal 
if __name__ == "__main__":
    # Menú principal 
    while True:
        # Solicitar el peso y la estatura
        print("\n--- Calculadora y Clasificador de IMC ---")
        datos = ingresar_datos()

        # Validar los datos y mostrar el resultado
        if validar_datos(*datos):
            mostrar_resultado(*datos)
        else:
            print("Por favor, intente nuevamente.")
            continue  # <--- Regresa al inicio del ciclo sin preguntar si desea continuar

        # Preguntar si el usuario desea continuar
        print("\nÚnicamente se aceptará 's' para continuar;")
        print("cualquier otra entrada terminará el programa.")
        continuar = input("¿Desea calcular otro IMC? (s/n): ").strip().lower()
        if continuar != "s":
            print("Gracias por usar la calculadora de IMC. ¡Hasta luego!")
            break