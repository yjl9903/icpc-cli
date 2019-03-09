from setuptools import setup, find_packages

setup(
    name="icpc",
    version="0.1",
    # packages=find_packages(),
    # include_package_data=True,
    py_modules=['icpc', 'src'],
    install_requires=[
        'Click', 'robobrowser', 'requests', 'colorama'
    ],
    entry_points='''
        [console_scripts]
        icpc=icpc:cli
    '''
)