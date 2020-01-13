# https://stackoverflow.com/questions/35653889/sqlalchemy-property-mapping
# https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
# https://stackoverflow.com/questions/9729381/sqlalchemy-relationships-with-postgresql-array
# https://www.google.com/search?q=sqlalchemy+array+of+foreign+keys+site:stackoverflow.com&safe=off&sxsrf=ACYBGNTUUP5YmnzDhsJ0wl7ZIk1ZSh9C6g:1576811168035&sa=X&ved=2ahUKEwjjoLGsn8PmAhV1NX0KHZPNDQAQrQIoBDAAegQIARAN&biw=1440&bih=696
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends
# https://www.2ndquadrant.com/en/blog/postgresql-9-3-development-array-element-foreign-keys/
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html

from sqlalchemy import case, func, Column, DateTime, Float, ForeignKey, Integer, MetaData, Numeric, String, Table, Text
#from sqlalchemy.types import ARRAY
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import backref, mapper, relationship, remote, foreign, column_property

from .database import Base

import logging
logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logger = logging.getLogger(__name__)

metadata = MetaData()

class AlbumVoiceMaster(Base):
    __tablename__ = 'album_voice_master'

    id = Column(Integer, primary_key=True, index=True)
    base_unit_id = Column(Integer)
    album_name = Column(Text)
    cue_sheet_name = Column(Text)
    cue_name = Column(Text)
    rarity = Column(Integer)
    priority = Column(Integer)

class ArenaNpcMaster(Base):
    __tablename__ = 'arena_npc_master'

    id = Column(Numeric, primary_key=True, index=True)
    rank_no = Column(Integer)
    arena_rank_name = Column(Text)
    ranking = Column(Integer)
    nickname = Column(Text)
    profile = Column(Text)
    battle_count = Column(Integer)
    win_count = Column(Integer)
    lose_count = Column(Integer)
    win_streak_count = Column(Integer)
    badge = Column(Integer)
    masters_battle_point = Column(Numeric)
    leader_unit_no = Column(Integer)
    unit_1_id = Column(Integer)
    unit_1_level = Column(Integer)
    unit_1_fortune_level = Column(Integer)
    unit_1_buff_hp = Column(Integer)
    unit_1_buff_attack = Column(Integer)
    unit_1_buff_defence = Column(Integer)
    unit_1_equipped_item_1_id = Column(Integer)
    unit_1_equipped_item_2_id = Column(Integer)
    unit_1_equipped_item_3_id = Column(Integer)
    unit_2_id = Column(Integer)
    unit_2_level = Column(Integer)
    unit_2_fortune_level = Column(Integer)
    unit_2_buff_hp = Column(Integer)
    unit_2_buff_attack = Column(Integer)
    unit_2_buff_defence = Column(Integer)
    unit_2_equipped_item_1_id = Column(Integer)
    unit_2_equipped_item_2_id = Column(Integer)
    unit_2_equipped_item_3_id = Column(Integer)
    unit_3_id = Column(Integer)
    unit_3_level = Column(Integer)
    unit_3_fortune_level = Column(Integer)
    unit_3_buff_hp = Column(Integer)
    unit_3_buff_attack = Column(Integer)
    unit_3_buff_defence = Column(Integer)
    unit_3_equipped_item_1_id = Column(Integer)
    unit_3_equipped_item_2_id = Column(Integer)
    unit_3_equipped_item_3_id = Column(Integer)
    unit_4_id = Column(Integer)
    unit_4_level = Column(Integer)
    unit_4_fortune_level = Column(Integer)
    unit_4_buff_hp = Column(Integer)
    unit_4_buff_attack = Column(Integer)
    unit_4_buff_defence = Column(Integer)
    unit_4_equipped_item_1_id = Column(Integer)
    unit_4_equipped_item_2_id = Column(Integer)
    unit_4_equipped_item_3_id = Column(Integer)
    party_power_total = Column(Integer)
    status = Column(Integer)

class ArenaRankMaster(Base):
    __tablename__ = 'arena_rank_master'

    id = Column(Integer, primary_key=True, index=True)
    rank_no = Column(Integer)
    arena_rank_name = Column(Text)
    bgm_name = Column(Text)
    background_name = Column(Text)
    need_badge = Column(Integer)
    win_reward_group_list = Column(Text)
    lose_reward_group_list = Column(Text)
    win_count_min = Column(Integer)
    reward_group_list = Column(Text)
    matching_threshold = Column(Integer)
    status = Column(Integer)

class ArenaRankingRewardMaster(Base):
    __tablename__ = 'arena_ranking_reward_master'

    id = Column(Integer, primary_key=True, index=True)
    ranking_reward_group = Column(Integer)
    ranking_min = Column(Integer)
    ranking_max = Column(Integer)
    reward_group_list = Column(Text)
    reward_message_title = Column(Text)
    reward_message_content = Column(Text)

class ArenaRewardMaster(Base):
    __tablename__ = 'arena_reward_master'

    id = Column(Integer, primary_key=True, index=True)
    reward_type = Column(Integer)
    reward_id = Column(Integer)
    reward_value = Column(Integer)
    reward_custom_parameter = Column(Text)

class ArenaShopMaster(Base):
    __tablename__ = 'arena_shop_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    need_type = Column(Integer)
    need_num = Column(Integer)
    object_type = Column(Integer)
    object_id = Column(Integer)
    value = Column(Integer)
    custom_parameter = Column(Text)
    max_purchase_value = Column(Integer)
    purchase_reset_type = Column(Integer)
    description = Column(Text)
    status = Column(Integer)
    priority = Column(Integer)
    start_at = Column(String)
    end_at = Column(String)

class BattleRelationMaster(Base):
    __tablename__ = 'battle_relation_master'

    id = Column(Integer, primary_key=True, index=True)
    quest_id = Column(Integer, ForeignKey('quest_master.id'))
    battle_no = Column(Integer)
    weight = Column(Integer)
    bgm_name = Column(Text)
    background_name = Column(Text)
    battlemaster_id = Column(Integer)
    field_setting_id = Column(Integer)

    quest = relationship("QuestMaster", foreign_keys=[quest_id])

class ChallengeEventMaster(Base):
    __tablename__ = 'challenge_event_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    start_at = Column(DateTime)
    end_at = Column(DateTime)

class ChallengeMaster(Base):
    __tablename__ = 'challenge_master'

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer)
    group_no = Column(Integer)
    reset_interval = Column(Integer)
    challenge_type = Column(Integer)
    challenge_ids = Column(Text)
    challenge_value = Column(Integer)
    name = Column(Text)
    description = Column(Text)
    present1_type = Column(Integer)
    present1_id = Column(Integer)
    present1_value = Column(Integer)
    present1_custom_parameter = Column(Text)
    present2_type = Column(Integer)
    present2_id = Column(Integer)
    present2_value = Column(Integer)
    present2_custom_parameter = Column(Text)
    present3_type = Column(Integer)
    present3_id = Column(Integer)
    present3_value = Column(Integer)
    present3_custom_parameter = Column(Text)
    present4_type = Column(Integer)
    present4_id = Column(Integer)
    present4_value = Column(Integer)
    present4_custom_parameter = Column(Text)
    present5_type = Column(Integer)
    present5_id = Column(Integer)
    present5_value = Column(Integer)
    present5_custom_parameter = Column(Text)
    init_unlock = Column(Integer)
    pri = Column(Integer)
    challenge_event_id = Column(Integer)

class ChallengeRewardMaster(Base):
    __tablename__ = 'challenge_reward_master'

    id = Column(Integer, primary_key=True, index=True)
    challenge_id = Column(Integer, ForeignKey('challenge_master.id'))
    no = Column(Integer)
    present1_type = Column(Integer)
    present1_id = Column(Integer)
    present1_value = Column(Integer)
    present1_custom_parameter = Column(Text)
    present2_type = Column(Integer)
    present2_id = Column(Integer)
    present2_value = Column(Integer)
    present2_custom_parameter = Column(Text)
    present3_type = Column(Integer)
    present3_id = Column(Integer)
    present3_value = Column(Integer)
    present3_custom_parameter = Column(Text)
    present4_type = Column(Integer)
    present4_id = Column(Integer)
    present4_value = Column(Integer)
    present4_custom_parameter = Column(Text)
    present5_type = Column(Integer)
    present5_id = Column(Integer)
    present5_value = Column(Integer)
    present5_custom_parameter = Column(Text)

    challenge = relationship("ChallengeMaster", foreign_keys=[challenge_id])

