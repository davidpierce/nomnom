import logging
logging.basicConfig(filename='/dev/stdout', level=logging.INFO)
import flask

app = flask.Flask(__name__)

@app.route('/')
def start():
    '''
    Starts the NOMNOM group generation process by obtaining a list
    of event participants from a Google Calendar event.
    '''
    return '''
    <h1>Welcome to NomNom!</h1>
    <form action="/generate" method="get">
    <input type="submit" value="Generate"/>
    </form>
    '''

@app.route('/generate')
def generate():
    '''
    Generates a randomized grouping of the participants.
    '''
    return '''
    <p>This is the page where you will review the groups.</p>
    <form action="/publish" method="get">
    <input type="submit" value="Publish"/>
    </form>
    '''

@app.route('/publish')
def publish():
    '''
    Publishes the participant groups.
    '''
    return 'Thank you for using NOMNOM!'

if __name__ == '__main__':
    app.run()
