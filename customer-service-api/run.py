from api import application
from api.utils.scripts import create_databases, create_tables

create_databases()
create_tables()

app = application()

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=False)