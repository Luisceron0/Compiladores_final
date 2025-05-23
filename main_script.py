import os
import sys
import json
from employee_dsl_interpreter import parse_and_interpret

def print_result(result, script_name):
    """Format and print the execution result"""
    print(f"\n{'=' * 50}")
    print(f"Ejecutando: {script_name}")
    print(f"{'=' * 50}")
    
    # Print number of records
    print(f"Registros encontrados: {result['record_count']}")
    
    # Print aggregations
    if result['aggregations']:
        print("\nAgregaciones:")
        for agg_name, agg_value in result['aggregations'].items():
            # Format the function and column name
            parts = agg_name.split('_', 1)
            func = parts[0]
            column = parts[1] if len(parts) > 1 else ""
            
            # Format the value based on the type
            if func == 'count':
                formatted_value = f"{agg_value}"
            elif func == 'sum':
                formatted_value = f"{agg_value:.2f}"
            elif func == 'average':
                formatted_value = f"{agg_value:.2f}"
            else:
                formatted_value = str(agg_value)
                
            print(f"{func.capitalize()} de {column}: {formatted_value}")
    
    # Print first few records of filtered data
    if result['record_count'] > 0:
        print("\nPrimeros 5 registros:")
        for i, record in enumerate(result['filtered_data'][:5]):
            print(f"{i+1}. {json.dumps(record, ensure_ascii=False)}")
    
    # If there are more records, indicate how many more
    if result['record_count'] > 5:
        print(f"... y {result['record_count'] - 5} registros más.")
    
    print(f"{'=' * 50}\n")