class CommonUnlockMaster(Base):
    __tablename__ = 'common_unlock_master'

    id = Column(Integer, primary_key=True, index=True)
    unlock_object_type = Column(Integer)
    unlock_object_master_id = Column(Integer)
    unlock_type1 = Column(Integer)
    unlock_id1 = Column(Integer)
    unlock_type2 = Column(Integer)
    unlock_id2 = Column(Integer)
    unlock_type3 = Column(Integer)
    unlock_id3 = Column(Integer)
    unlock_type4 = Column(Integer)
    unlock_id4 = Column(Integer)
    unlock_type5 = Column(Integer)
    unlock_id5 = Column(Integer)
    name = Column(Text)
    effect_position_x = Column(Integer)
    effect_position_y = Column(Integer)

class CommonstringMaster(Base):
    __tablename__ = 'commonstring_master'

    id = Column(Integer, primary_key=True, index=True)
    text_key = Column(Text)
    japanese_value = Column(Text)
    english_value = Column(Text)
    chinese_value = Column(Text)
    french_value = Column(Text)

class CookingRecipeMaster(Base):
    __tablename__ = 'cooking_recipe_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    created_food_id = Column(Integer, ForeignKey('food_master.id'))
    success_rate = Column(Integer)
    material_1_type = Column(Integer)
    material_1_id = Column(Integer, ForeignKey('food_master.id'))
    material_1_value = Column(Integer)
    material_2_type = Column(Integer)
    material_2_id = Column(Integer, ForeignKey('food_master.id'))
    material_2_value = Column(Integer)
    material_3_type = Column(Integer)
    material_3_id = Column(Integer)
    material_3_value = Column(Integer)
    material_4_type = Column(Integer)
    material_4_id = Column(Integer)
    material_4_value = Column(Integer)
    material_5_type = Column(Integer)
    material_5_id = Column(Integer)
    material_5_value = Column(Integer)
    need_coin = Column(Integer)
    description = Column(Text)
    exp_id = Column(Integer)

    food = relationship("FoodMaster", foreign_keys=[created_food_id])
    material1 = relationship("FoodMaster", foreign_keys=[material_1_id])
    material2 = relationship("FoodMaster", foreign_keys=[material_2_id])

class DungeonLauncherMaster(Base):
    __tablename__ = 'dungeon_launcher_master'

    id = Column(Integer, primary_key=True, index=True)
    dungeon_id = Column(Integer, ForeignKey('dungeon_master.id'))
    start_at = Column(DateTime)
    end_at = Column(DateTime)

    dungeon = relationship("DungeonMaster", foreign_keys=[dungeon_id])

class EnemyMaster(Base):
    __tablename__ = 'enemy_master'

    id = Column(Integer, ForeignKey('skill_relation_master.relation_id'), primary_key=True, index=True)
    unit_id = Column(Integer, ForeignKey('unit_master.id'))
    level = Column(Integer)
    hp = Column(Integer)
    attack = Column(Integer)
    deffence = Column(Integer)
    skill1_damage_value = Column(Integer)
    skill2_damage_value = Column(Integer)
    full_skill_damage_value = Column(Integer)
    break_capacity = Column(Integer)
    break_power = Column(Integer)
    resistant_poison_base = Column(Integer)
    resistant_poison_max = Column(Integer)
    resistant_poison_rise_count = Column(Integer)
    resistant_darkness_base = Column(Integer)
    resistant_darkness_max = Column(Integer)
    resistant_darkness_rise_count = Column(Integer)
    resistant_silent_base = Column(Integer)
    resistant_silent_max = Column(Integer)
    resistant_silent_rise_count = Column(Integer)
    resistant_paralyze_base = Column(Integer)
    resistant_paralyze_max = Column(Integer)
    resistant_paralyze_rise_count = Column(Integer)
    resistant_injury_base = Column(Integer)
    resistant_injury_max = Column(Integer)
    resistant_injury_rise_count = Column(Integer)
    resistant_sickness_base = Column(Integer)
    resistant_sickness_max = Column(Integer)
    resistant_sickness_rise_count = Column(Integer)
    resistant_stun_base = Column(Integer)
    resistant_stun_max = Column(Integer)
    resistant_stun_rise_count = Column(Integer)
    resistant_freeze_base = Column(Integer)
    resistant_freeze_max = Column(Integer)
    resistant_freeze_rise_count = Column(Integer)
    resistant_burn_base = Column(Integer)
    resistant_burn_stun_max = Column(Integer)
    resistant_burn_stun_rise_count = Column(Integer)
    skill_invocation_weight = Column(Integer)
    need_sp = Column(Integer)
    damage_drop_sp = Column(Integer)
    drop_sp = Column(Integer)
    drop_coin = Column(Integer)
    drop_user_exp = Column(Integer)
    drop_unit_exp = Column(Integer)
    weight = Column(Integer)
    size = Column(Integer)
    is_boss = Column(Integer)
    first_clear_drop_id = Column(Numeric)
    #name = Column(Text)
    _name = Column('name')

    chargearts_skill_id = Column(Integer)
    chargearts_skill_id2 = Column(Integer)
    full_chargearts_skill_id = Column(Integer)
    is_lua = Column(Integer)


    unit = relationship("UnitMaster", foreign_keys=[unit_id])
    skills = relationship("SkillRelationMaster", foreign_keys=[id], uselist=True)

    @hybrid_property
    def name(self):
        if self._name:
            return self._name
        else:
            return self.unit.name
    
    @name.setter
    def name(self, value):
        self._name = value

# https://docs.sqlalchemy.org/en/13/core/sqlelement.html?highlight=case#sqlalchemy.sql.expression.case
# https://stackoverflow.com/questions/11258770/case-when-with-orm-sqlalchemy
# https://docs.sqlalchemy.org/en/13/orm/mapping_columns.html#using-column-property-for-column-level-options
# https://docs.sqlalchemy.org/en/13/orm/extensions/hybrid.html#join-dependent-relationship-hybrid
# https://stackoverflow.com/questions/25272092/sqlalchemy-hybrid-property-case-statement
    @name.expression
    def name(cls):
        return case({None: cls._name}, value=cls._name, else_=UnitMaster.name)



    #skill1 = relationship("SkillMaster", foreign_keys=[chargearts_skill_id])
    #skill2 = relationship("SkillMaster", foreign_keys=[chargearts_skill_id2])
    #art = relationship("SkillMaster", foreign_keys=[full_chargearts_skill_id])    


class DungeonMaster(Base):
    __tablename__ = 'dungeon_master'

    id = Column(Integer, primary_key=True, index=True)
    map_id = Column(Integer)
    name = Column(Text)
    dungeon_type = Column(Integer)
    dungeon_no = Column(Integer)
    page_no = Column(Integer)
    desc_before_clear = Column(Text)
    desc_after_clear = Column(Text)
    icon_position_x = Column(Integer)
    icon_position_y = Column(Integer)
    background_name = Column(Text)
    event_id = Column(Integer, ForeignKey('event_master.id'))
    status = Column(Integer)
    title_pos_y = Column(Numeric)
    clear_pos_y = Column(Numeric)
    priority = Column(Integer)
    stock = Column(Integer)
    count_timing = Column(Integer)
    reset_interval = Column(Integer)
    need_rank = Column(Integer)
    tab_type = Column(Integer)
    drop_up_type = Column(Integer)
    drop_up_id = Column(Integer)
    drop_up_unit_dict = Column(Text)
    drop_up_item_dict = Column(Text)
    questlist_image_path = Column(Text)
    view_type = Column(Integer)

    #event = relationship("EventMaster", foreign_keys=[event_id])
    event = relationship("EventMaster", foreign_keys=[event_id], back_populates=("dungeon"))
    quests = relationship("QuestMaster", uselist=True)
    #enemies = relationship(
       #EnemyMaster,
        #order_by="asc(EnemyMaster.id)",
        #primaryjoin=foreign(func.substr(id, 1, 5)) == remote(func.substr(EnemyMaster.id, 1, 5)), viewonly=True, uselist=True)


class EventInfoMaster(Base):
    __tablename__ = 'event_info_master'

    id = Column(Integer, primary_key=True, index=True)
    view_type = Column(Integer)
    memo = Column(Text)
    action_type = Column(Text)
    action_param = Column(Text, ForeignKey('event_master.id'), ForeignKey('gacha_master.id'))
    view_image = Column(Text)
    label_image = Column(Text)
    pos_x = Column(Integer)
    pos_y = Column(Integer)
    param = Column(Text)
    priority = Column(Integer)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    view_start_day = Column(Integer)
    view_end_day = Column(Integer)
    status = Column(Integer)

    #if action_type == 3:
    banner = relationship("GachaMaster", foreign_keys=[action_param])
    event = relationship("EventMaster")

