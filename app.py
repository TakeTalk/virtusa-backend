import uvicorn

from config import *
from controller.SuggestionController import *
from controller.UserController import *

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
