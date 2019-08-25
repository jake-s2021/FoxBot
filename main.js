const Discord = require('discord.js');
var request = require("request");
const client = new Discord.Client();

function framedata(msg){
    var msg2 = msg.substring(4,msg.length);
    var com = "http://kuroganehammer.com/Ultimate/";

    switch(msg2){
        case "fox":
        case "Fox":
            return com + "Fox";
        case "kirby":
        case "Kirby":
            return com + "Kirby";
        case "pikachu":
        case "Pikachu":
            return com + "Pikachu";
        case "donkey kong":
        case "Donkey Kong":
        case "dk":
        case "DK":
            return com + "Donkey%20Kong";
        case "jigglypuff":
        case "Jigglypuff":
            return com + "Jigglypuff";
        case "mario":
        case "Mario":
            return com + "Mario";
        case "luigi":
        case "Luigi":
            return com + "Luigi";
        case "samus":
        case "Samus":
            return com + "Samus";
        case "link":
        case "Link":
            return com + "Link";
        case "yoshi":
        case "Yoshi":
        case "yosh":
        case "Yosh":
            if(msg2 === "yosh" || msg2 === "Yosh"){
                return ":yosh:   " + com + "Yoshi";
            }
            else{
                return com + "Yoshi";
            }
        case "ness":
        case "Ness":
            return com + "Ness";
        case "captain falcon":
        case "Captain Falcon":
            return com + "Captain%20Falcon";
        case "dark samus":
        case "Dark Samus":
            return com + "Dark%20Samus";
        case "peach":
        case "Peach":
            return com + "Peach";
        case "daisy":
        case "Daisy":
            return com + "Daisy";
        case "bowser":
        case "Bowser":
            return com + "Bowser";
        case "ice climbers":
        case "Ice Climbers":
            return com + "Ice%20Climbers";
        case "shiek":
        case "Shiek":
            return com + "Shiek";
        case "zelda":
        case "Zelda":
            return com + "Zelda";
        case "dr. mario":
        case "Dr. Mario":
        case "dr mario":
        case "Dr Mario":
            return com + "Dr.%20Mario";
        case "pichu":
        case "Pichu":
            return com +"Pichu";
        case "Falco":
        case "falco":
            return com + "Falco";
        case "marth":
        case "Marth":
            return com + "Marth";
        case "lucina":
        case "Lucina":
            return com + "Lucina";
        case "young link":
        case "Young Link":
            return com + "Young%20Link";
        case "ganondorf":
        case "Ganondorf":
            return com + "Ganondorf";
        case "mewtwo":
        case "Mewtwo":
            return com + "Mewtwo";
        case "roy":
        case "Roy":
            return com + "Roy";
        case "chrom":
        case "Chrom":
            return com + "Chrom";
        case "gw":
        case "GW":
        case "Mr. Game & Watch":
        case "mr game & watch":
            return com + "Mr.%20Game%20And%20Watch";
        case "pit":
        case "Pit":
            return com + "Pit";
        case "dark pit":
        case "Dark Pit":
        case "pitoo":
        case "Pitoo":
            return com + "Dark%20Pit";
        case "zss":
        case "ZSS":
        case "zero suit samus":
        case "Zero Suit Samus":
            return com + "Zero%20Suit%20Samus";
        case "wario":
        case "Wario":
            return com + "Wario";
        case "snake":
        case "Snake":
            return com + "Snake";
        case "ike":
        case "Ike":
            return com + "Ike";
        case "pkmn":
        case "PKMN":
        case "pokemon trainer":
        case "Pokemon Trainer":
            return com + "Charizard\n" + com + "Squritle\n" + com + "Ivysaur";
        case "diddy kong":
        case "Diddy Kong":
            return com + "Diddy%Kong";
        case "lucas":
        case "Lucas":
            return com + "Lucas";
        case "sonic":
        case "Sonic":
            return com + "Sonic";
        case "king dedede":
        case "King Dedede":
        case "dedede":
        case "Dedede":
            return com + "King%20Dedede";
        case "olimar":
        case "Olimar":
            return com + "Olimar";
        case "lucario":
        case "Lucario":
            return com + "Lucario";
        case "rob":
        case "ROB":
        case "R.O.B":
            return com + "R.O.B";
        case "toon link":
        case "Toon Link":
            return com + "Toon%20Link";
        case "wolf":
        case "Wolf":
            return com + "Wolf";
        case "villager":
        case "Villager":
            return com + "Villager";
        case "mega man":
        case "Mega Man":
            return com + "Mega%20Man";
        case "wft":
        case "WFT":
        case "wii fit trainer":
        case "Wii Fit Trainer":
            return com + "Wii%20Fit%20Trainer";
        case "rosa":
        case "Rosa":
        case "rosalina":
        case "Rosalina":
        case "Rosalina & Lima":
            return com + "Rosalina";
        case "mac":
        case "Mac":
        case "little mac":
        case "Little Mac":
            return com + "Little%20Mac";
        case "greninja":
        case "Greninja":
            return com + "Greninja";
        case "palutena":
        case "Palutena":
            return com + "Palutena";
        case "pac-man":
        case "pacman":
        case "Pac-Man":
        case "PAC-MAN":
            return com + "PAC-MAN";
        case "robin":
        case "Robin":
            return com + "Robin";
        case "shulk":
        case "Shulk":
            return com + "Shulk";
        case "jr":
        case "bowser jr":
        case "Bowser Jr":
            return com + "Bowser%20Jr";
        case "duck hunt":
        case "Duck Hunt":
            return com + "Duck%20Hunt";
        case "ryu":
        case "Ryu":
            return com + "Ryu";
        case "ken":
        case "Ken":
            return com + "Ken";
        case "cloud":
        case "Cloud":
            return com + "Cloud";
        case "corrin":
        case "Corrin":
            return com + "Corrin";
        case "bayonetta":
        case "Bayonetta":
            return com + "Bayonetta";
        case "inkling":
        case "Inkling":
            return com + "Inkling";
        case "ridley":
        case "Ridley":
            return com + "Ridley";
        case "simon":
        case "Simon":
            return com + "Simon";
        case "richter":
        case "Richter":
            return com + "Richter";
        case "krool":
        case "k rool":
        case "K Rool":
        case "K. Rool":
            return com + "King-K.-Rool";
        case "isabelle":
        case "Isabelle":
            return com + "Isabelle";
        case "incineroar":
        case "Incineroar":
            return com + "Incineroar";
        case "Piranha Plant":
        case "piranha plant":
            return com + "Piranha%20Plant";
        case "hero":
        case "Hero":
        case "the hero":
        case "The Hero":
            return com + "Hero";
        case "mii brawler":
        case "Mii Brawler":
            return com + "Mii%20Brawler";
        case "mii swordfighter":
        case "Mii Swordfighter":
            return com + "Mii%20Swordfighter";
        case "mii gunner":
        case "Mii Gunner":
            return com + "Mii%20Gunner";
        case "goku":
        case "Goku":
        case "steve":
        case "Steve":
        case "shrek":
        case "Shrek":
            return "https://imgur.com/a/AKKgmQ5"
        
        default:
            return "Not a character.";
        
    }
}

