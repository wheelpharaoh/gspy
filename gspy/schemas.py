from datetime import datetime

from typing import List, Optional, Any, Union, Type

from pydantic import BaseModel, Field, Json

# param: Union[Json, Any] = None # NULL
# startend: Union[datetime, str] = None
# description: str = None
# Union[dict, list, set, float, int, str, bytes]

class ArenaRankBase(BaseModel):
    rank_no: int
    arena_rank_name: str
    bgm_name: str
    background_name: Union[int, str]
    need_badge: int
    win_reward_group_list: Union[Json, dict, list, set, float, int, str, bytes]
    lose_reward_group_list: Union[Json, dict, list, set, float, int, str, bytes]
    win_count_min: int
    reward_group_list: Union[Json, dict, list, set, float, int, str, bytes]
    matching_threshold: int
    status: int
class ArenaRankMaster(ArenaRankBase):
    id: int

    class Config:
        orm_mode = True

class ArenaRankingRewardBase(BaseModel):
    ranking_reward_group: int
    ranking_min: int
    ranking_max: int
    reward_group_list: int
    reward_message_title: str
    reward_message_content: str
class ArenaRankingRewardMaster(ArenaRankingRewardBase):
    id: int

    class Config:
        orm_mode = True

class ArenaRewardBase(BaseModel):
    reward_type: int
    reward_id: int
    reward_value: int
    reward_custom_parameter: Union[Json, Any] = None
class ArenaRewardMaster(ArenaRewardBase):
    id: int

    class Config:
        orm_mode = True

class ArenaShopBase(BaseModel):
    name: str
    need_type: int
    need_num: int
    object_type: int
    object_id: int
    value: int
    custom_parameter: Union[Json, Any] = None # NULL
    max_purchase_value: int
    purchase_reset_type: int
    description: str
    status: int
    priority: int
    start_at: datetime
    end_at: datetime
class ArenaShopMaster(ArenaShopBase):
    id: int

    class Config:
        orm_mode = True

class BattleRelationBase(BaseModel):
    quest_id: int
    battle_no: int
    weight: int
    bgm_name: Optional[str] = None
    background_name: Union[int, str] = None
    battlemaster_id: int
    field_setting_id: Union[int, str]

    quest: Any
class BattleRelationMaster(BattleRelationBase):
    id: int

    class Config:
        orm_mode = True

class ChallengeBase(BaseModel):
    group_id: int
    group_no: int
    reset_interval: int
    challenge_type: int
    challenge_ids: Union[Json, dict, List[int], List[str], int, None] = None
    challenge_value: int
    name: str
    description: str
    present1_type: Union[int, str]
    present1_id: Union[int, str]
    present1_value: Union[int, str]
    present1_custom_param: Union[Json, Any] = None # NULL
    present2_type: Union[int, str]
    present2_id: Union[int, str]
    present2_value: Union[int, str]
    present2_custom_param: Union[Json, Any] = None # NULL
    present3_type: Union[int, str]
    present3_id: Union[int, str]
    present3_value: Union[int, str]
    present3_custom_param: Union[Json, Any] = None # NULL
    present4_type: Union[int, str]
    present4_id: Union[int, str]
    present4_value: Union[int, str]
    present4_custom_param: Union[Json, Any] = None # NULL
    present5_type: Union[int, str]
    present5_id: Union[int, str]
    present5_value: Union[int, str]
    present5_custom_param: Union[Json, Any] = None # NULL
    init_unlock: int
    pri: int
    challenge_event_id: Union[int, str] = None
class ChallengeMaster(ChallengeBase):
    id: int

    class Config:
        orm_mode = True

class ChallengeEventBase(BaseModel):
    name: str
    start_at: datetime
    end_at: datetime
class ChallengeEventMaster(ChallengeEventBase):
    id: int

    class Config:
        orm_mode = True

class ChallengeRewardBase(BaseModel):
    challenge_id: int
    no: int
    present1_type: int
    present1_id: int
    present1_value: int
    present1_custom_parameter: Union[Json, Any] = None # NULL
    present2_type: Union[int, str]
    present2_id: Union[int, str]
    present2_value: Union[int, str]
    present2_custom_parameter: Union[Json, Any] = None # NULL
    present3_type: Union[int, str]
    present3_id: Union[int, str]
    present3_value: Union[int, str]
    present3_custom_parameter: Union[Json, Any] = None # NULL
    present4_type: Union[int, str]
    present4_id: Union[int, str]
    present4_value: Union[int, str]
    present4_custom_parameter: Union[Json, Any] = None # NULL
    present5_type: Union[int, str]
    present5_id: Union[int, str]
    present5_value: Union[int, str]
    present5_custom_parameter: Union[Json, Any] = None # NULL

    challenge: Any
class ChallengeRewardMaster(ChallengeRewardBase):
    id: int

    class Config:
        orm_mode = True

class CommonUnlockBase(BaseModel):
    unlock_object_type: int
    unlock_object_master_id: int
    unlock_type1: int
    unlock_id1: int
    unlock_type2: int
    unlock_id2: int
    unlock_type3: int
    unlock_id3: int
    unlock_type4: int
    unlock_id4: int
    unlock_type5: int
    unlock_id5: int
    name: Union[int, str]
    effect_position_x: int
    effect_position_y: int
