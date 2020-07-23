# IdleBot
The automation bot for Idle Heroes game by DHGames.

The project was created to learn about UI automation in python using lackey. But it appeared to be stable enough to grow into full scale bot.
This bot automates daily events completion which are super boring in this game.

The bot is working slower than the human, since image recognition is not that fast. Yet it allows to get some free time while bot is doing the treadmill activities for you.

The bot is designed to run on Windows PC while the game is running on Bluestacks emulator. The project was developed in Visual Studio, so it should be run from it.

Bluestacks should be running in resolution 1920x1080, 240 DPI maximized window.

It is expected that your player level is high enough and all the game features are already unlocked. Bot doesn't have any fancy logic to deal with low level limitations.

# Which daily activities it does
* Gathers daily gems
* Gathers the checkin bonus
* Does event raid
* Gathers hearts in friends list and starts the quick explore in the Lost Underground
* Arena: does 3 fights in Crystal crown league
* Campaign: gathers the loot and gets the rewards 5 times
* Celestial Island: collects the resources, enters the expedion, gathers all the chests, kills the dragon and raids all the islands
* Market: buys arena tickes, all 3-star heroes which are bought for gold, 4-star hero for 1500k gold, 5 basic summon scrolls
* Wishing Fountain: does 2 spins of 1 coin
* Seal land: does the smash for the last used faction
* Blacksmith: forges 3 swords
* Collects daily quest rewards

Basically you just need to do the Adventure and Tavern quests yourself, everything else is covered by the bot.

# How to start it

1. Run Idle heroes in BlueStacks
2. Maximize BlueStacks window
3. Log into the game so that you see the main game screen (i.e. Campaign, Summon circle, Arena etc)
4. DO NOT SCROLL the screen in any direction
5. Open and run IdleBot solution in Visual Studio
6. Switch back to BlueStacks window so that IdleBot is running in background
7. Sit and watch while Idlebot is completing the daily activities for you

# Demo
A short [video](https://github.com/AntonKukoba1/IdleBot/blob/master/Demo.m4v) of how it looks when the bot is running.

# Extending and updating the bot

The bot logic is pretty straightforward: wait for some image to appear - click some screen element. So the only thing needed is some screen shots to feed them to lackey. So in \IdleBot\idleheroes you'll find all those elements, which are used by the image recognition engine. 

DHGAMES changes their interface once in 3-4 months, thus you'll need to update those images in order for bot to run.

# Bugs and things not implemented yet
* The lags in connection affect the stability of the bot dramatically.
* If the game disconnects while the bot is running, there's no way to recover after the game is reconnected. You still may comment out the completed steps in main() and resume.



