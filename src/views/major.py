from flask import Blueprint, render_template, request

from ..models import Major, db

bp = Blueprint("major", __name__, url_prefix="/major")


@bp.route("", methods=["GET"])
def major():
    return render_template("major.html.jinja")


@bp.route("", methods=["POST"])
def create_major():
    json_body = request.get_json()

    try:
        name = json_body.get("name")
    except Exception:
        return "OK",  404

    major = Major()
    major.name = name
    db.session.add(major)
    db.session.commit()

    return "OK"
