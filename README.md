# caas-ingest-cli

To install the ingestion tool run the following command:

```
bash setup.sh
```

Then, you need to create the ".env" file with the following structure:
```
export AUTH_TOKEN_API=''
export AUTH_TOKEN_AUDIO=''
```
Note that you should replace the empty lines with the correct api keys.

Then you need to source both the virtual environment and the ".env" file: 

```
source .venv/bin/activate
source .env
```

To upload a new audio file and process the conversation run the following
command:

```
python3 ingest.py -a [AUDIO_PATH] -c [CONVERSATION_CONFIG_JSON]
```

To process a conversation whose audio file was already upload run the command
below:

```
python3 ingest.py -c [CONVERSATION_CONFIG_JSON]
```

The [CONVERSATION\_CONFIG\_JSON] above needs to follow the same structure as 
the "exampleAudio.json" file. When you upload an audio file the file name will
be saved with the same name as the "external\_id" parameter. So, the "path" 
of the audio file inside "exampleAudio.json" needs to be updated accordingly.
