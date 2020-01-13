from sqlalchemy.orm import Session

from . import models, schemas


def get_arena_ranks(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ArenaRankMaster).offset(skip).limit(limit).all()

def get_arena_ranking_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ArenaRankingRewardMaster).offset(skip).limit(limit).all()

def get_arena_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ArenaRewardMaster).offset(skip).limit(limit).all()

def get_arena_shops(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ArenaShopMaster).offset(skip).limit(limit).all()

def get_battle_relations(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.BattleRelationMaster).offset(skip).limit(limit).all()

def get_challenges(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ChallengeMaster).offset(skip).limit(limit).all()

def get_challenge_events(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ChallengeEventMaster).order_by(models.ChallengeEventMaster.start_at.desc()).offset(skip).limit(limit).all()

def get_challenge_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ChallengeRewardMaster).offset(skip).limit(limit).all()

def get_common_unlocks(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.CommonUnlockMaster).offset(skip).limit(limit).all()

def get_common_strings(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.CommonstringMaster).offset(skip).limit(limit).all()

def get_cooking_recipes(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.CookingRecipeMaster).offset(skip).limit(limit).all()

def get_dungeon_launchers(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.DungeonLauncherMaster).order_by(models.DungeonLauncherMaster.start_at.desc()).offset(skip).limit(limit).all()


def get_dungeon(db: Session, dungeon_id: int):
    return db.query(models.DungeonMaster).filter(models.DungeonMaster.id == dungeon_id).first()

def get_dungeons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DungeonMaster).offset(skip).limit(limit).all()


def get_enemy(db: Session, enemy_id: int):
    return db.query(models.EnemyMaster).filter(models.EnemyMaster.id == enemy_id).first()
def get_enemys(db: Session, skip: int = 0, limit: int = 300):
    return db.query(models.EnemyMaster).offset(skip).limit(limit).all()
def get_enemys_by_name(db: Session, enemy_name: str, skip: int = 0, limit: int = 100):
    search = "%{}%".format(enemy_name)
    return db.query(models.EnemyMaster).join(models.EnemyMaster.unit).filter(models.EnemyMaster.name.ilike(search)).limit(limit).all()
    #return db.query(models.EnemyMaster).join(models.UnitMaster).filter(models.UnitMaster.name.like(search)).limit(limit).all()



def get_event_infos(db: Session, skip: int = 0, limit: int = 400):
    return db.query(models.EventInfoMaster).order_by(models.EventInfoMaster.start_at.desc()).offset(skip).limit(limit).all()

def get_event_items(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.EventItemMaster).offset(skip).limit(limit).all()


def get_event(db: Session, event_id: int):
    return db.query(models.EventMaster).filter(models.EventMaster.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 300):
    return db.query(models.EventMaster).order_by(models.EventMaster.start_at.desc()).offset(skip).limit(limit).all()


def get_event_shops(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.EventShopMaster).offset(skip).limit(limit).all()

def get_farms(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.FarmMaster).offset(skip).limit(limit).all()

def get_field_settings(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.FieldSettingMaster).offset(skip).limit(limit).all()

def get_food_boosts(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.FoodBoostMaster).offset(skip).limit(limit).all()

def get_food_effects(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.FoodEffectMaster).offset(skip).limit(limit).all()

def get_foods(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.FoodMaster).offset(skip).limit(limit).all()

def get_friend_multis(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.FriendMultiMaster).offset(skip).limit(limit).all()

def get_gacha_buttons(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.GachaButtonMaster).offset(skip).limit(limit).all()

def get_gachas(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.GachaMaster).order_by(models.GachaMaster.start_at.desc()).offset(skip).limit(limit).all()

def get_gacha_points(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.GachaPointMaster).offset(skip).limit(limit).all()

def get_gacha_step_ups(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.GachaStepUpMaster).offset(skip).limit(limit).all()

def get_item_evolutions(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ItemEvolutionMaster).offset(skip).limit(limit).all()

def get_item_limitbreak_exps(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ItemLimitbreakExpMaster).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(models.ItemMaster).filter(models.ItemMaster.id == item_id).first()
def get_items(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ItemMaster).offset(skip).limit(limit).all()
def get_items_by_name(db: Session, item_name: str, skip: int = 0, limit: int = 100):
    search = "%{}%".format(item_name)
    return db.query(models.ItemMaster).filter(models.ItemMaster.name.ilike(search)).limit(limit).all()



def get_item_recipes(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ItemRecipeMaster).offset(skip).limit(limit).all()

def get_keys(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.KeyMaster).offset(skip).limit(limit).all()

def get_limited_first_friends(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.LimitedFirstFriendMaster).offset(skip).limit(limit).all()

def get_link_skills(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.LinkSkillMaster).offset(skip).limit(limit).all()

def get_loginbonus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LoginBonusMaster).order_by(models.LoginBonusMaster.start_at.desc()).offset(skip).limit(limit).all()

def get_login_bonus_totals(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.LoginBonusTotalMaster).offset(skip).limit(limit).all()

def get_materials(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.MaterialMaster).offset(skip).limit(limit).all()

def get_missions(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.MissionMaster).offset(skip).limit(limit).all()


