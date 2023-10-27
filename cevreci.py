import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptik')

@bot.command()
async def cevre_kirliligi_nedir(ctx):
    await ctx.send(f'Merhaba {bot.user}doğanin, doğal kaynaklarin ve yaşanilan çevrenin aşiri ölçüde ve yanliş kullanilmasi nedeniyle doğal dengenin bozulmasi durumu.')
@bot.command()
async def Hava_kirliliği(ctx):
    await ctx.send(f'Merhaba {bot.user}Hava kirliliği, canlıların sağlığını olumsuz yönde etkileyen ve havadaki yabancı maddelerin, normalin üzerinde miktar ve yoğunluğa ulaşmasıdır.Hava kirliliği; havada katı, sıvı ve gaz şeklindeki yabancı maddelerin insan sağlığına, canlı hayatına ve ekolojik dengeye zarar verecek miktar, yoğunluk ve uzun sürede atmosferde bulunmasıdır. İnsanların çeşitli faaliyetleri sonucu meydana gelen üretim ve tüketim aktiviteleri sırasında ortaya çıkan atıklarla hava tabakası kirlenerek, yeryüzündeki canlı hayatını olumsuz yönde etkilemektedir. Hava kirliliği yüzünden her sene 7 milyon kişi ölmekte.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("KENDİ TOKENİNİ GİR BENİMKİNİV ÇALAMAZSIN HAHAHAHAAAA")
