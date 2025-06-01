# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcHAiLCJleHAiOjE3OTk5OTk5OTksInN1YiI6MTY4MzE2NCwiYXVkIjoiV0VCIiwiaWF0IjoxNjk0MDc2ODUxfQ.UhC3lv30vvivEEJek2DCjaRBOxJWPj5Y_lx65QgCf8c'
    # os.getenv("OPENAI_API_KEY")
    return openai_api_key
