import sys

from dataclasses import dataclass
from environs import Env
from io import TextIOWrapper


@dataclass
class TgBot:
    token: str


@dataclass
class LogSettings:
    level: str
    format: str
    stream: TextIOWrapper | None


@dataclass
class Config:
    bot: TgBot
    log: LogSettings


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        bot=TgBot(token=env('BOT_TOKEN')),
        log=LogSettings(
            level=env('LOG_LEVEL'),
            format=env('LOG_FORMAT'),
            stream=sys.stdout
        )
    )
