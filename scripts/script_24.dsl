load "empleados.csv";
filter column "cargo" == "Director Financiero";
filter column "salario" > 5000;
aggregate count column "id_empleado";
print;