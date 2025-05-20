load "empleados.csv";
filter column "cargo" == "Asistente Administrativo";
filter column "dias_laborados" < 730;
aggregate count column "id_empleado";
print;