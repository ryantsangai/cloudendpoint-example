#!/usr/bin/env python
# -*- coding: utf-8 -*-

import endpoints

from protorpc import message_types
from protorpc import messages
from protorpc import remote

import logging

from . import demo_api


class BugRequest(messages.Message):
    name = messages.StringField(1, required=True)


bug_resource = endpoints.ResourceContainer(
    BugRequest,
    number=messages.IntegerField(2, default=1)
)


class BugResponse(messages.Message):
    name = messages.StringField(1, required=True)
    created_by = messages.StringField(2)


class MultiBugResponse(messages.Message):
    results = messages.MessageField(BugResponse, 1, repeated=True)


@demo_api.api_class(resource_name='bugs', path='bugs')
class BugApi(remote.Service):

    @endpoints.method(bug_resource, MultiBugResponse, http_method="POST")
    def create_bug(self, request):
        # https://cloud.google.com/endpoints/docs/frameworks/python/authenticating-users
        auth = endpoints.get_current_user()
        email = auth.email() if auth else 'Guest'
        results = [BugResponse(name=request.name, created_by=email) for i in range(request.number)]
        return MultiBugResponse(results=results)
