import click
import os
from robobrowser import RoboBrowser
from icpc.config import *
from icpc.util import mkdir, mkfile, cpfile, execTest

@click.group()
@click.pass_context
def cli(ctx):
    if not BASE_PATH:
        click.echo('Your base path:')

        stdin = click.get_text_stream('stdin')
        s = stdin.readline().strip()

        while True:
            if not os.path.isabs(s):
                click.secho('Not a absolute path!', fg='red')
                click.echo('Your base path:')
                s = stdin.readline().strip()
            elif not os.path.isdir(s):
                click.secho('Not a directory!', fg='red')
                click.echo('Your base path:')
                s = stdin.readline().strip()
            else:
                break

        ctx.invoke(config, base_path=s)

@cli.command('config', short_help='show config file path')
@click.option('--base-path', help='set the base path')
def config(base_path):
    """
    Show config file path.
    """
    global BASE_PATH

    if BASE_PATH and base_path == BASE_PATH:
        return

    config_path = os.path.dirname(os.path.abspath(__file__))

    click.echo('Path => %s' % config_path)

    if base_path:
        cfg = []
        with click.open_file(config_path, 'r') as fin:
            cfg = fin.readlines()
        
        for i in range(len(cfg)):
            if cfg[i].strip()[0] == '#':
                continue
            if cfg[i].find('BASE_PATH') != -1:
                cfg[i] = "BASE_PATH = r'%s'\n" % base_path
                break
        
        with click.open_file(config_path, 'w') as f:
            f.writelines(cfg)

        BASE_PATH = base_path

        click.echo('BASE_PATH => %s' % base_path)

@cli.command('init', short_help='init a contest folder')
@click.argument('contest')
@click.option('--codeforces', '-cf', is_flag=True, default=False, help='Create a Codeforces contest')
@click.option('--folder', '-f', type=str, default='', help='Create a contest in this folder')
@click.option('--number', '-n', type=int, default=CF_NUMBER, help='Number of problems')
@click.option('--standard', '-s', is_flag=True, default=False, help='Create an ICPC contest')
def init(contest, codeforces, folder, number, standard):
    """
    Init a contest folder with Visual Studio Code environment and necessary files.
    """
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
            cpfile(path, src=item['src'])
        else:
            mkfile(path, file=item['name'])

    if codeforces:
        folder = CF_PATH
    if standard:
        number = STANDARD_NUMBER

    for i in range(number):
        mkfile(path, file=chr(i + ord('a')) + '.cpp')

    os.system('code ' + path)

@cli.command('open', short_help='open a contest folder')
@click.argument('contest')
@click.option('--codeforces', '-cf', is_flag=True, default=False)
@click.option('--folder', '-f', type=str, default='')
def open(contest, codeforces, folder):
    """
    Open a contest folder.
    """
    click.secho('open %s...' % (contest), fg='green')

    if folder and codeforces:
        raise Exception('open conflict!')
    if codeforces:
        folder = CF_PATH
    if not folder and contest in OJ_PATH:
        folder = OJ_PATH[contest]
        contest = ''

    path = os.path.join(BASE_PATH, folder, contest)
        
    click.echo('contest folder => %s' % path)
    os.system('code ' + path)
    
@cli.command('write', short_help='write a new problem')
@click.argument('contest')
@click.argument('problem')
def write(contest, problem):
    """
    Write a new problem in a contest.
    """
    click.secho('write %s => %s...' % (contest, problem), fg='green')

    if contest and contest in OJ_PATH:
        contest = OJ_PATH[contest]
    path = os.path.join(BASE_PATH, contest)
    problem += '.cpp'

    mkfile(path, file=problem)

    os.system('code ' + path)
    os.system('code ' + os.path.join(path, problem))

@cli.command('test', short_help='test your code')
@click.argument('problem')
@click.option('--input', '-i', default=DEFAULT_INPUT)
@click.option('--output', '-o', default=DEFAULT_OUTPUT)
@click.option('--max-print', '-m', type=int, default=DEFAULT_OUTPUT_SIZE)
@click.option('--no-print', '-n', is_flag=True, default=False)
@click.option('--time-limit', '-t', is_flag=True, default=False)
def test(problem, input, output, max_print, no_print, time_limit):
    """
    Test your code.
    """
    click.secho('Testing => %s...' % (problem.rstrip('.exe')), fg='green')

    input = os.path.join(DATA_PATH, input)
    output = os.path.join(DATA_PATH, output)

    s, t = execTest(problem, input, time_limit)

    with click.open_file(output, 'w') as f:
        f.write(s)

    if no_print:
        return

    if max_print == -1:
        click.echo(s)
    else:
        s = s.split('\n')
        for item in s[:max_print]:
            click.echo(item)
        rest = len(s) - max_print
        if rest > 0:
            click.echo('<%d lines in %s>' % (rest, input))

    if time_limit:
        click.echo('Time: %dms' % t)

@cli.command('submit', short_help='submit your code')
def submit():
    click.secho('Logining...', fg='green')

    if not CF_USER['handle'] or not CF_USER['password']:
        click.echo('No handle or password...')
        return 

    browser = RoboBrowser(parser='html.parser')
    browser.open('http://codeforces.com/enter')
        
    enter_form = browser.get_form('enterForm')
    enter_form['handleOrEmail'] = CF_USER['handle']
    enter_form['password'] = CF_USER['password']
    browser.submit_form(enter_form)
    
    try:
	    checks = list(map(lambda x: x.getText()[1:].strip(), browser.select('div.caption.titled')))
	    if CF_USER['handle'] not in checks:
	        click.secho('Login Failed!', fg = 'red')
	        return
    except Exception as e:
	    click.secho('Login Failed!', fg = 'red')
	    return 

    click.secho('Login Success...', fg='green')
    click.secho('Contest id:')

    stdin = click.get_text_stream('stdin')

    try:
        cid = int(stdin.readline().strip())
    except Exception as ex:
        return 

    while True:
        click.echo('Submit: ')
        inp = stdin.readline().strip()
        if inp == 'q' or inp == 'exit' or inp == 'quit':
            click.echo('quit')
            return

        browser.open('https://codeforces.com/contest/%d/submit' % cid)
        submit_form = browser.get_form(class_='submit-form')
        submit_form['submittedProblemIndex'] = inp.upper()

        try:
            submit_form['sourceFile'] = inp + '.cpp'
        except Exception as ex:
            click.secho('No File', fg='red')
            return
        
        browser.submit_form(submit_form)

        click.secho('Problem %s submitted...' % inp.upper(), fg = 'green')


if __name__ == '__main__':
    cli()