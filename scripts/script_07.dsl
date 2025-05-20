load "empleados.csv";
filter column "departamento" == "Finanzas";
aggregate average column "salario";
print;