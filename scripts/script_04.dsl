load "empleados.csv";
filter column "cargo" == "Director de Ventas";
filter column "salario" > 4000;
aggregate average column "salario";
print;