class CommonUnlockMaster(CommonUnlockBase):
    id: int

    class Config:
        orm_mode = True

class CommonStringBase(BaseModel):
    text_key: str
    japanese_value: str
    english_value: str
    chinese_value: str
    french_value: str
class CommonstringMaster(CommonStringBase):
    id: int

    class Config:
        orm_mode = True

class CookingRecipeBase(BaseModel):
    name: str
    created_food_id: int
    success_rate: int
    material_1_type: int
    material_1_id: int
    material_1_value: Union[int, str]
    material_2_type: Union[int, str]
    material_2_id: Union[int, str]
    material_2_value: Union[int, str]
    material_3_type: Union[int, str]
    material_3_id: Union[int, str]
    material_3_value: Union[int, str]
    material_4_type: Union[int, str]
    material_4_id: Union[int, str]
    material_4_value: Union[int, str]
    material_5_type: Union[int, str]
    material_5_id: Union[int, str]
    material_5_value: Union[int, str]
    need_coin: int
    description: str
    exp_id: int

    food: Any
    material1: Any
class CookingRecipeMaster(CookingRecipeBase):
    id: int

    class Config:
        orm_mode = True

class DungeonLauncherBase(BaseModel):
    dungeon_id: int
    start_at: datetime
    end_at: datetime

    dungeon: Any
class DungeonLauncherMaster(DungeonLauncherBase):
    id: int

    class Config:
        orm_mode = True

class DungeonBase(BaseModel):
    map_id: int 
    name: str 
    dungeon_type: int 
    dungeon_no: int 
    page_no: int 
    desc_before_clear: Union[int, str] 
    desc_after_clear: Union[int, str] 
    icon_position_x: int 
    icon_position_y: int 
    background_name: int 
    event_id: int 
    status: int 
    title_pos_y: int 
    clear_pos_y: int 
    priority: int 
    stock: int 
    count_timing: int 
    reset_interval: int 
    need_rank: int 
    tab_type: int 
    drop_up_type: Union[int, Any] = None
    drop_up_id: Union[int, Any] = None
    drop_up_unit_dict: Union[dict, Json, int] = None # NULL 
    drop_up_item_dict: Union[dict, Json, List, str] = None # NULL 
    questlist_image_path: str = None 
    view_type: int

    event: Union[Json, dict, int, str, Any] = None
    #enemies: Any
    quests: Any
class DungeonMaster(DungeonBase):
    id: int

    class Config:
        orm_mode = True

class EnemyBase(BaseModel):
    unit_id: int
    level: int
    hp: int
    attack: int
    deffence: int
    skill1_damage_value: Union[int, str]
    skill2_damage_value: Union[int, str]
    full_skill_damage_value: int
    break_capacity: int
    break_power: int
    resistant_poison_base: int
    resistant_poison_max: int
    resistant_poison_rise_count: int
    resistant_darkness_base: int
    resistant_darkness_max: int
    resistant_darkness_rise_count: int
    resistant_silent_base: int
    resistant_silent_max: int
    resistant_silent_rise_count: int
    resistant_paralyze_base: int
    resistant_paralyze_max: int
    resistant_paralyze_rise_count: int
    resistant_injury_base: int
    resistant_injury_max: int
    resistant_injury_rise_count: int
    resistant_sickness_base: int
    resistant_sickness_max: int
    resistant_sickness_rise_count: int
    resistant_stun_base: int
    resistant_stun_max: int
    resistant_stun_rise_count: int
    resistant_freeze_base: int
    resistant_freeze_max: int
    resistant_freeze_rise_count: int
    resistant_burn_base: int
    resistant_burn_stun_max: int
    resistant_burn_stun_rise_count: int
    skill_invocation_weight: int
    need_sp: int
    damage_drop_sp: int
    drop_sp: int
    drop_coin: int
    drop_user_exp: int
    drop_unit_exp: int
    weight: int
    size: int
    is_boss: int
    first_clear_drop_id: int
    name: Optional[str]
    chargearts_skill_id: int
    chargearts_skill_id2: int
    full_chargearts_skill_id: int
    is_lua: int
    
    unit: Any
    skills: Any
class EnemyMaster(EnemyBase):
    id: int

    class Config:
        orm_mode = True

class EventInfoBase(BaseModel):
    view_type: int
    memo: str
    action_type: Union[int, str]
    action_param: Union[Json, dict, int, str] = None # NULL
    view_image: str
    label_image: Union[str, Any] = None # NULL 
    pos_x: int
    pos_y: int
    param: Union[Json, dict, Any] = None # NULL 
    priority: int
    start_at: datetime
    end_at: datetime
    view_start_day: int
    view_end_day: int
    status: int

    banner: Any
    event: Any
class EventInfoMaster(EventInfoBase):
    id: int

    class Config:
        orm_mode = True

class EventItemBase(BaseModel):
    event_id:  int
    name: str
    rarity:  int
    limit_value:  int

    event: Any
class EventItemMaster(EventItemBase):
    id: int

    class Config:
        orm_mode = True

class EventBase(BaseModel):
    type: int
    name: Optional[str]
    param: Union[Json, int, str] = None # NULL
    description: str = None
    start_at: Union[datetime, Any] = None
    end_at: Union[datetime, Any] = None
    item_start_at: Union[datetime, Any] = None
    item_end_at: Union[datetime, Any] = None
    event_shop_type: int
    status: int

    dungeon: Any
    banner: Any
