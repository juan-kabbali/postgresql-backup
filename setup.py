from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as readme_file:
    readme = readme_file.read()


setup(
    name='pgbackup',
    version='0.1.0',
    description='Postgres database backups locally or to AWS S3.',
    long_description=readme,

    author='Juan Pablo Aguirre',
    author_email='juanpablomartinez590@hotmail.com',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=[]
)
