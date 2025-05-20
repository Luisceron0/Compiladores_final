load "empleados.csv";
filter column "dias_laborados" < 730;
aggregate count column "id_empleado";
aggregate average column "edad";
sort column "fecha_ingreso" desc;
print;