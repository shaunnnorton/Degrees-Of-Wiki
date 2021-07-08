from src.utils.utils import get_degree
from flask import (Blueprint, request, render_template, redirect,
                   url_for, flash)
from src.models import Matches


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def MainPage():
    """The main page for viewing"""
    recent = Matches.query.all()
    recent = recent[:-1]
    data = {
        "recent": recent
    }
    return render_template("home.html", **data)


@main.route("/degree", methods=["POST"])
def GetDegree():
    """Return the degree of the match in Flashed Message"""
    status, match = get_degree(request.form["term1"], request.form["term2"])
    if status:
        flash(f"The articles for {match.url1.name} and {match.url2.name}\n" +
              f"are seperated by {match.degrees} degrees\n" + "YAAAAY!")
        return redirect(url_for("main.MainPage"))
    flash(f"The articles for {match.url1.name} and {match.url2.name}\n" +
          f"are seperated by more than {match.degrees} degrees\n" + ":(")
    return redirect(url_for("main.MainPage"))
