import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import csv

# Definir constantes
NUM_EMPLOYEES = 300
DEPARTMENTS = ['Ventas', 'Marketing', 'Finanzas', 'Recursos Humanos', 'Tecnología', 'Operaciones', 'Legal', 'Administración']
POSITIONS = {
    'Ventas': ['Representante de Ventas', 'Gerente de Ventas', 'Director de Ventas', 'Asistente de Ventas'],
    'Marketing': ['Especialista en Marketing', 'Gerente de Marketing', 'Director de Marketing', 'Asistente de Marketing'],
    'Finanzas': ['Contador', 'Analista Financiero', 'Director Financiero', 'Tesorero'],
    'Recursos Humanos': ['Reclutador', 'Especialista en RRHH', 'Director de RRHH', 'Coordinador de Beneficios'],
    'Tecnología': ['Desarrollador', 'Ingeniero de Software', 'Arquitecto de Soluciones', 'Director de TI'],
    'Operaciones': ['Analista de Operaciones', 'Gerente de Operaciones', 'Director de Operaciones', 'Coordinador Logístico'],
    'Legal': ['Abogado', 'Asistente Legal', 'Director Legal', 'Asesor Jurídico'],
    'Administración': ['Asistente Administrativo', 'Gerente Administrativo', 'Analista Administrativo', 'Coordinador Administrativo']
}

FIRST_NAMES = ['Ana', 'Juan', 'María', 'Carlos', 'Laura', 'Pedro', 'Sofía', 'Miguel', 'Luisa', 'José',
               'Fernanda', 'Alberto', 'Daniela', 'Eduardo', 'Gabriela', 'Ricardo', 'Valentina', 'Javier',
               'Isabella', 'Andrés', 'Camila', 'Alejandro', 'Natalia', 'Diego', 'Victoria']

LAST_NAMES = ['González', 'Rodríguez', 'Fernández', 'López', 'Martínez', 'Sánchez', 'Pérez', 'Gómez',
              'Díaz', 'Torres', 'Ramírez', 'Flores', 'Álvarez', 'Ruiz', 'Hernández', 'Jiménez',
              'Moreno', 'Muñoz', 'Romero', 'Ortega', 'Vargas', 'Morales', 'Reyes', 'Cruz', 'Castillo']

# Función para generar datos aleatorios de empleados
def generate_employee_data():
    data = []
    
    for i in range(1, NUM_EMPLOYEES + 1):
        id_empleado = f'EMP{i:04d}'
        
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        nombre = f'{first_name} {last_name}'
        
        departamento = random.choice(DEPARTMENTS)
        cargo = random.choice(POSITIONS[departamento])
        
        # Salario basado en departamento y cargo
        base_salary = {
            'Ventas': 2500,
            'Marketing': 2800,
            'Finanzas': 3200,
            'Recursos Humanos': 2700,
            'Tecnología': 3500,
            'Operaciones': 2600,
            'Legal': 3300,
            'Administración': 2400
        }
        
        position_multiplier = {
            'Representante de Ventas': 1.0, 'Gerente de Ventas': 1.5, 'Director de Ventas': 2.0, 'Asistente de Ventas': 0.8,
            'Especialista en Marketing': 1.0, 'Gerente de Marketing': 1.5, 'Director de Marketing': 2.0, 'Asistente de Marketing': 0.8,
            'Contador': 1.0, 'Analista Financiero': 1.2, 'Director Financiero': 2.0, 'Tesorero': 1.3,
            'Reclutador': 1.0, 'Especialista en RRHH': 1.1, 'Director de RRHH': 1.8, 'Coordinador de Beneficios': 1.0,
            'Desarrollador': 1.2, 'Ingeniero de Software': 1.5, 'Arquitecto de Soluciones': 1.8, 'Director de TI': 2.0,
            'Analista de Operaciones': 1.0, 'Gerente de Operaciones': 1.5, 'Director de Operaciones': 1.8, 'Coordinador Logístico': 1.0,
            'Abogado': 1.5, 'Asistente Legal': 0.8, 'Director Legal': 2.0, 'Asesor Jurídico': 1.4,
            'Asistente Administrativo': 0.8, 'Gerente Administrativo': 1.5, 'Analista Administrativo': 1.0, 'Coordinador Administrativo': 1.2
        }
        
        salario = round(base_salary[departamento] * position_multiplier[cargo] * random.uniform(0.9, 1.1), 2)
        
        # Fecha de ingreso aleatoria en los últimos 10 años
        end_date = datetime.now()
        start_date = end_date - timedelta(days=10*365)
        random_days = random.randint(0, (end_date - start_date).days)
        fecha_ingreso = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        
        # Edad entre 20 y 65 años
        edad = random.randint(20, 65)
        
        # Días laborados desde la fecha de ingreso
        fecha_ingreso_dt = datetime.strptime(fecha_ingreso, '%Y-%m-%d')
        dias_laborados = (datetime.now() - fecha_ingreso_dt).days
        
        # Correo electrónico
        correo = f'{first_name.lower()}.{last_name.lower()}@empresa.com'
        
        # Teléfono
        telefono = f'+57 {random.randint(300, 350)} {random.randint(1000000, 9999999)}'
        
        employee = {
            'id_empleado': id_empleado,
            'nombre': nombre,
            'departamento': departamento,
            'cargo': cargo,
            'salario': salario,
            'fecha_ingreso': fecha_ingreso,
            'edad': edad,
            'dias_laborados': dias_laborados,
            'correo': correo,
            'telefono': telefono
        }
        
        data.append(employee)
    
    return data

# Generar datos
employee_data = generate_employee_data()

# Convertir a DataFrame
df = pd.DataFrame(employee_data)

# Guardar como CSV
df.to_csv('empleados.csv', index=False)

print(f"Archivo CSV 'empleados.csv' generado con {NUM_EMPLOYEES} registros.")
print("Columnas:", df.columns.tolist())
print("\nPrimeras 5 filas:")
print(df.head())
