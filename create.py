from application import db
from application.models import Genres, Songs, Users

db.create_all()

reggae = Genres(name = 'Reggae')
rock = Genres(name = 'Rock')
rap = Genres(name = 'Rap')
metal = Genres(name = 'Metal')
hardstyle = Genres(name = 'Hardstyle')
disco = Genres(name = 'Disco')
db.session.add(reggae, rock, rap, metal, hardstyle, disco)


#Reggae
skints = Songs(name='The Skints', genre = reggae, link = 'https://youtu.be/DWWkzWisRTQ')
chezidek = Songs(name='Chezidek',  genre = reggae, link = 'https://youtu.be/O3cPx6TZFSo')
chronixx = Songs(name= 'Chronixx', genre = reggae, link = 'https://youtu.be/LfeIfiiBTfY')
mungos_hifi = Songs(name='Mungos Hi-Fi', genre = reggae , link = 'https://youtu.be/8GzH-cAZSew')
max_romeo = Songs(name='Max Romeo', genre = reggae, link = 'https://youtu.be/H9oLSMSW4SI')

#Rock
greta_van_fleet = Songs(name= 'Greta Van Fleet', genre = rock, link = 'https://youtu.be/8cepUUKMp1g')
billy_idol = Songs(name= 'Billy Idol', genre = rock, link = 'https://youtu.be/gpo2y4yWFFc')
yes = Songs(name= 'Yes', genre = rock, link = 'https://youtu.be/cPCLFtxpadE')
pearl_jam = Songs(name= 'Pearl Jam', genre = rock, link = 'https://youtu.be/tkbgtVFlyCQ')
alice_in_chains = Songs(name= 'Alice In Chains', genre = rock, link = 'https://youtu.be/MNMqyrhPrXY')
#Rap
brotha_lynch_hung = songs (name= 'Brotha Lynch Hung', genre = rap, link = 'https://youtu.be/MwPNVXSuP-Y')
twopac = songs (name= '2Pac', genre = rap, link = 'https://youtu.be/41qC3w3UUkU')
seotaiji = Songs(name= 'Seotaiji', genre = rap, link = 'https://youtu.be/q3xy4p2JTfU')
joyner_lucas = Songs(name= 'Joyner Lucas', genre = rap, link = 'https://youtu.be/XBNUuGVFisU')
denzel_curry = Songs(name= 'Denzel Curry', genre = rap, link = 'https://youtu.be/3WHm6tfvKlk')
#Metal
ghost = Songs(name= 'Ghost', genre = metal, link = 'https://youtu.be/0mGr5bMItQY')
unleash_the_archers = Songs(name= 'Unleash The Archers', genre = metal, link = 'https://youtu.be/NTWbVUUkWm4')
caligulas_horse = Songs(name= 'Caligulas Horse', genre = metal, link = 'https://youtu.be/8e-O6OmvGP0')
agent_fresco = Songs(name= 'Agent Fresco', genre = metal, link = 'https://youtu.be/PgArsBIbiFg')
gojira = Songs(name= 'gojira', genre = metal, link = 'https://youtu.be/CFm8QpCghkU')
#Hardstyle
delete_and_outbreak = Songs(name= 'Delete and Outbreak', genre = hardstyle, link = 'https://youtu.be/C8CRc9A2wp4')
warface_and_dsturb = Songs(name= 'Warface & D-Sturb', genre = hardstyle, link = 'https://youtu.be/uxEotTWKJVA')
the_purge = Songs(name= 'The Purge', genre = hardstyle, link = 'https://youtu.be/kU6pDS3MW2k')
tnt = Songs(name= 'TNT', genre = hardstyle, link = 'https://youtu.be/lFl0_GiS7Z0')
rebelion = Songs(name= 'Rebelion', genre = hardstyle, link = 'https://youtu.be/5F48_ygN90g')
#Disco
average_white_band = Songs(name= 'Average White Band', genre = disco, link = 'https://youtu.be/FnH_zwVmiuE')
mariya_takeuchi = Songs(name= 'Mariya Takeuchi', genre = disco, link = 'https://youtu.be/9Gj47G2e1Jc')
eddie_murphy = Songs(name= 'Eddie Murphy', genre = disco, link = 'https://youtu.be/SyGjuAudW_g')
modern_talking = Songs(name= 'Modern Talking', genre = disco, link = 'https://youtu.be/4kHl4FoK1Ys')
brothers_johnson = Songs(name= 'The Brothers Johnson', genre = disco, link = 'https://youtu.be/tPBDMihPRJA')

db.session.add()
db.session.commit()