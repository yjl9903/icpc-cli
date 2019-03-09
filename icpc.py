import click
from src.config import FOLDERS, FILES
from util import mkdir, mkfile, cpfile

@click.group()
def cli():
    click.echo(click.style('Hello World!', fg='green'))

@cli.command()
@click.argument('contest')
@click.option('--codeforces', '-cf', is_flag=True, default=False)
def init(contest, codeforces):
    click.echo('init %s' % (contest))

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