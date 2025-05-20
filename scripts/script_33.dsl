load "empleados.csv";
filter column "departamento" == "Finanzas";
filter column "salario" > 4000;
aggregate count column "id_empleado";
aggregate average column "edad";
print;