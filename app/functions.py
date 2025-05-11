from flask import request, session

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

def get_form_values():
    formValues = {}
    formValues['divWidth'] = request.form.get('divWidth')
    formValues['divHeight'] = request.form.get('divHeight')
    formValues['containerHeight'] = int(formValues['divHeight']) + 70
    return formValues