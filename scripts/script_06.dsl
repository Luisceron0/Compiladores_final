load "empleados.csv";
filter column "dias_laborados" > 2500;
sort column "dias_laborados" desc;
aggregate count column "id_empleado";
aggregate average column "salario";
print;