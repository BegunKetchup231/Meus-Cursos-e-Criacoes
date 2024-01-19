
azul = '\033[1;34m'
color = '\033[92m'
end = '\033[0m'

npcid = str(input(azul+'NPC ID: ')).strip()
questid = str(input(azul+'Quest ID: ')).strip()

print('-' * 50)
print(color,'QuestKillMOB = 1')
print(color,'QuestItem = 2')
print(color,'QuestLevelRange = 4')
print(color,'QuestClass = 5')
print(color,'QuestExperienceGuild = 7')
print(color,'QuestRequire = 9')
print(color,'QuestItemChoice = 13')
print(color,'QuestExperience = 14')
print(color,'QuestGold = 15')
print(color,'QuestClassChange = 16')
print(color,'QuestTalkTo = 19')
print(color,'QuestPran = 21')
print(color,'QuestUse = 31')
print(color,'QuestMissionChoice = 37')
print(color,'QuestComeFrom = 38')
print(color,'QuestAfterMission = 48')
print(color,'QuestBattlefieldVictory = 51')
print(color,'QuestSkillAdquire = 62')
print(color,'QuestTitleAdquire = 63')
print(color,'QuestCash = 64',end)
print(azul+'-' * 50)


tipoquest = str(input(azul+'Tipo de quest: ')).strip()

print(color+'-' * 50)
print(color,'QuestDefault = 0')
print(color,'QuestReset = 1')
print(color,'QuestStartGreen = 2')
print(color,'QuestOngoing = 3')
print(color,'QuestDone = 4')
print(color,'QuestSaveLocation = 5')
print(color,'QuestNotEnoughLevel = 7')
print(color,'QuestStartRed = 8')
print(color,'QuestStartBlue = 9')
print(color,'QuestStartYellow = 11')
print(color+'-' * 50)

corquest = str(input(azul+'Cor da quest: ')).strip()

rewardgold = str(input(azul+'Recompensa em Gold: '))
rewardxp = str(input(azul+'Recompensa em XP: '))
levelmini = str(input(azul+'Level Mínimo: '))
reward1 = str(input(azul+'Id da Recompensa 1: '))
reward2 = str(input(azul+'Id da Recompensa 2: '))
reward3 = str(input(azul+'Id da Recompensa 3: '))
reward4 = str(input(azul+'Id da Recompensa 4: '))
reward5 = str(input(azul+'Id da Recompensa 5: '))
reward6 = str(input(azul+'Id da Recompensa 6: '))
requeriment1 = str(input(azul+'Id do Requisito 1: '))
requerimentamo1 = str(input(azul+'Quantidade do Requisito 1: '))
requeriment2 = str(input(azul+'Id do Requisito 2: '))
requerimentamo2 = str(input(azul+'Quantidade do Requisito 2: '))
requeriment3 = str(input(azul+'Id do Requisito 3: '))
requerimentamo3 = str(input(azul+'Quantidade do Requisito 3: '))
requeriment4 = str(input(azul+'Id do Requisito 4: '))
requerimentamo4 = str(input(azul+'Quantidade do Requisito 4: '))
requeriment5 = str(input(azul+'Id do Requisito 5: '))
requerimentamo5 = str(input(azul+'Quantidade do Requisito 5: '))
deleteitem1 = str(input(azul+'Item a ser deletado 1: '))
itemamou1 = str(input(azul+'Quantidade do item 1: '))
deleteitem2 = str(input(azul+'Item a ser deletado 2: '))
itemamou2 = str(input(azul+'Quantidade do item 2: '))
deleteitem3 = str(input(azul+'Item a ser deletado 3: '))
itemamou3 = str(input(azul+'Quantidade do item 3: '))

print('-' * 50)
print(color,'QuestKillMOB = 1')
print(color,'QuestItem = 2')
print(color,'QuestLevelRange = 4')
print(color,'QuestClass = 5')
print(color,'QuestExperienceGuild = 7')
print(color,'QuestRequire = 9')
print(color,'QuestItemChoice = 13')
print(color,'QuestExperience = 14')
print(color,'QuestGold = 15')
print(color,'QuestClassChange = 16')
print(color,'QuestTalkTo = 19')
print(color,'QuestPran = 21')
print(color,'QuestUse = 31')
print(color,'QuestMissionChoice = 37')
print(color,'QuestComeFrom = 38')
print(color,'QuestAfterMission = 48')
print(color,'QuestBattlefieldVictory = 51')
print(color,'QuestSkillAdquire = 62')
print(color,'QuestTitleAdquire = 63')
print(color,'QuestCash = 64',end)
print('-' * 50)

questype1 = str(input(azul+'Tipo de Requerimento 1: '))
questype2 = str(input(azul+'Tipo de Requerimento 2: '))
questype3 = str(input(azul+'Tipo de Requerimento 3: '))
questype4 = str(input(azul+'Tipo de Requerimento 4: '))
questype5 = str(input(azul+'Tipo de Requerimento 5: '))

print('-' * 50)
# Tipo de quest
questtype = int(tipoquest)

# Cor da quest
questmark = int(corquest)

# Id do NPC
um = int(npcid)

# Id da quest
dois = int(questid)

# Recompensa em GOLD
tres = int(rewardgold)

# Recompensa de XP
quatro = int(rewardxp)

# Level minimo da quest
levelmin = int(levelmini)

# ID DAS RECOMPENSAS
seis = int(reward1)
sete = int(reward2)
oito = int(reward3)
nove = int(reward4)
dez = int(reward5)
onze = int(reward6)

# requisitos do type, id do mob etc...
doze = int(requeriment1)
treze = int(requeriment2)
quator = int(requeriment3)
quinze = int(requeriment4)
dezeseis = int(requeriment5)

# Quantidade dos requisitos
dezesete = int(requerimentamo1)
dezoito = int(requerimentamo2)
dezenove = int(requerimentamo3)
vinte = int(requerimentamo4)
vinteum = int(requerimentamo5)

# Item a ser deletado quando entregar a quest
delete1 = int(deleteitem1)
itemamo1 = int(itemamou1)
delete2 = int(deleteitem2)
itemamo2 = int(itemamou2)
delete3 = int(deleteitem3)
itemamo3 = int(itemamou3)

print(f'{um},{dois},{questtype},{questmark},{seis},{sete},{oito},{nove},{dez},{onze},{doze},{treze},{quator},{quinze},{dezeseis},{questype1},{questype2},{questype3},{questype4},{questype5},{dezesete},{dezoito},{dezenove},{vinte},{vinteum},{delete1},{delete2},{delete3},{itemamo1},{itemamo2},{itemamo3},{rewardgold},{rewardxp},{levelmin}')
