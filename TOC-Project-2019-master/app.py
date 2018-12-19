from bottle import route, run, request, abort, static_file
from fsm import TocMachine


VERIFY_TOKEN = "123"
machine = TocMachine(
    states=[
        'user',
        'statea1',
        'statea2',
        'stateb1',
        'stateb2',
        'stateb3',
        'stateb4',
        'staten1',
        'staten2',
        'staten3',
        'staten4',
        'staten5',
        'staten6',
        'staten7',
        'statem1',
        'statem2',
        'statem3',
        'statem4',
        'statem5',
        'statem6',
        'states1',
        'states2',
        'states3',
        'statee1',
        'statee2',
        'statee3',
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'statea1',
            'conditions': 'is_going_to_statea1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'statea2',
            'conditions': 'is_going_to_statea2'
        },
        {
            'trigger': 'advance',
            'source': 'statea1',
            'dest': 'stateb1',
            'conditions': 'is_going_to_stateb1'
        },
        {
            'trigger': 'advance',
            'source': 'statea1',
            'dest': 'stateb2',
            'conditions': 'is_going_to_stateb2'
        },
        {
            'trigger': 'advance',
            'source': 'statea1',
            'dest': 'stateb3',
            'conditions': 'is_going_to_stateb3'
        },
        {
            'trigger': 'advance',
            'source': 'statea1',
            'dest': 'stateb4',
            'conditions': 'is_going_to_stateb4'
        },
        {
            'trigger': 'advance',
            'source': 'stateb1',
            'dest': 'staten1',
            'conditions': 'is_going_to_staten1'
        },
        {
            'trigger': 'advance',
            'source': 'stateb1',
            'dest': 'staten2',
            'conditions': 'is_going_to_staten2'
        },
        {
            'trigger': 'advance',
            'source': 'stateb1',
            'dest': 'staten3',
            'conditions': 'is_going_to_staten3'
        },
        {
            'trigger': 'advance',
            'source': 'stateb1',
            'dest': 'staten4',
            'conditions': 'is_going_to_staten4'
        },
        {
            'trigger': 'advance',
            'source': 'stateb1',
            'dest': 'staten5',
            'conditions': 'is_going_to_staten5'
        },
        {
            'trigger': 'advance',
            'source': 'stateb1',
            'dest': 'staten6',
            'conditions': 'is_going_to_staten6'
        },
        {
            'trigger': 'advance',
            'source': 'stateb1',
            'dest': 'staten7',
            'conditions': 'is_going_to_staten7'
        },
        {
            'trigger': 'advance',
            'source': 'stateb2',
            'dest': 'statem1',
            'conditions': 'is_going_to_statem1'
        },
        {
            'trigger': 'advance',
            'source': 'stateb2',
            'dest': 'statem2',
            'conditions': 'is_going_to_statem2'
        },
        {
            'trigger': 'advance',
            'source': 'stateb2',
            'dest': 'statem3',
            'conditions': 'is_going_to_statem3'
        },
        {
            'trigger': 'advance',
            'source': 'stateb2',
            'dest': 'statem4',
            'conditions': 'is_going_to_statem4'
        },
        {
            'trigger': 'advance',
            'source': 'stateb2',
            'dest': 'statem5',
            'conditions': 'is_going_to_statem5'
        },
        {
            'trigger': 'advance',
            'source': 'stateb2',
            'dest': 'statem6',
            'conditions': 'is_going_to_statem6'
        },
        {
            'trigger': 'advance',
            'source': 'stateb3',
            'dest': 'states1',
            'conditions': 'is_going_to_states1'
        },
        {
            'trigger': 'advance',
            'source': 'stateb3',
            'dest': 'states2',
            'conditions': 'is_going_to_states2'
        },
        {
            'trigger': 'advance',
            'source': 'stateb3',
            'dest': 'states3',
            'conditions': 'is_going_to_states3'
        },
        {
            'trigger': 'advance',
            'source': 'stateb4',
            'dest': 'statee1',
            'conditions': 'is_going_to_statee1'
        },
        {
            'trigger': 'advance',
            'source': 'stateb4',
            'dest': 'statee2',
            'conditions': 'is_going_to_statee2'
        },
        {
            'trigger': 'advance',
            'source': 'stateb4',
            'dest': 'statee3',
            'conditions': 'is_going_to_statee3'
        },
        {
            'trigger': 'advance',
            'source': ['staten1',
                      'staten2',
                      'staten3',
                      'staten4',
                      'staten5',
                      'staten6',
                      'staten7',
                      'statem1',
                      'statem2',
                      'statem3',
                      'statem4',
                      'statem5',
                      'statem6',
                      'states1',
                      'states2',
                      'states3',
                      'statee1',
                      'statee2',
                      'statee3',],
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'go_back',
            'source': [
                'statea1',
                'statea2'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'go_back',
            'source': [
                'stateb1',
                'stateb2',
                'stateb3',
                'stateb4'
            ],
            'dest': 'statea1'
        },
        {
            'trigger': 'go_back',
            'source': [
                'staten1',
                'staten2',
                'staten3',
                'staten4',
                'staten5',
                'staten6',
                'staten7'
            ],
            'dest': 'stateb1'
        },
        {
            'trigger': 'go_back',
            'source': [
                'statem1',
                'statem2',
                'statem3',
                'statem4',
                'statem5',
                'statem6'
            ],
            'dest': 'stateb2'
        },
        {
            'trigger': 'go_back',
            'source': [
                'states1',
                'states2',
                'states3'
            ],
            'dest': 'stateb3'
        },
        {
            'trigger': 'go_back',
            'source': [
                'statee1',
                'statee2',
                'statee3'
            ],
            'dest': 'stateb4'
        },    
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=220, debug=True)
