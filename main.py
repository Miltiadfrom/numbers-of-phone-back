from app.routes import app
from app.helpers import start

if __name__ == '__main__':
    start()
    app.run(port="8000")
