load "empleados.csv";
filter column "departamento" == "Tecnología";
filter column "salario" < 2500;
aggregate count column "id_empleado";
print;