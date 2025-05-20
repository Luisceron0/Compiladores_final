load "empleados.csv";
filter column "edad" > 50;
aggregate count column "id_empleado";
aggregate average column "salario";
sort column "edad" desc;
print;