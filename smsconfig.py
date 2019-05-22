#!/usr/local/bin/python
import nexmo

client = nexmo.Client(key='key', secret='secret')

client.send_message({
    'from': 'Surveilance Robot',
    'to': 'number',
    'text': 'Intruder Alert!',
})

