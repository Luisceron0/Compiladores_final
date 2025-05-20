load "empleados.csv";
filter column "salario" > 4000;
filter column "dias_laborados" < 365;
aggregate count column "id_empleado";
print;