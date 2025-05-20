load "empleados.csv";
filter column "departamento" == "Ventas";
sort column "dias_laborados" desc;
aggregate count column "id_empleado";
print;