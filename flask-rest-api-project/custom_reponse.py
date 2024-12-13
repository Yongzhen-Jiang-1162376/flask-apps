def success(data, message=None):
    return {
        "status": "success",
        "statusCode": 200,
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

def error(message, code):
    return {
        "status": "error",
        "statusCode": code,
        "data": None,
        "message": message
    }
