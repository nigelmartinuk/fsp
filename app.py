from flask import Flask, Blueprint, redirect, render_template, url_for, request
from views import le_views # get views from view.py without circular referencing


#create the app
app = Flask( __name__ )

# register a 404 error handler for the website
@app.errorhandler( 404)
def page_not_found(err):
#    return 'This page does not exist', 404
#    return redirect(url_for("fsp.landing_page"))
#    return redirect(url_for("fsp.opportunity_detail"))
#    app.logger.error( f"Yuk: {err}\nYuk_route: {request.full_path.upper()}")
    return render_template("404.html",e=err)# register a 404 error handler for the website

@app.errorhandler( 500)
def page_not_found(err):
#    return 'This page does not exist', 404
    return render_template("500.html",e=err)

# dynamically register the website views using externally created 
# blueprint object
app.register_blueprint( le_views)  

#if app creation was successful, start the website
if __name__ == "__main__" :
    app.run(debug=True, port=8000)