class EventItemMaster(Base):
    __tablename__ = 'event_item_master'

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('event_master.id'))
    name = Column(Text)
    rarity = Column(Integer)
    limit_value = Column(Integer)

    event = relationship("EventMaster", foreign_keys=[event_id])

class EventMaster(Base):
    __tablename__ = 'event_master'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer)
    name = Column(Text)
    param = Column(Text)
    description = Column(Text)
    start_at = Column(DateTime, nullable=True)
    end_at = Column(DateTime, nullable=True)
    item_start_at = Column(String, nullable=True)
    item_end_at = Column(String, nullable=True)
    event_shop_type = Column(Integer)
    status = Column(Integer)

    dungeon = relationship("DungeonMaster", back_populates=("event"))
    banner = None
    info = None
class EventShopMaster(Base):
    __tablename__ = 'event_shop_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    event_id = Column(Integer, ForeignKey('event_master.id'))
    need_item_id = Column(Integer, ForeignKey('event_item_master.id'))
    need_count = Column(Integer)
    object_type = Column(Integer)
    object_id = Column(Integer, ForeignKey('item_master.id'))
    value = Column(Integer)
    max_set_value = Column(Numeric)
    max_purchase_value = Column(Integer)
    custom_parameter = Column(Text)
    description = Column(Text)
    status = Column(Integer)
    priority = Column(Integer)

    event = relationship("EventMaster", foreign_keys=[event_id])
    need_item = relationship("EventItemMaster", foreign_keys=[need_item_id])
    item = relationship("ItemMaster", foreign_keys=[object_id])

class FarmMaster(Base):
    __tablename__ = 'farm_master'

    id = Column(Integer, primary_key=True, index=True)
    farm_point_id = Column(Integer)
    level = Column(Integer)
    gain_at = Column(Integer)
    max_gain_count = Column(Integer)

class FieldSettingMaster(Base):
    __tablename__ = 'field_setting_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    description = Column(Text)
    effect_name = Column(Text)
    field_effect_lua_id = Column(Integer)
    field_skill_effect_custom_parameter = Column(Text)
    popup_title_image_name = Column(Text)

class FoodBoostMaster(Base):
    __tablename__ = 'food_boost_master'

    id = Column(Integer, primary_key=True, index=True)
    created_food_id = Column(Integer, ForeignKey('food_master.id'))
    food_1_id = Column(Integer)
    food_2_id = Column(Integer)
    food_3_id = Column(Integer)
    food_4_id = Column(Integer)
    start_at = Column(String)
    end_at = Column(String)

    food = relationship("FoodMaster", foreign_keys=[created_food_id])

class FoodEffectMaster(Base):
    __tablename__ = 'food_effect_master'

    id = Column(Integer, primary_key=True, index=True)
    effect_type = Column(Integer)
    target = Column(Integer)
    effect_value = Column(Integer)
    description = Column(Text)

class FoodMaster(Base):
    __tablename__ = 'food_master'

    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer)
    name = Column(Text)
    rarity = Column(Integer)
    food_type = Column(Integer)
    food_effect_id1 = Column(Integer, ForeignKey('food_effect_master.id'))
    food_effect_id2 = Column(Integer)
    food_effect_id3 = Column(Integer)
    food_effect_id4 = Column(Integer)
    food_effect_id5 = Column(Integer)
    coin = Column(Integer)
    description = Column(Text)
    summary = Column(Text)
    non_sale = Column(Integer)

    food_effect1 = relationship("FoodEffectMaster", foreign_keys=[food_effect_id1])

class FriendMultiMaster(Base):
    __tablename__ = 'friend_multi_master'

    id = Column(Integer, primary_key=True, index=True)
    step = Column(Integer)
    multi_count = Column(Integer)
    reward_ids = Column(Integer)

class GachaButtonMaster(Base):
    __tablename__ = 'gacha_button_master'

    id = Column(Integer, primary_key=True, index=True)
    lowest_rarity_stock = Column(Integer)
    button_image = Column(Text)

class GachaMaster(Base):
    __tablename__ = 'gacha_master'

    id = Column(Integer, primary_key=True, index=True)
    gacha_button_id1 = Column(Integer, ForeignKey('gacha_button_master.id'))
    gacha_button_id2 = Column(Integer)
    gacha_button_id3 = Column(Integer)
    gacha_type = Column(Integer)
    gacha_system_type = Column(Integer)
    bg_name = Column(Text)
    bg_name_last = Column(Text)
    param = Column(Text)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    link_token_id = Column(Integer)

    gacha_button1 = relationship("GachaButtonMaster", foreign_keys=[gacha_button_id1])

class GachaPointMaster(Base):
    __tablename__ = 'gacha_point_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    description = Column(Text)
    count_limit = Column(Integer)
    reset_type = Column(Integer)

class GachaStepUpMaster(Base):
    __tablename__ = 'gacha_step_up_master'

    id = Column(Integer, primary_key=True, index=True)
    gacha_id = Column(Integer, ForeignKey('gacha_master.id'))
    step_no = Column(Integer)
    gacha_button_id = Column(Integer, ForeignKey('gacha_button_master.id'))
    param = Column(Text)

    gacha = relationship("GachaMaster", foreign_keys=[gacha_id])
    gacha_button = relationship("GachaButtonMaster", foreign_keys=[gacha_button_id])

class HelpMaster(Base):
    __tablename__ = 'help_master'

    id = Column(Integer, primary_key=True, index=True)
    key = Column(Text)
    value1 = Column(Integer)
    value2 = Column(Integer)
    pos_x = Column(Integer)
    pos_y = Column(Integer)
    layer_id = Column(Integer)
    rel_url = Column(Text)
    scenario_id = Column(Integer)

class ItemEvolutionMaster(Base):
    __tablename__ = 'item_evolution_master'

    id = Column(Integer, primary_key=True, index=True)
    base_item_id = Column(Integer, ForeignKey('item_master.id'))
    next_item_id = Column(Integer, ForeignKey('item_master.id'))
    material_1_type = Column(Integer)
    material_1_item_id = Column(Integer, ForeignKey('material_master.id'))
    material_1_item_value = Column(Integer)
    material_2_type = Column(Integer)
    material_2_item_id = Column(Integer)
    material_2_item_value = Column(Integer)
    material_3_type = Column(Integer)
    material_3_item_id = Column(Integer)
    material_3_item_value = Column(Integer)
    material_4_type = Column(Integer)
    material_4_item_id = Column(Integer)
    material_4_item_value = Column(Integer)
    material_5_type = Column(Integer)
    material_5_item_id = Column(Integer)
    material_5_item_value = Column(Integer)
    key_material_item_id = Column(Integer)
    key_material_item_value = Column(Integer)
    need_coin = Column(Integer)

    base_item = relationship("ItemMaster", foreign_keys=[base_item_id])
    next_item = relationship("ItemMaster", foreign_keys=[next_item_id])
    material1 = relationship("MaterialMaster", foreign_keys=[material_1_item_id])

class ItemLimitbreakExpMaster(Base):
    __tablename__ = 'item_limitbreak_exp_master'

    id = Column(Integer, primary_key=True, index=True)
    exp_id = Column(Integer)
    level = Column(Integer)
    exp = Column(Numeric)

class ItemMaster(Base):
    __tablename__ = 'item_master'

    id = Column(Integer, primary_key=True, index=True)
    base_item_id = Column(Integer, index=True)
    album_id = Column(Integer)
    name = Column(Text)
    short_name = Column(Text)
    type = Column(Integer)
    image_id = Column(Integer)
    rarity = Column(Integer)
    is_material = Column(Integer)
    evolution_stage = Column(Integer)
    hitpoint = Column(Integer)
    offence = Column(Integer)
    defence = Column(Integer)
    item_skill_id = Column(Integer, ForeignKey('skill_master.id'))
    coin = Column(Integer)
    orb = Column(Integer)
    size = Column(Numeric)
    max_limitbreak_cooltime = Column(Integer)
    min_limitbreak_cooltime = Column(Integer)
    limit_break_exp_id = Column(Integer)
    for_limit_break_exp = Column(Integer)
    description = Column(Text)
    drop_information = Column(Text)
    non_deletable = Column(Integer)

    skill = relationship("SkillMaster", foreign_keys=[item_skill_id])
    #effects = relationship("SkillEffectMaster", backref="effects")
    #effects = skill.effect

