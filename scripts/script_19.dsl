load "empleados.csv";
filter column "cargo" == "Desarrollador";
filter column "edad" < 28;
aggregate count column "id_empleado";
aggregate average column "salario";
print;