import asyncio
import urllib.request
import urllib.parse

#This class holds client objects so we don't have to refetch them
class ClientData:
    def __init__(self):
        self.channels = {}
        self.emojis = {}
        self.voiceBusy = False
        self.voiceConnection = False
    def fetch(self,channels,client):
        for server in client.servers:
            for emoji in server.emojis:
                self.emojis[emoji.name] = emoji.url
        for k,v in channels.items():
            self.channels[k] = client.get_channel(v)

#This class represents a relationship between a detected word and a response
class WordR:
    def __init__(self, bool, reaction):
        self.bool = bool;
        self.react = reaction;
    def check(self,message,dog):
        if self.bool(message,dog):
            return self.react
    