def get_orb_shops(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.OrbShopMaster).offset(skip).limit(limit).all()

def get_player_exps(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.PlayerExpMaster).offset(skip).limit(limit).all()

def get_premium_logins(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.PremiumLoginMaster).offset(skip).limit(limit).all()

def get_premium_presents(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.PremiumPresentMaster).offset(skip).limit(limit).all()

def get_premium_purchaseds(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.PremiumPurchasedMaster).offset(skip).limit(limit).all()

def get_quest_launchers(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.QuestLauncherMaster).offset(skip).limit(limit).all()

def get_quests(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.QuestMaster).offset(skip).limit(limit).all()

def get_quest_mission_changers(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.QuestMissionChangeMaster).offset(skip).limit(limit).all()

def get_quest_missions(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.QuestMissionMaster).offset(skip).limit(limit).all()

def get_raid_animations(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidAnimationMaster).offset(skip).limit(limit).all()


def get_raid_boss_fields(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidBossFieldMaster).offset(skip).limit(limit).all()


def get_raid_bosss(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidBossMaster).offset(skip).limit(limit).all()

def get_raid_destroy_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidDestroyRewardMaster).offset(skip).limit(limit).all()


def get_raid_field_effects(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidFieldEffectMaster).offset(skip).limit(limit).all()

def get_raid_general_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidGeneralRewardMaster).offset(skip).limit(limit).all()

def get_raids(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidMaster).offset(skip).limit(limit).all()

def get_raid_tickets(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidTicketMaster).offset(skip).limit(limit).all()

def get_raid_total_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RaidTotalRewardMaster).offset(skip).limit(limit).all()

def get_random_login_bonuss(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RandomLoginBonusMaster).offset(skip).limit(limit).all()

def get_random_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RandomRewardMaster).offset(skip).limit(limit).all()

def get_reset_orb_shop_counts(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ResetOrbShopCountMaster).offset(skip).limit(limit).all()

def get_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.Reward).offset(skip).limit(limit).all()

def get_reward(db: Session, reward_id: int):
    return db.query(models.Reward).filter(models.Reward.id == reward_id).first()

def get_runes(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RuneMaster).offset(skip).limit(limit).all()

def get_rune_types(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.RuneTypeMaster).offset(skip).limit(limit).all()

def get_settings(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.t_setting_master).offset(skip).limit(limit).all()

def get_sharpen_exp_bonuss(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SharpenExpbonusMaster).offset(skip).limit(limit).all()

def get_sharpens(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SharpenMaster).offset(skip).limit(limit).all()

def get_shops(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ShopMaster).order_by(models.ShopMaster.start_at.desc()).offset(skip).limit(limit).all()

def get_shop_banner_groups(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ShopBannerGroupMaster).offset(skip).limit(limit).all()

def get_shop_banners(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ShopBannerMaster).offset(skip).limit(limit).all()

def get_shop_deck_sets(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ShopDeckSetMaster).offset(skip).limit(limit).all()


def get_shop_dias(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ShopDiaMaster).order_by(models.ShopMaster.start_at.desc()).offset(skip).limit(limit).all()


def get_skill(db: Session, skill_id: int):
    return db.query(models.SkillMaster).filter(models.SkillMaster.id == skill_id).first()
def get_skills(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SkillMaster).offset(skip).limit(limit).all()
def get_skills_by_name(db: Session, skill_name: str, skip: int = 0, limit: int = 100):
    search = "%{}%".format(skill_name)
    return db.query(models.SkillMaster).filter(models.SkillMaster.name.ilike(search)).limit(limit).all()



def get_skill_effects(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SkillEffectMaster).offset(skip).limit(limit).all()

def get_skill_relations(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SkillRelationMaster).offset(skip).limit(limit).all()


def get_skill_weights(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SkillWeightMaster).offset(skip).limit(limit).all()

def get_skill_groups(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SkillGroupMaster).offset(skip).limit(limit).all()

def get_skins(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SkinMaster).offset(skip).limit(limit).all()

def get_stamps(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.StampMaster).offset(skip).limit(limit).all()

def get_support_rewards(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.SupporterRewardMaster).offset(skip).limit(limit).all()

def get_tools(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.ToolMaster).offset(skip).limit(limit).all()

def get_unit_ability_exps(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.UnitAbilityExpMaster).offset(skip).limit(limit).all()

def get_unit_evolutions(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.UnitEvolutionMaster).offset(skip).limit(limit).all()

def get_unit_exps(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.UnitExpMaster).offset(skip).limit(limit).all()

def get_unit_limitbreak_exps(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.UnitLimitbreakExpMaster).offset(skip).limit(limit).all()

def get_unit_limitbreaks(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.UnitLimitbreakMaster).offset(skip).limit(limit).all()


def get_unit(db: Session, unit_id: int):
    return db.query(models.UnitMaster).filter(models.UnitMaster.id == unit_id).first()
def get_units(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.UnitMaster).offset(skip).limit(limit).all()
def get_units_by_name(db: Session, unit_name: str, skip: int = 0, limit: int = 100):
    search = "%{}%".format(unit_name)
    return db.query(models.UnitMaster).filter(models.UnitMaster.name.ilike(search)).limit(limit).all()


