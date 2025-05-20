load "empleados.csv";
filter column "departamento" == "Administración";
filter column "dias_laborados" > 1095;
aggregate count column "id_empleado";
print;