class ItemRecipeMaster(Base):
    __tablename__ = 'item_recipe_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    created_item_id = Column(Integer, ForeignKey('item_master.id'))
    material_1_type = Column(Integer)
    material_1_item_id = Column(Integer, ForeignKey('material_master.id'))
    material_1_item_value = Column(Integer)
    material_2_type = Column(Integer)
    material_2_item_id = Column(Integer)
    material_2_item_value = Column(Integer)
    material_3_type = Column(Integer)
    material_3_item_id = Column(Integer)
    material_3_item_value = Column(Integer)
    material_4_type = Column(Integer)
    material_4_item_id = Column(Integer)
    material_4_item_value = Column(Integer)
    material_5_type = Column(Integer)
    material_5_item_id = Column(Integer)
    material_5_item_value = Column(Integer)
    need_coin = Column(Integer)
    description = Column(Text)

    created_item = relationship("ItemMaster", foreign_keys=[created_item_id])
    material1 = relationship("MaterialMaster", foreign_keys=[material_1_item_id])

class KeyMaster(Base):
    __tablename__ = 'key_master'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer)
    name = Column(Text)
    description = Column(Text)
    priority = Column(Integer)
    first_visible = Column(Integer)
    tab_no = Column(Integer)
    start_at = Column(String, nullable=True)
    end_at = Column(String, nullable=True)
    count_limit = Column(Integer)
    effect_time = Column(Integer)

class LimitedFirstFriendMaster(Base):
    __tablename__ = 'limited_first_friend_master'

    id = Column(Integer, primary_key=True, index=True)
    base_id = Column(Integer)
    stage = Column(Integer)
    friend_total_count = Column(Integer)
    friend_total_login = Column(Integer)
    reward_id = Column(Integer, ForeignKey('reward_master.id'))
    title = Column(Text)
    content = Column(Text)
    is_end = Column(Integer)
    status = Column(Integer)
    start_at = Column(DateTime)
    end_at = Column(DateTime)

    reward = relationship("Reward", foreign_keys=[reward_id])

class LinkSkillMaster(Base):
    __tablename__ = 'link_skill_master'

    id = Column(Integer, primary_key=True, index=True)
    base_unit_1_id = Column(Integer)
    base_unit_2_id = Column(Integer)
    base_unit_1_cutin_direction = Column(Integer)
    base_unit_2_cutin_direction = Column(Integer)
    skill_1_id = Column(Integer)
    skill_2_id = Column(Integer)
    skill_name = Column(Text)
    description = Column(Text)

association_table = Table('association', Base.metadata,
    Column('login_bonus_master_id', Integer, ForeignKey('login_bonus_master.id')),
    Column('reward_master_id', Integer, ForeignKey('reward_master.id'))
)

class LoginBonusMaster(Base):
    __tablename__ = 'login_bonus_master'

    id = Column(Integer, primary_key=True, index=True)
    message_title = Column(Text)
    message_content = Column(Text)
    _daily_reward_id_list = Column('daily_reward_id_list')
    #_daily_reward_id_list = Column('daily_reward_id_list', ForeignKey('reward_master.id'))
    #daily_reward_id_list = Column(Text)
    #daily_reward_id_list = Column(ARRAY(Integer))
    termview_flag = Column(Integer)
    infinite_flag = Column(Integer)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    priority = Column(Integer)

    @hybrid_property
    def daily_reward_id_list(self):
        return [float(x) for x in self._daily_reward_id_list.split(',')]
    @daily_reward_id_list.setter
    def daily_reward_id_list(self, value):
        self._daily_reward_id_list += ';%s' % value

    #@hybrid_property
    #def reward(self):
        #item = [float(x) for x in self.daily_reward_id_list.split(',')][0]
        #return relationship("Reward", foreign_keys=[item])

    #@reward.setter
    #def reward(self, value):
        #self._daily_reward_id_list = value

    #@reward.expression
    #def reward(cls):
        #return relationship("Reward", foreign_keys=[cls.daily_reward_id_list[0]])

    #rewards = relationship("Reward", foreign_keys=[_daily_reward_id_list])
    #rewards = relationship("Reward", secondary=association_table)
    #rewards = relationship("Reward")
    #rewards = []

class LoginBonusTotalMaster(Base):
    __tablename__ = 'login_bonus_total_master'

    id = Column(Integer, primary_key=True, index=True)
    day = Column(Integer)
    message_title = Column(Text)
    message_content = Column(Text)
    reward_id = Column(Integer, ForeignKey('reward_master.id'))
    popup_text = Column(Text)

    reward = relationship("Reward", foreign_keys=[reward_id])
# SKIP
class MapMaster(Base):
    __tablename__ = 'map_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    map_no = Column(Integer)
    icon_position_x = Column(Integer)
    icon_position_y = Column(Integer)
    is_special = Column(Integer)
    view_type = Column(Integer)
    start_at = Column(Numeric)
    end_at = Column(Numeric)
    status = Column(Integer)

class MaterialMaster(Base):
    __tablename__ = 'material_master'

    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer)
    name = Column(Text)
    type = Column(Integer)
    rarity = Column(Integer)
    description = Column(Text)
    drop_information = Column(Text)
    drop_information_id_info = Column(Text)

# SKIP
class MineBossBattleMaster(Base):
    __tablename__ = 'mine_boss_battle_master'

    id = Column(Integer, primary_key=True, index=True)
    mine_id = Column(Integer)
    start_floor_num = Column(Integer)
    info_image_name = Column(Text)
    battle_bgm_name = Column(Text)
    battle_bg_name = Column(Text)
    mine_enemy_type = Column(Integer)
    mine_enemy_id0 = Column(Integer)
    mine_enemy_id1 = Column(Integer)
    mine_enemy_id2 = Column(Integer)
    mine_enemy_id3 = Column(Integer)
    mine_enemy_id4 = Column(Integer)
    mine_enemy_id5 = Column(Integer)
    mine_enemy_id6 = Column(Integer)
    weight = Column(Integer)
    description = Column(Text)
    mine_fortune_drop_id = Column(Integer)
    drop_table_function = Column(Text)
    album_icon_name = Column(Text)
    album_priority = Column(Integer)
    name = Column(Text)
    element = Column(Integer)
    race = Column(Integer)
    field_setting_id = Column(Integer)

# SKIP
class MineEnemyMaster(Base):
    __tablename__ = 'mine_enemy_master'

    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(Integer)
    hp_threshold = Column(Integer)
    hp_function1 = Column(Text)
    hp_function2 = Column(Text)
    attack_threshold = Column(Integer)
    attack_function1 = Column(Text)
    attack_function2 = Column(Text)
    deffence_threshold = Column(Integer)
    deffence_function1 = Column(Text)
    deffence_function2 = Column(Text)
    skill1_damage_value = Column(Integer)
    skill2_damage_value = Column(Integer)
    full_skill_damage_value = Column(Integer)
    break_capacity_threshold = Column(Integer)
    break_capacity_function1 = Column(Text)
    break_capacity_function2 = Column(Text)
    level = Column(Integer)
    break_power = Column(Integer)
    resistant_poison_base = Column(Integer)
    resistant_poison_max = Column(Integer)
    resistant_poison_rise_count = Column(Integer)
    resistant_darkness_base = Column(Integer)
    resistant_darkness_max = Column(Integer)
    resistant_darkness_rise_count = Column(Integer)
    resistant_silent_base = Column(Integer)
    resistant_silent_max = Column(Integer)
    resistant_silent_rise_count = Column(Integer)
    resistant_paralyze_base = Column(Integer)
    resistant_paralyze_max = Column(Integer)
    resistant_paralyze_rise_count = Column(Integer)
    resistant_injury_base = Column(Integer)
    resistant_injury_max = Column(Integer)
    resistant_injury_rise_count = Column(Integer)
    resistant_sickness_base = Column(Integer)
    resistant_sickness_max = Column(Integer)
    resistant_sickness_rise_count = Column(Integer)
    resistant_stun_base = Column(Integer)
    resistant_stun_max = Column(Integer)
    resistant_stun_rise_count = Column(Integer)
    resistant_freeze_base = Column(Integer)
    resistant_freeze_max = Column(Integer)
    resistant_freeze_rise_count = Column(Integer)
    resistant_burn_base = Column(Integer)
    resistant_burn_stun_max = Column(Integer)
    resistant_burn_stun_rise_count = Column(Integer)
    skill_invocation_weight = Column(Integer)
    need_sp = Column(Integer)
    damage_drop_sp = Column(Integer)
    drop_sp = Column(Integer)
    size = Column(Integer)
    name = Column(Text)
    chargearts_skill_id = Column(Integer)
    chargearts_skill_id2 = Column(Integer)
    full_chargearts_skill_id = Column(Integer)
    is_lua = Column(Integer)
    is_boss = Column(Integer)

