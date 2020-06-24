import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("KEY")
print('Key is : {}'.format(key))