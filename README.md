# bmi203hw1

[![Build
Status](https://travis-ci.org/afkung/bmi203hw1.svg?branch=master)](https://travis-ci.org/afkung/bmi203hw1)

BMI HW #1 with testing.

## usage

To use the package, first make a new conda environment and activate it

```
conda create -n hw1env python=3
source activate hw1env
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
