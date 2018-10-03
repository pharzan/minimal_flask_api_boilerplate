from app.api import create_app
from app.api import User


app,api = create_app()

api.add_resource(User, '/api/user/<string:name>')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