# SKIP
class MineEventMaster(Base):
    __tablename__ = 'mine_event_master'

    id = Column(Integer, primary_key=True, index=True)
    mine_id = Column(Integer)
    start_at = Column(Numeric)
    end_at = Column(Numeric)

# SKIP
class MineMaster(Base):
    __tablename__ = 'mine_master'

    id = Column(Integer, primary_key=True, index=True)
    max_floor = Column(Integer)
    boss_magic_stone_rate = Column(Integer)
    stamina_function = Column(Text)
    drop_user_exp_function = Column(Text)
    first_rare_boss_battle_floor = Column(Integer)
    high_magic_stone_floor = Column(Integer)
    rare_boss_up_rate = Column(Integer)
    floor_change_interval = Column(Integer)
    floor_change_time = Column(Integer)
    floor_change_start = Column(Integer)

class MissionMaster(Base):
    __tablename__ = 'mission_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    difficulty = Column(Integer)
    requirement_type = Column(Integer)
    requirement_value_1 = Column(Integer)
    requirement_value_2 = Column(Integer)
    requirement_description = Column(Text)
    description = Column(Text)
    present_type = Column(Integer)
    present_id = Column(Integer)
    present_value = Column(Integer)
    custam_parameter = Column(Text)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    status = Column(Integer)
    story = Column(Text)

class OrbShopMaster(Base):
    __tablename__ = 'orb_shop_master'

    id = Column(Integer, primary_key=True, index=True)
    shop_type = Column(Integer)
    name = Column(Text)
    need_type1 = Column(Integer)
    need_id1 = Column(Integer)
    need_value1 = Column(Integer)
    need_type2 = Column(Integer)
    need_id2 = Column(Integer)
    need_value2 = Column(Integer)
    need_type3 = Column(Integer)
    need_id3 = Column(Integer)
    need_value3 = Column(Integer)
    need_type4 = Column(Integer)
    need_id4 = Column(Integer)
    need_value4 = Column(Integer)
    need_type5 = Column(Integer)
    need_id5 = Column(Integer)
    need_value5 = Column(Integer)
    object_type = Column(Integer)
    object_id = Column(Integer, ForeignKey('item_master.id'))
    value = Column(Integer)
    max_set_value = Column(Numeric)
    max_purchase_value = Column(Integer)
    reset_type = Column(Integer)
    custam_parameter = Column(Text)
    description = Column(Text)
    status = Column(Integer)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    priority = Column(Integer)
    is_time_display = Column(Integer)

    item = relationship("ItemMaster", foreign_keys=[object_id])

class PlayerExpMaster(Base):
    __tablename__ = 'player_exp_master'

    id = Column(Integer, primary_key=True, index=True)
    rank = Column(Integer)
    exp = Column(Numeric)
    max_stam = Column(Integer)
    max_party = Column(Numeric)
    max_friend = Column(Numeric)

class PremiumLoginMaster(Base):
    __tablename__ = 'premium_login_master'

    id = Column(Integer, primary_key=True, index=True)
    shopdia_id = Column(Integer)
    present_type = Column(Integer)
    present_id = Column(Integer)
    present_value = Column(Integer)
    present_custam_parameter = Column(Text)
    title = Column(Text)
    content = Column(Text)

class PremiumPresentMaster(Base):
    __tablename__ = 'premium_present_master'

    id = Column(Integer, primary_key=True, index=True)
    shopdia_id = Column(Integer)
    present_type = Column(Integer)
    present_id = Column(Integer)
    present_value = Column(Integer)
    present_custam_parameter = Column(Text)

class PremiumPurchasedMaster(Base):
    __tablename__ = 'premium_purchased_master'

    id = Column(Integer, primary_key=True, index=True)
    shopdia_id = Column(Integer)
    type = Column(Integer)
    value = Column(Integer)

class QuestLauncherMaster(Base):
    __tablename__ = 'quest_launcher_master'

    id = Column(Integer, primary_key=True, index=True)
    quest_id = Column(Integer)
    start_at = Column(Numeric)
    end_at = Column(Numeric)
    image = Column(Text)
    dungeon_image = Column(Text)
    quest_name = Column(Text)
    quest_description = Column(Text)

class QuestMaster(Base):
    __tablename__ = 'quest_master'

    id = Column(Integer, primary_key=True, index=True)
    quest_type = Column(Integer)
    map_id = Column(Integer)
    dungeon_id = Column(Integer, ForeignKey('dungeon_master.id'))
    quest_no = Column(Integer)
    fortune_drop_id = Column(Integer)
    next_quest_ids = Column(Text, ForeignKey('quest_master.id'))
    init_unlock = Column(Integer)
    continue_flag = Column(Integer)
    name = Column(Text)
    description = Column(Text)
    stamina = Column(Integer)
    difficulty = Column(Integer)
    drop_coin = Column(Integer)
    drop_user_exp = Column(Integer)
    drop_unit_exp = Column(Integer)
    status = Column(Integer)
    questmission1_id = Column(Integer)
    questmission1_reward_type = Column(Numeric)
    questmission1_reward_id = Column(Integer)
    questmission1_reward_value = Column(Integer)
    custam_parameter1 = Column(Text)
    questmission2_id = Column(Integer)
    questmission2_reward_type = Column(Numeric)
    questmission2_reward_id = Column(Integer)
    questmission2_reward_value = Column(Integer)
    custam_parameter2 = Column(Text)
    questmission3_id = Column(Integer)
    questmission3_reward_type = Column(Numeric)
    questmission3_reward_id = Column(Integer)
    questmission3_reward_value = Column(Integer)
    custam_parameter3 = Column(Text)
    complete_reward_type = Column(Numeric)
    complete_reward_id = Column(Integer)
    complete_reward_value = Column(Integer)
    complete_custam_parameter = Column(Text)
    is_first_clear_drop = Column(Integer)
    is_different_drop = Column(Integer)
    is_multi = Column(Integer)
    need_rank = Column(Integer)
    stock = Column(Integer)
    count_timing = Column(Integer)
    reset_interval = Column(Integer)
    key_id = Column(Integer, ForeignKey('key_master.id'))
    key_value = Column(Integer)
    not_same_unit = Column(Integer)
    drop_up_base_unit_ids = Column(Integer, ForeignKey('unit_master.base_unit_id'), nullable=True)
    drop_ability_exp = Column(Integer)
    is_view_party = Column(Integer)
    element_list = Column(Text)
    race_list = Column(Text)
    is_lua = Column(Integer)
    rune_drop_type_id = Column(Integer, ForeignKey('rune_type_master.id'))
    sharpen_exp = Column(Integer)

    dungeon = relationship("DungeonMaster", foreign_keys=[dungeon_id])
    next_quest = relationship("QuestMaster", foreign_keys=[next_quest_ids])
    key = relationship("KeyMaster", foreign_keys=[key_id])
    drop_up_unit = relationship("UnitMaster", foreign_keys=[drop_up_base_unit_ids])
    rune_drop_type = relationship("RuneTypeMaster", foreign_keys=[rune_drop_type_id])
    #questmission1_reward = relationship("?", foreign_keys=[questmission1_reward_id])

class QuestMissionChangeMaster(Base):
    __tablename__ = 'quest_mission_change_master'

    id = Column(Integer, primary_key=True, index=True)
    quest_id = Column(Integer)
    questmission1_id = Column(Integer)
    questmission1_reward_type = Column(Numeric)
    questmission1_reward_id = Column(Integer)
    questmission1_reward_value = Column(Integer)
    custam_parameter1 = Column(Text)
    questmission2_id = Column(Integer)
    questmission2_reward_type = Column(Numeric)
    questmission2_reward_id = Column(Integer)
    questmission2_reward_value = Column(Integer)
    custam_parameter2 = Column(Text)
    questmission3_id = Column(Integer)
    questmission3_reward_type = Column(Numeric)
    questmission3_reward_id = Column(Integer)
    questmission3_reward_value = Column(Integer)
    custam_parameter3 = Column(Text)
    complete_reward_type = Column(Numeric)
    complete_reward_id = Column(Integer)
    complete_reward_value = Column(Integer)
    complete_custam_parameter = Column(Text)

class QuestMissionMaster(Base):
    __tablename__ = 'quest_mission_master'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer)
    value = Column(Integer)
    value_list = Column(Text)

