
import random

characters = ["Phoenix", "Raze", "Brimstone", "Jett", "Sage", "Viper", "Breach", "Cypher", "Sova", "Omen", "Reyna", "Killjoy"]
sidearms = ["classic", "shorty", "frenzy", "ghost", "sheriff"]
primary = ["stinger", "spectre", "bulldog", "guardian", "phantom", "vandal", "bucky", "judge", "ares", "odin", "marshal", "operator"]

def ultimate_bravery(available_characters, available_sidearms, available_primary):
    random_cha = random.choice(available_characters)
    random_sid = random.choice(available_sidearms)
    random_pri = random.choice(available_primary)
    return random_cha, random_sid, random_pri

print(ultimate_bravery(characters, sidearms, primary))