class EventMaster(EventBase):
    id: int

    class Config:
        orm_mode = True

class EventShopBase(BaseModel):
    name: str = None
    event_id: int = None
    need_item_id: int = None
    need_count: int = None
    object_type: int = None
    object_id: int = None
    value: int = None
    max_set_value: int = None
    max_purchase_value: int = None
    custom_parameter: Union[Json, dict, Any] = None # NULL
    description: str = None
    status: int
    priority: int = None

    event: Any
    need_item: Any
    item: Any
class EventShopMaster(EventShopBase):
    id: int

    class Config:
        orm_mode = True

class FarmBase(BaseModel):
    farm_point_id: int
    level: int
    gain_at: int
    max_gain_count: int
class FarmMaster(FarmBase):
    id: int

    class Config:
        orm_mode = True

class FieldSettingBase(BaseModel):
    name: str = None
    description: str = None
    effect_name: Optional[str]
    field_effect_lua_id: Optional[int]
    field_skill_effect_custom_parameter: Union[Json, Any] = None # NULL
    popup_title_image_name: str = None
class FieldSettingMaster(FieldSettingBase):
    id: int

    class Config:
        orm_mode = True

class FoodBoostBase(BaseModel):
    created_food_id: int
    food_1_id: int
    food_2_id: int
    food_3_id: int
    food_4_id: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None

    food: Any
class FoodBoostMaster(FoodBoostBase):
    id: int

    class Config:
        orm_mode = True

class FoodEffectBase(BaseModel):
    effect_type: int
    target: int
    effect_value: int
    description: str
class FoodEffectMaster(FoodEffectBase):
    id: int

    class Config:
        orm_mode = True

class FoodBase(BaseModel):
    album_id: int
    name: str
    rarity: int
    food_type: int
    food_effect_id1: int
    food_effect_id2: Union[int, str] = None
    food_effect_id3: Union[int, str] = None
    food_effect_id4: Union[int, str] = None
    food_effect_id5: Union[int, str] = None
    coin: int
    description: str = None
    summary: str
    non_sale: int

    food_effect1: Any
class FoodMaster(FoodBase):
    id: int

    class Config:
        orm_mode = True

class FriendMultiBase(BaseModel):
    step: int
    multi_count: int
    reward_ids: int
class FriendMultiMaster(FriendMultiBase):
    id: int

    class Config:
        orm_mode = True

class GachaButtonBase(BaseModel):
    lowest_rarity_stock: int
    button_image: str
class GachaButtonMaster(GachaButtonBase):
    id: int

    class Config:
        orm_mode = True

class GachaBase(BaseModel):
    gacha_button_id1: int
    gacha_button_id2: int
    gacha_button_id3: int
    gacha_type: int
    gacha_system_type: int
    bg_name: str
    bg_name_last: str = None
    param: Union[Json, dict, List, str, Any] = None # NULL
    start_at: datetime
    end_at: datetime
    link_token_id: int

    gacha_button1: Any
class GachaMaster(GachaBase):
    id: int

    class Config:
        orm_mode = True

class GachaPointBase(BaseModel):
    name: str
    description: str
    count_limit: int
    reset_type: int
class GachaPointMaster(GachaPointBase):
    id: int

    class Config:
        orm_mode = True

class GachaStepUpBase(BaseModel):
    gacha_id: int
    step_no: int
    gacha_button_id: int
    param: Union[Json, Any] = None # NULL

    gacha: Any
    gacha_button: Any
class GachaStepUpMaster(GachaStepUpBase):
    id: int

    class Config:
        orm_mode = True

class ItemEvolutionBase(BaseModel):
    base_item_id: int
    next_item_id: int
    material_1_type: int
    material_1_item_id: int
    material_1_item_value: int
    material_2_type: int
    material_2_item_id: int
    material_2_item_value: int
    material_3_type: int
    material_3_item_id: int
    material_3_item_value: int
    material_4_type: int
    material_4_item_id: int
    material_4_item_value: int
    material_5_type: int
    material_5_item_id: int
    material_5_item_value: int
    key_material_item_id: int
    key_material_item_value: int
    need_coin: int

    base_item: Any
    next_item: Any
    material1: Any
class ItemEvolutionMaster(ItemEvolutionBase):
    id: int

    class Config:
        orm_mode = True

class ItemLimitBreakExpBase(BaseModel):
    exp_id: int
    level: int
    exp: int
class ItemLimitbreakExpMaster(ItemLimitBreakExpBase):
    id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    base_item_id: int
    album_id: int
    name: str
    short_name: str
    type: int
    image_id: int
    rarity: int
    is_material: int
    evolution_stage: int
    hitpoint: int
    offence: int
    defence: int
    item_skill_id: int
    coin: int
    orb: int
    size: int
    max_limitbreak_cooltime: int
    min_limitbreak_cooltime: int
    limit_break_exp_id: int
    for_limit_break_exp: int
    description: str = None
    drop_information: Union[int, str] = None
    non_deletable: int

    skill: Any
    #effects: Any
class ItemMaster(ItemBase):
    id: int

    class Config:
        orm_mode = True

