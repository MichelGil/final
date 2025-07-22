#Analizando los datos del registro de empleados
import pandas as pd

# cargar los datos a analizar
datosEmpleados=pd.read_csv("datos_empleados_bar.csv")


#aplicando trasformaciones y filtros
# Clasificar los empleados con salario mayor a 3 millones
salarioMayoresATres=datosEmpleados.query("`Salario (COP)`>3000000")
print(salarioMayoresATres.head(5))

#obtener los empleados con mas de 10 años de experiencia
EmpleadosExperienciaDiez=datosEmpleados.query("(`Experiencia (años)`>10)")
print(EmpleadosExperienciaDiez.head(5))

# empleados que trabajan mas de 180 horas
Empleados180=datosEmpleados.query("(`Horas laboradas/mes`>180)")
print(Empleados180.head(5))

# Empleados cuyo cargo es Bartender
bartenders=datosEmpleados.query("`Cargo en el bar`=='Bartender'") 
print(bartenders.head(5))
