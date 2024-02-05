import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="UTF-8") as f:
    readme = f.read()

setup(
    name='csv-generator-from-ember-jsonl',
    version='1.0.0',
    description="CSV generator from ember jsonl file.",
    long_description=readme,
    packages=['csv_generator_modules'],
    author='Saif Kandil'
)