class ItemRecipeBase(BaseModel):
    name: str
    created_item_id: int = None
    material_1_type: Union[int, str] = None
    material_1_item_id: Union[int, str] = None
    material_1_item_value: Union[int, str] = None
    material_2_type: Union[int, str] = None
    material_2_item_id: Union[int, str] = None
    material_2_item_value: Union[int, str] = None
    material_3_type: Union[int, str] = None
    material_3_item_id: Union[int, str] = None
    material_3_item_value: Union[int, str] = None
    material_4_type: Union[int, str] = None
    material_4_item_id: Union[int, str] = None
    material_4_item_value: Union[int, str] = None
    material_5_type: Union[int, str] = None
    material_5_item_id: Union[int, str] = None
    material_5_item_value: Union[int, str] = None
    need_coin: int = None
    description: str = None

    created_item: Any
    material1: Any
class ItemRecipeMaster(ItemRecipeBase):
    id: int

    class Config:
        orm_mode = True

class KeyBase(BaseModel):
    type: int
    name: str
    description: str
    priority: int
    first_visible: int
    tab_no: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    count_limit: int
    effect_time: int
class KeyMaster(KeyBase):
    id: int

    class Config:
        orm_mode = True

class LimitedFirstFriendBase(BaseModel):
    base_id: int
    stage: int
    friend_total_count: int
    friend_total_login: int
    reward_id: int
    title: str
    content: str
    is_end: int
    status: int
    start_at: datetime = None
    end_at: datetime = None

    reward: Any
class LimitedFirstFriendMaster(LimitedFirstFriendBase):
    id: int

    class Config:
        orm_mode = True

class LinkSkillBase(BaseModel):
    base_unit_1_id: int
    base_unit_2_id: int
    base_unit_1_cutin_direction: int
    base_unit_2_cutin_direction: int
    skill_1_id: int
    skill_2_id: int
    skill_name: str
    description: str
class LinkSkillMaster(LinkSkillBase):
    id: int

    class Config:
        orm_mode = True

class LoginBonusBase(BaseModel):
    message_title: str
    message_content: str
    #daily_reward_id_list: List[int]
    daily_reward_id_list: Any
    #daily_reward_id_list: Union[dict, list, set, float, int, str, bytes]
    termview_flag: int
    infinite_flag: int
    start_at: datetime
    end_at: datetime
    priority: int

    #rewards: Any
    #reward: Any
class LoginBonusMaster(LoginBonusBase):
    id: int

    class Config:
        orm_mode = True

class LoginBonusTotalBase(BaseModel):
    day: int
    message_title: str
    message_content: str
    reward_id: int
    popup_text: str = None

    reward: Any
class LoginBonusTotalMaster(LoginBonusTotalBase):
    id: int

    class Config:
        orm_mode = True

class MaterialBase(BaseModel):
    album_id: int
    name: str
    type: int
    rarity: int
    description: str
    drop_information: str = None
    drop_information_id_info: Union[Json, dict, int]
class MaterialMaster(MaterialBase):
    id: int

    class Config:
        orm_mode = True

class MissionBase(BaseModel):
    name: str
    difficulty: int
    requirement_type: int
    requirement_value_1: int
    requirement_value_2: int
    requirement_description: str
    description: str
    present_type: int
    present_id: int
    present_value: int
    custam_parameter: Union[Json, Any] = None # NULL
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    status: int
    story: int
class MissionMaster(MissionBase):
    id: int

    class Config:
        orm_mode = True

class OrbShopBase(BaseModel):
    shop_type: int
    name: str
    need_type1: int
    need_id1: int
    need_value1: int
    need_type2: int
    need_id2: int
    need_value2: int
    need_type3: int
    need_id3: int
    need_value3: int
    need_type4: int
    need_id4: int
    need_value4: int
    need_type5: int
    need_id5: int
    need_value5: int
    object_type: int
    object_id: int
    value: int
    max_set_value: int
    max_purchase_value: int
    reset_type: int
    custam_parameter: Union[Json, Any] = None # NULL
    description: str = None
    status: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    priority: int
    is_time_display: int

    item: Any
class OrbShopMaster(OrbShopBase):
    id: int

    class Config:
        orm_mode = True

class PlayerExpBase(BaseModel):
    rank: int
    exp: int
    max_stam: int
    max_party: int
    max_friend: int
class PlayerExpMaster(PlayerExpBase):
    id: int

    class Config:
        orm_mode = True

class PremiumLoginBase(BaseModel):
    shopdia_id: int
    present_type: int
    present_id: int
    present_value: int
    present_custam_parameter: Union[Json, Any] = None # NULL
    title: str
    content: str
class PremiumLoginMaster(PremiumLoginBase):
    id: int

    class Config:
        orm_mode = True

class PremiumPresentBase(BaseModel):
    shopdia_id: int
    present_type: int
    present_id: int
    present_value: int
    present_custam_parameter: Union[Json, Any] = None # NULL
class PremiumPresentMaster(PremiumPresentBase):
    id: int

    class Config:
        orm_mode = True

class PremiumPurchaseBase(BaseModel):
    shopdia_id: int
    type: int
    value: int
class PremiumPurchasedMaster(PremiumPurchaseBase):
    id: int

    class Config:
        orm_mode = True

class QuestLauncherBase(BaseModel):
    quest_id: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    image: str
    dungeon_image: str
    quest_name: str
    quest_description: str
