# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:30:43 2018

@author: Lukasz
"""
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import operator

data = pd.read_csv("HTC_FALL_OK_2018_winratios.csv")

df_list = [data]

df = pd.concat(df_list)

blo = ['Zoo Warlock', 'Odd Rogue', 'Malygos Druid', 'Secret Hunter']
Dac = ['Even Warlock', 'Shudderwock Shaman', 'Odd Rogue', 'Malygos Druid']
Goe = ['Control Warlock', 'Shudderwock Shaman', 'Control Priest', 'Taunt Druid']
Sin = ['Even Warlock', 'Shudderwock Shaman', 'Odd Rogue', 'Taunt Druid']

Cai = ['Malygos Druid', 'Tempo Mage', 'Zoo Warlock', 'Odd Rogue']
Moy = ['Taunt Druid', 'Odd Rogue', 'Even Warlock', 'Shudderwock Shaman']
Aku = ['Token Druid', 'Zoo Warlock', 'Quest Rogue', 'Shudderwock Shaman']
jus = ['Malygos Druid', 'Deathrattle Hunter', 'Even Warlock', 'Quest Rogue']

LPT = ['Zoo Warlock', 'Odd Rogue', 'Malygos Druid', 'Tempo Mage']
Hat = ['Odd Warrior', 'Spell Hunter', 'Control Priest', 'Big Druid']
Ing = ['Odd Rogue', 'Deathrattle Hunter', 'Shudderwock Shaman', 'Taunt Druid']
Blo = ['Even Warlock', 'Shudderwock Shaman', 'Malygos Druid', 'Deathrattle Hunter']

Isl = ['Odd Rogue', 'Tempo Mage', 'Zoo Warlock', 'Malygos Druid']
REN = ['Quest Rogue', 'Deathrattle Hunter', 'Cube Warlock', 'Malygos Druid']
Tyl = ['Quest Rogue', 'Deathrattle Hunter', 'Even Warlock', 'Malygos Druid']
Tin = ['Odd Rogue', 'Token Druid', 'Zoo Warlock', 'Tempo Mage']

players = {'bloodyface': blo, 'DacRyvius': Dac, 'GoeLionKing': Goe, 'Sintolol': Sin, 'Caimiao': Cai, 'Moyen': Moy,
           'Akumaker': Aku, 'justsaiyan': jus, 'LPTrunks': LPT, 'Hatul': Hat, 'lnguagehackr': Ing, 'Bloodtrail': Blo,
           'Islandcat': Isl, 'RENMEN': REN, 'Tyler': Tyl, 'Tincho': Tin}
player_list = ['bloodyface', 'DacRyvius', 'GoeLionKing', 'Sintolol', 'Caimiao', 'Moyen', 'Akumaker', 'justsaiyan',
               'LPTrunks', 'Hatul', 'lnguagehackr', 'Bloodtrail', 'Islandcat', 'RENMEN', 'Tyler', 'Tincho']
player_ids = [blo, Dac, Goe, Sin, Cai, Moy, Aku, jus, LPT, Hat, Ing, Blo, Isl, REN, Tyl, Tin]

total_card_packs_given_ids = np.zeros(16, dtype=int)
total_card_packs_given = dict(zip(player_list, total_card_packs_given_ids))

packs_distribution_ids = np.zeros((16, 6), dtype=int)
packs_distribution = dict(zip(player_list, packs_distribution_ids))

tournament_winner_ids = np.zeros(16, dtype=int)
tournament_winner = dict(zip(player_list, tournament_winner_ids))

result = np.zeros(16, dtype=int)


# print(card_packs_given[player_list[0]])

# print(players['ShtanUdachi'])
# print(list(players.keys())[list(players.values()).index(SU)])


def game(pl1, pl2):
    player1 = pl1[:]
    player2 = pl2[:]

    # preparation
    value_min = 1.0
    value_max = 0.0

    for idc1 in player1:
        for idc2 in player2:
            # print(idc1,idc2)
            if idc1 == idc2:
                win_ratio = 0.5
                # print(idc1,idc2,win_ratio)
            else:
                win_ratio = float(
                    df[(df.player_archetype == idc1) & (df.opponent_archetype == idc2)]['win_rate'] / 100.0)
                # print(idc1,idc2,win_ratio)

            if win_ratio > max:
                value_max = win_ratio
                ban1 = idc1

            if win_ratio < min:
                value_min = win_ratio
                ban2 = idc2

    # print(ban1,max,ban2,min)

    # random ban
    # ban1 = player1[np.random.choice([0,1,2,3])]
    # ban2 = player2[np.random.choice([0,1,2,3])]

    n = 10001

    results = np.zeros(n, dtype=int)

    for it in range(0, n):

        player1 = pl1[:]
        player2 = pl2[:]

        player1.remove(ban1)
        player2.remove(ban2)

        # play!
        win1 = 0
        win2 = 0

        while (win1 < 3) & (win2 < 3):

            deck1 = np.random.choice(player1)
            deck2 = np.random.choice(player2)

            rn = random.random()
            if deck1 == deck2:
                win_ratio = 0.5
            else:
                win_ratio = float(
                    df[(df.player_archetype == deck1) & (df.opponent_archetype == deck2)]['win_rate'] / 100.0)
            # print(deck1,deck2,win_ratio,type(win_ratio))

            if rn < win_ratio:
                # print(deck1,deck2,rn,win_ratio,'player 1 won')
                win1 += 1
                player1.remove(deck1)
            else:
                # print(deck1,deck2,rn,win_ratio,'player 2 won')
                win2 += 1
                player2.remove(deck2)

        if win1 > win2:
            # return pl1,pl2
            results[it] = 1
            # print(it,results)
        else:
            # return pl2,pl1
            results[it] = 2
            # print(it,results)

    results = sorted(results)
    # print(it,results)

    if results[int((n - 1) / 2)] == 1:
        return pl1, pl2
    else:
        return pl2, pl1


for i in range(0, 1):
    print('Calculate', i + 1, 'tournament simulation:')

    group_winners = {}
    group_winners_list = []
    group_winners_ids = []

    semifinals = {}
    semifinals_ids = []
    semifinals_list = []

    final = {}
    final_ids = []
    final_list = []

    champion = {}
    champion_ids = []
    champion_list = []

    card_packs_given_ids = np.zeros(16, dtype=int)
    card_packs_given = dict(zip(player_list, card_packs_given_ids))

    for pp in range(0, 4):

        p1, p2, p3, p4 = player_ids[4 * pp:4 * pp + 4]

        print('First game', list(players.keys())[list(players.values()).index(p1)],
              list(players.keys())[list(players.values()).index(p2)])
        p1w, p1l = game(p1[:], p2[:])
        print('Wins', list(players.keys())[list(players.values()).index(p1w)])
        card_packs_given[list(players.keys())[list(players.values()).index(p1w)]] += 1
        # print(p1w,p1l)

        print('Second game', list(players.keys())[list(players.values()).index(p3)],
              list(players.keys())[list(players.values()).index(p4)])
        p2w, p2l = game(p3[:], p4[:])
        print('Wins', list(players.keys())[list(players.values()).index(p2w)])
        card_packs_given[list(players.keys())[list(players.values()).index(p2w)]] += 1
        # print(p2w,p2l)

        print('Third game', list(players.keys())[list(players.values()).index(p1w)],
              list(players.keys())[list(players.values()).index(p2w)])
        p2ww, p2wl = game(p1w[:], p2w[:])
        print('Wins', list(players.keys())[list(players.values()).index(p2ww)])
        card_packs_given[list(players.keys())[list(players.values()).index(p2ww)]] += 1

        print('Fourth game', list(players.keys())[list(players.values()).index(p1l)],
              list(players.keys())[list(players.values()).index(p2l)])
        p2lw, p2ll = game(p1l[:], p2l[:])
        print('Wins', list(players.keys())[list(players.values()).index(p2lw)])
        card_packs_given[list(players.keys())[list(players.values()).index(p2lw)]] += 1

        print('Fifth game', list(players.keys())[list(players.values()).index(p2wl)],
              list(players.keys())[list(players.values()).index(p2lw)])
        p3wwl, p3wll = game(p2wl[:], p2lw[:])
        print('Wins', list(players.keys())[list(players.values()).index(p3wwl)])
        card_packs_given[list(players.keys())[list(players.values()).index(p3wwl)]] += 1

        group_winners_ids.append(p2ww)
        group_winners_ids.append(p3wwl)

        # print(list(players.keys())[list(players.values()).index(p2ww)],list(players.keys())[list(players.values()).index(p3wwl)])

        if (p2ww == p1) or (p3wwl == p1):
            result[4 * pp + 0] += 1
            # print('Player',list(players.keys())[list(players.values()).index(p1)],'+1=',result[4*pp+0])

        if (p2ww == p2) or (p3wwl == p2):
            result[4 * pp + 1] += 1
            # print('Player',list(players.keys())[list(players.values()).index(p2)],'+1=',result[4*pp+1])

        if (p2ww == p3) or (p3wwl == p3):
            result[4 * pp + 2] += 1
            # print('Player',list(players.keys())[list(players.values()).index(p3)],'+1=',result[4*pp+2])

        if (p2ww == p4) or (p3wwl == p4):
            result[4 * pp + 3] += 1
            # print('Player',list(players.keys())[list(players.values()).index(p4)],'+1=',result[4*pp+3])

    for idc in group_winners_ids:
        group_winners_list.append(str(list(players.keys())[list(players.values()).index(idc)]))
    print(group_winners_list)

    # quarter-finals
    # print('group_winners_list',group_winners_list)
    # print('group_winners_ids',group_winners_ids)
    group_winners = dict(zip(group_winners_list, group_winners_ids))

    # print(players)
    # print('group_winners',group_winners)

    sf1, x = game(group_winners_ids[0][:], group_winners_ids[3][:])
    sf2, x = game(group_winners_ids[4][:], group_winners_ids[7][:])
    sf3, x = game(group_winners_ids[2][:], group_winners_ids[1][:])
    sf4, x = game(group_winners_ids[6][:], group_winners_ids[5][:])

    card_packs_given[list(players.keys())[list(players.values()).index(sf1)]] += 1
    card_packs_given[list(players.keys())[list(players.values()).index(sf2)]] += 1
    card_packs_given[list(players.keys())[list(players.values()).index(sf3)]] += 1
    card_packs_given[list(players.keys())[list(players.values()).index(sf4)]] += 1

    semifinals_ids.append(sf1)
    semifinals_ids.append(sf2)
    semifinals_ids.append(sf3)
    semifinals_ids.append(sf4)
    # print('semifinals_ids',semifinals_ids)
    for idc in semifinals_ids:
        semifinals_list.append(str(list(group_winners.keys())[list(group_winners.values()).index(idc)]))
    print(semifinals_list)

    semifinals = dict(zip(semifinals_list, semifinals_ids))
    # print(semifinals)

    # semifinals
    f1, x = game(semifinals_ids[0][:], semifinals_ids[1][:])
    f2, x = game(semifinals_ids[2][:], semifinals_ids[3][:])

    card_packs_given[list(players.keys())[list(players.values()).index(f1)]] += 1
    card_packs_given[list(players.keys())[list(players.values()).index(f2)]] += 1

    final_ids.append(f1)
    final_ids.append(f2)
    # print('final_ids',final_ids)
    for idc in final_ids:
        final_list.append(str(list(semifinals.keys())[list(semifinals.values()).index(idc)]))
    print(final_list)

    final = dict(zip(final_list, final_ids))

    # final
    champion, vicechampion = game(final_ids[0][:], final_ids[1][:])
    card_packs_given[list(players.keys())[list(players.values()).index(champion)]] += 1
    champion_ids.append(champion)

    for idc in champion_ids:
        champion_list.append(str(list(final.keys())[list(final.values()).index(idc)]))
    print(champion_list)

    champion = dict(zip(champion_list, champion_ids))

    tournament_winner[champion_list[0]] += 1

    for idc in card_packs_given:
        total_card_packs_given[idc] += card_packs_given[idc].sum()
        packs_distribution[idc][card_packs_given[idc].sum()] += 1
    # print(card_packs_given)

# sort tournament_winner and total packs given dictionaries
sorted_tournament_winner = sorted(tournament_winner.items(), key=operator.itemgetter(1), reverse=True)
sorted_total_card_packs_given = sorted(total_card_packs_given.items(), key=operator.itemgetter(1), reverse=True)

print('Tournament winner:')
for idc in sorted_tournament_winner:
    print(idc[0], idc[1])

print('')

print('Total packs given:')
for idc in sorted_total_card_packs_given:
    print(idc[0], idc[1])
# print(total_card_packs_given)
# print(packs_distribution)


for idc in packs_distribution.keys():
    # print(idc)
    plt.bar(range(6), packs_distribution[idc], width=0.5)
    # plt.legend(player_list, loc='upper right', bbox_to_anchor=(1.35, 1.1))
    plt.legend([idc], loc='upper center', bbox_to_anchor=(0.5, 1.15))
    plt.show()

print('Group winners:\n')
groups = ['A', 'B', 'C', 'D']
for pp in range(0, 4):
    print('Group', groups[pp] + ':')
    for idc in player_list[4 * pp:4 * pp + 4]:
        # print(idc,result[player_list[4*pp:4*pp+4].index(idc)])
        print(idc, result[4 * pp + player_list[4 * pp:4 * pp + 4].index(idc)])
    print('')

# 1st game Hoej DocPwn
# Wins DocPwn
# 2nd game Orange Tom60229
# Wins Tom60229
# 3rd game DocPwn Tom60229
# Wins DocPwn
# 4th game Hoej Orange
# Wins Orange
# 5th game Tom60229 Orange
# Wins Tom60229

# 1st game Muzzy Jason Zhou
# Wins Muzzy
# 2nd game Kolento SamuelTsao
# Wins SamuelTsao
# 3rd game Muzzy SamuelTsao
# Wins Muzzy
# 4th game Jason Zhou Kolento
# Wins Kolento
# 5th game SamuelTsao Kolento
# Wins SamuelTsao

# 1st game ShtanUdachi Ant
# Wins Ant
# 2nd game Sintolol Purple
# Wins Purple
# 3rd game Ant Purple
# Wins Purple
# 4th game ShtanUdachi Sintolol
# Wins ShtanUdachi
# 5th game Ant ShtanUdachi
# Wins Ant

# 1st game Surrender OmegaZero
# Wins Surrender
# 2nd game Fr0zen Neirea
# Wins Fr0zen
# 3rd game Surrender Fr0zen
# Wins Surrender
# 4th game OmegaZero Neirea
# Wins OmegaZero
# 5th game Fr0zen OmegaZero
# Wins Fr0zen

# ['DocPwn', 'Tom60229', 'Muzzy', 'SamuelTsao', 'Purple', 'Ant', 'Surrender', 'Fr0zen']
# ['SamuelTsao', 'Fr0zen', 'Tom60229', 'Surrender']
# ['Fr0zen', 'Tom60229']
# ['Tom60229']
# Tournament winner:
# Tom60229 1