class RaidAnimationMaster(Base):
    __tablename__ = 'raid_animation_master'

    id = Column(Integer, primary_key=True, index=True)
    start_animation_name = Column(Text)
    start_animation_type = Column(Text)
    end_animation_name = Column(Text)
    end_animation_type = Column(Text)
    end_text = Column(Text)

class RaidBossFieldMaster(Base):
    __tablename__ = 'raid_boss_field_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    effect_1 = Column(Integer)
    effect_2 = Column(Integer)
    bg_name = Column(Text)
    background_name = Column(Text)
    start_at = Column(DateTime)
    end_at = Column(DateTime)

class RaidBossMaster(Base):
    __tablename__ = 'raid_boss_master'

    id = Column(Integer, primary_key=True, index=True)
    enemy_id = Column(Integer, ForeignKey('enemy_master.id'))
    difficulty = Column(Integer)
    bgm_name = Column(Text)
    image_id = Column(Integer)
    raid_animation_id = Column(Integer, ForeignKey('raid_animation_master.id'))
    ticket_num = Column(Integer)
    ticket_id = Column(Integer, ForeignKey('raid_ticket_master.id'))
    limit_time_num = Column(Integer)
    break_time_num = Column(Integer)
    max_member = Column(Integer)
    gain_unit_exp = Column(Integer)
    max_gain_unit_exp = Column(Integer)
    gain_user_exp = Column(Integer)
    max_gain_user_exp = Column(Integer)
    gain_coin = Column(Integer)
    max_gain_coin = Column(Integer)
    point_magnification = Column(Float)
    background_name = Column(Text)
    break_reward_num1 = Column(Integer)
    break_reward_num2 = Column(Integer)
    is_total_destroy_count = Column(Integer)
    raid_type = Column(Integer)
    battle_max_count = Column(Integer)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    field_setting_id = Column(Integer)

    enemy = relationship("EnemyMaster", foreign_keys=[enemy_id])
    raid_animation = relationship("RaidAnimationMaster", foreign_keys=[raid_animation_id])
    ticket = relationship("RaidTicketMaster", foreign_keys=[ticket_id])


class RaidDestroyRewardMaster(Base):
    __tablename__ = 'raid_destroy_reward_master'

    id = Column(Integer, primary_key=True, index=True)
    raid_id = Column(Integer, ForeignKey('raid_master.id'))
    conditions_type = Column(Integer)
    conditions_value = Column(Integer)
    reward_id_list = Column(Integer, ForeignKey('reward_master.id'))
    priority = Column(Integer)

    raid = relationship("RaidMaster", foreign_keys=[raid_id])
    reward = relationship("Reward", foreign_keys=[reward_id_list])

class RaidFieldEffectMaster(Base):
    __tablename__ = 'raid_field_effect_master'

    id = Column(Integer, primary_key=True, index=True)
    skill_type = Column(Text)
    target = Column(Integer)
    effect_value = Column(Integer)
    script_id = Column(Integer)
    value_1 = Column(Integer)
    value_2 = Column(Integer)
    value_3 = Column(Integer)
    description = Column(Text)

class RaidGeneralRewardMaster(Base):
    __tablename__ = 'raid_general_reward_master'

    id = Column(Integer, primary_key=True, index=True)
    raid_id = Column(Integer)
    raid_type = Column(Integer)
    reward_id_list = Column(Text)
    num = Column(Integer)
    message_content = Column(Text)

class RaidMaster(Base):
    __tablename__ = 'raid_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    boss_master_ids = Column(Text)
    event_id = Column(Integer, ForeignKey('event_master.id'))
    drop_up_base_unit_ids = Column(Text)
    raid_start_at = Column(DateTime)
    battle_start_at = Column(DateTime)
    battle_end_at = Column(DateTime)
    raid_end_at = Column(DateTime)
    destroy_view_start_at = Column(String)
    destroy_view_end_at = Column(String)
    damage_raid_view_start_at = Column(String)
    damage_raid_view_end_at = Column(String)

    event = relationship("EventMaster", foreign_keys=[event_id])
class RaidTicketMaster(Base):
    __tablename__ = 'raid_ticket_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    description = Column(Text)
    priority = Column(Integer)
    start_at = Column(String)
    end_at = Column(String)
    count_limit = Column(Integer)
    effect_time = Column(Integer)

class RaidTotalRewardMaster(Base):
    __tablename__ = 'raid_total_reward_master'

    id = Column(Integer, primary_key=True, index=True)
    raid_id = Column(Integer)
    reward_id = Column(Integer)
    destroy_num = Column(Integer)
    explain_text = Column(Text)
    reward_message_title = Column(Text)
    reward_message_content = Column(Text)

class RandomLoginBonusMaster(Base):
    __tablename__ = 'random_login_bonus_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    type = Column(Integer)
    _reward_id_list = Column('reward_id_list')
    last_reward_id = Column(Integer)
    start_at = Column(String)
    end_at = Column(String)
    receive_grace = Column(Integer)

    @hybrid_property
    def reward_id_list(self):
        return [float(x) for x in self._reward_id_list.split(',')]
    @reward_id_list.setter
    def reward_id_list(self, value):
        self._reward_id_list += ';%s' % value    

class RandomRewardMaster(Base):
    __tablename__ = 'random_reward_master'

    id = Column(Integer, primary_key=True, index=True)
    message_title = Column(Text, nullable=True)
    message_content = Column(Text, nullable=True)
    reward_type = Column(Integer)
    reward_id = Column(Integer)
    reward_value = Column(Integer)
    reward_custom_parameter = Column(Text, nullable=True)

class ResetOrbShopCountMaster(Base):
    __tablename__ = 'reset_orb_shop_count_master'

    id = Column(Integer, primary_key=True, index=True)
    reset_orb_shop_ids = Column(Text)
    start_at = Column(Numeric)

class Reward(Base):
    __tablename__ = "reward_master"

    id = Column(Integer, primary_key=True, index=True)
    receive_grace = Column(Integer, nullable=True)
    present_type = Column(Integer)
    present_id = Column(Integer, nullable=True)#,ForeignKey("users.id"))
    present_value = Column(Integer)
    present_custom_parameter = Column(String, nullable=True)
    box_rarity = Column(String, nullable=True)

class RuneMaster(Base):
    __tablename__ = 'rune_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    type_id = Column(Integer, ForeignKey('rune_type_master.id'))
    level = Column(Integer)
    is_plus = Column(Integer)
    skill_id = Column(Integer, ForeignKey('skill_master.id'))
    level_up_value = Column(Integer)
    equipment_value = Column(Integer)
    change_value = Column(Integer)
    limit_value = Column(Integer)
    image = Column(Text, nullable=True)
    spine_animation_name = Column(Text, nullable=True)

    type = relationship("RuneTypeMaster", foreign_keys=[type_id])
    skill = relationship("SkillMaster", foreign_keys=[skill_id])

class RuneTypeMaster(Base):
    __tablename__ = 'rune_type_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    is_tool_drop = Column(Integer)
    is_limited = Column(String)

t_setting_master = Table(
    'setting_master', metadata,
    Column('key', Text),
    Column('value', Text),
    Column('description', Text)
)

class SharpenExpbonusMaster(Base):
    __tablename__ = 'sharpen_expbonus_master'

    id = Column(Integer, primary_key=True, index=True)
    bonus_type = Column(Integer)
    rate_bonus_value = Column(Integer)
    fix_bonus_value = Column(Integer)
    start_at = Column(String)
    end_at = Column(String)
    quest_ids = Column(Text, nullable=True)
    item_ids = Column(Text, nullable=True)
    display_text = Column(Text)

class SharpenMaster(Base):
    __tablename__ = 'sharpen_master'

    id = Column(Integer, primary_key=True, index=True)
    base_item_id = Column(Integer, ForeignKey('item_master.base_item_id'))
    sharpen_exp_max = Column(Integer)
    status_sum_min = Column(Integer)
    status_sum_max = Column(Integer)
    skill_num_0_weight = Column(Integer)
    skill_num_1_weight = Column(Integer)
    skill_num_2_weight = Column(Integer)
    skill_num_3_weight = Column(Integer)
    skill_1_group = Column(Integer, ForeignKey('skill_group_master.id'))
    skill_2_group = Column(Integer, ForeignKey('skill_group_master.id'))
    skill_3_group = Column(Integer, ForeignKey('skill_group_master.id'))
    detail_text = Column(Text)

    base_item = relationship("ItemMaster", foreign_keys=[base_item_id])
    skill1_group = relationship("SkillGroupMaster", foreign_keys=[skill_1_group])
    skill2_group = relationship("SkillGroupMaster", foreign_keys=[skill_2_group])
    skill3_group = relationship("SkillGroupMaster", foreign_keys=[skill_3_group])

