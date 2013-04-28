#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann.  All rights reserved.
#
"""Create Django projects automatically with virtualenvwrapper.
"""

import logging
import os
import subprocess

log = logging.getLogger('virtualenvwrapper.django')


def template(args):
    """Installs Django and runs django-admin to create a new project.
    """
    project, project_dir = args
    os.chdir(project_dir)
    subprocess.check_call(['pip', 'install', 'django'])
    log.info('Running "django-admin.py startproject %s"', project)
    subprocess.check_call(['django-admin.py', 'startproject', project])
    return
