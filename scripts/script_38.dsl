load "empleados.csv";
filter column "fecha_ingreso" == "2020-05-15";
aggregate count column "id_empleado";
print;