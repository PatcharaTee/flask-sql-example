from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy import select

from ..models import Subject, db

bp = Blueprint("student", __name__, url_prefix="/student")


@bp.route("", methods=["GET"])
def student():
    students = db.session.execute(
        select(Subject)
    ).scalars().all()
    return render_template(
        "student.html.jinja",
        students=students
    )
