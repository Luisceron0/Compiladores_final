# DSL para Consultas de Empleados con ANTLR4 y Python

Este proyecto implementa un Lenguaje de Dominio Específico (DSL) para realizar consultas sobre datos de empleados almacenados en formato CSV. El proyecto utiliza ANTLR4 para el análisis léxico y sintáctico, y Python para la interpretación de las consultas.

## Descripción del Proyecto

El DSL permite:
- Cargar datos desde archivos CSV
- Aplicar filtros sobre diferentes campos
- Realizar operaciones de agregación (count, sum, average)
- Ordenar datos
- Imprimir resultados

Las operaciones se acumulan y se ejecutan de manera diferida hasta que se encuentra un comando `print;`.

## Estructura del Proyecto

```
proyecto/
├── EmployeeDSL.g4               # Gramática ANTLR4 para el DSL
├── employee_dsl_interpreter.py  # Intérprete del DSL
├── generate_employee_data.py    # Generador de datos sintéticos
├── example_scripts.txt          # 40 scripts de ejemplo
├── main.py                      # Script principal para ejecutar consultas
├── scripts/                     # Directorio de scripts individuales
├── empleados.csv                # Datos generados de empleados
└── README.md                    # Este archivo
```

## Requisitos de Instalación

1. Python 3.7 o superior
2. ANTLR4 runtime para Python
3. pandas
4. numpy

Instalar dependencias:

```bash
pip install antlr4-python3-runtime pandas numpy
```

## Generación de Parser con ANTLR4

Si necesitas regenerar el parser:

1. Descarga ANTLR4:
   ```bash
   curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
   ```

2. Genera el parser:
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 EmployeeDSL.g4
   ```

## Pasos para Ejecutar el Proyecto

### 1. Generar datos de prueba

```bash
python generate_employee_data.py
```

Esto creará un archivo `empleados.csv` con 300 registros de empleados.

### 2. Extraer los scripts de ejemplo

```bash
python main.py extract
```

Esto extraerá los 40 scripts de ejemplo del archivo `example_scripts.txt` y los guardará como archivos individuales en el directorio `scripts/`.

### 3. Ejecutar scripts

#### Ejecutar todos los scripts de ejemplo:

```bash
python main.py run-all
```

#### Ejecutar un script específico (por ejemplo, el script 5):

```bash
python main.py run 5
```

#### Ejecutar en modo interactivo:

```bash
python main.py interactive
```

En el modo interactivo, puedes escribir comandos DSL línea por línea y ver los resultados inmediatamente después de un comando `print;`.

## Sintaxis del DSL

### Comandos básicos:

- **load**: Carga un archivo CSV
  ```
  load "empleados.csv";
  ```

- **filter**: Aplica un filtro a los datos
  ```
  filter column "edad" > 25;
  filter column "departamento" == "Tecnología";
  filter column "salario" between 3000 and 4000;
  ```

- **aggregate**: Realiza una operación de agregación
  ```
  aggregate count column "id_empleado";
  aggregate sum column "dias_laborados";
  aggregate average column "salario";
  ```

- **sort**: Ordena los datos
  ```
  sort column "salario" desc;
  sort column "edad" asc;
  ```

- **print**: Ejecuta todas las operaciones acumuladas y muestra los resultados
  ```
  print;
  ```

### Operadores soportados:

- Comparación: `>`, `<`, `>=`, `<=`, `==`, `!=`
- Rango: `between`
- Lógicos: `and`, `or`

## Parse Tree

Para visualizar el Parse Tree de un script específico, se puede utilizar la herramienta GUI de ANTLR4:

```bash
java -cp antlr-4.13.1-complete.jar org.antlr.v4.gui.TestRig EmployeeDSL program -gui scripts/script_01.dsl
```

## Detalles de Implementación

1. **Gramática ANTLR4**: Define la sintaxis del DSL, incluyendo reglas para comandos, filtros, agregaciones, y operadores.

2. **Intérprete**: Implementa un visitante que recorre el árbol sintáctico y acumula las operaciones para ejecutarlas cuando se encuentra un comando `print;`.

3. **Conversión JSON**: Los datos se cargan desde CSV y se convierten internamente a formato JSON para facilitar su manipulación y consulta.

4. **Ejecución Diferida**: Las operaciones de filtrado, agregación y ordenamiento se acumulan y solo se ejecutan cuando se encuentra un comando `print;`.

## Ejemplos

### Ejemplo 1: Filtrar empleados mayores de 25 años

```
load "empleados.csv";
filter column "edad" > 25;
aggregate count column "id_empleado";
aggregate average column "salario";
aggregate sum column "dias_laborados";
print;
```

### Ejemplo 2: Filtrar empleados de Tecnología con alto salario

```
load "empleados.csv";
filter column "departamento" == "Tecnología";
filter column "salario" > 3000;
aggregate count column "id_empleado";
aggregate average column "edad";
print;
```

### Ejemplo 3: Rango salarial específico

```
load "empleados.csv";
filter column "salario" between 3000 and 4000;
aggregate count column "id_empleado";
aggregate average column "edad";
print;
```
