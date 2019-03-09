import click
import os
from src.config import BASE_PATH, FOLDERS, FILES
from util import mkdir, mkfile, cpfile

@click.group()
def cli():
    click.echo(click.style('Hello World!', fg='green'))

@cli.command()
@click.argument('contest')
@click.option('--codeforces', '-cf', is_flag=True, default=False)
def init(contest, codeforces):
    click.echo('init %s' % (contest))
    path = os.path.join(BASE_PATH, contest)
    mkdir(path)
    for item in FOLDERS:
        if 'name' not in item:
            raise Exception('FOLDERS configure loses a name')

        mkdir(path, item['name'])
        
        if 'empty_files' in item:
            for f in item['empty_files']:
                mkfile(path, item['name'], file=f)
        if 'src_files' in item:
            for s in item['src_files']:
                cpfile(path, item['name'], src=s)




@cli.command()
@click.argument('contest')
def open(contest):
    click.echo('open %s' % (contest))
    

@cli.command()
def test():
    click.echo('test')

@cli.command()
def submit():
    click.echo('submit')

if __name__ == '__main__':
    cli()