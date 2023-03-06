from instance.config import DevelopmentConfig
from project.server import create_app
import create_tables
import load_fixtures

app = create_app(DevelopmentConfig)


if __name__ == "__main__":
    create_tables
    load_fixtures
    app.run()
