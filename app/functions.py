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
    # Default Values  
    formValues = {
        'divWidth': 410,
        'divHeight': 410,
        'containerHeight': 480,
        'divStyle': 'testing',
        'divDetail': 60,
        'divVar': 16,
        'divCol': '#bbbbbb'
    }
    # If the form is submitted, update the formValues with the submitted data
    if request.method == 'POST':
        for key in formValues:
            if key in request.form:
                formValues[key] = request.form.get(key)
    return formValues