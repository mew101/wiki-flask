from flask import Flask, render_template, request, jsonify
import wikipedia
from wikipedia import exceptions

app = Flask(__name__, subdomain_matching=True)
app.config["SERVER_NAME"] = 'wiki-search.com:5000'

@app.route('/', subdomain="<dogs>")
def home(dogs):
    
    links = []

    ## returns searchbox
    # if request.method == "GET":
    #     return render_template("index.html")
    # else:
    #     search = request.form["search_term"]

    ## wikipedia data
    try:
        return jsonify(links =  wikipedia.page(dogs).url)
    except wikipedia.exceptions.DisambiguationError as e:
        results =  e.options
        
        for r in results:
            try:
                links.append(wikipedia.page(r, "a").url)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
       
    return jsonify(links=links)

if __name__ == '__main__':
    app.run(debug=True)



