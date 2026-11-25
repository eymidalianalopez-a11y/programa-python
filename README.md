# Fase 5 - Evaluación Final POA

**Universidad Nacional Abierta y a Distancia - UNAD**
Curso: Fundamentos de Programación (213022) - Ingeniería de Sistemas

## Problema 1: Nivel de compromiso de sesiones de clientes

Una matriz almacena sesiones de clientes con el formato
`[ID del cliente, Duración (segundos), Número de clics]`.
El programa clasifica cada sesión y muestra un informe con el ID del cliente
y su clasificación final de compromiso.

### Reglas de negocio

| Nivel | Condición |
|-------|-----------|
| Alto  | Duración > 180 s **y** clics > 8 |
| Bajo  | Duración < 60 s **o** clics < 3 |
| Medio | Cualquier otro caso |

### Estructura del programa

- `clasificar_compromiso(duracion, clics)`: función con la lógica de negocio (if / elif / else).
- `mostrar_informe(matriz)`: recorre la matriz con un ciclo `for`, clasifica cada sesión e imprime el informe.
- `main()`: define la matriz inicial (7 sesiones) y muestra el resumen por nivel.

## Ejecución

Requiere Python 3.

```bash
python problema1_compromiso_sesiones.py
```

### Salida esperada

```
ID Cliente     Compromiso
101            Alto
102            Bajo
103            Medio
104            Bajo
105            Medio
106            Medio
107            Alto

Resumen de sesiones por nivel de compromiso:
  Alto: 2
  Medio: 3
  Bajo: 2
```

## Autor

Brayan Elias Carrillo Chaparro
