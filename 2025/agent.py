from flask import Flask, request, render_template_string
from openai import OpenAI

app = Flask(__name__)
# Reads OPENAI_API_KEY from the environment (do not hardcode keys in this file)
client = OpenAI()

# HTML template for the interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GPT-4 Chat Interface</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div>
    <h1>My Personal GPT-4 Agent</h1>
    </div>
    <form method="POST">
        <label for="user_input">Your message:</label>
        <br>
        <div>
            <input type="text" id="user_input" name="user_input" size="50">
            <input type="submit" value="Submit">
        </div>
        {% if response %}
            <h2>Response:</h2>
            <p>{{ response }}</p>
        {% endif %}
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = client.responses.create(
            model="gpt-4o",
            tools=[{"type": "web_search_preview"}],
            input=user_input
        )
        response = result.output_text
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
