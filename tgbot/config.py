from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    port: int
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_id=env.int("ADMIN_ID")
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            port=env.int('DB_PORT'),
            password=env.str('DB_PASSWORD'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        )
    )
