#!/usr/local/bin/python3.10
# coding: utf-8
import subprocess
import click
from datetime import datetime

@click.command()
@click.option('-s', '--semestre', default='2022-2', help='Semestre')
@click.option('-m', '--materia', required=True, help='Materia')
@click.option('-u', '--unidad', required=True, help='Unidad')
@click.option('-a', '--actividad', required=True, help='Actividad')
@click.option('-p', 
    '--portada', 
    default='./portada.pdf', 
    help='Archivo de la portada, por default es ./portada.pdf')
@click.option('-t', 
    '--trabajo', 
    default='./tarea.pdf', 
    help='Archivo del trabajo por default es ./tarea.pdf')
def homework(semestre, materia, unidad, actividad, portada, trabajo):
    # Constantes
    back = 'sanchez_toledano_javier.pdf'
    name = 'Javier Tonatihut Sanchez Toledano'
    short_name = 'Javier Sanchez Toledano'
    account = '419135069'
    message = 'Hecho en Tlaxcala'
    date = datetime.utcnow().strftime('%Y%m%d%H%M%S') # ya sé
    try:
        task = f'{materia}:{unidad}:{actividad}'
    except SyntaxError() as e:
        raise click.UsageError('Faltan argumentos')

    # Se construyen los argumentos
    args = ['gs', 
        '-dQUIET', '-sDEVICE=pdfwrite', 
        '-dCompatibilityLevel=1.4', 
        '-dPDFSETTINGS=/ebook', '-dBATCH', 
        '-dNOPAUSE', '-q', '-dAutoRotatePages=/None', 
        '-sPAPERSIZE=letter', 
        '-dFIXEDMEDIA', 
        f'-sOutputFile={materia}_{unidad}_{actividad}_{back}', 
        f'{portada}', f'{trabajo}',
        '-dPDFACompatibilityPolicy=3', 
        '-c', f"[ /Title (Tarea {task} de {name}) \
            /Author ({short_name} <cuenta: 419135069>) \
            /materia (Semestre: {semestre} | Materia: {materia} | Unidad: {unidad} | Actividad: {actividad}) \
            /Keywords ({semestre}, {materia}, fca, unam) \
            /Creator ({message}) \
            /CreationDate (D:{date}+06'00') \
            /ModDate (D:{date}+06'00') \
            /DOCINFO pdfmark", 
        '-f']

    p = subprocess.Popen(args)

    if p.returncode == None:
        click.echo(f'El archivo {task} fue generado exitosamente')

if __name__ == '__main__':
    homework()