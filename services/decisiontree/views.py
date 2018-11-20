#!/usr/bin/env python3
#-*-coding:utf-8-*-

from webapp import app, api
from flask import request
from flask import jsonify
from flask_restful import Resource
import os
import requests

details = {
    "name" : "http://details:9080",
    "endpoint" : "details",
    "children" : []
}

class ApiWorkingCondition(Resource):

    def get(self):
        return self.post()

    def post(self):

        url = 'http://details:9080/details/1'
        res = requests.get(url)
        return res.json()
        #data = \
        #{
        #    'code': 0,
        #    'result':
        #    {
        #        'data':[]
        #    },
        #    'name':servicesDomain
        #}
        #return data

api.add_resource(ApiWorkingCondition, '/api/v2/test')
