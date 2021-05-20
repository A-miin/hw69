from django.shortcuts import render
import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def add(request, *args, **kwargs):
    answer = {}
    response = {}
    if request.body:
        print(request.body)
        res = json.loads(request.body)
        try:
            a = float(res['A'])
            b = float(res['B'])
            answer["answer"] = a + b
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
        except Exception as e:
            answer['error'] = str(e)
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            print('views py error = ', e)
    response['Content-Type'] = 'application/json'
    return response


def subtract(request, *args, **kwargs):
    answer = {}
    response = {}
    if request.body:
        res = json.loads(request.body)
        try:
            a = float(res['A'])
            b = float(res['B'])
            answer["answer"] = a - b
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
        except Exception as e:
            answer['error'] = str(e)
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


def multiply(request, *args, **kwargs):
    answer = {}
    response = {}
    if request.body:
        res = json.loads(request.body)
        try:
            a = float(res['A'])
            b = float(res['B'])
            answer["answer"] = a * b
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
        except Exception as e:
            answer['error'] = str(e)
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


def divide(request, *args, **kwargs):
    answer = {}
    response = {}
    if request.body:
        res = json.loads(request.body)
        try:
            a = float(res['A'])
            b = float(res['B'])
            answer["answer"] = a / b
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
        except Exception as e:
            answer['error'] = str(e)
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response
