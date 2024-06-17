import requests
import sys
import json
import os

AUTH_TOKEN_API = os.getenv('AUTH_TOKEN_API')
AUTH_TOKEN_AUDIO = os.getenv('AUTH_TOKEN_AUDIO')

audio_manager_url = 'https://caas.randylabs.cloud/v1/audio'
api_url = 'https://caas.randylabs.cloud/v1/conversation'

def helper():
    print('COMMANDS')
    print('')
    print('Upload a new conversation and start the processing:')
    print('python3 ingest.py -a [AUDIO_FILE_PATH] -c [CONVERSATION_CONFIG_FILE_PATH]')
    print('')
    print('Process a previously uploaded file')
    print('python3 ingest.py -c [CONVERSATION_CONFIG_FILE_PATH]')
    print('')
    print('Check the processing status of a conversation')
    print('python3 ingest.py -s [CONVERSATION ID]')
    print('')
    print('Get the general information of a conversation')
    print('python3 ingest.py -i [CONVERSATION ID]')
    print('')
    print('Get the timeline of a conversation')
    print('python3 ingest.py -t [CONVERSATION ID]')

def upload_file(file_path):
    res = 0
    try:
        with open(file_path, 'rb') as audio_file:
            response = requests.post(url = audio_manager_url, files={'file': audio_file}, headers={'X-Auth-Token': AUTH_TOKEN_AUDIO})
            res = response.status_code
            if response.status_code == 200:
                print('File uploaded with success!')
            else:
                print('Something went wrong when uploading the file.')
    except Exception as e:
        print('Something went wrong when uploading the file.')
        print(e)

        return 0

    return res

def get_info(conv_id: str):
    try:
        response = requests.get(url = f"{api_url}/{conv_id}", headers={'X-Auth-Token': AUTH_TOKEN_API})
        print(response.json())

    except Exception as e:
        print("Failed to fetch status")

def get_status(conv_id: str):
    try:
        response = requests.get(url = f"{api_url}/{conv_id}/status", headers={'X-Auth-Token': AUTH_TOKEN_API})
        print(response.json())

    except Exception as e:
        print("Failed to fetch status")

def get_timeline(conv_id: str):
    try:
        response = requests.get(url = f"{api_url}/{conv_id}/timeline", headers={'X-Auth-Token': AUTH_TOKEN_API})
        print(response.json())

    except Exception as e:
        print("Failed to fetch status")

def process_call(config_path):
    try:
        with open(config_path) as config:
            config_file = json.load(config)
        response = requests.post(url = api_url, json = config_file, headers={'X-Auth-Token': AUTH_TOKEN_API})

        if response.status_code == 200:
            print('Processing the conversation. You can now find the conversation in the UI.')
            print('Conversation id: ' + response.json()['conversation_id'])
        else:
            print('Call processing went wrong, please check the configuration file and try again.')
    except Exception as e:
        print(f"Something went wrong, please check the configuration file and try again.")

def main():
    if len(sys.argv) == 5:
        if sys.argv[1] == '-a' and sys.argv[3] == '-c':
            res = upload_file(sys.argv[2])
            if res == 200:
                process_call(sys.argv[4])
        else:
            print('Incorrect arguments.')
            helper()
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-c':
            process_call(sys.argv[2])

        elif sys.argv[1] == '-i':
            get_info(sys.argv[2])

        elif sys.argv[1] == '-s':
            get_status(sys.argv[2])

        elif sys.argv[1] == '-t':
            get_timeline(sys.argv[2])
        else:
            print('Incorrect arguments.')
            helper()
    elif len(sys.argv) == 2 and sys.argv[1] == '-h':
        helper()
    else:
        print('Incorrect arguments.')
        helper()

if __name__ == "__main__":
    main()
