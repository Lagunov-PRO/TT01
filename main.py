from app import app as application

if __name__ == '__main__':
    # application.run(port=9876, debug=True)
    application.run(port=application.config['PORT'])
