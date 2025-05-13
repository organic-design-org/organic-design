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
        'divStyle': 'rectJag',
        'divWidth': 410,
        'divHeight': 410,
        'divDetail': 60,
        'divVar': 16,
        'divCol': '#bbbbbb',
        'divGradCheck': "False",
        'divGradCol':'#bbbbbb',
        'divShadowCheck': "False",
        'divShadowCol': '#bbbbbb',
        'divBorderCheck': "False",
        'divBorderCol': '#bbbbbb'
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
        formValues['orgDivWidth'] = formValues['divWidth'] 
        formValues['orgDivHeight'] = formValues['divHeight']
    return formValues

def rectJag(formValues):
    divDetail = 110 - int(formValues['divDetail'])
    divVariation = int(formValues['divVar'])
    divWidth = int(formValues['divWidth'])
    divHeight = int(formValues['divHeight'])
    padding = 20
    margin = 50
    containerPadding = 70
    xs = divVariation + padding # x coordinate start point
    ys = divVariation + padding # y coordinate start point
    xe = divWidth + xs
    ye = divHeight + ys
    formValues['orgDivHeight'] = divHeight + divVariation + margin
    formValues['orgDivWidth'] = divWidth + divVariation + margin
    formValues['containerHeight'] = divHeight + divVariation + containerPadding
    coords = f'{xs}px {ys}px'
    
    for i in range(4):
        x = xs if i < 2 else xe
        y = ys if i < 1 or i > 2 else ye
        while True:
            mvFw = intRandom(1,intRandom(1, divDetail))
            mvSide = intRandom(0, divVariation * 2) - divVariation
            if i == 0:
                y += mvFw
                x = xs + mvSide
                if y >= ye:
                    x = xs
                    y = ye
                    break
            elif i == 1:
                x += mvFw
                y = ye + mvSide
                if x >= xe:
                    x = xe
                    y = ye
                    break
            elif i == 2:
                y -= mvFw
                x = xe + mvSide
                if y <= ys:
                    x = xe
                    y = ys
                    break
            elif i == 3:    
                x -= mvFw
                y = ys + mvSide
                if x <= xs:
                    x = xs
                    y = ys
                    break
            coords += f", {x}px {y}px"
    formValues['clipPath'] = f'polygon({coords})'
    formValues['shapeOutside'] = f'polygon({coords})'

