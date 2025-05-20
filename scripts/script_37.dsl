load "empleados.csv";
filter column "departamento" == "Tecnología";
sort column "salario" desc;
aggregate average column "salario";
print;