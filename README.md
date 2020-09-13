<p align="center">
  <img src="https://github.com/pseudoPixels/iSeaborn/blob/master/docs/_static/logo/iSeaborn.png" width="40%" title="iSeaborn">
</p>


# iSeaborn
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pseudoPixels/iSeaborn/master)
[![Documentation Status](https://readthedocs.org/projects/iseaborn/badge/?version=latest)](https://iseaborn.readthedocs.io/en/latest/?badge=latest)

iSeaborn is an interactive version of the popular statistical data visualization library - Seaborn. iSeaborn is build on top of Seaborn (i.e., for advanced statistical
computation) and Bokeh (i.e., for interactive plots). 

Checkout the installation and details documentations of [iSeaborn here](https://iseaborn.readthedocs.io/en/latest/) .


## Installation


### From PyPI

Installing the package from PyPI is the easiest method of installation. To install:

```
$ pip install iSeaborn
```

### From Source
The package can also be installed direct from source. This a method of installation is preferred
for development or contribution to the package. To install from git source:

```
$ git clone https://github.com/pseudoPixels/iSeaborn.git
$ cd iSeaborn
$ pip install -e .
```







## Contributing
If you are planning to contribute to iSeaborn, you will first need to set up a local development
environment.

### Environment Setup and Dev Installation


1. Install Python. Python 3.6 or above recommended.

2. Create and activate a virtualenv, using the tool of your choice:

```
$ conda create -n iSeabornEnv python=3.6
$ conda activate iSeabornEnv
```

3. Clone the dagster repository to the destination of your choice:

```
$ git clone https://github.com/pseudoPixels/iSeaborn.git
```

4. Install from the setup.py in development mode:

```
$ cd iSeaborn
$ pip install -e .
```

### Developing Docs
The documentation of the project is created using sphinx. Our documentation employs a combination of Markdown and reStructuredText.
To build your updated docs:

```
$ cd docs
$ make html
```


## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope
This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team on Slack. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution
This Code of Conduct is adapted from the Contributor Covenant, version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq


