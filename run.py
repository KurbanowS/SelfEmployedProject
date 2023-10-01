from main import create_app, db
from main.developers.models import Developers, Banners
from main.designers.models import Designers
from main.admin.models import Me


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return{'db' : db, 'Me' : Me, 'Developers' : Developers, 'Designers' : Designers, 'Banners' : Banners}
















