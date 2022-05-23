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

thumbs = {
    "akira": "thumb_akira.jpg",
    "atlantis": "thumb_atlantis.jpg",
    "cryingfreeman": "thumb_cryingfreeman.jpg",
    "fringe": "thumb_fringe.jpg",
    "princessbride": "thumb_princessbride.jpg",
    "reddwarf": "thumb_reddwarf.jpg",
    "rogueone": "thumb_rogueone.jpg",
    "sg1": "thumb_sg1.jpg",
}

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
    # define dictionary of accepted formats for known routes
    # (refactor if time premits to a 'dictionary of lists'
    #  reduce repplicated strings )
    dict = {
        'akira':             'akira.html',
        'atlantis':          'atlantis.html',
        'stargateatlantis':  'atlantis.html',
        'stargate_atlantis': 'atlantis.html',
        'stargate atlantis': 'atlantis.html',
        'cryingfreeman':     'cryingfreeman.html',
        'crying_freeman':    'cryingfreeman.html',
        'crying freeman':    'cryingfreeman.html',
        'fringe':            'fringe.html',
        'princessbride':     'princessbride.html',
        'princess_bride':     'princessbride.html',
        'princess bride':     'princessbride.html',
        'reddwarf':          'reddwarf.html',
        'red_dwarf':         'reddwarf.html',
        'red dwarf':         'reddwarf.html',
        'rogueone':          'rogueone.html',
        'rogue_one':         'rogueone.html',
        'rogue one':         'rogueone.html',
        'rogue1':            'rogueone.html',
        'rogue_1':           'rogueone.html',
        'rogue 1':           'rogueone.html',
        'stargate':          'stargate.html'
        }

    # try to match parameter url string with a known dictionary key
    try:
        html_str = dict[url.lower()]  # assign correct html filename if key matches
    except:
        html_str = '404.html'  # otherwise assign error page
    return html_str

@le_views.route("/<user_url>") # route string from everything after domain
def render_all(user_url):
    return render_template(get_url(user_url))
