#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of <%= package.name %>.
# <%= package.url %>

# Licensed under the <%= package.license %> license:
# http://www.opensource.org/licenses/<%= package.license%>-license
# Copyright (c) <%= package.created.year %>, <%= package.author.name %> <<%= package.author.email %>>

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', '<%= package.pythonName %>.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
