import uvicorn

from config import *
from controller.SuggestionController import *
from controller.UserController import *
from controller.TokenizeController import *
from controller.replyController import *
from controller.ChatController import *


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
