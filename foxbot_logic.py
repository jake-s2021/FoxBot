import discord
import twitchio
import facebook
import twitter

'''
   retired code, switched to nodejs
'''



client = discord.Client()

'''
   if await twitchio.client.Client().get_stream(channel="hungrybox") is not None and switch:
   
      switch = False
   if await twitchio.client.Client().get_stream(channel="hungrybox") is None and not switch:
      switch = True
'''


def framedata(schar): #returns a url corresponding to a character
    #im aware the implementation is bad, might redo this as a dictionary in the future

    
    schar = schar[4:] #chops the string for easier comparison
    com = "http://kuroganehammer.com/Ultimate/" #com stands for common, all urls accessed start with this

    if schar == "fox" or schar == "Fox": #i really wish python had switch statements
       return com + "Fox"

    elif schar == "kirby" or schar == "Kirby":
       return com + "Kirby"

    elif schar == "pikachu" or schar == "Pikachu":
        return com + "Pikachu"

    elif schar == "donkey kong" or schar == "Donkey Kong" or schar == "DK" or schar == "dk":
        return com + "Donkey%20Kong"
    
    elif schar == "jigglypuff" or schar == "Jigglypuff":
       return com + "Jigglypuff"
    
    elif schar == "mario" or schar == "Mario":
       return com + "Mario"

    elif schar == "luigi" or schar == "Luigi":
       return com + "Luigi"
    
    elif schar == "samus" or schar == "Samus":
       return com + "Samus"

    elif schar == "link" or schar == "Link":
       return com + "Link"
    
    elif schar == "yoshi" or schar == "Yoshi" or schar == "yosh" or schar == "Yosh":
        if schar == "yosh" or schar == "Yosh":
            return ":yosh:  " + com + "Yoshi"
        else:
            return com + "Yoshi"

    elif schar == "ness" or schar == "Ness":
       return com + "Ness"
    
    elif schar == "captain falcon" or schar == "Captain Falcon":
       return com + "Captain%20Falcon"

    elif schar == "dark samus" or schar == "Dark Samus":
        return com + "Dark%20Samus"
    
    elif schar == "peach" or schar == "Peach":
       return com + "Peach"

    elif schar == "daisy" or schar == "Daisy":
       return com + "Daisy"

    elif schar == "bowser" or schar == "Bowser":
       return com + "Bowser"

    elif schar == "ice climbers" or schar == "Ice Climbers":
       return com + "Ice%20Climbers"

    elif schar == "shiek" or schar == "Shiek":
       return com + "Shiek"

    elif schar == "zelda" or schar == "Zelda":
       return com + "Zelda"

    elif schar == "dr. mario" or schar == "Dr. Mario" or schar == "dr mario" or schar == "Dr Mario":
       return com + "Dr.%20Mario"

    elif schar == "pichu" or schar == "Pichu":
       return com + "Pichu"

    elif schar == "falco" or schar == "Falco":
       return com + "Falco"
    
    elif schar == "marth" or schar == "Marth":
       return com + "Marth"

    elif schar == "lucina" or schar == "Lucina":
       return com + "Lucina"

    elif schar == "young link" or schar == "Young Link":
       return com + "Young%20Link"

    elif schar == "ganondorf" or schar == "Ganondorf":
       return com + "Ganondorf"

    elif schar == "mewtwo" or schar == "Mewtwo":
       return com + "Mewtwo"

    elif schar == "roy" or schar == "Roy":
       return com + "Roy"

    elif schar == "chrom" or schar == "Chrom":
       return com + "Chrom"

    elif schar == "gw" or schar == "GW":
       return com + "Mr.%20Game%20And%20Watch"

    elif schar == "mk" or schar == "MK" or schar == "meta knight" or schar == "Meta Knight":
       return com + "Meta%20Knight"

    elif schar == "pit" or schar == "Pit":
       return com + "Pit"

    elif schar == "dark pit" or schar == "Dark Pit" or schar == "pitoo" or schar == "Pitoo":
       return com + "Dark%20Pit"

    elif schar == "zss" or schar == "ZSS" or schar == "zero suit samus" or schar == "Zero Suit Samus":
       return com + "Zero%20Suit%20Samus"

    elif schar == "wario" or schar == "Wario":
       return com + "Wario"

    elif schar == "snake" or schar == "Snake":
       return com + "Snake"

    elif schar == "ike" or schar == "Ike":
       return com + "Ike"

    elif schar == "pkmn" or schar == "PKMN" or schar == "pokemon trainer" or schar == "Pokemon Trainer":
       return com + "Charizard\n" + com + "Squritle\n" + com + "Ivysaur"

    elif schar == "diddy kong" or schar == "Diddy Kong":
       return com + "Diddy%Kong"

    elif schar == "lucas" or schar == "Lucas":
       return com + "Lucas"

    elif schar == "sonic" or schar == "Sonic":
       return com + "Sonic"

    elif schar == "goku" or schar == "Goku" or schar == "steve" or schar == "Steve" or schar == "shrek" or schar == "Shrek":
       return "https://imgur.com/a/AKKgmQ5"

    elif schar == "king dedede" or schar == "King Dedede" or schar == "dedede" or schar == "Dedede":
       return com + "King%20Dedede"

    elif schar == "olimar" or schar == "Olimar":
       return com + "Olimar"

    elif schar == "lucario" or schar == "Lucario":
       return com + "Lucario"

    elif schar == "rob" or schar == "ROB":
       return com + "R.O.B"

    elif schar == "toon link" or schar == "Toon Link" or schar == "tl":
       return com + "Toon%20Link"

    elif schar == "wolf" or schar == "Wolf":
       return com + "Wolf"

    elif schar == "villager" or schar == "Villager":
       return com + "Villager"

    elif schar == "mega man" or schar == "Mega Man":
       return com + "Mega%20Man"

    elif schar == "wft" or schar == "WFT" or schar == "wii fit trainer" or schar == "Wii Fit Trainer":
       return com + "Wii%20Fit%20Trainer"

    elif schar == "rosa" or schar == "Rosa" or schar == "rosalina & luma" or schar == "Rosalina & Luma" or schar == "rosalina" or schar == "Rosalina":
       return com + "Rosalina"

    elif schar == "mac" or schar == "Mac" or schar == "little mac" or schar == "Little Mac":
       return com + "Little%20Mac"

    elif schar == "greninja" or schar == "Greninja":
       return com + "Greninja"

    elif schar == "palutena" or schar == "Palutena":
       return com + "Palutena"

    elif schar == "pac-man" or schar == "Pac-Man" or schar == "PAC-MAN":
       return com + "PAC-MAN"

    elif schar == "robin" or schar == "Robin":
       return com + "Robin"

    elif schar == "shulk" or schar == "Shulk":
       return com + "Shulk"

    elif schar == "jr" or schar == "bowser jr" or schar == "Bowser Jr":
       return com + "Bowser%20Jr"

    elif schar == "duck hunt" or schar == "Duck Hunt":
       return com + "Duck%20Hunt"

    elif schar == "ryu" or schar == "Ryu":
       return com + "Ryu"

    elif schar == "ken" or schar == "Ken":
       return com + "Ken"

    elif schar == "cloud" or schar == "Cloud":
       return com + "Cloud"

    elif schar == "corrin" or schar == "Corrin":
       return com + "Corrin"

    elif schar == "bayonetta" or schar == "Bayonetta":
       return com + "Bayonetta"

    elif schar == "inkling" or schar == "Inkling":
       return com + "Inkling"

    elif schar == "ridley" or schar == "Ridley":
       return com + "Ridley"

    elif schar == "simon" or schar == "Simon":
       return com + "Simon"

    elif schar == "richter" or schar == "Richter":
       return com + "Richter"

    elif schar == "krool" or schar == "k rool" or schar == "K Rool" or schar == "King K Rool" or schar == "king k rool":
       return com + "King-K.-Rool"

    elif schar == "isabelle" or schar == "Isabelle":
       return com + "Isabelle"

    elif schar == "incineroar" or schar == "Incineroar":
       return com + "Incineroar"

    elif schar == "Piranha Plant" or schar == "piranha plant":
       return com + "Piranha%20Plant"

    elif schar == "joker" or schar == "Joker":
       return com + "Joker"

    elif schar == "hero" or schar == "Hero" or schar == "the hero" or schar == "The Hero":
       return com + "Hero"

    elif schar == "Mii Brawler" or schar == "mii brawler":
       return com + "Mii%20Brawler"

    elif schar == "Mii Swordfighter" or schar == "mii swordfighter":
       return com + "Mii%20Swordfighter"

    elif schar == "Mii Gunner" or schar == "mii gunner":
       return com + "Mii%20Gunner"


    else:
        return "(Not a character! Please check your spelling.)"



def message_select(mess):  # make this a normal function that returns a string back to on_message()

    if mess.startswith("=fd"):
       return framedata(mess)

    elif mess == "=help":
        return """=fd (character name)
=downb"""

    elif mess == "=downb":
       return "*blip*"
    else:
       return "(not a command, type =help for list of commands)"



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
        


@client.event
async def on_message(message):


   if message.author == client.user:
      return

   if message.content.startswith('='):
      await message.channel.send(message_select(message.content))

client.loop.create_task(my_background_task())
client.run('')