def show_code(formValues):
    # HTML
    htmlcode = ""
    if formValues['divShadowCheck'] == "True" or formValues['divBorderCheck'] == "True":
        htmlcode += '<div id="organicDivContainer">' 
    htmlcode += "<div id='organicDiv'></div>"
    if formValues['divShadowCheck'] == "True" or formValues['divBorderCheck'] == "True":
        htmlcode += '</div>' 
    # CSS
    csscode = ""
    if formValues['divShadowCheck'] == "True" or formValues['divBorderCheck'] == "True":
        csscode += "#organicDivContainer {\n\tfilter: "
        if formValues['divBorderCheck'] == "True":
            csscode += f"\tdrop-shadow(1px 0px 0px {formValues['divBorderCol']})\n\t\t\t\tdrop-shadow(-1px 0px 0px {formValues['divBorderCol']})\n\t\t\t\tdrop-shadow(0px 1px 0px {formValues['divBorderCol']})\n\t\t\t\tdrop-shadow(0px -1px 0px {formValues['divBorderCol']})\n\t\t\t\tdrop-shadow(1px 1px 0px {formValues['divBorderCol']})\n\t\t\t\tdrop-shadow(-1px -1px 0px {formValues['divBorderCol']})\n\t\t\t\tdrop-shadow(-1px 1px 0px {formValues['divBorderCol']})\n\t\t\t\tdrop-shadow(1px -1px 0px {formValues['divBorderCol']})"
        if formValues['divShadowCheck'] == "True" and formValues['divBorderCheck'] == "True":
            csscode += "\n\t\t\t\t"
        if formValues['divShadowCheck'] == "True":
            csscode += f"drop-shadow(2px 8px 8px {formValues['divShadowCol']})"
        csscode += ";\n}\n"
    csscode += "#organicDiv {\n\t"
    if formValues['divGradCheck'] == "True":
        csscode += f"background-image: linear-gradient(to right, {formValues['divCol']}, {formValues['divGradCol']});"
    else:
        csscode += f"background-color: {formValues['divCol']};"
    csscode += f"\n\theight: {formValues['divHeight']}px;\n\twidth: {formValues['divWidth']}px;"
    if formValues['divStyle'] != 'testing':
        csscode += f"\n\tclip-path: {formValues['clipPath']};"
        csscode += f"\n\tshape-outside: {formValues['shapeOutside']};"
    csscode += "\n}\n\n"
    # SASS
    sasscode = ""
    if formValues['divShadowCheck'] == "True" or formValues['divBorderCheck'] == "True":
        sasscode += "\n$filter: "
        if formValues['divBorderCheck'] == "True":
            sasscode += f"drop-shadow(1px 0px 0px {formValues['divBorderCol']}) drop-shadow(-1px 0px 0px {formValues['divBorderCol']}) drop-shadow(0px 1px 0px {formValues['divBorderCol']}) drop-shadow(0px -1px 0px {formValues['divBorderCol']}) drop-shadow(1px 1px 0px {formValues['divBorderCol']}) drop-shadow(-1px -1px 0px {formValues['divBorderCol']}) drop-shadow(-1px 1px 0px {formValues['divBorderCol']}) drop-shadow(1px -1px 0px {formValues['divBorderCol']})"
        if formValues['divShadowCheck'] == "True":
            sasscode += f"drop-shadow(2px 8px 8px {formValues['divShadowCol']})"
        sasscode += ";"
    if formValues['divGradCheck'] == "True":
        sasscode += f"$background-image: linear-gradient(to right, {formValues['divCol']}, {formValues['divGradCol']});"
    else:
        sasscode += f"$background-color: {formValues['divCol']};"
    sasscode += f"\n$height: {formValues['divHeight']}px;\n$width: {formValues['divWidth']}px;"
    if formValues['divStyle'] != 'testing':
        sasscode += f"\n$clip-path: {formValues['clipPath']};\n$shape-outside: {formValues['shapeOutside']};"
    sasscode += "\n\n"    
    # JSON
    jsoncode = "{"
    if formValues['divShadowCheck'] == "True" or formValues['divBorderCheck'] == "True":
        jsoncode += '\n"#organicDivContainer": {'
        jsoncode += f'\n\t"filter": "'
        if formValues['divBorderCheck'] == "True":
            jsoncode += f"drop-shadow(1px 0px 0px {formValues['divBorderCol']}) drop-shadow(-1px 0px 0px {formValues['divBorderCol']}) drop-shadow(0px 1px 0px {formValues['divBorderCol']}) drop-shadow(0px -1px 0px {formValues['divBorderCol']}) drop-shadow(1px 1px 0px {formValues['divBorderCol']}) drop-shadow(-1px -1px 0px {formValues['divBorderCol']}) drop-shadow(-1px 1px 0px {formValues['divBorderCol']}) drop-shadow(1px -1px 0px {formValues['divBorderCol']}) "
        if formValues['divShadowCheck'] == "True":
            jsoncode += f"drop-shadow(2px 8px 8px {formValues['divShadowCol']})"
        jsoncode += '"\n\t},'    
    jsoncode += '\n"#organicDiv\": {'
    if formValues['divGradCheck'] == "True":
        jsoncode += f'\n\t"background-image": "linear-gradient(to right, {formValues['divCol']}, {formValues['divGradCol']})",'
    else:
        jsoncode += f'\n\t"background-color": "{formValues['divCol']}",'
    jsoncode += f'\n\t"height": "{formValues['divHeight']}px",\n\t"width": "{formValues['divWidth']}px",'
    if formValues['divStyle'] != 'testing':
        jsoncode += f'\n\t"clip-path": "{formValues['clipPath']}",'
        jsoncode += f'\n\t"shape-outside": "{formValues['shapeOutside']}"'
    jsoncode += "\n\t}\n}\n\n"

    code = {
        "html": htmlcode,
        "css": csscode,
        "sass": sasscode,
        "json": jsoncode
    }
    return code