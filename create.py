from application import db
from application.models import Genres, Songs, Users

db.drop_all() #clear database and create again REMOVE WHEN TIME COMES
db.create_all()

reggae = Genres(name = 'Reggae')
rock = Genres(name = 'Rock')
rap = Genres(name = 'Rap')
metal = Genres(name = 'Metal')
hardstyle = Genres(name = 'Hardstyle')
disco = Genres(name = 'Disco')

db.session.add_all([reggae, rock, rap, metal, hardstyle, disco])
db.session.commit()

#Reggae
skints = Songs(name='The Skints', playlist = reggae, link = 'https://youtu.be/DWWkzWisRTQ')
chezidek = Songs(name='Chezidek',  playlist = reggae, link = 'https://youtu.be/O3cPx6TZFSo')
chronixx = Songs(name= 'Chronixx', playlist = reggae, link = 'https://youtu.be/LfeIfiiBTfY')
mungos_hifi = Songs(name='Mungos Hi-Fi', playlist = reggae , link = 'https://youtu.be/8GzH-cAZSew')
max_romeo = Songs(name='Max Romeo', playlist = reggae, link = 'https://youtu.be/H9oLSMSW4SI')

#Rock
greta_van_fleet = Songs(name= 'Greta Van Fleet', playlist= rock, link = 'https://youtu.be/8cepUUKMp1g')
billy_idol = Songs(name= 'Billy Idol', playlist = rock, link = 'https://youtu.be/gpo2y4yWFFc')
yes = Songs(name= 'Yes', playlist = rock, link = 'https://youtu.be/cPCLFtxpadE')
pearl_jam = Songs(name= 'Pearl Jam', playlist = rock, link = 'https://youtu.be/tkbgtVFlyCQ')
alice_in_chains = Songs(name= 'Alice In Chains', playlist = rock, link = 'https://youtu.be/MNMqyrhPrXY')
#Rap
brotha_lynch_hung = Songs(name= 'Brotha Lynch Hung', playlist = rap, link = 'https://youtu.be/MwPNVXSuP-Y')
twopac = Songs(name= '2Pac', playlist= rap, link = 'https://youtu.be/41qC3w3UUkU')
seotaiji = Songs(name= 'Seotaiji', playlist = rap, link = 'https://youtu.be/q3xy4p2JTfU')
joyner_lucas = Songs(name= 'Joyner Lucas', playlist= rap, link = 'https://youtu.be/XBNUuGVFisU')
denzel_curry = Songs(name= 'Denzel Curry', playlist = rap, link = 'https://youtu.be/3WHm6tfvKlk')
#Metal
ghost = Songs(name= 'Ghost', playlist = metal, link = 'https://youtu.be/0mGr5bMItQY')
unleash_the_archers = Songs(name= 'Unleash The Archers', playlist = metal, link = 'https://youtu.be/NTWbVUUkWm4')
caligulas_horse = Songs(name= 'Caligulas Horse', playlist = metal, link = 'https://youtu.be/8e-O6OmvGP0')
agent_fresco = Songs(name= 'Agent Fresco', playlist = metal, link = 'https://youtu.be/PgArsBIbiFg')
gojira = Songs(name= 'gojira', playlist = metal, link = 'https://youtu.be/CFm8QpCghkU')
#Hardstyle
delete_and_outbreak = Songs(name= 'Delete and Outbreak', playlist = hardstyle, link = 'https://youtu.be/C8CRc9A2wp4')
warface_and_dsturb = Songs(name= 'Warface & D-Sturb', playlist= hardstyle, link = 'https://youtu.be/uxEotTWKJVA')
the_purge = Songs(name= 'The Purge', playlist= hardstyle, link = 'https://youtu.be/kU6pDS3MW2k')
tnt = Songs(name= 'TNT', playlist = hardstyle, link = 'https://youtu.be/lFl0_GiS7Z0')
rebelion = Songs(name= 'Rebelion', playlist = hardstyle, link = 'https://youtu.be/5F48_ygN90g')
#Disco
average_white_band = Songs(name= 'Average White Band', playlist = disco, link = 'https://youtu.be/FnH_zwVmiuE')
mariya_takeuchi = Songs(name= 'Mariya Takeuchi', playlist = disco, link = 'https://youtu.be/9Gj47G2e1Jc')
eddie_murphy = Songs(name= 'Eddie Murphy', playlist = disco, link = 'https://youtu.be/SyGjuAudW_g')
modern_talking = Songs(name= 'Modern Talking', playlist = disco, link = 'https://youtu.be/4kHl4FoK1Ys')
brothers_johnson = Songs(name= 'The Brothers Johnson', playlist = disco, link = 'https://youtu.be/tPBDMihPRJA')
