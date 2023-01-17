# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:30:43 2018

@author: Lukasz
"""
import pandas as pd
import random
import numpy as np

data = pd.read_csv("HTC_FALL_OK_2018_winratios.csv")

df_list = [data]

df = pd.concat(df_list)

blo = ['Zoo Warlock', 'Odd Rogue', 'Malygos Druid', 'Secret Hunter']
Dac = ['Odd Rogue', 'Shudderwock Shaman', 'Even Warlock', 'Malygos Druid']
Goe = ['Control Priest', 'Control Warlock', 'Taunt Druid', 'Shudderwock Shaman']
Sin = ['Odd Rogue', 'Even Warlock', 'Taunt Druid', 'Shudderwock Shaman']

Cai = ['Tempo Mage', 'Zoo Warlock', 'Malygos Druid', 'Odd Rogue']
Moy = ['Odd Rogue', 'Even Warlock', 'Shudderwock Shaman', 'Taunt Druid']
Aku = ['Zoo Warlock', 'Token Druid', 'Quest Rogue', 'Shudderwock Shaman']
jus = ['Malygos Druid', 'Deathrattle Hunter', 'Even Warlock', 'Quest Rogue']

LPT = ['Zoo Warlock', 'Odd Rogue', 'Malygos Druid', 'Tempo Mage']
Hat = ['Odd Warrior', 'Spell Hunter', 'Control Priest', 'Big Druid']
Ing = ['Odd Rogue', 'Deathrattle Hunter', 'Shudderwock Shaman', 'Taunt Druid']
Blo = ['Even Warlock', 'Shudderwock Shaman', 'Malygos Druid', 'Deathrattle Hunter']

Isl = ['Odd Rogue', 'Tempo Mage', 'Zoo Warlock', 'Malygos Druid']
REN = ['Deathrattle Hunter', 'Quest Rogue', 'Cube Warlock', 'Malygos Druid']
Tyl = ['Deathrattle Hunter', 'Even Warlock', 'Quest Rogue', 'Malygos Druid']
Tin = ['Token Druid', 'Odd Rogue', 'Zoo Warlock', 'Tempo Mage']

players = {'bloodyface': blo, 'DacRyvius': Dac, 'GoeLionKing': Goe, 'Sintolol': Sin, 'Caimiao': Cai, 'Moyen': Moy,
           'Akumaker': Aku, 'justsaiyan': jus, 'LPTrunks': LPT, 'Hatul': Hat, 'lnguagehackr': Ing, 'Bloodtrail': Blo,
           'Islandcat': Isl, 'RENMEN': REN, 'Tyler': Tyl, 'Tincho': Tin}
player_list = ['bloodyface', 'DacRyvius', 'GoeLionKing', 'Sintolol', 'Caimiao', 'Moyen', 'Akumaker', 'justsaiyan',
               'LPTrunks', 'Hatul', 'lnguagehackr', 'Bloodtrail', 'Islandcat', 'RENMEN', 'Tyler', 'Tincho']
player_ids = [blo, Dac, Goe, Sin, Cai, Moy, Aku, jus, LPT, Hat, Ing, Blo, Isl, REN, Tyl, Tin]


def game(player1, player2):
    win1 = 0
    win2 = 0

    while (win1 < 3) & (win2 < 3):

        deck1 = np.random.choice(player1)
        deck2 = np.random.choice(player2)

        rn = random.random()
        if deck1 == deck2:
            win__ratio = 0.5
        else:
            win__ratio = float(
                df[(df.player_archetype == deck1) & (df.opponent_archetype == deck2)]['win_rate'] / 100.0)
        # print(deck1,deck2,win_ratio,type(win_ratio))

        if rn < win__ratio:
            # print(deck1,deck2,rn,win_ratio,'player 1 won')
            win1 += 1
            player1.remove(deck1)
        else:
            # print(deck1,deck2,rn,win_ratio,'player 2 won')
            win2 += 1
            player2.remove(deck2)

    if win1 > win2:
        return 1
    else:
        return 0


p1 = Tin
p2 = Blo

range_min = 1.0
range_max = 0.0

for idc1 in p1:
    for idc2 in p2:

        if idc1 == idc2:
            win_ratio = 0.5
            print(idc1, idc2, win_ratio)
        else:
            win_ratio = float(df[(df.player_archetype == idc1) & (df.opponent_archetype == idc2)]['win_rate'] / 100.0)
            print(idc1, idc2, win_ratio)

        if win_ratio > range_max:
            range_max = win_ratio
            ban1 = idc1

        if win_ratio < range_min:
            range_min = win_ratio
            ban2 = idc2

print(list(players.keys())[list(players.values()).index(p2)], 'bans:', ban1, range_max)
print(list(players.keys())[list(players.values()).index(p1)], 'bans:', ban2, range_min)

tabelka = '[table][tr][td][/td][td]' + list(players.keys())[list(players.values()).index(p2)] + '[/td]'
for idc2 in p2:
    tabelka += '[td]' + idc2 + '[/td]'
tabelka += '[/tr]'
tabelka += '[tr][td]' + list(players.keys())[
    list(players.values()).index(p1)] + '[/td][td][/td][td][/td][td][/td][td][/td][td][/td][/tr]'

N = 1000

for idc1 in p1:
    tabelka += '[tr][td]' + idc1 + '[/td][td][/td]'
    for idc2 in p2:
        p11 = p1[:]
        p22 = p2[:]

        p11.remove(idc1)
        p22.remove(idc2)

        wins = 0
        for games in range(0, N):
            wins += game(p11[:], p22[:])

        win_probability = 1.0 * wins / N
        print(idc1, idc2, win_probability)
        if win_probability > 0.5:
            tabelka += '[th]' + str(float("{0:.1f}".format(win_probability * 100.0))) + '[/th]'
        else:
            tabelka += '[td]' + str(float("{0:.1f}".format(win_probability * 100.0))) + '[/td]'

    tabelka += '[/tr]'
tabelka += '[/table]'
print(tabelka)
