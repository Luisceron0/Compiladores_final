load "empleados.csv";
filter column "dias_laborados" < 180;
aggregate count column "id_empleado";
sort column "fecha_ingreso" desc;
print;