load "empleados.csv";
sort column "salario" desc;
aggregate average column "salario";
print;