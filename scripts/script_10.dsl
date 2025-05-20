load "empleados.csv";
filter column "departamento" == "Ventas";
filter column "salario" > 3500;
aggregate count column "id_empleado";
aggregate average column "dias_laborados";
print;