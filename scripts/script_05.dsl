load "empleados.csv";
filter column "departamento" == "Recursos Humanos";
filter column "edad" < 30;
aggregate count column "id_empleado";
print;