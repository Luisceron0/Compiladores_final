load "empleados.csv";
filter column "cargo" == "Reclutador";
filter column "dias_laborados" between 730 and 1825;
aggregate count column "id_empleado";
print;