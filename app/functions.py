import random
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

def intRandom(min, max):
    return random.randint(min, max)

def get_form_values():
    # Default Values  
    formValues = {
        'divWidth': 410,
        'orgDivWidth': 410,
        'divHeight': 410,
        'orgDivHeight': 410,
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
    
    if formValues['divStyle'] == 'testing':
        formValues['containerHeight'] = int(formValues['divHeight']) + 70
        formValues['clipPath'] = 'none'
        formValues['shapeOutside'] = 'none'
    return formValues

def rectJag(formValues):
    divDetail = 110 - int(formValues['divDetail'])
    xs = int(formValues['divVar']) + 20
    ys = int(formValues['divVar']) + 20
    xe = int(formValues['divWidth']) + xs
    ye = int(formValues['divHeight']) + ys
    formValues['orgDivHeight'] = str(int(formValues['divHeight']) + int(formValues['divVar']) + 50) + 'px'
    formValues['orgDivWidth'] = str(int(formValues['divWidth']) + int(formValues['divVar']) + 50) + 'px'
    formValues['containerHeight'] = str(int(formValues['divHeight']) + int(formValues['divVar']) + 70) + 'px'
    coords = str(xs) + 'px ' + str(ys) + 'px, '
    # 1st line: xs, ys - xs, ye
    x = xs
    y = ys
    br = False
    while (br == False):
        mvFw = intRandom(1,intRandom(1, divDetail))
        mvSide = intRandom(0, (int(formValues['divVar']) * 2)) - int(formValues['divVar'])
        y += mvFw
        x = xs + mvSide
        if y >= ye:
            x = xs
            y = ye
            br = True
        coords += str(x) + 'px ' + str(y) + 'px, '
    # 2nd line: xs, ye - xe, ye
    x = xs
    y = ye
    br = False
    while (br == False):
        mvFw = intRandom(1,intRandom(1, divDetail))
        mvSide = intRandom(0, (int(formValues['divVar']) * 2)) - int(formValues['divVar'])
        x += mvFw
        y = ye + mvSide
        if x >= xe:
            x = xe
            y = ye
            br = True
        coords += str(x) + 'px ' + str(y) + 'px, '
    # 3rd line: xe, ye - xe, ys
    x = xe
    y = ye
    br = False
    while (br == False):
        mvFw = intRandom(1,intRandom(1, divDetail))
        mvSide = intRandom(0, (int(formValues['divVar']) * 2)) - int(formValues['divVar'])
        y -= mvFw
        x = xe + mvSide
        if y <= ys:
            x = xe
            y = ys
            br = True
        coords += str(x) + 'px ' + str(y) + 'px, '
    # 4th line: xe, ys - xs, ys
    x = xe
    y = ys
    br = False
    while (br == False):
        mvFw = intRandom(1,intRandom(1, divDetail))
        mvSide = intRandom(0, (int(formValues['divVar']) * 2)) - int(formValues['divVar'])
        x -= mvFw
        y = ys + mvSide
        if x <= xs:
            x = xs
            y = ys
            br = True
        coords += str(x) + 'px ' + str(y) + 'px, '
    coords += str(x) + 'px ' + str(y) + 'px'
    formValues['clipPath'] = 'polygon(' + str(coords) + ')'
    formValues['shapeOutside'] = 'polygon(' + str(coords) + ')'


def show_code(formValues):    
    htmlcode = "<div id='organicDiv'><div>"
    csscode = "#organicDiv {\n  background-color: " + str(formValues['divCol']) + ";\n  height: " + str(formValues['divHeight']) + "px;\n  width: " + str(formValues['divWidth']) + "px;"
    sasscode = "$backgroundColour: " + str(formValues['divCol']) + ";\n$height: " + str(formValues['divHeight']) + "px;\n$width: " + str(formValues['divWidth']) + "px;"
    jsoncode = '{\n"#organicDiv": {\n  "backgroundColour": "' + str(formValues['divCol']) + '",\n  "height": "' + str(formValues['divHeight']) + '",\n  "width": "' + str(formValues['divWidth']) + '"'
    if formValues['divStyle'] == 'rectJag':
        csscode += "\n  clip-path: polygon;"
    if formValues['divStyle'] == 'rectCurve':
        csscode += "\n  clip-path: path;"
    csscode += "\n}"
    jsoncode += "  \n}\n}"
    code = {
        "html": htmlcode,
        "css": csscode,
        "sass": sasscode,
        "json": jsoncode
    }
    return code