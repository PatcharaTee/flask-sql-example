from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy import select, update

from ..exceptions import InvalidSubjectID
from ..models import Major, Subject, db

bp = Blueprint("subject", __name__, url_prefix="/subject")


@bp.route("", methods=["GET"])
def subject():
    majors = db.session.execute(select(Major)).scalars().all()
    subjects = db.session.execute(select(Subject)).scalars().all()
    return render_template("subject.html.jinja", majors=majors, subjects=subjects)


@bp.route("", methods=["POST"])
def create_subject():
    name = request.form.get("name", "")
    major_id = request.form.get("major_id", -1, type=int)
    if name is None or name.isspace():
        return "OK", 200

    subject = Subject()
    subject.name = name  # type: ignore
    subject.major_id = major_id  # type: ignore
    db.session.add(subject)
    db.session.commit()

    return redirect(url_for("subject.subject"))


@bp.route("/<sid>", methods=["POST"])
def update_subject(sid: int):
    print(sid)
    subject = db.session.get(Subject, sid)
    if subject is None:
        raise InvalidSubjectID()

    name = request.form.get("name", "")
    professor = request.form.get("professor", "")
    print(name)
    print(professor)

    values = {}
    if not name.isspace():
        values.update(
            {
                "name": name
            }
        )

    if not professor.isspace():
        values.update(
            {
                "professor": professor
            }
        )

    print(values)
    db.session.execute(
        update(Subject).where(
            Subject.id == sid
        ).values(values)
    )
    db.session.commit()

    return redirect(url_for("subject.subject"))


@ bp.route("", methods=["DELETE"])
def delete_subject():
    sid = request.args.get("id", -1, type=int)
    if sid is not None or sid != -1:
        subject = db.session.get(Subject, sid)
        if subject is not None:
            db.session.delete(subject)
            db.session.commit()

    return "OK", 200
