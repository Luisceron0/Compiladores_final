load "empleados.csv";
filter column "dias_laborados" > 2555;
aggregate count column "id_empleado";
aggregate average column "salario";
print;