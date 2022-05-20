from flask import render_template, redirect, url_for, request, Blueprint, abort

# A blueprint is an object that allows defining application functions
# without requiring an application object ahead of time. It uses the
# same decorators as ~flask.Flask, but defers the need for an
# application by recording them for later registration.
# [excerpt from code completion dialog]
# In our case it prevents circular referencing occuring with our Full
# Stack Project (fsp) module structure.
le_views = Blueprint('fsp', __name__,
                     template_folder='templates',
                     static_folder='static')

# default route points to the opportunity detail page


@le_views.route("/")
def landing_page():
    return render_template('index.html')

# these three routes point to the index.html page

@le_views.route("/index")
@le_views.route("/default")
@le_views.route("/home")
def basic_redirects():
    return redirect(url_for("fsp.landing_page"))

def get_url(url):
    dict = {
        'opp':              'opportunity.html',
        'opportunity':      'opportunity.html',
        'desk':             'desk_selection.html',
        'desk_selection':   'desk_selection.html',
        'io':               'io_selection.html',
        'io_selection':     'io_selection.html',
        'spares':           'spares_selection.html',
        'spares_selection': 'spares_selection.html',
        'quote':            'quote_document.html',
        'quote_document':   'quote_document.html',
        'order':            'order_detail.html',
        'order_detail':     'order_detail.html'}

    try:
        html_str = dict[url.lower()]  # assign html filename if key matches
    except:
        html_str = '404.html'  # otherwise assign error page

    return html_str

@le_views.route("/<user_url>")
def render_all(user_url):
    return render_template(get_url(user_url))