class QuestLauncherMaster(QuestLauncherBase):
    id: int

    class Config:
        orm_mode = True

class QuestBase(BaseModel):
    quest_type: int
    map_id: int
    dungeon_id: int
    quest_no: int
    fortune_drop_id: int
    next_quest_ids: Optional[int] = None
    init_unlock: int
    continue_flag: int
    name: str
    description: str
    stamina: int
    difficulty: int
    drop_coin: int
    drop_user_exp: int
    drop_unit_exp: int
    status: int
    questmission1_id: int
    questmission1_reward_type: int
    questmission1_reward_id: Union[int, str]
    questmission1_reward_value: int
    custam_parameter1: Union[Json, dict, str, None] = None # NULL
    questmission2_id: int
    questmission2_reward_type: int
    questmission2_reward_id: int
    questmission2_reward_value: int
    custam_parameter2: Union[Json, dict, str, None] = None # NULL
    questmission3_id: int
    questmission3_reward_type: int
    questmission3_reward_id: int
    questmission3_reward_value: int
    custam_parameter3: Union[Json, dict, str, None] = None # NULL
    complete_reward_type: int
    complete_reward_id: Union[int, str]
    complete_reward_value: int
    complete_custam_parameter: Union[Json, dict, str, None] = None # NULL
    is_first_clear_drop: int
    is_different_drop: int
    is_multi: int
    need_rank: int
    stock: int
    count_timing: int
    reset_interval: int
    key_id: Union[int, str]
    key_value: Union[int, str]
    not_same_unit: int
    drop_up_base_unit_ids: Union[int, None] = None # NULL
    drop_ability_exp: int
    is_view_party: int
    element_list: str = None
    race_list: str = None
    is_lua: int
    rune_drop_type_id: Union[int, str]
    sharpen_exp: int

    dungeon: Any
    next_quest: Any
    key: Any
    drop_up_unit: Any
    rune_drop_type: Any
    #questmission1_reward: Any
class QuestMaster(QuestBase):
    id: int

    class Config:
        orm_mode = True

class QuestMissionChangerBase(BaseModel):
    quest_id: int
    questmission1_id: int
    questmission1_reward_type: int
    questmission1_reward_id: Union[int, str] = None
    questmission1_reward_value: int
    custam_parameter1: Union[Json, Any] = None # NULL
    questmission2_id: int
    questmission2_reward_type: int
    questmission2_reward_id: int
    questmission2_reward_value: int
    custam_parameter2: Union[Json, Any] = None # NULL
    questmission3_id: int
    questmission3_reward_type: int
    questmission3_reward_id: int
    questmission3_reward_value: int
    custam_parameter3: Union[Json, Any] = None # NULL
    complete_reward_type: int
    complete_reward_id: Union[int, str] = None
    complete_reward_value: int
    complete_custam_parameter: Union[Json, Any] = None # NULL
class QuestMissionChangeMaster(QuestMissionChangerBase):
    id: int

    class Config:
        orm_mode = True

class QuestMissionBase(BaseModel):
    type: int
    value: int
    value_list: Union[List[int], List[str], str] = None
class QuestMissionMaster(QuestMissionBase):
    id: int

    class Config:
        orm_mode = True

class RaidBase(BaseModel):
    id: int
    name: str
    boss_master_ids: Union[int, List, str]
    event_id: int
    drop_up_base_unit_ids: Union[Json, dict] = None # NULL
    raid_start_at: Union[datetime, str] = None
    battle_start_at: Union[datetime, str] = None
    battle_end_at: Union[datetime, str] = None
    raid_end_at: Union[datetime, str] = None
    destroy_view_start_at: Union[datetime, str] = None
    destroy_view_end_at: Union[datetime, str] = None
    damage_raid_view_start_at: Union[datetime, str] = None
    damage_raid_view_end_at: Union[datetime, str] = None

    event: Any
class RaidMaster(RaidBase):
    id: int

    class Config:
        orm_mode = True

class RaidAnimationBase(BaseModel):
    start_animation_name: str
    start_animation_type: str
    end_animation_name: str
    end_animation_type: str
    end_text: str
class RaidAnimationMaster(RaidAnimationBase):
    id: int

    class Config:
        orm_mode = True

class RaidBossBase(BaseModel):
    enemy_id: int
    difficulty: int
    bgm_name: str
    image_id: int
    raid_animation_id: int
    ticket_num: int
    ticket_id: int
    limit_time_num: int
    break_time_num: int
    max_member: int
    gain_unit_exp: int
    max_gain_unit_exp: int
    gain_user_exp: int
    max_gain_user_exp: int
    gain_coin: int
    max_gain_coin: int
    point_magnification: int
    background_name: str = None
    break_reward_num1: int
    break_reward_num2: int
    is_total_destroy_count: int
    raid_type: int
    battle_max_count: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    field_setting_id: Union[int, str] = None

    enemy: Any
    raid_animation: Any
    ticket: Any
class RaidBossMaster(RaidBossBase):
    id: int

    class Config:
        orm_mode = True

class RaidDestroyRewardBase(BaseModel):
    raid_id: int
    conditions_type: int
    conditions_value: int
    reward_id_list: Union[List, int, str, None]
    priority: int

    raid: Any
    reward: Any
class RaidDestroyRewardMaster(RaidDestroyRewardBase):
    id: int

    class Config:
        orm_mode = True

