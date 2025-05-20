load "empleados.csv";
filter column "nombre" == "Ana González";
aggregate count column "id_empleado";
print;