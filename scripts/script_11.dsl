load "empleados.csv";
filter column "cargo" == "Gerente de Marketing";
filter column "dias_laborados" > 1825;
aggregate count column "id_empleado";
aggregate average column "edad";
print;