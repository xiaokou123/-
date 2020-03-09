import requests
import json,time
def senddingding(params):
    data = {
        "msgtype": "text",
        "text": {
            "content":params.get("content")
        },
        "at": {
            "atMobiles": [
                params.get("atMobiles")
            ],
            "isAtAll":params.get("isAtAll")
        }
    }

    ### 发送请求


    url = "https://oapi.dingtalk.com/robot/send?access_token=308586b57e4843d155df2f8dbb523319f6a6921bf391d6ad8699aed9e78a15aa"
    headers = {'Content-Type': 'application/json'}
    ## 转json
    data = json.dumps(data)
    resp = requests.post(url,headers = headers,data=data)
    print(resp.content.decode())