class ShopBannerGroupMaster(Base):
    __tablename__ = 'shop_banner_group_master'

    id = Column(Integer, primary_key=True, index=True)
    title_image_path = Column(Text, nullable=True)
    title_text = Column(Text)
    priority = Column(Integer)

class ShopBannerMaster(Base):
    __tablename__ = 'shop_banner_master'

    id = Column(Integer, primary_key=True, index=True)
    shop_type = Column(Integer)
    event_id = Column(Integer, ForeignKey('event_master.id'))
    bg_name = Column(Text)
    description_text = Column(Text, nullable=True)
    priority = Column(Integer)
    consume_image = Column(Text, nullable=True)
    consume_type = Column(Integer)
    consume_id = Column(Integer)
    popup_type = Column(Integer)

    event = relationship("EventMaster", foreign_keys=[event_id])

class ShopDeckSetMaster(Base):
    __tablename__ = 'shop_deck_set_master'

    id = Column(Integer, primary_key=True, index=True)
    unit1_id = Column(Integer)
    unit1_custom_parameter = Column(Text)
    unit1_item1 = Column(Integer)
    unit1_item1_limitbreak = Column(Integer)
    unit1_item2 = Column(Integer)
    unit1_item2_limitbreak = Column(Integer)
    unit1_item3 = Column(Integer)
    unit1_item3_limitbreak = Column(Integer)
    unit2_id = Column(Integer)
    unit2_custom_parameter = Column(Text)
    unit2_item1 = Column(Integer)
    unit2_item1_limitbreak = Column(Integer)
    unit2_item2 = Column(Integer)
    unit2_item2_limitbreak = Column(Integer)
    unit2_item3 = Column(Integer)
    unit2_item3_limitbreak = Column(Integer)
    unit3_id = Column(Integer)
    unit3_custom_parameter = Column(Text)
    unit3_item1 = Column(Integer)
    unit3_item1_limitbreak = Column(Integer)
    unit3_item2 = Column(Integer)
    unit3_item2_limitbreak = Column(Integer)
    unit3_item3 = Column(Integer)
    unit3_item3_limitbreak = Column(Integer)
    unit4_id = Column(Integer)
    unit4_custom_parameter = Column(Text)
    unit4_item1 = Column(Integer)
    unit4_item1_limitbreak = Column(Integer)
    unit4_item2 = Column(Integer)
    unit4_item2_limitbreak = Column(Integer)
    unit4_item3 = Column(Integer)
    unit4_item3_limitbreak = Column(Integer)

class ShopDiaMaster(Base):
    __tablename__ = 'shop_dia_master'

    id = Column(Integer, primary_key=True, index=True)
    os_type = Column(Integer)
    name = Column(Text)
    value = Column(Integer)
    value_free = Column(Integer)
    price = Column(Float)
    product_id = Column(Text)
    product_type = Column(Integer)
    description = Column(Text)
    status = Column(Integer)
    purchase_limit = Column(Integer)
    message_title = Column(Text, nullable=True)
    message_content = Column(Text, nullable=True)
    bonus_id_list = Column(Text, nullable=True)
    bonus_id_list_rand = Column(Text, nullable=True)
    sale_flag = Column(Integer)
    sale_display_count = Column(Integer)
    sale_image_path = Column(Text, nullable=True)
    sale_priority = Column(Integer)
    base_shop_id = Column(Integer)
    token_id = Column(Integer)
    pri = Column(Integer)
    group_id = Column(Integer)
    banner_group_id = Column(Integer, ForeignKey('shop_banner_group_master.id'))
    premium_days = Column(String)
    premium_purchased_days = Column(String)
    premium_popup_title = Column(Text, nullable=True)
    banner_image = Column(Text, nullable=True)
    description_image = Column(Text, nullable=True)
    description_image_rect1 = Column(Text, nullable=True)
    description_image_url1 = Column(Text, nullable=True)
    url1_action_type = Column(Integer)
    description_image_rect2 = Column(Text, nullable=True)
    description_image_url2 = Column(Text, nullable=True)
    url2_action_type = Column(Integer)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    webview_content = Column(Text, nullable=True)
    webview_attention = Column(Text, nullable=True)
    shop_deck_id = Column(Text)

    banner_group = relationship("ShopBannerGroupMaster", foreign_keys=[banner_group_id])

class ShopMaster(Base):
    __tablename__ = 'shop_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    sale_type = Column(Integer)
    product_type = Column(Integer)
    object_id = Column(Integer)
    value = Column(Integer)
    price = Column(Integer)
    description = Column(Text)
    status = Column(Integer)
    priority = Column(Integer)
    start_at = Column(DateTime)
    end_at = Column(DateTime)

class SkillEffectMaster(Base):
    __tablename__ = 'skill_effect_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=True)
    effect_type = Column(Integer)
    skill_id = Column(Integer, ForeignKey('skill_master.id'))
    target = Column(Integer)
    effect_time = Column(Integer)
    effect_value = Column(Integer)
    mine_eff_val_threshold = Column(Integer)
    mine_eff_val_function1 = Column(Text)
    mine_eff_val_function2 = Column(Text)
    effect_min = Column(Integer)
    effect_max = Column(Integer)
    weight = Column(Integer)
    buff_type = Column(Integer)
    script_id = Column(Integer)
    script_value_1 = Column(Integer)
    script_value_2 = Column(Integer)
    script_value_3 = Column(Integer)
    script_value_4 = Column(Integer)
    script_value_5 = Column(Integer)
    tumbnail_name = Column(Text, nullable=True)
    text_image_no = Column(Integer)
    animation_id = Column(Integer)
    group_id = Column(Integer, ForeignKey('skill_group_master.id'))
    priority = Column(Integer)

    skill = relationship("SkillMaster", foreign_keys=[skill_id])
    group = relationship("SkillGroupMaster", foreign_keys=[group_id], lazy='immediate')

class SkillGroupMaster(Base):
    __tablename__ = 'skill_group_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    description = Column(Text, nullable=True)

class SkillMaster(Base):
    __tablename__ = 'skill_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    skill_type = Column(Integer)
    skill_group_id = Column(Integer, ForeignKey('skill_group_master.id'))
    priority = Column(Integer)
    damage_value = Column(Integer)
    break_value = Column(Integer)
    range_y = Column(Integer)
    element = Column(Integer)
    attribute = Column(Integer)
    need_sp = Column(Integer)
    cooltime = Column(Integer)
    cooltime_max = Column(Integer)
    animation_id = Column(Integer)
    description = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    tumbnail_name1 = Column(Text, nullable=True)
    tumbnail_name2 = Column(Text, nullable=True)
    ai_id = Column(Integer)
    ai_id2 = Column(Integer)
    ai_id3 = Column(Integer)
    battle_summary = Column(Text)
    unit_exp_value = Column(Integer)
    user_exp_value = Column(Integer)
    coin_up_value = Column(String)

    skill_group = relationship("SkillGroupMaster", foreign_keys=[skill_group_id], lazy='immediate')
    effects = relationship("SkillEffectMaster", backref="effects", lazy='immediate')
    

class SkillRelationMaster(Base):
    __tablename__ = 'skill_relation_master'

    id = Column(Integer, primary_key=True, index=True)
    relation_type = Column(Integer)
    relation_id = Column(Integer)#, ForeignKey('enemy_master.id'))
    skill_id = Column(Integer, ForeignKey('skill_master.id'))
    need_level = Column(Integer)

    #enemy = relationship("EnemyMaster", foreign_keys=[relation_id])
    skill = relationship("SkillMaster", foreign_keys=[skill_id], lazy='immediate')
    enemy = relationship("EnemyMaster")

class SkillWeightMaster(Base):
    __tablename__ = 'skill_weight_master'

    id = Column(Integer, primary_key=True, index=True)
    skill_id = Column(Integer, ForeignKey('skill_master.id'))
    group_no = Column(Integer)

    skill = relationship("SkillMaster", foreign_keys=[skill_id])

class SkinMaster(Base):
    __tablename__ = 'skin_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    description = Column(Text)
    base_unit_id = Column(Integer)
    skin_no = Column(Integer)
    min_rarity = Column(Integer)

class StampMaster(Base):
    __tablename__ = 'stamp_master'

    id = Column(Integer, primary_key=True, index=True)
    shop_id = Column(Integer, ForeignKey('shop_master.id'))
    set_no = Column(Numeric)
    name = Column(Text)
    image_name = Column(Text)
    description = Column(Text)

