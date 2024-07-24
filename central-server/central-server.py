from bottle import run, get, post, request, route, response
from json import dumps

@get('/test')
def process_test():
    return "This is dummy central server. Test passed\n"

@route('/mode/<tl_id>', method = 'GET')
def process_test(tl_id):
    print(f"requested mode for TL with ID {tl_id}")
    mode = { "request_id": "AAA-BBB",
             "direction_1": {
                 "red_duration_sec": 99,
                 "yellow_duration_sec": 2,
                 "green_duration_sec": 15
             }
           }
    response.content_type = 'application/json'
    return dumps(mode)


@post('/diagnostics')
def process_kos():
    tl_data = request.json

    # print the dictionary
    print(f"\n{tl_data}\n")

    # and/or extract data and print nicer
    tl_id   = tl_data["tl-id"]
    tl_status = tl_data["tl-status"]
    tl_mode_id = tl_data["tl-mode-id"]

    print(f"tl-id: {tl_id}\n"
          f"tl-status: {tl_status}\n"
          f"tl-mode-id: {tl_mode_id}\n"
          )
    return "TL diagnostics received ok\n"


run(host='0.0.0.0', port=8081, debug=True)
