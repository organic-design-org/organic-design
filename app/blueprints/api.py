from flask import Blueprint, request, jsonify
from app import functions

api = Blueprint('api', __name__)

@api.route('/api/div/<string:style>/<int:width>/<int:height>')
def generate_div(style, width, height):
    # Build formValues dict using URL + query params
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

    # Dispatch to the matching style function
    if style in functions.style_map:
        functions.style_map[style](formValues)
        output = functions.show_code(formValues)
        return jsonify(output)
    else:
        return jsonify({"error": "Style not found"}), 404
