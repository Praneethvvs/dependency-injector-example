# Project Setup Guide

This guide will walk you through the steps to set up your project environment using `pyenv-win`, `venv`, and `poetry`.

## Prerequisites

- Windows OS
- Git installed (optional for cloning repositories)
- Visual Studio Code installed (for launching the app)

## Steps

### 1. Install pyenv-win

Install `pyenv-win` by following the instructions on the [pyenv-win GitHub page](https://github.com/pyenv-win/pyenv-win).

### 2. Check pyenv version

After installing `pyenv-win`, open a command prompt and run:

```sh
pyenv --version
```

### 3.  Install Python 3.10.0 using pyenv

Install python 3.10.0 using pyenv

```sh
pyenv install 3.10.0
```

### 4.  Set Python 3.10.0 Globally

Set the installed Python version as the global version:

```sh
pyenv global 3.10.0
```

### 5.  Verify Python Version

Check if Python 3.10.0 is set globally. Close and reopen the command prompt to ensure the changes take effect, then run:

```sh
python --version
```

### 6.  Set Up Virtual Environment

Navigate to your project directory and create a virtual environment at the root. Activate the virtual environment.

```sh
cd path/to/your/project
python -m venv venv
.\venv\Scripts\activate
```

### 7.  Install Poetry

Install a specific version poetry inside the venv. For this project we will use poetry 1.7.1 

```sh
pip install poetry==1.7.1
poetry --version
```

### 8.  Install Project Dependencies

Use poetry to install the project dependencies defined in the pyproject.toml file:

```sh
poetry install
```

### 9.  Launch the App Using VSCode

Use the launch.json configuration in Visual Studio Code to launch the application. Ensure you have the launch.json file properly configured in the .vscode directory of your project. For reference, a sample launch.json is included in this project.

Open VSCode, navigate to the Run and Debug view, and start the app using the configured launch settings.







