 # -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse,JsonResponse

def index(request):

    return render(request,'login.html')

def regist(request):

    sign_id = request.GET.get('sign_id')
    sign_pw = request.GET.get('sign_pw')
    sign_name = request.GET.get('sign_name')

    print sign_id
    print sign_pw
    print sign_name


    with connections['default'].cursor() as cur:
            query = '''
                insert into login(id, password, name)
                values('{id}','{password}','{name}')
            '''.format(id=sign_id,password=sign_pw,name=sign_name,)
            cur.execute(query)
            print query

    return JsonResponse({'return':'success', 'sign_id':sign_id, 'sign_pw':sign_pw,'sign_name':sign_name})