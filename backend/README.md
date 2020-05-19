## Clean workspace
```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
```

## Requirements 

### Proceso
1. Reunión de comité para recibir informe financiero para verificar que contamos con los recursos.
2. Luego de tener aprobación para la ejecución de la misión procedemos a selección de lugares candidatos a realizar la misión, y después de un análisis se elige una ciudad o pueblo donde se realizará la misión.
3. En una fecha posterior ya programada hacemos un reconocimiento de campo usando el método FODA [fortalezas, oportunidades, debilidades, amenazas] para hacer una preparación más adecuada.
4. Seleccionamos las áreas de atención que estaremos ofreciendo. {medicina general, medicina natural, nutrición, odontología, masaje, donaciones, consulta jurídica, orientación cristiana etc.} 
5. Organizamos equipos de trabajo con los elementos humanos más diestros en cada área, para darles capacitaciones y orientaciones previas a la misión. Además en esta etapa elaboramos el material con el que estaremos trabajando. 
6. Realizamos gestiones para recaudar fondos o donaciones de equipo, medicina, víveres etc mediante solicitudes y material audiovisual en redes sociales, TV y radio para promocionar nuestro evento.
7. Llegada la fecha de ejecución, reunimos al personal voluntario y procedemos a instalarnos en un centro social o educativo el cual ya ha sido reservado con esta finalidad. Un día antes de la misión, damos las últimas orientaciones a personal voluntario [150 personas aprox. entre médicos, enfermeros, orientadores, masajistas y equipo de jóvenes y niños asistentes.
8. Procedemos a realizar nuestra actividad, siguiendo las instrucciones previas. El número de personas atendidas en la última misión fue de más de 500. Y el valor de la ayuda superó los 300mil lempiras.

### Projects
- id
- name
- place
- area
- status
- type [enum]
- tasks

### Task
- id
- type [enum]
- due
- responsable [collaborator]
- description
- status

### Fase post misión.
1. hacemos un resumen financiero para determinar el coste de nuestra inversión. Como también para valorar aquellos casos en los cuales se debe continuar ayudando.
2. se entregan informes a la organización superior. {Unión Hondureña}
3. Se establece un Misionero en la zona donde se realizó la misión para darle continuidad a las atenciones recibidas.
4. se realizan visitas periódicas por parte del presidente de Manos Bondadosas para conocer el resultado del trabajo en el sector. Se hacen visitas personalizadas y además se continúa dando tratamientos y atenciones a las personas que siguen su estado de recuperación, hasta lograr que se haya superado.