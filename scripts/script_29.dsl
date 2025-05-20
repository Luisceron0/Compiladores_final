load "empleados.csv";
filter column "cargo" == "Abogado";
filter column "dias_laborados" < 1825;
aggregate count column "id_empleado";
print;