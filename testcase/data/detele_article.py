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
#         管理员发表的文章
        "test_delete_article_010": {
        "req_data": {
            "aid":"261",
            "state": "1"
        },
        "res_key": "status",
        "res_value": "success"
        },
        # 管理员发表的多篇文章
        "test_delete_article_011": {
        "req_data": {
            "aid":[246,245],
            "state": "1"
        },
        "res_key": "status",
        "res_value": "success"
        },
        # 其他用户发表的文章
        "test_delete_article_012": {
        "req_data": {
            "aid":"264",
            "state": "1"
        },
        "res_key": "status",
        "res_value": "success"
        },
        # 不传aid参数
        "test_delete_article_013": {
        "req_data": {
            "state": "1"
        },
        "res_key": "status",
        "res_value": "success"
        },
}