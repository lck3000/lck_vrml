import click
import os

@click.command()
@click.option('--name')
def exec_wrl(name):
    absname = os.path.abspath(name)
    os.system('iexplore.exe '+absname)

if __name__ == "__main__":
    exec_wrl()