# SKIP
class SugorokuBonusMaster(Base):
    __tablename__ = 'sugoroku_bonus_master'

    id = Column(Integer, primary_key=True, index=True)
    sugoroku_master_id = Column(Integer)
    type = Column(Integer)
    value = Column(Integer)
    reset_type = Column(Integer)
    give_count = Column(Integer)

# SKIP
class SugorokuEffectMaster(Base):
    __tablename__ = 'sugoroku_effect_master'

    id = Column(Integer, primary_key=True, index=True)
    sugoroku_master_id = Column(Integer)
    stage_id = Column(Integer)
    type = Column(Integer)
    value = Column(Text)
    image_path = Column(Text)
    bg_image_path = Column(Text)

# SKIP
class SugorokuMaster(Base):
    __tablename__ = 'sugoroku_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    start_at = Column(Numeric)
    end_at = Column(Numeric)
    start_stage_id = Column(Integer)
    height = Column(Integer)
    width = Column(Integer)
    clear_reward_id_list = Column(Text)

class SupporterRewardMaster(Base):
    __tablename__ = 'supporter_reward_master'

    id = Column(Integer, primary_key=True, index=True)
    mine_id = Column(Integer)
    no = Column(Integer)
    name = Column(Text)
    description = Column(Text)
    clear_value = Column(Integer)
    present_type = Column(Integer)
    present_id = Column(Integer)
    present_value = Column(Integer)
    present_custom_parameter = Column(Text)

class ToolMaster(Base):
    __tablename__ = 'tool_master'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    description = Column(Text)
    type = Column(Integer)
    effect1 = Column(Integer)
    effect1_type = Column(Integer)
    effect2 = Column(Integer)
    effect2_type = Column(Integer)
    start_at = Column(String)
    end_at = Column(String)
    first_visible = Column(Integer)
    tab_no = Column(Integer)
    count_limit = Column(Integer)
    priority = Column(Integer)
    is_quest_item = Column(Integer)

class UnitAbilityExpMaster(Base):
    __tablename__ = 'unit_ability_exp_master'

    id = Column(Integer, primary_key=True, index=True)
    exp_id = Column(Integer)
    level = Column(Numeric)
    exp = Column(Numeric)

class UnitEvolutionMaster(Base):
    __tablename__ = 'unit_evolution_master'

    id = Column(Integer, primary_key=True, index=True)
    base_unit_id = Column(Integer)
    next_unit_id = Column(Integer)
    material_1_type = Column(Integer)
    material_1_id = Column(Integer)
    material_1_value = Column(Integer)
    material_2_type = Column(Integer)
    material_2_id = Column(Integer)
    material_2_value = Column(Integer)
    material_3_type = Column(Integer)
    material_3_id = Column(Integer)
    material_3_value = Column(Integer)
    material_4_type = Column(Integer)
    material_4_id = Column(Integer)
    material_4_value = Column(Integer)
    material_5_type = Column(Integer)
    material_5_id = Column(Integer)
    material_5_value = Column(Integer)
    need_coin = Column(Integer)
    evolution_need_value = Column(Integer)

class UnitExpMaster(Base):
    __tablename__ = 'unit_exp_master'

    id = Column(Integer, primary_key=True, index=True)
    exp_id = Column(Integer)
    level = Column(Numeric)
    exp = Column(Numeric)


class UnitLimitbreakExpMaster(Base):
    __tablename__ = 'unit_limitbreak_exp_master'

    id = Column(Integer, primary_key=True, index=True)
    exp_id = Column(Integer)
    level = Column(Numeric)
    exp = Column(Numeric)

class UnitLimitbreakMaster(Base):
    __tablename__ = 'unit_limitbreak_master'

    id = Column(Integer, primary_key=True, index=True)
    base_unit_id = Column(Integer)
    limit_break_level = Column(Numeric)
    equipped1_type = Column(Integer)
    equipped1_rarity = Column(Integer)
    equipped2_type = Column(Integer)
    equipped2_rarity = Column(Integer)
    equipped3_type = Column(Integer)
    equipped3_rarity = Column(Integer)
    buff_fortune_level = Column(Integer)
    buff_hp = Column(Integer)
    buff_attack = Column(Integer)
    buff_defence = Column(Integer)

class UnitMaster(Base):
    __tablename__ = 'unit_master'

    id = Column(Integer, primary_key=True, index=True)
    base_unit_id = Column(Integer)
    cue_sheet_name = Column(Text)
    cue_sheet_system_name = Column(Text)
    cue_name = Column(Text)
    album_id = Column(Integer)
    name = Column(Text)
    element = Column(Integer)
    race = Column(Integer)
    sexuality = Column(Integer)
    is_material = Column(Integer)
    exp_id = Column(Integer)
    limit_break_exp_id = Column(Integer)
    rarity = Column(Integer)
    evolution_stage = Column(Integer)
    level_max = Column(Integer)
    fortune_level_max = Column(Integer)
    hitpoint_base = Column(Integer)
    hitpoint_max = Column(Integer)
    offence_base = Column(Integer)
    offence_max = Column(Integer)
    defence_base = Column(Integer)
    defence_max = Column(Integer)
    attribute = Column(Integer)
    attack_delay = Column(Numeric)
    range_min = Column(Integer)
    range_max = Column(Integer)
    range_y = Column(Integer)
    break_power = Column(Numeric)
    break_capacity = Column(Numeric)
    chargearts_skill_id = Column(Integer, ForeignKey('skill_master.id'))
    chargearts_skill_id2 = Column(Integer, ForeignKey('skill_master.id'))
    full_chargearts_skill_id = Column(Integer, ForeignKey('skill_master.id'))
    full_chargearts_skill_id2 = Column(Integer, ForeignKey('skill_master.id'))
    coin = Column(Integer)
    for_powerup_coin = Column(Integer)
    for_powerup_exp = Column(Integer)
    for_powerup_buff_hp = Column(Integer)
    for_powerup_buff_attack = Column(Integer)
    for_powerup_buff_defence = Column(Integer)
    for_limit_break_coin = Column(Integer)
    for_limit_break_exp = Column(Integer)
    for_limit_break_ability_exp = Column(Integer)
    orb = Column(Integer)
    description = Column(Text)
    comment_gain = Column(Text)
    comment_powerup = Column(Text)
    comment_evolution = Column(Text)
    comment_limitberak = Column(Text)
    comment_fortune_max = Column(Text)
    seiyu = Column(Text)
    image_pos_x = Column(Numeric)
    image_pos_y = Column(Numeric)
    image_scale = Column(Text)
    is_boss = Column(Integer)
    non_deletable = Column(Integer)
    non_sellable = Column(Integer)
    is_lock = Column(Integer)
    drop_information = Column(Text)
    is_limitbreak_ball = Column(Integer)
    ability_exp_id = Column(Integer)
    is_lua = Column(Integer)
    limited_id = Column(Integer)
    rune_num = Column(Integer)
    antialias_type = Column(Integer)

    #unit_limit_break = relationship(
        #UnitLimitbreakMaster,
        #primaryjoin=remote(UnitLimitbreakMaster.base_unit_id) == foreign(func.concat(func.substr(id, 1, 7),'%')))
    #limit_break = association_proxy('unit_limit_break', 'buff_hp')

    #unit_limit_break = relationship(
        #UnitLimitbreakMaster,
        #primaryjoin=foreign(func.substr(id, 1, 5)) == remote(func.substr(UnitLimitbreakMaster.id, 1, 5)), viewonly=True)

    #unit_limit_break = relationship(
        #UnitLimitbreakMaster,
        #primaryjoin=foreign(func.substr(id, 1, 5)) == remote(func.substr(UnitLimitbreakMaster.id, 1, 5)), viewonly=True, uselist=True)

    limit_break = relationship(
        UnitLimitbreakMaster,
        order_by="asc(UnitLimitbreakMaster.id)",
        primaryjoin=foreign(func.substr(id, 1, 5) + '05') == remote(UnitLimitbreakMaster.id), viewonly=True, uselist=False)

    #mlb_hp = association_proxy('limit_break', 'buff_hp')
    #enemy = relationship("EnemyMaster", backref=backref("enemy_master"))
    skill1 = relationship("SkillMaster", foreign_keys=[chargearts_skill_id])
    skill2 = relationship("SkillMaster", foreign_keys=[chargearts_skill_id2])
    art = relationship("SkillMaster", foreign_keys=[full_chargearts_skill_id])
    trueart = relationship("SkillMaster", foreign_keys=[full_chargearts_skill_id2])



