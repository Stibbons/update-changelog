================
update-changelog
================

Changelog management script.

Features
========

- Retrieve the changes from one project, reading the git commit messages
- Store it in various format:
  - GNU Changelog
  - one page reStructuredText file
  - one page MarkDown file
- Able to update just the **new** changes, since last refresh

Installation
============

.. code-block: bash

  pip install update-changelog


Advanced Feature (not yet planified)
====================================
- ability to refresh from more than one project (aka work with android's repo)
