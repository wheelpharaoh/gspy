import json
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/arena_ranks/", response_model=List[schemas.ArenaRankMaster])
def read_arena_ranks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    arena_ranks = crud.get_arena_ranks(db, skip=skip, limit=limit)
    return arena_ranks

@app.get("/arena_ranking_rewards/", response_model=List[schemas.ArenaRankingRewardMaster])
def read_arena_ranking_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    arena_ranking_rewards = crud.get_arena_ranking_rewards(db, skip=skip, limit=limit)
    return arena_ranking_rewards

@app.get("/arena_rewards/", response_model=List[schemas.ArenaRewardMaster])
def read_arena_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    arena_rewards = crud.get_arena_rewards(db, skip=skip, limit=limit)
    return arena_rewards

@app.get("/arena_shops/", response_model=List[schemas.ArenaShopMaster])
def read_arena_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    arena_shops = crud.get_arena_shops(db, skip=skip, limit=limit)
    return arena_shops

@app.get("/battle_relations/", response_model=List[schemas.BattleRelationMaster])
def read_battle_relations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    battle_relations = crud.get_battle_relations(db, skip=skip, limit=limit)
    return battle_relations

@app.get("/challenges/", response_model=List[schemas.ChallengeMaster])
def read_challenges(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    challenges = crud.get_challenges(db, skip=skip, limit=limit)
    return challenges

@app.get("/challenge_events/", response_model=List[schemas.ChallengeEventMaster])
def read_challenge_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    challenge_events = crud.get_challenge_events(db, skip=skip, limit=limit)
    return challenge_events

@app.get("/challenge_rewards/", response_model=List[schemas.ChallengeRewardMaster])
def read_challenge_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    challenge_rewards = crud.get_challenge_rewards(db, skip=skip, limit=limit)
    return challenge_rewards

@app.get("/common_unlocks/", response_model=List[schemas.CommonUnlockMaster])
def get_common_unlocks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    common_unlocks = crud.get_common_unlocks(db, skip=skip, limit=limit)
    return common_unlocks

@app.get("/common_strings/", response_model=List[schemas.CommonstringMaster])
def get_common_strings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    common_strings = crud.get_common_strings(db, skip=skip, limit=limit)
    return common_strings

@app.get("/cooking_recipes/", response_model=List[schemas.CookingRecipeMaster])
def get_cooking_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cooking_recipes = crud.get_cooking_recipes(db, skip=skip, limit=limit)
    return cooking_recipes

@app.get("/dungeon_launchers/", response_model=List[schemas.DungeonLauncherMaster])
def get_dungeon_launchers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dungeon_launchers = crud.get_dungeon_launchers(db, skip=skip, limit=limit)
    return dungeon_launchers


@app.get("/dungeon/{dungeon_id}", response_model=schemas.DungeonMaster)
def read_unit(dungeon_id: int, db: Session = Depends(get_db)):
    dungeon = crud.get_dungeon(db, dungeon_id=dungeon_id)
    return dungeon

@app.get("/dungeons/", response_model=List[schemas.DungeonMaster])
def get_dungeons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dungeons = crud.get_dungeons(db, skip=skip, limit=limit)
    return dungeons



@app.get("/enemy/{enemy_id}", response_model=schemas.EnemyMaster)
def read_unit(enemy_id: int, db: Session = Depends(get_db)):
    enemy = crud.get_enemy(db, enemy_id=enemy_id)
    return enemy

@app.get("/enemys/", response_model=List[schemas.EnemyMaster])
def read_enemys(skip: int = 0, limit: int = 300, db: Session = Depends(get_db)):
    enemys = crud.get_enemys(db, skip=skip, limit=limit)
    return enemys

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying-with-joins
@app.get("/enemys_name/{enemy_name}", response_model=List[schemas.EnemyMaster])
def read_enemys_by_name(enemy_name: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enemys = crud.get_enemys_by_name(db, enemy_name, skip=skip, limit=limit)
    return enemys


@app.get("/event_infos/", response_model=List[schemas.EventInfoMaster])
def read_event_infos(skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    event_infos = crud.get_event_infos(db, skip=skip, limit=limit)
    return event_infos

@app.get("/event_items/", response_model=List[schemas.EventItemMaster])
def read_event_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    event_items = crud.get_event_items(db, skip=skip, limit=limit)
    return event_items


@app.get("/event/{event_id}", response_model=schemas.EventMaster)
def read_event(event_id: int, db: Session = Depends(get_db)):
    event = crud.get_event(db, event_id=event_id)
    return event
@app.get("/events/", response_model=List[schemas.EventMaster])
def read_events(skip: int = 0, limit: int = 300, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events


@app.get("/event_shops/", response_model=List[schemas.EventShopMaster])
def read_event_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    event_shops = crud.get_event_shops(db, skip=skip, limit=limit)
    return event_shops

@app.get("/farms/", response_model=List[schemas.FarmMaster])
def read_farms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    farms = crud.get_farms(db, skip=skip, limit=limit)
    return farms

@app.get("/field_settings/", response_model=List[schemas.FieldSettingMaster])
def read_field_settings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    field_settings = crud.get_field_settings(db, skip=skip, limit=limit)
    return field_settings

@app.get("/food_boosts/", response_model=List[schemas.FoodBoostMaster])
def read_food_boosts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    food_boosts = crud.get_food_boosts(db, skip=skip, limit=limit)
    return food_boosts

@app.get("/food_effects/", response_model=List[schemas.FoodEffectMaster])
def read_food_effects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    food_effects = crud.get_food_effects(db, skip=skip, limit=limit)
    return food_effects

@app.get("/foods/", response_model=List[schemas.FoodMaster])
def read_foods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    foods = crud.get_foods(db, skip=skip, limit=limit)
    return foods

@app.get("/friend_multis/", response_model=List[schemas.FriendMultiMaster])
def read_friend_multis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    friend_multis = crud.get_friend_multis(db, skip=skip, limit=limit)
    return friend_multis

@app.get("/gacha_buttons/", response_model=List[schemas.GachaButtonMaster])
def read_gacha_buttons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gacha_buttons = crud.get_gacha_buttons(db, skip=skip, limit=limit)
    return gacha_buttons

@app.get("/gachas/", response_model=List[schemas.GachaMaster])
def read_gachas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gachas = crud.get_gachas(db, skip=skip, limit=limit)
    return gachas

@app.get("/gacha_points/", response_model=List[schemas.GachaPointMaster])
def read_gacha_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gacha_points = crud.get_gacha_points(db, skip=skip, limit=limit)
    return gacha_points

@app.get("/gacha_step_ups/", response_model=List[schemas.GachaStepUpMaster])
def read_gacha_step_ups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gacha_step_ups = crud.get_gacha_step_ups(db, skip=skip, limit=limit)
    return gacha_step_ups

@app.get("/item_evolutions/", response_model=List[schemas.ItemEvolutionMaster])
def read_item_evolutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    item_evolutions = crud.get_item_evolutions(db, skip=skip, limit=limit)
    return item_evolutions

@app.get("/item_limitbreak_exps/", response_model=List[schemas.ItemLimitbreakExpMaster])
def read_item_limitbreak_exps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    item_limitbreak_exps = crud.get_item_limitbreak_exps(db, skip=skip, limit=limit)
    return item_limitbreak_exps


@app.get("/item/{item_id}", response_model=schemas.ItemMaster)
def read_event(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id=event_id)
    return item
@app.get("/items/", response_model=List[schemas.ItemMaster])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items



@app.get("/item_recipes/", response_model=List[schemas.ItemRecipeMaster])
def read_item_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    item_recipes = crud.get_item_recipes(db, skip=skip, limit=limit)
    return item_recipes

@app.get("/keys/", response_model=List[schemas.KeyMaster])
def read_keys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    keys = crud.get_keys(db, skip=skip, limit=limit)
    return keys

@app.get("/limited_first_friends/", response_model=List[schemas.LimitedFirstFriendMaster])
def read_limited_first_friends(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    limited_first_friends = crud.get_limited_first_friends(db, skip=skip, limit=limit)
    return limited_first_friends

@app.get("/link_skills/", response_model=List[schemas.LinkSkillMaster])
def read_link_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    link_skills = crud.get_link_skills(db, skip=skip, limit=limit)
    return link_skills

@app.get("/login_bonuss/", response_model=List[schemas.LoginBonusMaster])
def read_login_bonus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    login_bonus = crud.get_loginbonus(db, skip=skip, limit=limit)
    return login_bonus

@app.get("/login_bonus_totals/", response_model=List[schemas.LoginBonusTotalMaster])
def read_login_bonus_totals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    login_bonus_totals = crud.get_login_bonus_totals(db, skip=skip, limit=limit)
    return login_bonus_totals

@app.get("/materials/", response_model=List[schemas.MaterialMaster])
def read_materials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    materials = crud.get_materials(db, skip=skip, limit=limit)
    return materials

@app.get("/missions/", response_model=List[schemas.MissionMaster])
def read_missions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    missions = crud.get_missions(db, skip=skip, limit=limit)
    return missions

@app.get("/orb_shops/", response_model=List[schemas.OrbShopMaster])
def read_orb_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orb_shops = crud.get_orb_shops(db, skip=skip, limit=limit)
    return orb_shops

@app.get("/player_exps/", response_model=List[schemas.PlayerExpMaster])
def read_player_exps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    player_exps = crud.get_player_exps(db, skip=skip, limit=limit)
    return player_exps

@app.get("/premium_logins/", response_model=List[schemas.PremiumLoginMaster])
def read_premium_logins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    premium_logins = crud.get_premium_logins(db, skip=skip, limit=limit)
    return premium_logins

@app.get("/premium_presents/", response_model=List[schemas.PremiumPresentMaster])
def read_premium_presents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    premium_presents = crud.get_premium_presents(db, skip=skip, limit=limit)
    return premium_presents

@app.get("/premium_purchaseds/", response_model=List[schemas.PremiumPurchasedMaster])
def read_premium_purchaseds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    premium_purchaseds = crud.get_premium_purchaseds(db, skip=skip, limit=limit)
    return premium_purchaseds

@app.get("/quests/", response_model=List[schemas.QuestMaster])
def read_quests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    quests = crud.get_quests(db, skip=skip, limit=limit)
    return quests

@app.get("/quest_launchers/", response_model=List[schemas.QuestLauncherMaster])
def read_quest_launchers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quest_launchers = crud.get_quest_launchers(db, skip=skip, limit=limit)
    return quest_launchers

@app.get("/quest_mission_changers/", response_model=List[schemas.QuestMissionChangeMaster])
def read_quest_mission_changers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quest_mission_changers = crud.get_quest_mission_changers(db, skip=skip, limit=limit)
    return quest_mission_changers

@app.get("/quest_missions/", response_model=List[schemas.QuestMissionMaster])
def read_quest_missions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quest_missions = crud.get_quest_missions(db, skip=skip, limit=limit)
    return quest_missions

@app.get("/raid_animations/", response_model=List[schemas.RaidAnimationMaster])
def read_raid_animations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raid_animations = crud.get_raid_animations(db, skip=skip, limit=limit)
    return raid_animations

@app.get("/raid_boss_fields/", response_model=List[schemas.RaidBossFieldMaster])
def read_raid_boss_fields(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raid_boss_fields = crud.get_raid_boss_fields(db, skip=skip, limit=limit)
    return raid_boss_fields

@app.get("/raid_bosss/", response_model=List[schemas.RaidBossMaster])
def read_raid_bosss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raid_bosss = crud.get_raid_bosss(db, skip=skip, limit=limit)
    return raid_bosss

@app.get("/raid_destroy_rewards/", response_model=List[schemas.RaidDestroyRewardMaster])
def read_raid_destroy_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raid_destroy_rewards = crud.get_raid_destroy_rewards(db, skip=skip, limit=limit)
    return raid_destroy_rewards

@app.get("/raid_field_effects/", response_model=List[schemas.RaidFieldEffectMaster])
def read_raid_field_effects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raid_field_effects = crud.get_raid_field_effects(db, skip=skip, limit=limit)
    return raid_field_effects

@app.get("/raid_general_rewards/", response_model=List[schemas.RaidGeneralRewardMaster])
def read_raid_general_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raid_general_rewards = crud.get_raid_general_rewards(db, skip=skip, limit=limit)
    return raid_general_rewards

@app.get("/raids/", response_model=List[schemas.RaidMaster])
def read_raids(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raids = crud.get_raids(db, skip=skip, limit=limit)
    return raids

@app.get("/raid_tickets/", response_model=List[schemas.RaidTicketMaster])
def read_raid_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raid_tickets = crud.get_raid_tickets(db, skip=skip, limit=limit)
    return raid_tickets

@app.get("/raid_total_rewards/", response_model=List[schemas.RaidTotalRewardMaster])
def read_raid_total_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raid_total_rewards = crud.get_raid_total_rewards(db, skip=skip, limit=limit)
    return raid_total_rewards

@app.get("/random_login_bonuss/", response_model=List[schemas.RandomLoginBonusMaster])
def read_random_login_bonuss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    random_login_bonuss = crud.get_random_login_bonuss(db, skip=skip, limit=limit)
    return random_login_bonuss


@app.get("/random_rewards/", response_model=List[schemas.RandomRewardMaster])
def read_random_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    random_rewards = crud.get_random_rewards(db, skip=skip, limit=limit)
    return random_rewards


@app.get("/reset_orb_shop_counts/", response_model=List[schemas.ResetOrbShopCountMaster])
def read_reset_orb_shop_counts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reset_orb_shop_counts = crud.get_reset_orb_shop_counts(db, skip=skip, limit=limit)
    return reset_orb_shop_counts


@app.get("/rewards/", response_model=List[schemas.Reward])
def read_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rewards = crud.get_rewards(db, skip=skip, limit=limit)
    return rewards

@app.get("/reward/{reward_id}", response_model=schemas.Reward)
def read_reward(reward_id: int, db: Session = Depends(get_db)):
    reward = crud.get_reward(db, reward_id=reward_id)
    if reward is None:
        raise HTTPException(status_code=404, detail="Reward not found")
    return reward


@app.get("/runes/", response_model=List[schemas.RuneMaster])
def read_runes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    runes = crud.get_runes(db, skip=skip, limit=limit)
    return runes

@app.get("/rune_types/", response_model=List[schemas.RuneTypeMaster])
def read_rune_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rune_types = crud.get_rune_types(db, skip=skip, limit=limit)
    return rune_types

@app.get("/settings/", response_model=List[schemas.t_setting_master])
def read_settings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    settings = crud.get_settings(db, skip=skip, limit=limit)
    return settings

@app.get("/sharpen_exp_bonuss/", response_model=List[schemas.SharpenExpbonusMaster])
def read_sharpen_exp_bonuss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sharpen_exp_bonuss = crud.get_sharpen_exp_bonuss(db, skip=skip, limit=limit)
    return sharpen_exp_bonuss

@app.get("/sharpens/", response_model=List[schemas.SharpenMaster])
def read_sharpens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sharpens = crud.get_sharpens(db, skip=skip, limit=limit)
    return sharpens

@app.get("/shop_banner_groups/", response_model=List[schemas.ShopBannerGroupMaster])
def read_shop_banner_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shop_banner_groups = crud.get_shop_banner_groups(db, skip=skip, limit=limit)
    return shop_banner_groups

@app.get("/shop_banners/", response_model=List[schemas.ShopBannerMaster])
def read_shop_banners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shop_banners = crud.get_shop_banners(db, skip=skip, limit=limit)
    return shop_banners

@app.get("/shop_deck_sets/", response_model=List[schemas.ShopDeckSetMaster])
def read_shop_deck_sets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shop_deck_sets = crud.get_shop_deck_sets(db, skip=skip, limit=limit)
    return shop_deck_sets

@app.get("/shop_dias/", response_model=List[schemas.ShopDiaMaster])
def read_shop_dias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shop_dias = crud.get_shop_dias(db, skip=skip, limit=limit)
    return shop_dias

@app.get("/shops/", response_model=List[schemas.ShopMaster])
def read_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shops = crud.get_shops(db, skip=skip, limit=limit)
    return shops

@app.get("/skill_effects/", response_model=List[schemas.SkillEffectMaster])
def read_skill_effects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skill_effects = crud.get_skill_effects(db, skip=skip, limit=limit)
    return skill_effects

@app.get("/skills/", response_model=List[schemas.SkillMaster])
def read_skills(skip: int = 0, limit: int = 300, db: Session = Depends(get_db)):
    skills = crud.get_skills(db, skip=skip, limit=limit)
    return skills

@app.get("/skill_relations/", response_model=List[schemas.SkillRelationMaster])
def read_skill_relations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skill_relations = crud.get_skill_relations(db, skip=skip, limit=limit)
    return skill_relations

@app.get("/skill_weights/", response_model=List[schemas.SkillWeightMaster])
def read_skill_weights(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skill_weights = crud.get_skill_weights(db, skip=skip, limit=limit)
    return skill_weights

@app.get("/skill_groups/", response_model=List[schemas.SkillGroupMaster])
def read_skill_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skill_groups = crud.get_skill_groups(db, skip=skip, limit=limit)
    return skill_groups

@app.get("/skins/", response_model=List[schemas.SkinMaster])
def read_skins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skins = crud.get_skins(db, skip=skip, limit=limit)
    return skins

@app.get("/stamps/", response_model=List[schemas.StampMaster])
def read_stamps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stamps = crud.get_stamps(db, skip=skip, limit=limit)
    return stamps

@app.get("/support_rewards/", response_model=List[schemas.SupporterRewardMaster])
def read_support_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    support_rewards = crud.get_support_rewards(db, skip=skip, limit=limit)
    return support_rewards

@app.get("/tools/", response_model=List[schemas.ToolMaster])
def read_tools(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tools = crud.get_tools(db, skip=skip, limit=limit)
    return tools

@app.get("/unit_ability_exps/", response_model=List[schemas.UnitAbilityExpMaster])
def read_unit_ability_exps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    unit_ability_exps = crud.get_unit_ability_exps(db, skip=skip, limit=limit)
    return unit_ability_exps

@app.get("/unit_evolution/", response_model=List[schemas.UnitEvolutionMaster])
def read_unit_evolutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    unit_evolutions = crud.get_unit_evolutions(db, skip=skip, limit=limit)
    return unit_evolutions

@app.get("/unit_exps/", response_model=List[schemas.UnitExpMaster])
def read_unit_exps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    unit_exps = crud.get_unit_exps(db, skip=skip, limit=limit)
    return unit_exps

@app.get("/unit_limitbreak_exps/", response_model=List[schemas.UnitLimitbreakExpMaster])
def read_unit_limitbreak_exps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    unit_limitbreaks_exps = crud.get_unit_limitbreak_exps(db, skip=skip, limit=limit)
    return unit_limitbreaks_exps

@app.get("/unit_limitbreaks/", response_model=List[schemas.UnitLimitbreakMaster])
def read_unit_limitbreaks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    unit_limitbreaks = crud.get_unit_limitbreaks(db, skip=skip, limit=limit)
    return unit_limitbreaks

@app.get("/units/", response_model=List[schemas.UnitMaster])
def read_units(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    units = crud.get_units(db, skip=skip, limit=limit)
    return units

@app.get("/unit/{unit_id}", response_model=schemas.UnitMaster)
def read_unit(unit_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    unit = crud.get_unit(db, unit_id=unit_id)
    return unit

