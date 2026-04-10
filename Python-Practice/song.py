# gTTS = text ko voice me convert karega
from gtts import gTTS

# pygame = audio play karega
import pygame

# time = delay ke liye (jab tak song chale)
import time


# 💌 Step 1: Apne song/lyrics likho
lyrics = """Jag Chhadd Ke Tere Naal Laaiyan
Chhora Ve Raavi Vaalaneya
Mainu Mardi Na Chhadd Jayi Ve
Chhora Ve Raavi

Ranjha Ranjha Kardi Ve Main
Aape Ranjha Hoi
Is Duniya Nu Main Na Jana
Mera Ghar Na Koi

Door Desh Mainu Laija Ve
Mera Dil Nai Parhda Koi
Ranjha Ranjha Kardi Ve Main
Aape Ranjha Hoi Ho Ho…

Ranjha Ranjha…

Jag Chhadd Ke Tere Naal Laaiyan
Chhora Ve Raavi Vaalaneya
Mainu Mardi Na Chhadd Jayi Ve
Chhora Ve Raavi Vaalaneya

Duniya De Rang Rang Jaavan
Te Main Changi Kehlavan
Dil Apne Di Kar Baitha
Te Main Khasma Nu Khavan

Dum Humdum Mera Ghutda Jaave
Til Til Mardi Jaavan
Rooh Meri Nu Seene Laa
Tainu Ik Ik Dard Sunavan

Ve Mainu Duniya Taane Maare
Ve Main Chhad Aavan Mahal Minare
Ve Mainu Laija Takht Hazare
Jithe Ishq De Hon Nazare

Ve Aakhon Heer Heer Na Koi
Ve Main Taan Jogan Ohdi Hoi
Ni Ranjha Ranjha Kardi Kardi
Ve Main Aape Ranjha Hoi

Ho Ho Ho…

Ranjha Ranjha…

Jag Chhadd Ke Tere Naal Laaiyan
Chhora Ve Raavi Vaalaneya
Mainu Mardi Na Chhadd Jayi Ve
Chhora Ve Raavi Vaalaneya

Jag Chhadd Ke Tere Naal Laaiyan
Chhora Ve Raavi Vaalaneya
Mainu Mardi Na Chhadd Jayi Ve
Chhora Ve Raavi Vaalaneya"""

# 🎧 Step 2: Text ko voice me convert karo
# lang='hi' means Hindi voice
tts = gTTS(text=lyrics, lang='hi')


# 💾 Step 3: Audio file save karo (mp3 file banegi)
tts.save("confession_song.mp3")




# ▶️ Step 4: Audio play karne ke liye pygame start karo
pygame.mixer.init()


# 📂 Step 5: Jo mp3 bani hai usko load karo
pygame.mixer.music.load("confession_song.mp3")


# ▶️ Step 6: Song play karo
pygame.mixer.music.play()

print("🎶 Song play...")


# ⏳ Step 7: Jab tak song chal raha hai tab tak wait karo
# warna program turant band ho jayega
while pygame.mixer.music.get_busy():
    time.sleep(1)


# ✅ Step 8: End message
print("🎉 Song complete!")