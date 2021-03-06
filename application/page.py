#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
from flask import Flask
from blueprint import PageBlueprint

import charcollection

page_bp = PageBlueprint('page', __name__, static_folder='../view/static', template_folder='../view/template')

@page_bp.route('/')
def main():
    return page_bp.make_response(collections = charcollection.collections, storage = charcollection.storage)


