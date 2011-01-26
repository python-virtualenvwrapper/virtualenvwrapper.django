#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann.  All rights reserved.
#
"""Create Django projects automatically with virtualenvwrapper.
"""

import subprocess

def template(args):
    """Installs Django and runs django-admin to create a new project.
    """
    project = args[0]
    subprocess.check_call(['pip', 'install', 'django'])
    subprocess.check_call(['django-admin.py', 'startproject', project])
    return
