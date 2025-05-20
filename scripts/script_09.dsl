load "empleados.csv";
filter column "cargo" == "Analista Financiero";
filter column "edad" between 25 and 35;
aggregate count column "id_empleado";
print;