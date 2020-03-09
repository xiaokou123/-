from __future__ import absolute_import
from Qshop.celery import app



@app.task
def Test():
    print("hello world")

@app.task
def Myprint(num):
    print(num)

from sdk.dingding import senddingding
@app.task
def senddingd(params):
    senddingding(params)