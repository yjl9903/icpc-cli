import click
import os
from src.config import BASE_PATH, FOLDERS, FILES, CF_PATH, CF_NUMBER, STANDARD_NUMBER, OJ_PATH
from util import mkdir, mkfile, cpfile

@click.group()
def cli():
    # click.echo(click.style('Hello World!', fg='green'))
    pass

@cli.command()
@click.argument('contest')
@click.option('--codeforces', '-cf', is_flag=True, default=False)
@click.option('--folder', '-f', type=str, default='')
@click.option('--number', '-n', type=int, default=CF_NUMBER)
@click.option('--standard', '-s', is_flag=True, default=False)
def init(contest, codeforces, folder, number, standard):
    click.secho('init %s...' % contest, fg='green')

    if folder and codeforces:
        raise Exception('init conflict!')
    if codeforces:
        folder = CF_PATH
    if folder and folder in OJ_PATH:
        folder = OJ_PATH[folder]

    path = os.path.join(BASE_PATH, folder, contest)
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

    for item in FILES:
        if 'name' not in item:
            raise Exception('FILES configure loses a name')
        if 'src' in item:
            cpfile(path, item['name'], src=item['src'])
        else:
            mkfile(path, file=item['name'])

    if codeforces:
        folder = CF_PATH
    if standard:
        number = STANDARD_NUMBER

    for i in range(number):
        mkfile(path, file=chr(i + ord('a')) + '.cpp')

    os.system('code ' + path)

@cli.command()
@click.argument('contest')
@click.option('--codeforces', '-cf', is_flag=True, default=False)
@click.option('--folder', '-f', type=str, default='')
def open(contest, codeforces, folder):
    click.secho('open %s...' % (contest), fg='green')

    if folder and codeforces:
        raise Exception('open conflict!')
    if codeforces:
        folder = CF_PATH
    if folder and folder in OJ_PATH:
        folder = OJ_PATH[folder]

    path = os.path.join(BASE_PATH, folder, contest)
        
    click.echo('contest folder => %s' % path)
    os.system('code ' + path)
    
@cli.command()
@click.argument('contest')
@click.argument('problem')
def write(contest, problem):
    click.secho('write %s => %s' % (contest, problem), fg='green')

    if contest and contest in OJ_PATH:
        contest = OJ_PATH[contest]
    path = os.path.join(BASE_PATH, contest)
    problem += '.cpp'

    mkfile(path, file=problem)

    os.system('code ' + path)
    os.system('code ' + os.path.join(path, problem))

@cli.command()
def test():
    click.secho('test', fg='green')

@cli.command()
def submit():
    click.secho('submit', fg='green')

if __name__ == '__main__':
    cli()