#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann.  All rights reserved.
#
"""Create Django projects automatically with virtualenvwrapper.
"""

import logging
import subprocess

log = logging.getLogger('virtualenvwrapper.django')

def template(args):
    """Installs Django and runs django-admin to create a new project.
    """
    project = args[0]
    subprocess.check_call(['pip', 'install', 'django'])
    log.info('Running "django-admin.py startprojects %s"', project)
    subprocess.check_call(['django-admin.py', 'startproject', project])
    return
