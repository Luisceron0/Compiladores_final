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

def extract_examples_to_files(example_file='example_scripts.txt', output_dir='scripts'):
    """Extract individual scripts from the example file and save them as separate files"""
    if not os.path.exists(example_file):
        print(f"El archivo de ejemplos '{example_file}' no existe.")
        return
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(example_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split the content by script comments
    parts = content.split('// Script ')
    
    # Process each script
    for i, part in enumerate(parts):
        if i == 0:  # Skip the first part (empty)
            continue
        
        # Split by the first newline to separate script number from content
        try:
            script_number, script_content = part.split(':', 1)
            script_number = script_number.strip()
            
            # Create a file for this script
            filename = f"{output_dir}/script_{script_number.zfill(2)}.dsl"
            with open(filename, 'w', encoding='utf-8') as script_file:
                script_file.write(script_content.strip())
            
            print(f"Script {script_number} extraído a {filename}")
        except ValueError:
            print(f"Error al procesar parte del ejemplo: {part[:50]}...")

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

def main():
    """Main function to run the DSL interpreter"""
    if len(sys.argv) < 2:
        print("Uso: python main.py [OPCIÓN]")
        print("Opciones:")
        print("  extract           - Extrae los scripts de ejemplo a archivos individuales")
        print("  run-all           - Ejecuta todos los scripts de ejemplo")
        print("  run NUMBER        - Ejecuta un script específico por número")
        print("  interactive       - Modo interactivo para ejecutar comandos DSL")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'extract':
        extract_examples_to_files()
    elif command == 'run-all':
        run_example_scripts()
    elif command == 'run' and len(sys.argv) > 2:
        run_specific_script(sys.argv[2])
    elif command == 'interactive':
        interactive_mode()
    else:
        print(f"Opción desconocida: {command}")

if __name__ == "__main__":
    main()
