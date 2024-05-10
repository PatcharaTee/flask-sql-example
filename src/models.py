from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from . import db


class Major(db.Model):
    __tablename__ = "major"

    id = Column(
        Integer,
        index=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String)

    subjects: Mapped[List["Subject"]] = relationship(
        "Subject",
        back_populates="major"
    )
    students: Mapped[List["Student"]] = relationship(
        "Student",
        back_populates="major"
    )


class Subject(db.Model):
    __tablename__ = "subject"

    id = Column(
        Integer,
        index=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String)
    major_id = Column(Integer, ForeignKey(Major.id))

    major: Mapped[Major] = relationship(
        "Major",
        back_populates="subjects"
    )


class Student(db.Model):
    __tablename__ = "student"

    id = Column(
        Integer,
        index=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String)
    age = Column(Integer)
    major_id = Column(Integer, ForeignKey(Major.id))

    major: Mapped[Major] = relationship(
        "Major",
        back_populates="students"
    )


class Class(db.Model):
    __tablename__ = "class"

    id = Column(
        Integer,
        index=True,
        nullable=False,
        primary_key=True
    )
