load "empleados.csv";
filter column "departamento" == "Operaciones";
filter column "salario" between 2500 and 3500;
aggregate count column "id_empleado";
print;