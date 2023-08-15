from flask import Flask, request, render_template
from stories import *

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    inputs = story.prompts

    return render_template("home.html", inputs=inputs)

@app.route('/story')
def add_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)