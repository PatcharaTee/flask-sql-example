from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy import select

from ..models import Major, db

bp = Blueprint("major", __name__, url_prefix="/major")


@bp.route("", methods=["GET"])
def major():
    majors = db.session.execute(select(Major)).scalars().all()
    return render_template("major.html.jinja", majors=majors)


@bp.route("", methods=["POST"])
def create_major():
    name = request.form.get("name", "")
    if name is None or name.isspace():
        return "OK", 200

    major = Major()
    major.name = name  # type: ignore
    db.session.add(major)
    db.session.commit()

    return redirect(url_for("major.major"))


@bp.route("", methods=["DELETE"])
def delete_major():
    mid = request.args.get("id", -1, type=int)
    if mid is not None or mid == -1:
        major = db.session.get(Major, mid)
        if major is not None:
            db.session.delete(major)
            db.session.commit()

    return "OK", 200
