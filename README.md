# Random Name Generator
## About
This is a project that uses machine learning to generate names similar to a those from a specified language. This does not pick from a list, instead it uses markov chains to find patterns in a given list, and generates names that follows those patterns.

## Dependencies
Pomegranate's MarkovChain functions are used to read the markov chain models used. To get it you simply have to use

```pip install pomegranate```

## Running
Run ```demo.py``` to see the preliminary demonstration of this project

## Built With
[Pomegranate](https://pomegranate.readthedocs.io/en/latest/index.html) - Generates and reads markov chains

[Pandas](https://pandas.pydata.org/) - Edit the data to be used by Pomegranate

[SQLite](https://www.sqlite.org/index.html) - Generate a sqlite file for use with SQLAlchemy

[SQLAlchemy](https://www.sqlalchemy.org/) - Manipulate the data for easier use with Pandas

## Authors
* Kent Hazen