function message_select(msg){
    if (msg.startsWith("=fd")){
       return framedata(msg);
    }
    switch(msg){
        case "=help":
            return "=fd (character name)\n"+
            "=downb\n"+
            "=upb\n";
        case "=downb":
            return "*blip*";
        case "=upb":
            return "FIYAH!!";
        default:
            return "not a command, type =help for list of commands";
    }
}

client.setInterval(getBody = () => { //periodically updates nintendo's twitch stream data and alerts when live

   /* if(getBody.count === undefined){
        getBody.count = 0;
    }*/
    var options = { method: 'GET',
        url: 'https://api.twitch.tv/helix/streams?user_id= channel id here',
        headers:
            { 
                'Client-ID': 'twitch client id here'} };
                    
    request(options, function (error, response, body) {
        if (!error && response.statusCode == 200) {

           // console.log(getBody.count++,JSON.parse(body)); // twitch updates stream info about every 2-3 minutes
            var data = JSON.parse(body)["data"];

            if(getBody.switcher === undefined){
                getBody.switcher = true;
            }
            try{
                var id = data[0]["id"];

                if(getBody.switcher){
                    console.log("online");
                    try{
                    client.channels.get("channel id here").send("Nintendo is Live on Twitch! https://www.twitch.tv/nintendo");
                    }
                    catch(e){
                        console.log(e);
                    }
                    getBody.switcher = false;
                }
                
            }
            catch(e){
                if(!(getBody.switcher)){
                    console.log("offline");
                    getBody.switcher = true;
                }
            }
        }
        else
            console.log(error);
        })  
}, delay = 15000)//15s interval


client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content.startsWith("=")) {
    msg.reply(message_select(msg.content));
  }
});

client.login('needs key');


