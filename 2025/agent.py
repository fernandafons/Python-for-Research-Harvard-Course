from flask import Flask, request, render_template_string
from openai import OpenAI
import markdown
import nh3
from markupsafe import Markup

app = Flask(__name__)
# Reads OPENAI_API_KEY from the environment (do not hardcode keys in this file)
client = OpenAI()

def render_markdown(text: str) -> Markup:
    """Convert the model's Markdown to HTML, then sanitize before rendering."""
    html = markdown.markdown(text, extensions=["fenced_code", "tables"])
    return Markup(nh3.clean(html))  # strips <script>, event handlers, etc.

# HTML template for the interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GPT-4 Chat Interface</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>My Personal GPT-4 Agent</h1>
    <form method="POST">
        <label for="user_input">Your message:</label>
        <br>
        <div>
            <input type="text" id="user_input" name="user_input" size="50">
            <input type="submit" value="Submit">
        </div>
    </form>
    {% if response %}
        <h2>Response:</h2>
        <div class="response">{{ response }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            result = client.responses.create(
                model="gpt-4o",
                tools=[{"type": "web_search_preview"}],
                input=user_input
            )
            response = render_markdown(result.output_text)
        except Exception as e:
            response = "Something went wrong, please try again."
            app.logger.exception(e)
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)