
from flask import Flask

#ccria o app
app = Flask(__name__)


from fakepinterest import routes
#importa das rotas depois que o app é criado acima