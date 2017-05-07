import asyncio
import models
import stringHelper as sh
import preferences as p
import io
import discord

#The purpose of this file is to hold code pertaining to client interactions
class DogBot:     
    def __init__(self):
        self.client = discord.Client()
        self.clientData = models.ClientData()

    @asyncio.coroutine
    async def makeover(self,name,user):
        self.client.change_nickname(user,name);

    @asyncio.coroutine
    async def applyRules(self,rules,eventData):
        for rule in rules:
            reaction = rule.check(eventData,self)
            if reaction != None:
                await reaction(eventData,self)
                break

    def set_voice_free(self):
        self.clientData.voiceBusy = False

    @asyncio.coroutine
    async def helpMenu(self,message):
        menu = ""
        menu += "Soundboard Commands:\n"
        f = open("data/soundboard.txt",'r')
        for line in f:
            if not line.split(':',1)[0].startswith('#'):
                menu += "!"+line.split(':',1)[0]+"\n"
        await self.client.send_message(message.channel, menu)

    @asyncio.coroutine
    async def play_jams(self,message):
        counter = 0
        async for msg in self.client.logs_from(self.clientData.channels['jamChannel'], limit=200):
            if(counter != 15 and sh.is_a_song(msg.content)):
                await asyncio.sleep(1)
                counter = counter + 1
            await self.client.send_message(clientData.channels['musicChannel'],"!play " + sh.strip_song_message(msg.content))
        await self.client.send_message(message.channel, p.PersonalCollection)
        await self.client.send_message(message.channel, "!queue")

    @asyncio.coroutine
    async def simple_reply(self,message,reply):
        await self.client.send_message(message.channel,reply)
    
    @asyncio.coroutine
    async def play_sound(self,filename):
        await self.silence()
        if(hasattr(self.clientData,'player') and self.clientData.player.is_playing()):
            print("Tried but voice was busy")
            return None    
        if(not self.clientData.voiceConnection):
            await self.connectToVoice("wokeVoiceChannel")
        self.clientData.player = self.clientData.voice.create_ffmpeg_player("data/"+filename)
        self.clientData.player.volume = 0.2
        self.clientData.player.start()

    @asyncio.coroutine
    async def play_stream(self,url):
        await self.silence()
        if(hasattr(self.clientData,'player') and self.clientData.player.is_playing()):
            print("Tried but voice was busy")
            return None
        if(not self.clientData.voiceConnection):
            await self.connectToVoice("wokeVoiceChannel")
        self.clientData.player = self.clientData.voice.create_ffmpeg_player(url)
        self.clientData.player.volume = 0.2
        self.clientData.player.start()
    
    @asyncio.coroutine
    async def silence(self):
        print("silencing..")
        if(hasattr(self.clientData,'player') and self.clientData.player.is_playing()):
            self.clientData.player.stop()

    @asyncio.coroutine
    async def connectToVoice(self,channel):
        self.clientData.voice = await self.client.join_voice_channel(self.clientData.channels[channel])
        self.clientData.voiceConnection = True

    @asyncio.coroutine
    async def onStartup(self):
        print('Logged in as')
        print(self.client.user.name)
        print(self.client.user.id)
        print('------')
        self.clientData.fetch(p.channelIds.dict,self.client);
