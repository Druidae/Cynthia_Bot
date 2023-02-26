from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database: str # Database name
    db_host: str # Database URL - addres
    db_user: str # Database Username
    db_password: str # Password from database

@dataclass
class TgBot:
    token: str # Token for Telegram Bot access
    admin_ids: list[int] # List with admins IDs 

@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

# Get path to .env files, then create an instance of Config class and return it
def load_config(path: str| None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        )
    )