class RaidBossFieldBase(BaseModel):
    name: str
    effect_1: int
    effect_2: int
    bg_name: str
    background_name: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
class RaidBossFieldMaster(RaidBossFieldBase):
    id: int

    class Config:
        orm_mode = True

class RaidFieldEffectBase(BaseModel):
    skill_type: str
    target: int
    effect_value: int
    script_id: int
    value_1: int
    value_2: int
    value_3: int
    description: str
class RaidFieldEffectMaster(RaidFieldEffectBase):
    id: int

    class Config:
        orm_mode = True

class RaidGeneralRewardBase(BaseModel):
    raid_id: int
    raid_type: int
    reward_id_list: Union[List[str], str]
    num: int
    message_content: str
class RaidGeneralRewardMaster(RaidGeneralRewardBase):
    id: int

    class Config:
        orm_mode = True

class RaidTicketBase(BaseModel):
    name: str
    description: str
    priority: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    count_limit: int
    effect_time: Union[int, str] = None
class RaidTicketMaster(RaidTicketBase):
    id: int

    class Config:
        orm_mode = True

class RaidTotalRewardBase(BaseModel):
    raid_id: int
    reward_id: int
    destroy_num: int
    explain_text: str
    reward_message_title: str
    reward_message_content: str
class RaidTotalRewardMaster(RaidTotalRewardBase):
    id: int

    class Config:
        orm_mode = True

class RandomLoginBonusMasterBase(BaseModel):
    name: str
    type: int
    reward_id_list: Union[List[int], List[str]] = None
    last_reward_id: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    receive_grace: int
class RandomLoginBonusMaster(RandomLoginBonusMasterBase):
    id: int

    class Config:
        orm_mode = True

class RandomRewardMasterBase(BaseModel):
    message_title: Optional[str]
    message_content: Optional[str]
    reward_type: int
    reward_id: int
    reward_value: int
    reward_custom_parameter: Union[Json, Any] = None # NULL
class RandomRewardMaster(RandomRewardMasterBase):
    id: int

    class Config:
        orm_mode = True

class ResetOrbShopCountMasterBase(BaseModel):
    reset_orb_shop_ids: str
    start_at: int
class ResetOrbShopCountMaster(ResetOrbShopCountMasterBase):
    id: int

    class Config:
        orm_mode = True

class RewardBase(BaseModel):
    receive_grace: Union[int, str]
    present_type: int
    present_id: Union[int, str] # str-None
    present_value: int
    present_custom_parameter: Union[Json, Any] = None # NULL
    box_rarity: Union[int, str] = None
class Reward(RewardBase):
    id: int

    class Config:
        orm_mode = True

class RuneMasterBase(BaseModel):
    name: str
    type_id: int
    level: int
    is_plus: int
    skill_id: int
    level_up_value: int
    equipment_value: int
    change_value: int
    limit_value: int
    image: Optional[str]
    spine_animation_name: Optional[str]

    type: Any
    skill: Any
class RuneMaster(RuneMasterBase):
    id: int

    class Config:
        orm_mode = True

class RuneTypeMasterBase(BaseModel):
    name: str
    is_tool_drop: int
    is_limited: Union[int, str]
class RuneTypeMaster(RuneTypeMasterBase):
    id: int

    class Config:
        orm_mode = True

class SettingMasterBase(BaseModel):
    value: str
    description: str
class t_setting_master(SettingMasterBase):
    key: str

    class Config:
        orm_mode = True

class SharpenExpbonusMasterBase(BaseModel):
    bonus_type: int
    rate_bonus_value: int
    fix_bonus_value: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    quest_ids: Optional[str]
    item_ids: Optional[str]
    display_text: str
class SharpenExpbonusMaster(SharpenExpbonusMasterBase):
    id: int

    class Config:
        orm_mode = True

class SharpenMasterBase(BaseModel):
    base_item_id: int
    sharpen_exp_max: int
    status_sum_min: int
    status_sum_max: int
    skill_num_0_weight: int
    skill_num_1_weight: int
    skill_num_2_weight: int
    skill_num_3_weight: int
    skill_1_group: int
    skill_2_group: int
    skill_3_group: int
    detail_text: str

    base_item: Any
    skill1_group: Any
    skill2_group: Any
    skill3_group: Any
class SharpenMaster(SharpenMasterBase):
    id: int

    class Config:
        orm_mode = True

class ShopBannerGroupMasterBase(BaseModel):
    title_image_path: Optional[str]
    title_text: str
    priority: int
class ShopBannerGroupMaster(ShopBannerGroupMasterBase):
    id: int

    class Config:
        orm_mode = True

class ShopBannerMasterBase(BaseModel):
    shop_type: Union[int, str]
    event_id: Union[int, str]
    bg_name: str
    description_text: Optional[str]
    priority: int
    consume_image: Optional[str]
    consume_type: int
    consume_id: int
    popup_type: int

    event: Any
class ShopBannerMaster(ShopBannerMasterBase):
    id: int

    class Config:
        orm_mode = True

