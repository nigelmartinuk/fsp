from flask import Flask, Blueprint, redirect
from views import le_views # get views from view.py without circular referencing

#create the app
app = Flask( __name__ )
# dynamically register the website views using externally created 
# blueprint object
app.register_blueprint( le_views)  

#if app creation was successful, start the website
if __name__ == "__main__" :
    app.run(debug=True, port=8000)
