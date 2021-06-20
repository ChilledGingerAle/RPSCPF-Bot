const Discord = require("discord.js");
const config = require("./config.json");
const client = new Discord.Client();
const prefix = ">>";


client.on("message", function(message) {
  if (message.author.bot) return;
  if (!message.content.startsWith(prefix)) return;

  const commandBody = message.content.slice(prefix.length);
  const args = commandBody.split(' ');
  const command = args.shift().toLowerCase();
  const StartChannel = null

  if (command === "ping") {
    const timeTaken = Date.now() - message.createdTimestamp;
    message.reply(`Pong! This message had a latency of ${timeTaken}ms.`);
  }
});

client.on('ready', () => {
    
    client.user.setActivity("out for ping commands", {type: "WATCHING"})

    // Alternatively, you can set the activity to any of the following:
    // PLAYING, STREAMING, LISTENING, WATCHING
    // For example:
    // client.user.setActivity("TV", {type: "WATCHING"})
    
    client.channels.cache.get("850391054029160468").send("Javascript Program is operational.");
})

client.login(config.BOT_TOKEN);
