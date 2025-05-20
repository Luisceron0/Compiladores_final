load "empleados.csv";
filter column "salario" == 3500;
aggregate count column "id_empleado";
print;