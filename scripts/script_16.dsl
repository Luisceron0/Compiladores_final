load "empleados.csv";
filter column "departamento" == "Legal";
filter column "edad" < 40;
aggregate count column "id_empleado";
aggregate average column "salario";
print;