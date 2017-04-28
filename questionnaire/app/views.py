# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# some_app/views.py
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
