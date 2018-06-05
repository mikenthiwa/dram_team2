# manage.py

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import db, create_app
from app import models

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app=app, db=db)
manager = Manager(app=app)


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
