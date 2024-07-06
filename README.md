# Chip the Cool Cat
 
Chip is the mascot of the Computer Science Society at The University of Windsor!

He's represented by a discord bot, has a couple cool features that help make our discord a better place.

For one, he's equipped with a message screener that helps mods flag potentially harmful content in the server (see: https://github.com/uwindsorcss/ai-automod)

You can also talk to him! He's very knowledgeable about Computer Science at uwindsor, and would be happy to answer your questions if you use /ask (see: https://github.com/uwindsorcss/ai-assistant/)

Join our discord today to say hi to Chip!

For developers: To set up Chip locally so you can make contributions, download our ai automod state dict from https://drive.google.com/file/d/1zH6KJqPkyujFv_2yo_P_lYJMYtZ72Irj/view?usp=drive_link and place it in the `src` folder. Copy `.env.example` into your own `.env` file and fill out the appropriate values (you may have to set up your own qdrant cluster and run ingest.py over at https://github.com/uwindsorcss/ai-assistant/ if you're not oficially on the team and don't have access to our cluster). Then install the requirements and run `bot.py`. 