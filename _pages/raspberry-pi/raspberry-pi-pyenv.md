---
title: pyenv
date: 2016-01-08 15:04:23
category: raspberry-pi
tags: [python]

layout: page
---

Have multiple python versions never been so easy using `pyenv`.

Similar to `rbenv`

## Pre reqisites

```
bzip2 libbz2-dev libreadline6 libreadline6-dev libffi-dev libssl1.0-dev sqlite3 libsqlite3-dev
```

## Installation

Enter in the terminal:

```bash
git clone git://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

### Refresh

```bash
. ~/.bashrc
```

## Usage

### Installation

Enter the following for installing a specific Python version:

```bash
pyenv install 3.8.2
```

### Versions

The installation takes a while. Now, show all installed versions by entering

```bash
pyenv versions
```

A specific Python version can be linked to a directory:

```
mkdir app && cd app
pyenv local 3.8.2
python -V
```
### Global

```bash
pyenv global 3.8.2
```
