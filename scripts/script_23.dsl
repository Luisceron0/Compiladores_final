load "empleados.csv";
filter column "departamento" == "Marketing";
sort column "dias_laborados" desc;
aggregate average column "dias_laborados";
print;