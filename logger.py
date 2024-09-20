import logging   #Bot Created by @NtrRazYt
from logging.handlers import RotatingFileHandler   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
logging.basicConfig(   #Bot Created by @NtrRazYt
    level=logging.ERROR,   #Bot Created by @NtrRazYt
    format=   #Bot Created by @NtrRazYt
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",   #Bot Created by @NtrRazYt
    datefmt="%d-%b-%y %H:%M:%S",   #Bot Created by @NtrRazYt
    handlers=[   #Bot Created by @NtrRazYt
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),   #Bot Created by @NtrRazYt
        logging.StreamHandler(),   #Bot Created by @NtrRazYt
    ],   #Bot Created by @NtrRazYt
)   #Bot Created by @NtrRazYt
logging.getLogger("pyrogram").setLevel(logging.WARNING)   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
logging = logging.getLogger()   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
