#Analizando los datos del registro de empleados
import pandas as pd

# cargar los datos a analizar
datosEmpleados=pd.read_csv("datos_empleados_bar.csv")
print(datosEmpleados)

#aplicando trasformaciones y filtros
# Clasificar los empleados con salario mayor a 3 millones
salarioMayoresATres=datosEmpleados.query("`Salario (COP)`>3000000")

#obtener los empleados con mas de 10 años de experiencia
EmpleadosExperienciaDiez=datosEmpleados.query("(`Experiencia (años)`>10)")

# empleados que trabajan mas de 180 horas
Empleados180=datosEmpleados.query("(`Horas laboradas/mes`>180)")

# Empleados cuyo cargo es Bartender
EmpleadosBartender=datosEmpleados.query("`Cargo en el bar`==`Bartender`)")

