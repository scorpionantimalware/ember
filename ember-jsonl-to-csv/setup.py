import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="UTF-8") as f:
    readme = f.read()

setup(
    name='ember-jsonl-to-csv',
    version='1.0.0',
    description="Converts ember jsonl files to csv files.",
    long_description=readme,
    packages=['ember_jsonl_to_csv'],
    author='Saif Kandil'
)
