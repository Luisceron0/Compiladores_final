load "empleados.csv";
filter column "cargo" == "Ingeniero de Software";
filter column "salario" between 4000 and 5000;
aggregate count column "id_empleado";
print;