def run_script_file(script_file):
    """Run a script from a file"""
    with open(script_file, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    try:
        result = parse_and_interpret(script_content)
        print_result(result, script_file)
        return True
    except Exception as e:
        print(f"Error al ejecutar el script {script_file}: {str(e)}")
        return False

def run_example_scripts(scripts_dir='scripts'):
    """Run all script files in the specified directory"""
    # Create scripts directory if it doesn't exist
    if not os.path.exists(scripts_dir):
        os.makedirs(scripts_dir)
        print(f"Directorio '{scripts_dir}' creado. Por favor, coloque los scripts DSL aquí.")
        return
    
    # Get all script files
    script_files = [f for f in os.listdir(scripts_dir) if f.endswith('.dsl')]
    
    if not script_files:
        print(f"No se encontraron archivos .dsl en el directorio '{scripts_dir}'")
        return
    
    # Run each script
    success_count = 0
    for script_file in sorted(script_files):
        full_path = os.path.join(scripts_dir, script_file)
        if run_script_file(full_path):
            success_count += 1
    
    print(f"\nEjecución completada: {success_count} de {len(script_files)} scripts ejecutados correctamente.")

def run_scripts_from_json(example_file='example_scripts.json'):
    """Run all scripts directly from the JSON file"""
    if not os.path.exists(example_file):
        print(f"El archivo de ejemplos '{example_file}' no existe.")
        return
    
    with open(example_file, 'r', encoding='utf-8') as f:
        scripts = json.load(f)
    
    success_count = 0
    for script in scripts:
        script_content = script.get('contenido', '')
        script_num = script.get('numero', 'unknown')
        script_title = script.get('titulo', 'Sin título')
        try:
            result = parse_and_interpret(script_content)
            print_result(result, f"Script {script_num}: {script_title}")
            success_count += 1
        except Exception as e:
            print(f"Error al ejecutar el script {script_num}: {str(e)}")
    
    print(f"\nEjecución completada: {success_count} de {len(scripts)} scripts ejecutados correctamente.")


def extract_examples_to_files(example_file='example_scripts.json', output_dir='scripts'):
    """Extract individual scripts from the JSON file and save them as separate .dsl files"""
    import json

    if not os.path.exists(example_file):
        print(f"El archivo de ejemplos '{example_file}' no existe.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(example_file, 'r', encoding='utf-8') as f:
        scripts = json.load(f)

    for script in scripts:
        num = str(script['numero']).zfill(2)
        content = script['contenido']
        filename = os.path.join(output_dir, f"script_{num}.dsl")
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(content)
        print(f"Script {num} extraído a {filename}")


def run_specific_script(script_number, scripts_dir='scripts'):
    """Run a specific script by number"""
    script_file = f"{scripts_dir}/script_{script_number.zfill(2)}.dsl"
    if os.path.exists(script_file):
        run_script_file(script_file)
    else:
        print(f"El script {script_number} no existe en '{script_file}'")

def interactive_mode():
    """Run in interactive mode"""
    print("Modo interactivo del DSL para Empleados")
    print("Ingrese comandos DSL línea por línea. Escriba 'exit' para salir.")
    
    script = ""
    prompt = ">> "
    
    while True:
        line = input(prompt)
        if line.lower() == 'exit':
            break
        
        script += line + "\n"
        
        # Check if the command is complete (ends with semicolon)
        if line.strip().endswith(';'):
            # Check if it's a print command
            if line.strip().startswith('print'):
                try:
                    result = parse_and_interpret(script)
                    print_result(result, "Consulta interactiva")
                    script = ""  # Reset for the next query
                except Exception as e:
                    print(f"Error: {str(e)}")
                    script = ""  # Reset after error
    
    print("Saliendo del modo interactivo.")

import os
import sys
import json
import pandas as pd
from antlr4 import *
from EmployeeDSLLexer import EmployeeDSLLexer
from EmployeeDSLParser import EmployeeDSLParser
from EmployeeDSLVisitor import EmployeeDSLVisitor

def print_result(result, script_name):
    """Format and print the execution result"""
    print(f"\n{'=' * 50}")
    print(f"Ejecutando: {script_name}")
    print(f"{'=' * 50}")
    
    # Print number of records
    print(f"Registros encontrados: {result['record_count']}")
    
    # Print aggregations
    if result['aggregations']:
        print("\nAgregaciones:")
        for agg_name, agg_value in result['aggregations'].items():
            # Format the function and column name
            parts = agg_name.split('_', 1)
            func = parts[0]
            column = parts[1] if len(parts) > 1 else ""
            
            # Format the value based on the type
            if func == 'count':
                formatted_value = f"{agg_value}"
            elif func == 'sum':
                formatted_value = f"{agg_value:.2f}"
            elif func == 'average':
                formatted_value = f"{agg_value:.2f}"
            else:
                formatted_value = str(agg_value)
                
            print(f"{func.capitalize()} de {column}: {formatted_value}")
    
    # Print first few records of filtered data
    if result['record_count'] > 0:
        print("\nPrimeros 5 registros:")
        for i, record in enumerate(result['filtered_data'][:5]):
            print(f"{i+1}. {json.dumps(record, ensure_ascii=False)}")
    
    # If there are more records, indicate how many more
    if result['record_count'] > 5:
        print(f"... y {result['record_count'] - 5} registros más.")
    
    print(f"{'=' * 50}\n")

def run_script_file(script_file):
    """Run a script from a file"""
    with open(script_file, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    try:
        result = parse_and_interpret(script_content)
        print_result(result, script_file)
        return True
    except Exception as e:
        print(f"Error al ejecutar el script {script_file}: {str(e)}")
        return False

def run_example_scripts(scripts_dir='scripts'):
    """Run all script files in the specified directory"""
    # Create scripts directory if it doesn't exist
    if not os.path.exists(scripts_dir):
        os.makedirs(scripts_dir)
        print(f"Directorio '{scripts_dir}' creado. Por favor, coloque los scripts DSL aquí.")
        return
    
    # Get all script files
    script_files = [f for f in os.listdir(scripts_dir) if f.endswith('.dsl')]
    
    if not script_files:
        print(f"No se encontraron archivos .dsl en el directorio '{scripts_dir}'")
        return
    
    # Run each script
    success_count = 0
    for script_file in sorted(script_files):
        full_path = os.path.join(scripts_dir, script_file)
        if run_script_file(full_path):
            success_count += 1
    
    print(f"\nEjecución completada: {success_count} de {len(script_files)} scripts ejecutados correctamente.")

def run_scripts_from_json(example_file='example_scripts.json'):
    """Run all scripts directly from the JSON file"""
    if not os.path.exists(example_file):
        print(f"El archivo de ejemplos '{example_file}' no existe.")
        return
    
    with open(example_file, 'r', encoding='utf-8') as f:
        scripts = json.load(f)
    
    success_count = 0
    for script in scripts:
        script_content = script.get('contenido', '')
        script_num = script.get('numero', 'unknown')
        script_title = script.get('titulo', 'Sin título')
        try:
            result = parse_and_interpret(script_content)
            print_result(result, f"Script {script_num}: {script_title}")
            success_count += 1
        except Exception as e:
            print(f"Error al ejecutar el script {script_num}: {str(e)}")
    
    print(f"\nEjecución completada: {success_count} de {len(scripts)} scripts ejecutados correctamente.")


def extract_examples_to_files(example_file='example_scripts.json', output_dir='scripts'):
    """Extract individual scripts from the JSON file and save them as separate .dsl files"""
    import json

    if not os.path.exists(example_file):
        print(f"El archivo de ejemplos '{example_file}' no existe.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(example_file, 'r', encoding='utf-8') as f:
        scripts = json.load(f)

    for script in scripts:
        num = str(script['numero']).zfill(2)
        content = script['contenido']
        filename = os.path.join(output_dir, f"script_{num}.dsl")
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(content)
        print(f"Script {num} extraído a {filename}")


def run_specific_script(script_number, scripts_dir='scripts'):
    """Run a specific script by number"""
    script_file = f"{scripts_dir}/script_{script_number.zfill(2)}.dsl"
    if os.path.exists(script_file):
        run_script_file(script_file)
    else:
        print(f"El script {script_number} no existe en '{script_file}'")

def interactive_mode():
    """Run in interactive mode"""
    print("Modo interactivo del DSL para Empleados")
    print("Ingrese comandos DSL línea por línea. Escriba 'exit' para salir.")
    
    script = ""
    prompt = ">> "
    
    while True:
        line = input(prompt)
        if line.lower() == 'exit':
            break
        
        script += line + "\n"
        
        # Check if the command is complete (ends with semicolon)
        if line.strip().endswith(';'):
            # Check if it's a print command
            if line.strip().startswith('print'):
                try:
                    result = parse_and_interpret(script)
                    print_result(result, "Consulta interactiva")
                    script = ""  # Reset for the next query
                except Exception as e:
                    print(f"Error: {str(e)}")
                    script = ""  # Reset after error
    
    print("Saliendo del modo interactivo.")

def display_parse_tree(script_content):
    """Parse the script content and display its parse tree"""
    input_stream = InputStream(script_content)
    lexer = EmployeeDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EmployeeDSLParser(token_stream)
    tree = parser.program()
    print("\nÁrbol de análisis sintáctico (parse tree):")
    print(tree.toStringTree(recog=parser))
    print()

def select_test_script(example_file='example_scripts.json'):
    """List available test scripts from JSON and let the user select one"""
    if not os.path.exists(example_file):
        print(f"El archivo de ejemplos '{example_file}' no existe.")
        return None, None
    with open(example_file, 'r', encoding='utf-8') as f:
        scripts = json.load(f)
    if not scripts:
        print(f"No se encontraron scripts en '{example_file}'.")
        return None, None
    print("Scripts disponibles:")
    for idx, script in enumerate(scripts, 1):
        title = script.get('titulo', f"Script {idx}")
        print(f"{idx}. {title}")
    while True:
        choice = input("Seleccione un script por número (o 'q' para salir): ").strip()
        if choice.lower() == 'q':
            return None, None
        if choice.isdigit() and 1 <= int(choice) <= len(scripts):
            selected_script = scripts[int(choice) - 1]
            content = selected_script.get('contenido', '')
            title = selected_script.get('titulo', f"Script {choice}")
            return title, content
        print("Selección inválida. Intente de nuevo.")

def select_columns(csv_file='empleados.csv'):
    """Let the user select one or more columns from the CSV file"""
    if not os.path.exists(csv_file):
        print(f"El archivo '{csv_file}' no existe.")
        return None
    df = pd.read_csv(csv_file)
    columns = list(df.columns)
    print("Columnas disponibles:")
    for idx, col in enumerate(columns, 1):
        print(f"{idx}. {col}")
    print("Ingrese números separados por comas para seleccionar columnas, o 'a' para todas:")
    while True:
        choice = input("Seleccione columnas: ")
        if choice.lower() == 'a':
            return columns
        selected_cols = []
        parts = choice.split(',')
        valid = True
        for part in parts:
            part = part.strip()
            if part.isdigit() and 1 <= int(part) <= len(columns):
                selected_cols.append(columns[int(part) - 1])
            else:
                valid = False
                break
        if valid and selected_cols:
            return selected_cols
        print("Selección inválida. Intente de nuevo.")

def display_selected_columns(columns, csv_file='empleados.csv'):
    """Display the selected columns from the CSV file"""
    if not os.path.exists(csv_file):
        print(f"El archivo '{csv_file}' no existe.")
        return
    df = pd.read_csv(csv_file)
    if not columns:
        print("No se seleccionaron columnas.")
        return
    print(f"\nMostrando columnas: {', '.join(columns)}")
    print(df[columns].to_string(index=False))
    print()

def menu_mode():
    """Interactive menu mode"""
    while True:
        print("\nMenú principal:")
        print("1. Mostrar un test específico con su árbol de análisis")
        print("2. Mostrar una o varias columnas específicas de toda la data")
        print("q. Salir")
        choice = input("Seleccione una opción: ").strip()
        if choice == '1':
            script_name, script_content = select_test_script()
            if script_content:
                print(f"\nMostrando script: {script_name}")
                print(script_content)
                display_parse_tree(script_content)
                # Run the script and display full detailed result
                try:
                    result = parse_and_interpret(script_content)
                    print_result(result, f"Script: {script_name}")
                except Exception as e:
                    print(f"Error al ejecutar el script: {str(e)}")
        elif choice == '2':
            selected_columns = select_columns()
            if selected_columns:
                display_selected_columns(selected_columns)
        elif choice.lower() == 'q':
            print("Saliendo del menú.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def main():
    """Main function to run the DSL interpreter"""
    if len(sys.argv) < 2:
        print("Uso: python main.py [OPCIÓN]")
        print("Opciones:")
        print("  extract           - Extrae los scripts de ejemplo a archivos individuales")
        print("  run-all           - Ejecuta todos los scripts de ejemplo")
        print("  run NUMBER        - Ejecuta un script específico por número")
        print("  run-json          - Ejecuta todos los scripts directamente desde el JSON")
        print("  interactive       - Modo interactivo para ejecutar comandos DSL")
        print("  menu              - Menú interactivo para tests y columnas")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'extract':
        extract_examples_to_files()
    elif command == 'run-all':
        run_example_scripts()
    elif command == 'run-json':
        run_scripts_from_json()
    elif command == 'run' and len(sys.argv) > 2:
        run_specific_script(sys.argv[2])
    elif command == 'interactive':
        interactive_mode()
    elif command == 'menu':
        menu_mode()
    else:
        print(f"Opción desconocida: {command}")

if __name__ == "__main__":
    main()
