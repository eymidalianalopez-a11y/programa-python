"""
Universidad Nacional Abierta y a Distancia - UNAD
Curso: Fundamentos de Programación (213022)
Fase 5 - Evaluación Final POA
Problema 1: Nivel de compromiso de sesiones de clientes

Descripción:
    Una matriz almacena sesiones de clientes en una plataforma digital con el
    formato [ID del cliente, Duración (segundos), Número de clics].
    El programa clasifica el nivel de compromiso de cada sesión como
    "Alto", "Medio" o "Bajo" y muestra un informe con el ID del cliente
    y su clasificación final.

Autor: Brayan Elias Carrillo Chaparro
"""

# ---------------------------------------------------------------------------
# CONSTANTES (umbrales de la lógica de negocio)
# ---------------------------------------------------------------------------
DURACION_ALTA = 180   # segundos: más de este valor cuenta para "Alto"
CLICS_ALTO = 8        # clics: más de este valor cuenta para "Alto"
DURACION_BAJA = 60    # segundos: menos de este valor implica "Bajo"
CLICS_BAJO = 3        # clics: menos de este valor implica "Bajo"

# Posiciones de cada dato dentro de una fila de la matriz
POS_ID = 0
POS_DURACION = 1
POS_CLICS = 2


# ---------------------------------------------------------------------------
# MÓDULO (función) DE CLASIFICACIÓN
# ---------------------------------------------------------------------------
def clasificar_compromiso(duracion, clics):
    """Devuelve "Alto", "Medio" o "Bajo" según la duración y los clics.

    Reglas:
      - Alto : duración > 180 segundos Y clics > 8
      - Bajo : duración < 60 segundos O clics < 3
      - Medio: cualquier otro caso
    """
    if duracion > DURACION_ALTA and clics > CLICS_ALTO:
        return "Alto"
    elif duracion < DURACION_BAJA or clics < CLICS_BAJO:
        return "Bajo"
    else:
        return "Medio"


# ---------------------------------------------------------------------------
# MÓDULO (procedimiento) QUE GENERA EL INFORME
# ---------------------------------------------------------------------------
def mostrar_informe(matriz):
    """Recorre la matriz, clasifica cada sesión e imprime el informe.

    Devuelve un diccionario con la cantidad de sesiones por clasificación.
    """
    conteo = {"Alto": 0, "Medio": 0, "Bajo": 0}

    print("=" * 40)
    print("   INFORME DE COMPROMISO DE SESIONES")
    print("=" * 40)
    print(f"{'ID Cliente':<15}{'Compromiso':<15}")
    print("-" * 40)

    for sesion in matriz:
        id_cliente = sesion[POS_ID]
        duracion = sesion[POS_DURACION]
        clics = sesion[POS_CLICS]

        nivel = clasificar_compromiso(duracion, clics)
        conteo[nivel] += 1

        print(f"{id_cliente:<15}{nivel:<15}")

    print("=" * 40)
    return conteo


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------
def main():
    # Matriz inicial: [ID del cliente, Duración (s), Número de clics]
    sesiones = [
        [101, 240, 12],   # Alto: duración > 180 y clics > 8
        [102, 45, 10],    # Bajo: duración < 60
        [103, 150, 5],    # Medio
        [104, 200, 2],    # Bajo: clics < 3
        [105, 90, 6],     # Medio
        [106, 180, 8],    # Medio: valores límite (no superan los umbrales)
        [107, 300, 9],    # Alto
    ]

    conteo = mostrar_informe(sesiones)

    print("\nResumen de sesiones por nivel de compromiso:")
    for nivel in conteo:
        print(f"  {nivel}: {conteo[nivel]}")


if __name__ == "__main__":
    main()
