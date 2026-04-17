# Tutorial

This page contains a complete tutorial on how to create and start working on your project.

## Step 1: Install cookiecutter-hydro

```bash
pip install cookiecutter-hydro
```

## Step 2: Generate your project

Navigate to the directory in which you want the project to be
created.

```bash
cchydro
```

For an explanation of the prompt arguments which you will need to answer, see
[Prompt Arguments](./prompt_arguments.md).

After this step, you will have the structure of your project ready.

Then install dependencies and run checks:

```bash
cd <project_name>
pixi install
pixi run all
```

## Step 3: Set up your Github repository

Create an empty [new repository](https://github.com/new) on Github. Give
it a name that only contains alphanumeric characters and optionally `-`.
DO NOT check any boxes under the option `Initialize this repository
with`.

## Step 4: Upload your project to Github

Run the following commands, replacing `<project-name>` with the name
that you also gave the Github repository and `<github_author_handle>`
with your Github username.

```bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

## Step 5: Use the devcontainer (Recommended)

Devcontainers are incredible in making sure that whoever gets to look at you model will have an exact replica of your repository. That includes yourself if you sometimes work on different machines. Inside the .devcontainer folder is a configuration for the container. All you need to do is to download Devcontainer extension to VSCode and click "Reopen in devcontainer", what will immediatelly contenerize your project.

## Step 6: You're all set!

That's it! I hope this repository saved you a lot of manual configuration. If you have any improvement suggestions, feel
free to raise an issue or open a PR on Github!
