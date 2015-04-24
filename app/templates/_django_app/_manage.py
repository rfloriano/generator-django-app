#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of <%= package.name %>.
# <%= package.url %>

# Licensed under the <%= package.license %> license:
# http://www.opensource.org/licenses/<%= package.license%>-license
# Copyright (c) <%= package.created.year %>, <%= package.author.name %> <<%= package.author.email %>>

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<%= package.pythonName %>.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
