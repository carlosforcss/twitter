import environ

env = environ.Env(
    DB_PORT=(int, 5432),
    DB_USERNAME=(str, "postgres"),
    DB_PASSWORD=(str, "postgres"),
    DB_HOST=(str, "db"),
)
environ.Env.read_env()

# DB Configuration
DB_NAME = env.get("DB_NAME")
DB_USERNAME = env.get("DB_USERNAME")
DB_PASSWORD = env.get("DB_PASSWORD")
DB_HOST = env.get("DB_HOST")
DB_PORT = env.get("DB_PORT")
