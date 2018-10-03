from app.api import my_app
from app.api import User, Auth


app_instance = my_app()
app_instance.api.add_resource(User, '/api/user',
                                    '/api/user/<string:name>', endpoint='user')
app_instance.api.add_resource(Auth, '/api/auth')

if __name__ == '__main__':
    app_instance.app.run(debug=True, host='127.0.0.1', port=5000)
