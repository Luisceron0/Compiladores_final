load "empleados.csv";
filter column "edad" > 60;
aggregate count column "id_empleado";
aggregate average column "dias_laborados";
print;