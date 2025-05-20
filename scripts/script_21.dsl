load "empleados.csv";
filter column "edad" between 30 and 40;
aggregate count column "id_empleado";
print;