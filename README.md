# discordBot
Python Discord bot, using the Rapptz discord api wrapper

A discord bot with a focus on being flexible, with multiple levels of function templates. 

The highest level template is a (condition bool function,reaction void function) pair. These are then grouped into named lists which correspond to events, and on that event occuring we use the condition function to determine if we should run the reaction function.

The next level down is a function which generates that pair of functions for common commands (i.e. if a user types "!sound" play a sound)

The only two events that are supported are a user sending a message and a users voice chat status changing.

If I continue working on this I'll probably do the following:
  -Make the application more portable
  -Make it more configurable by server users (Let them add commands through the discord client)
