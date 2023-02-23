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

# Create Env() class copy
env: Env = Env()

# Add variables from .env file to environment
env.read_env()

# Create Config class copy and add it's data from environment variable
config = Config(
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

# Print values for Config instance fields to verify accuracy of information
print('BOT_TOKEN: ', config.tg_bot.token)
print('ADMIN_IDS: ', config.tg_bot.admin_ids)
print()
print('DATABASE: ', config.db.database)
print('DB_HOST: ', config.db.db_host)
print('DB_USER: ', config.db.db_user)
print('DB_PASSWORD: ', config.db.db_password)
