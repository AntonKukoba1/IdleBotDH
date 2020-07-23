from lackey import *
import time

def wait_and_click(path, t):
    wait(path, t)
    time.sleep(1)
    click(path)

def wait_and_click_with_sim(path, t, similarity):
    pattern = Pattern(path)
    pattern.similarity = similarity
    wait(pattern, t)
    time.sleep(1)
    click(pattern)

def wait_and_hover(path, time):
    wait(path, time)
    hover(path)

def has_elements(iter):
  from itertools import tee
  iter, any_check = tee(iter)
  try:
    any_check.next()
    return True, iter
  except StopIteration:
    return False, iter

# get campaign items
def GetCampaign():
    wait_and_click(".\\idleheroes\\campaign.png", 2)
    wait(".\\idleheroes\\campaign_loot.png", 3)
    buttons = findAll(".\\idleheroes\\campaign_loot.png")
    lootButton = max(buttons, key=lambda button: button.x)
    time.sleep(1)
    click(lootButton)
    wait_and_click(".\\idleheroes\\campaign_claim.png", 2)
    for x in range(5):
        wait_and_click(".\\idleheroes\\campaign_get.png", 2)
        time.sleep(6)

    click(".\\idleheroes\\campaign_back.png")

def CollectChests():
    chests = findAll(".\\idleheroes\\celestial_chest.png")
    while chests:
        wasCalled = False
        for chest in chests:
            click(chest)
            time.sleep(1)
            wasCalled = True
        if wasCalled:
            chests = findAll(".\\idleheroes\\celestial_chest.png")
        else:
            break

def BeatSkinIslands():
    islands = findAll(".\\idleheroes\\celestial_skin_island.png")
    while islands:
        wasCalled = False
        for island in islands:
            click(island)
            wait_and_click(".\\idleheroes\\celestial_dragon_smash.png", 3)
            wait_and_click(".\\idleheroes\\celestial_dragon_smash_ok.png", 3)
            time.sleep(1)
            wait_and_click(".\\idleheroes\\arena_start_fight.png", 3)
            wait_and_click(".\\idleheroes\\campaign_claim.png", 3)
            wasCalled = True
        if wasCalled:
            chests = findAll(".\\idleheroes\\celestial_skin_island.png")
        else:
            break
    

# get celestial island
def GetCelestialIsland():
    wait_and_click(".\\idleheroes\\celestial.png", 5)
    wait_and_click(".\\idleheroes\\celestial_claim.png", 3)
    time.sleep(2)
    wait_and_click(".\\idleheroes\\celestial_expedition.png", 3)
    time.sleep(3)

    CollectChests()
    BeatSkinIslands()
    #DragScreenDown()
    #CollectChests()
    #BeatSkinIslands()
    
    wait_and_click(".\\idleheroes\\celestial_dragon.png", 3)
    wait_and_click(".\\idleheroes\\celestial_dragon_smash.png", 3)
    #wait_and_click(".\\idleheroes\\celestial_dragon_smash_plus.png", 3)
    wait_and_click(".\\idleheroes\\celestial_dragon_smash_ok.png", 3)
    time.sleep(1)
    wait_and_click(".\\idleheroes\\arena_start_fight.png", 3)
    wait_and_click(".\\idleheroes\\campaign_claim.png", 3)
    time.sleep(3)
    
    wait_and_click(".\\idleheroes\\celestial_smash.png", 3)
    okPattern = Pattern(".\\idleheroes\\celestial_smash_yes.png")
    okPattern.similarity = 0.95
    wait_and_click(okPattern, 3)
    time.sleep(1)
    wait_and_click(".\\idleheroes\\arena_start_fight.png", 3)
    wait_and_click(".\\idleheroes\\campaign_claim.png", 3)
    time.sleep(2)

    #click(".\\idleheroes\\celestial_back.png")
    type(Key.ESC)
    time.sleep(1)
    type(Key.ESC)

def DoSummon():
    freePattern = Pattern(".\\idleheroes\\summon_free.png")
    freePattern.similarity = 0.95
    basicPattern = Pattern(".\\idleheroes\\summon_one.png")
    basicPattern.similarity = 0.95
    if exists(freePattern):
        wait_and_click_with_sim(".\\idleheroes\\summon_free.png", 2, 0.95)
        wait(".\\idleheroes\\summon_ok.png", 3)
        type(Key.ESC)
    elif exists(basicPattern):
        wait_and_click_with_sim(".\\idleheroes\\summon_one.png", 2, 0.95)
        wait(".\\idleheroes\\summon_ok.png", 3)
        type(Key.ESC)


def GetSummon():
    wait_and_click(".\\idleheroes\\summon_circle.png", 2)
    time.sleep(2)
    DoSummon()

    wait_and_click(".\\idleheroes\\summon_circle.png", 2)
    wait_and_click(".\\idleheroes\\summon_heroic_section.png", 2)
    time.sleep(2)

    DoSummon()

