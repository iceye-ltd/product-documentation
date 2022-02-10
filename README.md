# ICEYE Product Documentation

If you are reading this then you are probably interested to look 'under the hood' of the [ICEYE Product Documentation](https://iceye-ltd.github.io/product-documentation/). This doc will tell you how it works and how to add to it or make ammendments. There are two types of contributors :

* The general public, enthusiasts, scientists, engineers, geeks (and grammer ninjas)
* ICEYE staff with access to github and our internal engineering environment

We welcome input from both groups but the access to the github repo is different for each. 

* ICEYE Engineers can make edits to the documentation directly. Please don't ;-) (unless its a small typo
change or error). Otherwise, clone the repo, make a branch with your changes and submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) so that we can have a second pair of eyes look over the changes.
* Everyone else, feel free to fork this repo into your own Github account and make the changes there. When you are happy with the changes, make a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to merge your work including a short summary about what the changes are and why.

## Installation
The ICEYE Product Documentation is built using `python`, `mkdoc`, `material for mkdocs` and `mike`. 

1. Make sure you have a github account and clone the repo.
2. Install python 3.8 or higher
3. Install [`mkdocs`](https://mkdocs.readthedocs.io/en/stable/#installation)
4. Install [`Material` for `mkdocs`](https://squidfunk.github.io/mkdocs-material/getting-started/)


To get the documentation running on your own local computer :

1. `cd product-documentation`
2. `mkdocs serve`
3. open `http://127.0.0.1:8000/product-documentation/` using your web browser.
4. Edit the documentation in the `docs` folder. Everytime you save a file the documentation will be updated and your browser will be refreshed.
5. When you are happy check your code back in to GitHub and make a pull request.