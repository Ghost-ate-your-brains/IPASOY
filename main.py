from LIPASOY import Encryptor

spell = str(input("Type a spell: "))
enc = Encryptor.Encryptor(spell)
ready_spell = enc.encrypt()
print(ready_spell)