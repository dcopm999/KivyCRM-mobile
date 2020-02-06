import json

settings_json = json.dumps([
    {
        'type': 'title',
        'title': 'Connection parameters'
    },
    {
        'type': 'string',
        'title': 'Host name',
        'desc': 'server url',
        'section': 'authorization',
        'key': 'hostname',
    },
    {
        'type': 'numeric',
        'title': 'port',
        'desc': 'server port number',
        'section': 'authorization',
        'key': 'port',
    },
    {
        'type': 'string',
        'desc': 'username for authorization',
        'title': 'Username',
        'section': 'authorization',
        'key': 'username'
    },
    {
        'type': 'string',
        'title': 'Password',
        'desc': 'password for authorization',
        'section': 'authorization',
        'key': 'password'
    }
])