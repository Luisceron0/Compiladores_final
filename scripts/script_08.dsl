load "empleados.csv";
filter column "salario" between 3000 and 4000;
aggregate count column "id_empleado";
aggregate average column "edad";
print;