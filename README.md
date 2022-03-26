![ci](https://github.com/Esme-Sudria-Database/lab-postgresql/workflows/ci/badge.svg)


This blueprint provides an environment to build a workstation based on ``docker-compose``.

A workstation make easier activities as :

* organize a lab with students
* provision a developer environment for new comers
* ...

Services
===================

* [webconsole](http://localhost:7681) : un terminal disponible dans son navigateur web
* (add your own services ...)

Requirement 1 : installation to perform on your computer
========================================================

You will need those softwares on your computer :

* [Docker](https://www.docker.com/)
* [Git](https://git-scm.com/)

On linux
---------

* 1. [install docker](https://docs.docker.com/engine/install/ubuntu/)

* 2. install git

```
sudo apt-get install git
```

* 3. [install docker-compose](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)

On windows
-----------

* 1. [install docker](https://docs.docker.com/docker-for-windows/install/)

* 2. [install git](https://git-scm.com/download/win)

On mac
-------

* 1. [install docker](https://docs.docker.com/docker-for-mac/install/)

* 2. install git

```
brew install git
```

Step 1 : install the environment
================================

1. clone this repository :

```
git clone https://github.com/FabienArcellier/blueprint-docker-workstation.git
```

3. go on the directory and mount the workstation

```bash
cd blueprint-docker-workstation
docker-compose up
```

Architecture
============

[To complete]

Troubleshooting
===============

[To complete]

Run continuous integration process
==================================

    make tests
