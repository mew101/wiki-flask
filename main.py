from flask import Flask, render_template, request, jsonify
import wikipedia
from wikipedia import exceptions

app = Flask(__name__, subdomain_matching=True)

@app.route('/', subdomain="<var>", methods=['GET'])
def home(var):
    
    links = []

    ## returns searchbox
    # if request.method == "GET":
    #     return render_template("index.html")
    # else:
    #     search = request.form["search_term"]
   
    ## for searchbox switch to var

    ## wikipedia data
    
    try:
        return jsonify(links =  wikipedia.page(var).url) 
    except wikipedia.exceptions.DisambiguationError as e:
        results =  e.options
        
        for r in results:
            try:
                links.append(wikipedia.page(r, "a").url)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
       
    return jsonify(links=links)

if __name__ == '__main__':
    website_url = 'wiki-search.com:5000'
    app.config['SERVER_NAME'] = website_url
    app.run()



