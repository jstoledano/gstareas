#!/usr/bin/env python3
# coding: utf-8
import subprocess
import click
from datetime import datetime
from pathlib import Path
import os

if os.name == 'nt':
    home_path = Path("D:/", "Users", "javier")
    pandoc_path = Path("C:/", "ProgramData", "chocolatey", "bin", "pandoc.exe")
    gs_path = Path("C:/", "Program Files", "gs", "gs9.55.0", "bin", "gswin64c.exe")
else:
    pandoc_path = "/usr/bin/pandoc"
    gs_path = '/usr/bin/gs'
    home_path = os.environ['HOME']

def pandoc(reto, unidad, trabajo):
    bib = Path(home_path, ".pandoc", "library.bib")
    apa = Path(home_path, ".pandoc", "apa.csl")
    args = [pandoc_path,
            "--pdf-engine=xelatex",
            "--citeproc",
            f"--bibliography={bib}",
            f"--csl={apa}",
            "--metadata=lang=es-MX",
            "--toc",
            "--from=markdown",
            "--output=tarea.pdf",
            f"{trabajo}"
            ]
    click.echo(f'Procesando el Reto {reto} de la Unidad {unidad}. Espera un momento.')
    p = subprocess.Popen(args)
    return p.wait()


def homework(materia, unidad, reto, portada, trabajo):
    front = 'Sanchez_Javier'
    name = 'Javier Tonatihut Sanchez Toledano'
    short_name = 'Javier Sanchez Toledano'
    account = '19012324'
    message = 'Hecho en Tlaxcala'
    date = datetime.utcnow().strftime('%Y%m%d%H%M%S')  # ya sé
    try:
        task = f'{materia}:{unidad}:{reto}'
    except SyntaxError() as e:
        raise click.UsageError(f'Faltan argumentos. Error {e}')

    # Se construyen los argumentos
    args = [gs_path,
            '-dQUIET', '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.4',
            '-dPDFSETTINGS=/ebook', '-dBATCH',
            '-dNOPAUSE', '-q', '-dAutoRotatePages=/None',
            '-sPAPERSIZE=letter',
            '-dFIXEDMEDIA',
            f'-sOutputFile={front}_{reto}_{unidad}.pdf',
            f'{portada}', f'{trabajo}',
            '-dPDFACompatibilityPolicy=3',
            '-c', f"[ /Title (Reto {reto} de {name}) \
            /Author ({short_name} <cuenta: {account}>) \
            /materia (Materia: {materia} | Unidad: {unidad} | Reto: {reto}) \
            /Keywords ({materia}, uveg, isc) \
            /Creator ({message}) \
            /CreationDate (D:{date}+06'00') \
            /ModDate (D:{date}+06'00') \
            /DOCINFO pdfmark",
            '-f']
    p = subprocess.Popen(args)
    return p.wait()

@click.command()
@click.option('-m', '--materia', required=True, help='Materia')
@click.option('-u', '--unidad', required=True, help='Unidad')
@click.option('-r', '--reto', required=True, help='Reto')
@click.option('-p',
              '--portada',
              default='./portada.pdf',
              help='Archivo de la portada, por default es ./portada.pdf')
@click.option('-t',
              '--trabajo',
              default='./tarea.pdf',
              help='Archivo del trabajo por default es ./tarea.pdf')
@click.option('-f', '--final', is_flag=True)
@click.option('-a', '--apuntes', is_flag=True)
@click.option('-s', '--solo', is_flag=True)
def iniciar(materia, unidad, reto, portada, trabajo, final, apuntes, solo):
    start = datetime.now()
    if apuntes:
        p = pandoc(reto, unidad, trabajo)
        h = 0
    if solo:
        h = homework(materia, unidad, reto, portada, trabajo)
        p = 0
    if final:
        p = pandoc(reto, unidad, trabajo)
        h = homework(materia, unidad, reto, portada, trabajo)
    end = datetime.now()
    time = end - start

    if p == 0 and h == 0:
        click.echo(f'El archivo fue generado exitosamente.\nEl proceso tomó {time.seconds} segundos.')


if __name__ == '__main__':
    iniciar()