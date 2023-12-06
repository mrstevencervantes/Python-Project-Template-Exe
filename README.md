# Python Project Template

This Python Project Template provides a starting point for Python automations, featuring a main error handler, custom logging, and Excel configuration settings. Follow the instructions below to get started.  <small>**Note**: The following commands are for Windows. Please follow these steps in your terminal (Command Prompt, PowerShell, or any terminal emulator):</small>

## Table of Contents
- [Using this Template](#using-this-template)
  - [Create a Repository](#create-a-repository)
  - [Clone the Repository](#clone-the-repository)
- [Setting Up a Virtual Environment (Optional)](#setting-up-a-virtual-environment-optional)
- [Installing Dependencies](#installing-dependencies)

---

## Using this Template

Choose from the following options to use this template for your project:

### Create a Repository

Creating a new repository from this template allows you to start fresh with a clean slate. This is useful when you want to maintain a separate repository history, collaborate with others, and manage your project independently.

1. Click the green "Use this template" button near the top-right corner.
2. Specify repository details (name, description, visibility).
3. Click "Create repository from template."

For detailed instructions, refer to GitHub's [official documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

### Clone the Repository

Cloning the template repository is a quick way to begin your project by copying its structure and files. This method is suitable when you want to work on a personal project or experiment without the need for a separate repository. There are multiple ways to clone a repository that won't be discussed here.

Refer to this [guide](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-a-repository) for various methods to clone a repository.

## Setting Up a Virtual Environment (Optional)

To maintain a clean and isolated development environment, it's a good idea to set up a virtual environment before you begin development. In this context, we'll utilize the [venv](https://docs.python.org/3/library/venv.html) package that comes included with the standard library.

1. Create a virtual environment:<br><br>
`py -m venv c:\path\to\myenv --upgrade-deps`<br><br>
<small>**Note**: The **<code>c:\path\to\myenv</code>** can be anything you choose. In this example we will use **venv**, which will create the virtual environment in the current working directory wtih the name **venv**. Additionally, the `upgrade-deps` flag will install the latest versions of **pip** and **setuptools** in the **venv** virtual environment.</small><br><br>
2. Activate the virtual environment:<br><br>
`c:\path\to\myenv\Scripts\activate`<br><br>
3. Add the virtual environment to the .gitignore file:<br><br>
<code>Add-Content -Path ".gitignore" -Value "c:\path\to\myenv/"</code>


Example commands:
```bash
py -m venv venv --upgrade-deps
venv\Scripts\activate
Add-Content -Path ".gitignore" -Value "venv/"
```

To deactivate the virtual environment when not in use or switching environments:

   `deactivate`

## Installing Dependencies

Before beginning development, ensure your environment is up to date.

1. If you did not use the `upgrade-deps` flag when creating the virtual environment, then it is recommended that you now update pip and setuptools and/or install wheel:<br><br>
`py -m pip install --upgrade pip setuptools wheel`<br><br>
2. This template relies on 3rd party packages to run. Install the required packages from `requirements.txt`:<br><br>
`pip install -r requirements.txt`<br><br>
3. After installing the necessary packages, update your existing requirements.txt file with the latest package details:<br><br>
<code>pip freeze > requirements.txt</code>


Example commands:
```bash
py -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip freeze > requirements.txt
```

By following these steps, you will have a well-prepared environment for development.


Delete to here to use the templated README.md below.


---

# Project Name

Short project description.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction

A brief introduction to your project. Explain its purpose, goals, and any relevant background information.

## Features

Highlight key features and functionality of your project. Provide a bulleted list or brief descriptions.

## Installation

Provide step-by-step instructions on how to install and set up your project. Include any prerequisites, dependencies, or system requirements.

```bash
# Example commands
git clone https://github.com/yourusername/your-project.git
cd your-project
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Explain how to use your project. Include code examples, command-line usage, or any other relevant information.

```bash
# Example commands
python main.py --input input_file.txt
```

## Configuration

Explain how to configure your project, including any configuration files, environment variables, or settings.
