# bmi203hw1

[![Build
Status](https://travis-ci.org/afkung/bmi203hw1.svg?branch=master)](https://travis-ci.org/afkung/bmi203hw1)

Example python project with testing.

## usage

To use the package, first make a new conda environment and activate it

```
conda create -n exampleenv python=3
source activate exampleenv
```

then run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `bmi203hw1/__main__.py`) can be run as follows

```
python -m bmi203hw1
```

## testing

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.
