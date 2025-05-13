import random

from flask import Blueprint, request, jsonify, render_template, redirect
from app import functions

api = Blueprint('api', __name__)

@api.route('/api')
@api.route('/api/div')
@api.route('/api/div/rectJag')
def api_redirect():
    return redirect("/api/div/rectJag/200/200")

@api.route('/api/div/<string:style>/<int:width>/<int:height>')
def generate_div(style, width, height):
    formValues = {
        "divStyle": style,
        "divWidth": width,
        "divHeight": height,
        "divVar": request.args.get("variation", 16, type=int),
        "divDetail": request.args.get("detail", 60, type=int),
        "divCol": request.args.get("color", "#bbbbbb"),
        "divShadowCol": request.args.get("shadow", "#666666"),
        "divBorderCol": request.args.get("border", "#444444")
    }

    if style in functions.style_map:
        functions.style_map[style](formValues)
        output = functions.show_code(formValues)
        return jsonify(output)
    else:
        return jsonify({"error": "Style not found"}), 404

@api.route('/demo')
def live_demo_server_rendered():
    style = "rectJag"
    # width = functions.intRandom(120, 250)
    # height = functions.intRandom(120, 250)
    width = 200
    height = 200
    detail = functions.intRandom(20, 100)
    variation = functions.intRandom(2, 30)

    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    formValues = {
        "divStyle": style,
        "divWidth": width,
        "divHeight": height,
        "divVar": variation,
        "divDetail": detail,
        "divCol": color,
        "divGradCheck": "False",
        "divGradCol": color,
        "divShadowCheck": "False",
        "divShadowCol": "#444444",
        "divBorderCheck": "False",
        "divBorderCol": "#222222"
    }

    # Generate style
    functions.style_map[style](formValues)
    code = functions.show_code(formValues)

    return render_template("pages/demo.html", title="Live API Demonstration", code=code, form=formValues)