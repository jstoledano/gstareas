# GhostScript Homework

Este es  un pequeño script  para automatizar la  generación de
las tareas en la FCA.

Toma un archivo de portada y un archivo con el trabajo y los une en un solo archivo de menor tamaño con una identificación única que incluye el la clave de la materia, la unidad y la actividad.

Adicionalmente, modifica los metadatos del archivo pdf resultante para incluir el _autor_, _fecha de creación_, y otros datos relevantes.

## Parámetros

Toma los siguientes parámetros:

- `-s`, `--semestre`, indica el semestre, por default es '`2022-2`'
- `-m`, `--materia`, indica la clave de la materia _requerido_
- `-u`, `--unidad`, indica la unidad, a dos dígitos, como '`01`', parámetro _requerido_
- `-a`, `--actividad`, indica la actividad a dos o tres posiciones, como '`01`' o '`LQA`'. Parámetro _requerido_
- `-p`, `--portada`, indica el archivo de la portada, por default es `./portada.pdf`. _Opcional_.
- `-t`, `--trabajo`, indica el aArchivo del trabajo por default es `./tarea.pdf`. _Opcional_.

## Ejemplo de uso

Un comando típico es como sigue:

```sh
$ gshw.py -m 1908 -u 01 -a 06 
```

Esto produce el archivo `1908_01_06_sanchez_toledano_javier.pdf`