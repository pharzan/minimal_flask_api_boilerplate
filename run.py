from app.api import my_app
from app.api import User


app_instance = my_app()

# app_instance.api.add_resource(User, '/api/user', defaults={'name': ''})
# app_instance.api.add_resource(User, '/api/user/<string:name>')
app_instance.api.add_resource(User, '/api/user',
                 '/api/user/<string:name>', 
                 endpoint='user')

if __name__ == '__main__':
    app_instance.app.run(debug=True, host='127.0.0.1', port=5000)