class ShopDeckSetMasterBase(BaseModel):
    unit1_id: int
    unit1_custom_parameter: Union[Json, Any] = None # NULL
    unit1_item1: int
    unit1_item1_limitbreak: int
    unit1_item2: int
    unit1_item2_limitbreak: int
    unit1_item3: int
    unit1_item3_limitbreak: int
    unit2_id: int
    unit2_custom_parameter: Union[Json, Any] = None # NULL
    unit2_item1: int
    unit2_item1_limitbreak: int
    unit2_item2: int
    unit2_item2_limitbreak: int
    unit2_item3: int
    unit2_item3_limitbreak: int
    unit3_id: int
    unit3_custom_parameter: Union[Json, Any] = None # NULL
    unit3_item1: int
    unit3_item1_limitbreak: int
    unit3_item2: int
    unit3_item2_limitbreak: int
    unit3_item3: int
    unit3_item3_limitbreak: int
    unit4_id: int
    unit4_custom_parameter: Union[Json, Any] = None # NULL
    unit4_item1: int
    unit4_item1_limitbreak: int
    unit4_item2: int
    unit4_item2_limitbreak: int
    unit4_item3: int
    unit4_item3_limitbreak: int
class ShopDeckSetMaster(ShopDeckSetMasterBase):
    id: int

    class Config:
        orm_mode = True

class ShopDiaMasterBase(BaseModel):
    os_type: int
    name: str
    value: int
    value_free: int
    price: float
    product_id: str
    product_type: int
    description: Union[int, str]
    status: int
    purchase_limit: int
    message_title: Optional[str]
    message_content: Optional[str]
    bonus_id_list: Union[List, dict, Json, str, None]
    bonus_id_list_rand: Union[List, dict, Json, str, None]
    sale_flag: int
    sale_display_count: int
    sale_image_path: Optional[str]
    sale_priority: int
    base_shop_id: int
    token_id: int
    pri: int
    group_id: int
    banner_group_id: int
    premium_days: Union[int, str] = None
    premium_purchased_days: Union[int, str] = None
    premium_popup_title: Optional[str]
    banner_image: Optional[str]
    description_image: Optional[str]
    description_image_rect1: Optional[str]
    description_image_url1: Optional[str]
    url1_action_type: int
    description_image_rect2: Optional[str]
    description_image_url2: Optional[str]
    url2_action_type: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
    webview_content: Optional[str]
    webview_attention: Optional[str]
    shop_deck_id: Union[int, str] = None

    banner_group: Any
class ShopDiaMaster(ShopDiaMasterBase):
    id: int

    class Config:
        orm_mode = True

class ShopMasterBase(BaseModel):
    name: str
    sale_type: int
    product_type: int
    object_id: int
    value: int
    price: int
    description: str
    status: int
    priority: int
    start_at: Union[datetime, str] = None
    end_at: Union[datetime, str] = None
class ShopMaster(ShopMasterBase):
    id: int

    class Config:
        orm_mode = True

class SkillEffectMasterBase(BaseModel):
    name: Optional[str]
    effect_type: int
    skill_id: int
    target: int
    effect_time: Union[int, str]
    effect_value: int
    mine_eff_val_threshold: int
    mine_eff_val_function1: Union[int, str]
    mine_eff_val_function2: Union[int, str]
    effect_min: Union[int, str]
    effect_max: Union[int, str]
    weight: Union[int, str]
    buff_type: int
    script_id: Union[int, str]
    script_value_1: Union[int, str]
    script_value_2: Union[int, str]
    script_value_3: Union[int, str]
    script_value_4: Union[int, str]
    script_value_5: Union[int, str]
    tumbnail_name: Optional[str]
    text_image_no: Union[int, str]
    animation_id: Union[int, str]
    group_id: Union[int, str]
    priority: Union[int, str]

    skill: Any
    group: Any
class SkillEffectMaster(SkillEffectMasterBase):
    id: int

    class Config:
        orm_mode = True

class SkillMasterBase(BaseModel):
    name: str
    skill_type: int
    skill_group_id: int
    priority: int
    damage_value: int
    break_value: int
    range_y: int
    element: int
    attribute: Union[int, str]
    need_sp: Union[int, str]
    cooltime: Union[int, str]
    cooltime_max: Union[int, str]
    animation_id: Union[int, str]
    description: Optional[str]
    summary: Optional[str]
    tumbnail_name1: Optional[str]
    tumbnail_name2: Optional[str]
    ai_id: int
    ai_id2: int
    ai_id3: int
    battle_summary: Union[int, str] = None
    unit_exp_value: Union[int, str, None] = None
    user_exp_value: Union[int, str, None] = None
    coin_up_value: Union[int, str, None] = None

    skill_group: Any
    effects: Any
class SkillMaster(SkillMasterBase):
    id: int

    class Config:
        orm_mode = True

class SkillRelationMasterBase(BaseModel):
    relation_type: int
    relation_id: int
    skill_id: int
    need_level: int

    #enemy: Any
    skill: Any
class SkillRelationMaster(SkillRelationMasterBase):
    id: int

    class Config:
        orm_mode = True

class SkillWeightMasterBase(BaseModel):
    skill_id: int
    group_no: int

    skill: Any
class SkillWeightMaster(SkillWeightMasterBase):
    id: int

    class Config:
        orm_mode = True

class SkillGroupMasterBase(BaseModel):
    name: str
    description: Optional[str]
class SkillGroupMaster(SkillGroupMasterBase):
    id: int

    class Config:
        orm_mode = True

class SkinMasterBase(BaseModel):
    name: str
    description: str
    base_unit_id: int
    skin_no: int
    min_rarity: int
