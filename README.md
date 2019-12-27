## Reporte de estudiantes por minutos

Este programa tiene como finalidad entregar un archivo de salida con el total de minutos 
que estuvieron los alumnos registrados dentro de la institución.

Para su ejecución:
```
python Main.py /path/to/input.txt
```
## Consideraciones

### 1. Se asume que todos los estudiantes que tienen ingreso y salida estan dentro de el arreglo 
```
students_array
```
### 2. El script siempre termina con:
```
=D
```
### 3. El archivo de output tendrá el nombre de: 
```
output.txt
```
	
### 4. Ruta donde se guardará archivo de output
```
/path/to/script/src/output.txt
```

### 5. Para una mejor lectura y simplicidad para tratar los datos se dejaron separados en dos arreglos:
```
students_array
```
	
- este arreglo tiene como objetivo almacenar los datos del commando **Student**
```
presence_array
```
- este arreglo almacenará los datos del comando **Presence**

### 6. Los datos para generar el reporte se ordenan considerando como llave el alumno con menor cantidad de horas
### después se invierten para conservar el con mayor cantidad de horas quede en la cabecera.

### 7. Las pruebas para generar el reporte fallaron todas, pero resultado esperado se obtiene en la ejecución del script




