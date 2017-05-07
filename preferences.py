from models import WordR
import stringHelper
import asyncio
import dogBot

#The purpose of this file is to have a configurable list of variables which dictate the bots function

def sb(command,filename):
    return WordR((lambda m,d: (m.content == ("!"+command))),(lambda m,d: d.play_sound(filename)))

def en(command,filename):
    return WordR((lambda m,d: (m.id + "_en" == command)),
    (lambda m,d: d.play_sound(filename)))

def ex(command,filename):
    return WordR((lambda m,d: (m.id + "_ex" == command)),
        (lambda m,d: d.play_sound(filename)))

def sa(command,url):
    return WordR((lambda m,d: (m.content == ("!stream "+command))),(lambda m,d: d.play_stream(url)))

def cr(contains,reply):
    return WordR((lambda m,d: (contains in m.content and m.author.id != config.botId) ),(lambda m,d: d.simple_reply(m,reply)))

def generateWordR(filename,func,endCode):
    returnList = []
    f = open(filename,'r')
    for line in f:
        temp = line.split(':',1)
        if not temp[0].startswith("#") and temp[0].endswith(endCode):
            returnList.append(func(temp[0],temp[1][:-1])) #cut off the newline
    f.close()
    return returnList 

class stringBank:
    PersonalCollection = "I queued some stuff up from my personal collection, you're going to love these hot tracks"
    songMatchTokens = ["www.youtube.com/watch?","youtu.be/",".bandcamp.com","www.soundcloud.com"]

class config:
    songLimit = 10
    #This is an array of boolean function void function pairs (b,f)  with "Message satisfies b, do f"
    #All response functions must be defined in clientInteractions.py as an asyncio coroutine
    #Remember: These are ordered. Once one is found the rest are skipped over!
    responses = [WordR((lambda m,d: (m.content == "!help")),lambda m,d: d.helpMenu(m)),
                 WordR((lambda m,d: (m.content == "!silence")),lambda m,d: d.silence()),
                 WordR(lambda m,d: m.content.startswith("!playJams"),lambda m,d: dog.play_jams)] 
    responses += generateWordR('data/soundboard.txt',sb,"")
    responses +=  generateWordR('data/streams.txt',sa,"")
    responses += generateWordR('data/common_reply.txt',cr,"")
    #These are sounds that are only played when someone enters/exits the voice channel
    entrances = generateWordR("data/entrances.txt",en,"en")
    exits = generateWordR("data/exits.txt",ex,"ex")
    f = open("data/botSettings.txt",'r')
    botName = f.readline()
    botId = f.readline()
    botToken = f.readline()

class channelIds:
    dict = {"jamChannel":"189413429499527168",
    "musicChannel":"288147211978801152",
    "favoriteChannel":"277542845999611904",
    "talkDog":"288749058707816449",
    "wokeVoiceChannel":"276512387203596288"}

