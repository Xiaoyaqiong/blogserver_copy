DELETE_DATA={
    "test_delete_article_001":{
        "req_data":{
            "aids": "260",
            "state": "-1"
        },
        "res_key": "status",
        "res_value": "error"
    },
    "test_delete_article_002": {
        "req_data": {
            "aids": "263",
            "state": "0"
        },
        "res_key": "status",
        "res_value": "success"
    },
    "test_delete_article_003": {
        "req_data": {
            "aids": "255",
            "state": "2"
        },
        "res_key": "status",
        "res_value": "success"
    },
    "test_delete_article_004": {
        "req_data": {
            "aids": "247",
            "state": "1"
        },
        "res_key": "status",
        "res_value": "success"
    },
    "test_delete_article_005": {
        "req_data": {
            "aids": "145",
        },
        "res_key": "status",
        "res_value": 400
    },
#     aid参数校验
        "test_delete_article_006": {
        "req_data": {
            "aids": "261",
            "state": "1"
        },
        "res_key": "status",
        "res_value": "success"
        },
        "test_delete_article_007": {
        "req_data": {
            "aids": [259,246],
            "state": "1"
        },
        "res_key": "status",
        "res_value": "success"
        },
        "test_delete_article_008": {
        "req_data": {
            "aids": "264",
            "state": "1"
        },
        "res_key": "status",
        "res_value": "error"
        },
        "test_delete_article_009": {
        "req_data": {
            "state": "1"
        },
        "res_key": "status",
        "res_value": 400
        },
#     管理员特权
}