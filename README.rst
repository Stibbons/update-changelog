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

Install it through Pypi:

  pip install update-changelog

Dependencies
============

- ``git``
- ``python-jinja``
- ``python-yaml`` and ``libyaml`` library

Usage
=====

Configure the ``.update-changelog.yml`` in your project.

Run ``update-changelog`` from the root of your project, so the configuration file is in the current directory.

Configuration File Syntax
=========================

Yaml file is organised in node. Please keep in mind that you should really be careful with the indentation!

The configuration file ``.update-changelog.yml`` should be at the root of your project.

General settings
----------------

 ``name``
   Name of your application
 
Input settings
--------------
 ``repository``
   ``.`` by default, meaning the current directory. If you use git, it will look for the root
  
Output settings
---------------

``formats``
  The desired output formats. You can enter more than one, simply configure them independantely::
  
    output:
      formats:
        changelog:
          ...
        default_rst:
          ...

For each format, use the following settings:

``enable``
  Boolean. Set to false to temporarily disable this output format.

``filename``
  Path to the file to generate/update, relative to the current path
  
``template``
  You may want to personalize the template. These are jinja template files.



Advanced Feature (not yet planified)
====================================
- ability to refresh from more than one project (aka work with android's repo)
