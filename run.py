import discord
import asyncio
import datetime
import models
import preferences
import stringHelper
import dogBot

#As much as possible, we want this file to only catch events
dog = dogBot.DogBot();
@dog.client.event
async def on_ready():
    await dog.onStartup()

@dog.client.event
async def on_message(message):
    await dog.applyRules(preferences.config.responses,message)

@dog.client.event
async def on_voice_state_update(beforeMember,afterMember):
    if(beforeMember.voice.voice_channel == None and  
        afterMember.voice.voice_channel != None): #An entrance to the voice channel
        await dog.applyRules(preferences.config.entrances,afterMember)
    elif(beforeMember.voice.voice_channel != None and
        afterMember.voice.voice_channel == None): #An exit from the voice channel
        await dog.applyRules(preferences.config.exits,afterMember)
    elif((not beforeMember.voice.mute) and afterMember.voice.mute):
        await dog.play_sound("shutUp.mp3")
    

dog.client.run('thanks chaten')
