#!/usr/bin/env python3

import requests


def handler(ctx, inputs):
    url = inputs["url"]
    method = "GET"
    if "method" in inputs:
        method = inputs["method"]

    headers = {}
    if "headers" in inputs:
        headers = inputs["headers"]

    url_params = {}
    if "urlParams" in inputs:
        url_params = inputs["urlParams"]

    payload = None
    if "payload" in inputs:
        payload = inputs["payload"]
    if "bodyParams" in inputs:
        payload = inputs["bodyParams"]

    print("Performing {} request to {}".format(method, url))

    try:
        response = requests.request(method=method,
                                    url=url,
                                    headers=headers,
                                    params=url_params,
                                    data=payload,
                                    verify=False)

        print("Got {}: {}".format(response.status_code, response.reason))

        # extract header values to plain dict so that json.dumps don't fail
        headers_out = {}
        for k, v in response.headers.items():
            headers_out[k] = v

        #context.outputs["responseBody"] = response.text
        #context.outputs["responseHeaders"] = headers_out
        
        return {'responseBody' : response.text, 'responseHeaders': headers_out}
    except Exception as e:
        print("Got exception: " + str(e))
        raise
