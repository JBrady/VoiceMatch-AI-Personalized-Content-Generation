import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the yaml file to configure the endpoints
app.add_api('api_spec.yaml')

if __name__ == '__main__':
    app.run(port=5000)
