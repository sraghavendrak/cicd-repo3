import logging

def function_cicd(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Log the incoming request for debugging purposes
    logging.info(f"Request args: {request.args}")
    try:
        request_json = request.get_json(silent=True)
        logging.info(f"Request JSON: {request_json}")
    except Exception as e:
        logging.error(f"Failed to parse JSON: {e}")
        return f"Failed to parse JSON: {e}", 400

    # Handle the request based on query parameters or JSON payload
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return 'CloudFunction with v1.0 with CI/CD Pipeline'