class SkinMaster(SkinMasterBase):
    id: int

    class Config:
        orm_mode = True

class StampBase(BaseModel):
    shop_id: int
    set_no: int
    name: str
    image_name: str
    description: str
class StampMaster(StampBase):
    id: int

    class Config:
        orm_mode = True

class SupporterRewardBase(BaseModel):
    mine_id: int
    no: int
    name: str
    description: str
    clear_value: int
    present_type: int
    present_id: int
    present_value: int
    present_custom_parameter: Union[Json, Any] = None # NULL
class SupporterRewardMaster(SupporterRewardBase):
    id: int

    class Config:
        orm_mode = True

class ToolBase(BaseModel):
    name: str
    description: str
    type: int
    effect1: int
    effect1_type: int
    effect2: int
    effect2_type: int
    start_at: Union[datetime, str]
    end_at: Union[datetime, str]
    first_visible: int
    tab_no: int
    count_limit: int
    priority: int
    is_quest_item: int
class ToolMaster(ToolBase):
    id: int

    class Config:
        orm_mode = True

class UnitAbilityExpBase(BaseModel):
    exp_id: int
    level: int
    exp: int
class UnitAbilityExpMaster(UnitAbilityExpBase):
    id: int

    class Config:
        orm_mode = True

class UnitEvolutionBase(BaseModel):
    base_unit_id: int
    next_unit_id: int
    material_1_type: int
    material_1_id: int
    material_1_value: int
    material_2_type: int
    material_2_id: int
    material_2_value: int
    material_3_type: int
    material_3_id: int
    material_3_value: Union[int, str]
    material_4_type: Union[int, str]
    material_4_id: Union[int, str]
    material_4_value: Union[int, str]
    material_5_type: Union[int, str]
    material_5_id: Union[int, str]
    material_5_value: Union[int, str]
    need_coin: int
    evolution_need_value: Union[int, str]
class UnitEvolutionMaster(UnitEvolutionBase):
    id: int

    class Config:
        orm_mode = True

class UnitExpBase(BaseModel):
    exp_id: int
    level: int
    exp: int
class UnitExpMaster(UnitExpBase):
    id: int

    class Config:
        orm_mode = True

class UnitLimitbreakExpBase(BaseModel):
    exp_id: int
    level: int
    exp: int
class UnitLimitbreakExpMaster(UnitLimitbreakExpBase):
    id: int

    class Config:
        orm_mode = True

class UnitLimitbreakBase(BaseModel):
    base_unit_id: int
    limit_break_level: int
    equipped1_type: int
    equipped1_rarity: int
    equipped2_type: int
    equipped2_rarity: int
    equipped3_type: int
    equipped3_rarity: int
    buff_fortune_level: int
    buff_hp: int
    buff_attack: int
    buff_defence: int
class UnitLimitbreakMaster(UnitLimitbreakBase):
    id: int

    class Config:
        orm_mode = True

class UnitBase(BaseModel):
    base_unit_id: int
    cue_sheet_name: Union[int, str]
    cue_sheet_system_name: Union[int, str] = None
    cue_name: Union[int, str] = None
    album_id: int
    name: str
    element: int
    race: int
    sexuality: int
    is_material: int
    exp_id: float
    limit_break_exp_id: float
    rarity: int
    evolution_stage: int
    level_max: float
    fortune_level_max: float
    hitpoint_base: int
    hitpoint_max: int
    offence_base: int
    offence_max: int
    defence_base: int
    defence_max: int
    attribute: int
    attack_delay: float
    range_min: int
    range_max: int
    range_y: int
    break_power: float
    break_capacity: float
    chargearts_skill_id: Union[int, str]
    chargearts_skill_id2: Union[int, str]
    full_chargearts_skill_id: Union[int, str]
    full_chargearts_skill_id2: Union[int, str]
    coin: int
    for_powerup_coin: int
    for_powerup_exp: int
    for_powerup_buff_hp: int
    for_powerup_buff_attack: int
    for_powerup_buff_defence: int
    for_limit_break_coin: int
    for_limit_break_exp: int
    for_limit_break_ability_exp: int
    orb: int
    description: Optional[str]
    comment_gain: Optional[str]
    comment_powerup: Optional[str]
    comment_evolution: Optional[str]
    comment_limitberak: Optional[str]
    comment_fortune_max: Optional[str]
    seiyu: Optional[str]
    image_pos_x: float
    image_pos_y: float
    image_scale: Union[int, float, str]
    is_boss: int
    non_deletable: int
    non_sellable: int
    is_lock: int
    drop_information: Union[str, int] = None
    is_limitbreak_ball: int
    ability_exp_id: float
    is_lua: int
    limited_id: int
    rune_num: Union[int, str]
    antialias_type: Union[int, str]

    limit_break: Any
    #mlb_hp: Any
    skill1: Optional[Any]
    skill2: Optional[Any]
    art: Optional[Any]
    trueart: Optional[Any]
class UnitMaster(UnitBase):
    id: int

    class Config:
        orm_mode = True




class Schedule(BaseModel):
    '''A model for everything dropping on a particular day

    '''
    date_start: Any
    date_end: Any
    
    banner: Any
    challenges: Any
    enemies: Any
    equips: Any
    item_shop: Any
    quest: Any
    units: Any
    
    