def GetFountain():
    wait_and_click(".\\idleheroes\\fountain.png", 2)
    wait_and_click(".\\idleheroes\\fountain_wish.png", 2)
    #wait(".\\idleheroes\\fountain_next_refresh.png")
    time.sleep(2)
    wait_and_click(".\\idleheroes\\fountain_one.png", 2)
    click(".\\idleheroes\\fountain_one.png")
    wait_and_click(".\\idleheroes\\fountain_ok.png", 10)

    wait_and_click(".\\idleheroes\\fountain_one.png", 2)
    wait_and_click(".\\idleheroes\\fountain_ok.png", 10)

    #wait_and_click(".\\idleheroes\\fountain_back.png", 2)
    type(Key.ESC)
    time.sleep(1)
    type(Key.ESC)

def FightOneBattle():
    wait_and_click(".\\idleheroes\\arena_battle.png", 6)
    wait(".\\idleheroes\\arena_do_battle.png", 6)
    battles = findAll(".\\idleheroes\\arena_do_battle.png")
    lowestBattle = max(battles, key=lambda battle: battle.y)
    #time.sleep(1)
    click(lowestBattle)
    #click(lowestBattle)

    wait_and_click(".\\idleheroes\\arena_start_fight.png", 4)
    wait_and_click(".\\idleheroes\\arena_question.png", 4)
    time.sleep(2)
    click(".\\idleheroes\\arena_grey_ok.png")
    wait_and_click(".\\idleheroes\\arena_ok.png", 4)

def FightOneTrialBattle():
    wait_and_click(".\\idleheroes\\arena_battle.png", 4)
    wait(".\\idleheroes\\arena_do_battle.png", 4)
    battles = findAll(".\\idleheroes\\arena_do_battle.png")
    lowestBattle = max(battles, key=lambda battle: battle.y)
    click(lowestBattle)

    wait_and_click(".\\idleheroes\\arena_start_trial_fight.png", 4)
    wait_and_click(".\\idleheroes\\arena_question.png", 4)
    click(".\\idleheroes\\arena_grey_ok.png")
    wait_and_click(".\\idleheroes\\arena_ok.png", 4)

def GetArena():
    wait_and_click(".\\idleheroes\\arena.png", 2)
    wait(".\\idleheroes\\arena_league.png", 2)
    time.sleep(1)
    click(".\\idleheroes\\arena_join.png")
    
    time.sleep(1)
    FightOneBattle()
    time.sleep(2)
    FightOneBattle()
    time.sleep(2)
    FightOneBattle()
    time.sleep(2)
    #wait_and_click(".\\idleheroes\\arena_back.png", 2)
    type(Key.ESC)
    time.sleep(1)
    type(Key.ESC)

def BuyItem(item):
    click(item)
    wait(".\\idleheroes\\market_yes.png", 3)
    buttons = findAll(".\\idleheroes\\market_yes.png")
    yesButton = max(buttons, key=lambda button: button.x)
    click(yesButton)
    wait_and_click(".\\idleheroes\\market_ok.png", 2)
  

def GetMarket():
    wait_and_click(".\\idleheroes\\market.png", 2)
    time.sleep(1)

    # buy arena tickets
    pattern = Pattern(".\\idleheroes\\market_3star.png")
    pattern.similarity = 0.95
    BuyItem(pattern)
    time.sleep(2)

    wait_and_click(".\\idleheroes\\market_right.png", 2)

    # buy all 3* heroes at second page
    pattern = Pattern(".\\idleheroes\\market_3star.png")
    pattern.similarity = 0.94
    heroes3star = findAll(pattern)
    for hero in heroes3star:
        BuyItem(hero)
        time.sleep(2)


    pattern = Pattern(".\\idleheroes\\market_4star.png")
    pattern.similarity = 0.95
    BuyItem(pattern)
    time.sleep(2)

    wait_and_click(".\\idleheroes\\market_right.png", 2)
    wait_and_click(".\\idleheroes\\market_right.png", 2)

    pattern = Pattern(".\\idleheroes\\market_scrolls.png")
    pattern.similarity = 0.95
    BuyItem(pattern)
    time.sleep(2)

    wait_and_click(".\\idleheroes\\market_back.png", 2)

def GetSealLand():
    wait_and_click(".\\idleheroes\\seal_land.png", 2)
    wait_and_click(".\\idleheroes\\seal_land_battle.png", 3)
    wait(".\\idleheroes\\seal_land_smash.png", 2)
    buttons = findAll(".\\idleheroes\\seal_land_smash.png")
    smashButton = max(buttons, key=lambda button: button.y)
    click(smashButton)
    
    wait_and_click(".\\idleheroes\\seal_land_max_smash.png", 2)
    wait_and_click(".\\idleheroes\\seal_land_ok.png", 2)
    wait_and_click(".\\idleheroes\\seal_land_claim.png", 2)
    time.sleep(2)
    wait_and_click(".\\idleheroes\\seal_land_back.png", 2)
    time.sleep(2)
    wait_and_click(".\\idleheroes\\seal_land_back.png", 2)

