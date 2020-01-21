from flask import Flask

from views import Top4Winners, Q2
app = Flask(__name__)

# No blieprint for now :D , Will do it when we have muttiple module to define the url
app.add_url_rule(f'/api/{Top4Winners.URL}/', view_func=Top4Winners.as_view('top_4_winners'))
app.add_url_rule(f'/api/{Q2.URL}/', view_func=Q2.as_view('q2'))


if __name__ == '__main__':
    app.run()