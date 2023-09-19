from main import app, db
from main.models import Me


@app.shell_context_processor
def make_shell_context():
    return{'db' : db, 'Me' : Me}
















