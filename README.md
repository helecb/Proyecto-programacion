# A definir

## Descripción del proyecto
`¿Qué es? ¿Para qué sirve? ¿Quién lo usaría?`

## Dependencias e instalación
`Para ejecutar el proyecto se necesita:`
- Tener instalado el Kivi (Guía de instalación en investigación)

| Dependencia | Versión | Para qué se usa |
| --- | --- | --- |
| Python | 3.x | Lenguaje del proyecto |
| KivyMD | 2.3.1 | Interfaz gráfica |

`Instalación:`

```
py -m pip install kivymd
```

## Cómo levantar el proyecto
1. Descargar o copiar al carpeta del proyecto.
2. Instalar las dependencias (ver sección anterior)
3. Abrir una terminal dentro de __carpeta/archivo__ del proyecto.
4. Ejecutar:
```
python app.py
```
## Estructura de archivos
- Proyecto
  - bd
    - leeme.txt
  - clases
    - leeme.txt
  - home
    - home.kv
    - home.py
  - images
    - avatar.png
    - CASTRO.jpg
    - CONTRERAS.jpg
    - LEONFANTI.jpg
    - TABERNA.jpg
    - leeme.txt
  - inicio 
    - inicio.kv
    - inicio.py
  - perfil
    - perfil.kv
    - perfil.py
  - programadores
    - programadores.kv
    - programadores.py
  - registro
    - registro.kv
    - registro.py
  - app.py
  - README.md

## Estructura de la base de datos
A definir. Cuando se elija el dataset se van a listar acá las tablas y sus columnas, con este formato:

| Tabla | Columna | Tipo | Descripción | 
| --- | --- | --- | --- |
| Ejemplo | Id | INT | Identificador (clave primaria) | 

## Clase Usuario
| Atributos | Metodos | Tipo |
| --- | --- | --- |
| Nombre | --- | STR |
| Edad | --- | INT |
| Correo | validar_correo(): comprueba que el correo tenga "@" y "." | STR |
| Contraseña | contrasena_corecta(): comprueba que la contraseña que escribe el usuario sea la misma que esta guardada con ese correo| STR |


## Integrantes, materia y división
- Helena Castro Belmonte
- Martina Contreras
- Delfina Taberna
- Inés Leonfanti

__Materia:__ Taller de Programación __Curso:__ 4to A