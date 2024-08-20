from config.__init__ import *

@app.route('/')
def index():
    return "render_template('index.html')"