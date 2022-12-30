import os
from api import create_app

app = create_app(os.getenv('CONFIG', 'development'))

if __name__ in '__main__':
    app.run(host="imageapi-production-429b.up.railway.app", port=5000)
