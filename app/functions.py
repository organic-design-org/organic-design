from flask import session

def msg_modal(msg):
    if msg == 'clear':
        session['msg'] = False
        return
    if len(session['messages']) == 0:
        session['msg'] = True
        session['messages'] = []
        session['messages'].append(msg)
    else:
        session['messages'].append(msg)

def conf_modal(msg, url, cancel=False):
    session['conf'] = True
    session['confirm'] = msg
    session['confirmroute'] = url
    if cancel:
        session['cancel'] = True