from setuptools import setup, find_packages

#Read Readme File

with open ('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='src',
    version='1.0.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ArnabMitra0408',
    url='https://github.com/ArnabMitra0408/Flight-Price',
    packages=["src"],
    license="GNU",
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'pandas',
        'scikit-learn'
    ]
)