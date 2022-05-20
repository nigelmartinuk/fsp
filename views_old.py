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
    # abort(500)
    return render_template('index.html')

# these three routes point to the index.html page
@le_views.route("/index")
@le_views.route("/default")
@le_views.route("/home")
def basic_redirects():
    return redirect(url_for("fsp.landing_page"))

# A marketing opportunity is a sales-accepted lead that has been
# qualified as being in need of a product. The sales representative
# determines that there is an opportunity to sell to this individual
# or company.
@le_views.route("/opp")
@le_views.route("/opportunity")
def opportunity_detail():
    return render_template('opportunity.html')

# If consoles (control desks) are required they are selected, designed,
# customised detailed here.
@le_views.route("/desk")
@le_views.route("/desk_selection")
def desk_selection():
    return render_template('desk_selection.html')

# If io boxes are required they are detailed here.
@le_views.route("/io")
@le_views.route("/io_selection")
def io_selection():
    return render_template('io_selection.html')

# If spare parts are required they are detailed here.
@le_views.route("/spares")
@le_views.route("/spares_selection")
def spares_selection():
    return render_template('spares_selection.html')

# The quotation is built here. Functionality for optional extras and
# document customisation is a first tier requirement.
@le_views.route("/quote")
@le_views.route("/quote_document")
def quote_document():
    return render_template('quote_document.html')

# Order detail is a oneway dump of the SKU parts list required to
# fulfil the quotation. This dump is meant for import into a MRP or ERP
# system. Quote customisations are documented in a separate file.
@le_views.route("/order")
@le_views.route("/order_detail")
def order_detail():
    return render_template('order_detail.html')
