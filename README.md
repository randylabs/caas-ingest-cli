# caas-ingest-cli

To install the ingestion tool run the following command:

```
bash setup.sh
```

Afterwards you can run the following command to show you the helper:
```
python3 ingest.py
```

You can change the 'config.json' file to process other calls. 
Inside the json file change the filename inside the "audio\_file" section.

Example:
"path": "audio\_calls/english\_Call1\_Stereo\_audio\_2.wav"
"path": "audio\_calls/arabic\_call\_1.wav"

Note that the "audio\_calls" should be mantained.

The other parts of the metadata of the file can be altered.

## Env file:
```
AUTH_TOKEN_API=''
AUTH_TOKEN_AUDIO=''
```
