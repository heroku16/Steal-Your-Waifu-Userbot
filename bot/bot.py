from os import path, environ
from configparser import ConfigParser
from pyrogram import Client

API_ID = environ.get('API_ID', None)
API_HASH = environ.get('API_HASH', None)
USERBOT_SESSION = environ.get('USERBOT_SESSION', None)

class bot(Client):
    def __init__(self, name):
        config_file = f"{name}.ini"
        config = ConfigParser()
        config.read(config_file)
        name = name.lower()
        plugins = {'root': path.join(__package__, 'plugins')}
        api_id = API_ID or config.get('pyrogram', 'api_id')
        api_hash = API_HASH or config.get('pyrogram', 'api_hash')
        super().__init__(
            USERBOT_SESSION if USERBOT_SESSION is not None else name,
            api_id=api_id,
            api_hash=api_hash,
            config_file=config_file,
            workers=16,
            plugins=plugins,
            workdir="./",
        )
    async def start(self):
        await super().start()
        print("bot started. Hi.")
    async def stop(self, *args):
        await super().stop()
        print("bot stopped. Bye.")
