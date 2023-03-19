"""
https://www.codewars.com/kata/54acc128329e634e9a000362/train/python
"""


class State:
    initial_state = ''
    event = ''
    new_state = ''

    def __init__(self, _initial_state, _event, _new_state):
        self.initial_state = _initial_state
        self.event = _event
        self.new_state = _new_state


def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always
    states = [
        State('CLOSED', 'APP_PASSIVE_OPEN', 'LISTEN'),
        State('CLOSED', 'APP_ACTIVE_OPEN', 'SYN_SENT'),
        State('LISTEN', 'RCV_SYN', 'SYN_RCVD'),
        State('LISTEN', 'APP_SEND', 'SYN_SENT'),
        State('LISTEN', 'APP_CLOSE', 'CLOSED'),
        State('SYN_RCVD', 'APP_CLOSE', 'FIN_WAIT_1'),
        State('SYN_RCVD', 'RCV_ACK', 'ESTABLISHED'),
        State('SYN_SENT', 'RCV_SYN', 'SYN_RCVD'),
        State('SYN_SENT', 'RCV_SYN_ACK', 'ESTABLISHED'),
        State('SYN_SENT', 'APP_CLOSE', 'CLOSED'),
        State('ESTABLISHED', 'APP_CLOSE', 'FIN_WAIT_1'),
        State('ESTABLISHED', 'RCV_FIN', 'CLOSE_WAIT'),
        State('FIN_WAIT_1', 'RCV_FIN', 'CLOSING'),
        State('FIN_WAIT_1', 'RCV_FIN_ACK', 'TIME_WAIT'),
        State('FIN_WAIT_1', 'RCV_ACK', 'FIN_WAIT_2'),
        State('CLOSING', 'RCV_ACK', 'TIME_WAIT'),
        State('FIN_WAIT_2', 'RCV_FIN', 'TIME_WAIT'),
        State('TIME_WAIT', 'APP_TIMEOUT', 'CLOSED'),
        State('CLOSE_WAIT', 'APP_CLOSE', 'LAST_ACK'),
        State('LAST_ACK', 'RCV_ACK', 'CLOSED'),
    ]

    for e in events:
        updated = False
        for s in states:
            if state == s.initial_state and e == s.event:
                state = s.new_state
                updated = True
                break
        if not updated:
            return 'ERROR'
    return state

if __name__ == '__main__':
    print(traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]))
