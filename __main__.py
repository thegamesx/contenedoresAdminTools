from apiCalls import *
import click
from passwordGen import generate_password

import pickle


@click.group()
def cli():
    pass


@cli.command(name='newvigia', help="Ingresa una nueva placa a la base de datos.")
@click.option('-n', '--name', prompt='Nombre', help='Nombre de la placa.')
@click.option('-p', '--password', default=generate_password(),
              help='La contraseña se genera automáticamente, pero se puede especificar de así desearlo.')
@click.option('-c', '--config', default='default', help='Nombre de la configuración. Default si se deja vacío.')
def new_vigia(name, config, password):
    result = requestNewCont(name, config, password)
    with open('log.pkl', 'wb') as f:
        pickle.dump(result, f)
    click.echo(f'Status code: {result.status_code}\n'
               f'Response: {result.text}\n'
               f'Contraseña: {password}')



if __name__ == '__main__':
    cli()
