#!/usr/bin/env python
# -*- coding: utf-8 -*-

import endpoints

from apis import demo_api
from apis.bugs import BugApi
from apis.count import CountApi

import logging


api = endpoints.api_server([
    demo_api,
])
