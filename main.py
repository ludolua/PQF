from flask import Flask, render_template, request
import sqlparse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    formatted_query = ""
    selected_style = "style_1"  # Default style

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        selected_style = request.form.get('style', 'style_1')

        if query:
            formatted_query = format_sql(query, selected_style)

    return render_template('index.html', formatted_query=formatted_query, selected_style=selected_style)

def format_sql(query, style):
    if style == 'style_1':
        return format_style_1(query)
    elif style == 'style_2':
        return format_style_2(query)
    elif style == 'style_3':
        return format_style_3(query)
    else:
        return query

def format_style_1(query):
    formatted = sqlparse.format(query, reindent=True, keyword_case='upper')
    formatted = formatted.replace('SELECT', 'SELECT\n    ').replace('FROM', '\nFROM').replace('WHERE', '\nWHERE').replace('AND', '\n    AND')
    return formatted

def format_style_2(query):
    formatted = sqlparse.format(query, reindent=True, keyword_case='upper')
    formatted = formatted.replace('SELECT ', 'SELECT\n    ').replace('FROM ', '\nFROM ').replace('WHERE ', '\nWHERE ').replace('AND ', '\n    AND ').replace('ORDER BY ', '\nORDER BY ').replace('LIMIT ', '\nLIMIT ')
    return formatted

def format_style_3(query):
    formatted = sqlparse.format(query, reindent=True, keyword_case='upper')
    formatted = formatted.replace('SELECT ', 'SELECT\n    ').replace('FROM ', '\nFROM ').replace('WHERE ', '\nWHERE ').replace('AND ', '\n    AND ').replace('OR ', '\n    OR ').replace('ORDER BY ', '\nORDER BY ').replace('LIMIT ', '\nLIMIT ')
    return formatted

if __name__ == "__main__":
    app.run(debug=True)