def GetBlackSmith():
    wait_and_click(".\\idleheroes\\blacksmith.png", 2)
    wait_and_click(".\\idleheroes\\blacksmith_sword.png", 2)
    wait_and_click(".\\idleheroes\\blacksmith_input.png", 2)
    type(Key.BACKSPACE)
    type(Key.BACKSPACE)
    type(Key.BACKSPACE)
    type("3")
    wait_and_click(".\\idleheroes\\blacksmith_forge.png", 2)
    wait_and_click(".\\idleheroes\\blacksmith_ok.png", 5)
    #wait_and_click(".\\idleheroes\\blacksmith_back.png", 2)
    type(Key.ESC)

def DragScreenDown():
    dargStart = Region(900, 360, 1, 1)
    dragEnd = Region(900, 720, 1, 1)
    drag(dargStart)
    dropAt(dragEnd)

def DragScreenLeft():
    drag(".\\idleheroes\\fountain.png")
    dropAt(".\\idleheroes\\arena.png")

def DragScreenLeftToCenter():
    drag(".\\idleheroes\\altar.png")
    dropAt(".\\idleheroes\\tavern.png")

def DragScreenRight():
    drag(".\\idleheroes\\arena.png")
    dropAt(".\\idleheroes\\summon_circle.png")

def DragScreenRightToCenter():
    drag(".\\idleheroes\\aspen_dungeon.png")
    dropAt(".\\idleheroes\\tower.png")

def GetEventRaid():

    if wait(".\\idleheroes\\event_raid.png", 2) is None:
        if wait(".\\idleheroes\\event_raid2x.png", 2) is not None:
            click(".\\idleheroes\\event_raid2x.png")
    else:
        click(".\\idleheroes\\event_raid.png")

    wait_and_click(".\\idleheroes\\event_raid.png", 2)
    wait(".\\idleheroes\\event_raid_challenge.png", 2)
    challenges = findAll(".\\idleheroes\\event_raid_challenge.png")
    for challenge in challenges:
        click(challenge)
        wait(".\\idleheroes\\event_raid_challenge2.png", 2)
        pattern = Pattern(".\\idleheroes\\event_raid_challenge2.png")
        pattern.similarity = 0.9
        realChallenges = findAll(pattern)

        lowestChallenge = max(realChallenges, key=lambda realChallenge: realChallenge.y)
        click(lowestChallenge)
        time.sleep(1)
        wait_and_click(".\\idleheroes\\arena_start_fight.png", 2)
        time.sleep(2)
        wait_and_click(".\\idleheroes\\event_raid_next.png", 3)
        time.sleep(2)
        type(Key.ESC)
        time.sleep(2)
        type(Key.ESC)
        time.sleep(2)
    type(Key.ESC)

def GetFriends():
    wait_and_click(".\\idleheroes\\friend_list.png", 5)
    wait_and_click(".\\idleheroes\\friend_list_claim.png", 5)
    time.sleep(2)
    wait_and_click(".\\idleheroes\\friend_list_explore.png", 5)
    wait_and_click(".\\idleheroes\\friend_list_quick_explore.png", 10)
    wait_and_click(".\\idleheroes\\friend_list_do_explore.png", 5)
    time.sleep(2)
    type(Key.ESC)

def CollectDailyPrizes():
    wait_and_click(".\\idleheroes\\daily_quest.png", 5)

    pattern = Pattern(".\\idleheroes\\daily_claim.png")
    pattern.similarity = 0.95
    claim = find(pattern)
    while claim:
        click(claim)
        time.sleep(1)
        if not exists(pattern):
            break
        claim = find(pattern)

    type(Key.ESC)

def GetCheckinBonus():
    wait_and_click(".\\idleheroes\\daily_bonus.png", 5)
    wait_and_click(".\\idleheroes\\checkin.png", 5)
    time.sleep(1)
    type(Key.ESC)
    time.sleep(1)
    type(Key.ESC)

def main():

    ###Trial of the champion
    #for i in range(66):
    #    FightOneTrialBattle()
    #    time.sleep(2)

    ##Crystal crown league
    #for i in range(60):
    #    FightOneBattle()
    #    time.sleep(2)

    #wait_and_click(".\\idleheroes\\daily_gems.png", 5)
    #time.sleep(1)
    #GetCheckinBonus()
    #GetEventRaid() 
    GetFriends()
    
    GetArena()
    GetCampaign() 
    GetSummon() 

    DragScreenLeft()
    GetCelestialIsland()
    GetMarket() 
    GetFountain()

    DragScreenLeftToCenter()
    DragScreenRight()

    GetSealLand() 
    GetBlackSmith()
    DragScreenRightToCenter()
    CollectDailyPrizes()

if __name__ == "__main__":
    main()

