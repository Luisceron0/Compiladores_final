load "empleados.csv";
filter column "salario" < 3000;
aggregate count column "id_empleado";
aggregate average column "salario";
print;