from flask import Flask

from views import Top4Winners, Q2,Q3, Q4,Q5,Q6
from utils.utils_response import Response

app = Flask(__name__)

# No blueprint for now :D , Will do it when we have muttiple module to define the url
app.add_url_rule(f'/api/{Top4Winners.URL}/', view_func=Top4Winners.as_view('top_4_winners'))
app.add_url_rule(f'/api/{Q2.URL}/', view_func=Q2.as_view('q2'))
app.add_url_rule(f'/api/{Q3.URL}/', view_func=Q2.as_view('q3'))
app.add_url_rule(f'/api/{Q4.URL}/', view_func=Q2.as_view('q4'))
app.add_url_rule(f'/api/{Q5.URL}/', view_func=Q2.as_view('q5'))
app.add_url_rule(f'/api/{Q6.URL}/', view_func=Q2.as_view('q6'))


# In view i have many class, as above you can add all url for each view and expose this end URL's
# (y) ?

@app.errorhandler(404)
def page_not_found(e):
    return Response.get({}, _type='URL NOT FOUND', message='use /api/q2/', status_code=404)


@app.errorhandler(Exception)
def error_found(error):
    return Response.get({}, _type='INTERNAL SERVER ERROR', message='Unknown Exception', status_code=500)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
