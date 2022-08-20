class Config(object):
	API_ID = "" # from my.telegram.org
	API_HASH = "" # from my.telegram.org
	BOT_TOKEN = "" # bot token from https://t.me/BotFather
	OWNER = 864 # Your telegram id
	DATABASE_URL = "postgresql://postgres:password@localhost:5172/db" # Your database URI
	WORKERS = 6
	CUSTOM_PREFIXS = ['/', '$']
	LOG_CHAT = -1001233232 # required for global restrictions
	LOG_STICKER = -1001233232 # required for kang sticker
	USE_OCR = False # you need to install tesseract on your server to enable ocr
