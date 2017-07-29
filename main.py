#!/usr/bin/env python
# -*- coding: utf-8 -*-

import endpoints

from apis.demo import DemoApi

import logging



api = endpoints.api_server([DemoApi])
