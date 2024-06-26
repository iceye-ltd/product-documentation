# ICEYE Product Documentation

If you are reading this then you are probably interested to look 'under the hood' of the [ICEYE Product Documentation](https://iceye-ltd.github.io/product-documentation/). This doc will tell you how it works and how to add to it or make ammendments. There are two types of contributors :

* The general public, enthusiasts, scientists, engineers, geeks (and grammer ninjas)
* ICEYE staff with access to github and our internal engineering environment

We welcome input from both groups but the access to the github repo is different for each.

* ICEYE Engineers can make edits to the documentation directly. Please don't ;-) (unless its a small typo
change or error). Otherwise, clone the repo, make a branch with your changes and submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) so that we can have a second pair of eyes look over the changes.
* Everyone else, feel free to fork this repo into your own Github account and make the changes there. When you are happy with the changes, make a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to merge your work including a short summary about what the changes are and why.

## Installation
### Easy way

The ICEYE Product Documentation is built using `python`, `mkdocs`, `material for mkdocs` and `mike`. The easiest way to install these is to use `uv` and the `requirements` file.

Install [uv](https://github.com/astral-sh/uv) - the fast python package manager:
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# For a specific version.
curl -LsSf https://astral.sh/uv/0.2.15/install.sh | sh
powershell -c "irm https://astral.sh/uv/0.2.15/install.ps1 | iex"

# With pip.
pip install uv

# With pipx.
pipx install uv

# With Homebrew.
brew install uv
```

From Linux / OSX terminal:
```bash
uv venv --python 3.11 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### By hand

1. Make sure you have a github account and clone the repo.
2. Install python 3.8 or higher
3. Install [`mike`](https://github.com/jimporter/mike)
4. Install [`mkdocs`](https://mkdocs.readthedocs.io/en/stable/#installation)
5. Install [`Material` for `mkdocs`](https://squidfunk.github.io/mkdocs-material/getting-started/)


## Running the documentation locally
To get the documentation running on your own local computer :

1. `cd product-documentation`
2. `mkdocs serve`
3. open `http://127.0.0.1:8000/product-documentation/` using your web browser.
4. Edit the documentation in the `docs` folder. Everytime you save a file the documentation will be updated and your browser will be refreshed.
5. When you are happy check your code back in to GitHub and make a pull request.

## How to Make a New Release

1. Make changes and check back in as described above
2. Deploy the changes to the latest version on the gh-pages branch using `mike`

    `mike deploy <version> latest -u`

This command deploys the latest changes on the master branch to the gh-pages under the version 5.0 and updates the 'latest' tag to be this one.
