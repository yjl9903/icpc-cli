from setuptools import setup, find_packages

setup(
    name="icpc-cli",
    version="0.9",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'icpc': ['static/*', 'static/.vscode/*']
    },
    py_modules=['icpc', 'src'],
    install_requires=[
        'Click', 'robobrowser', 'requests', 'colorama'
    ],
    entry_points='''
        [console_scripts]
        icpc=icpc.app:cli
        init=icpc.app:init
        open=icpc.app:open
        test=icpc.app:test
    '''
)