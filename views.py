from flask import render_template, redirect, url_for, request, Blueprint, abort
from jinja2 import TemplateNotFound

# A blueprint is an object that allows defining application functions
# without requiring an application object ahead of time. It uses the
# same decorators as ~flask.Flask, but defers the need for an
# application by recording them for later registration.
# [excerpt from code completion dialog]
# In our case it prevents circular referencing occuring with our Full
# Stack Project (fsp) module structure.
le_views = Blueprint(
    "fsp", __name__, template_folder="templates", static_folder="static"
)


# hardcoded json dictionary until flask file load examples are found.
# FSP require 5 html pages, 8 supplied
favs = {
    # key :          { image,                    html }
    "akira":         ["large_akira.jpg",         "akira.html" ],
    "atlantis":      ["large_atlantis.jpg",      "atlantis.html"],
    "cryingfreeman": ["large_cryingfreeman.jpg", "cryingfreeman.html"],
    "fringe":        ["large_fringe.jpg",        "fringe.html"],
    "princessbride": ["large_princessbride.jpg", "princessbride.html"],
    "reddwarf":      ["large_reddwarf.jpg",      "reddwarf.html"],
    "rogueone":      ["large_rogueone.jpg",      "rogueone.html"],
    "sg1":           ["large_sg1.jpg",           "sg1e.html"]
}

@le_views.route("/")
def landing_page():
    return render_template("index.html")

@le_views.route("/index")
@le_views.route("/default")
@le_views.route("/home")
def basic_redirects():
    return redirect(url_for("fsp.landing_page"))


def get_url(url):
    # try to match parameter url string with a known dictionary key
    try:
        image, html_str = favs[url.lower()]  # assign correct html filename if key matches
    except:
        html_str = "404.html"  # otherwise assign error page
    return html_str

@le_views.route("/<user_url>")  # route string from everything after domain
def render_all(user_url):
    try:
        return render_template(get_url(user_url))
    except TemplateNotFound:
        abort(500,"JSON Favourites: html file does not exist")
