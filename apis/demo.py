#!/usr/bin/env python
# -*- coding: utf-8 -*-

import endpoints

from protorpc import message_types
from protorpc import messages
from protorpc import remote

import logging


class DemoRequest(messages.Message):
    message = messages.StringField(1, required=True)


class DemoResponse(messages.Message):
    word_count = messages.IntegerField(1, required=True)
    message = messages.StringField(2)


@endpoints.api(name='demo', version='v1')
class DemoApi(remote.Service):

    @endpoints.method(DemoRequest, DemoResponse, path="demo")
    def count_words(self, request):
        message = request.message
        result = DemoResponse()
        result.word_count = len(message)
        result.message = message
        return result
