def success(data, code=200, message=None):
    return {
        "status": "success",
        "statusCode": code,
        "data": data,
        "message": message
    }

def notfound(message):
    return {
        "status": "error",
        "statusCode": 404,
        "data": None,
        "message": message
    }

def error(code, message):
    return {
        "status": "error",
        "statusCode": code,
        "data": None,
        "message": message
    }
