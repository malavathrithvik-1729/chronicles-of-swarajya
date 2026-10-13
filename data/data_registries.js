// Chronicles of Swarajya: Master Data Registries
// Auto-generated from data/*.json

const ITEM_DATABASE = {
  "wood_sagwan": {
    "id": "wood_sagwan",
    "name": "Sagwan Teak Wood",
    "category": "material",
    "slot": null,
    "tier": 1,
    "description": "Dense, water-resistant teak timber harvested from Sahyadri groves. Essential for tool handles, scabbards, and fortified gate construction.",
    "icon": "ChroniclesOfSwarajya_Art/08_Trees/stumps_and_fallen_trees.png",
    "stackable": true,
    "maxStack": 99,
    "sellValue": 2,
    "buyValue": 5
  },
  "ore_iron": {
    "id": "ore_iron",
    "name": "Sahyadri Hematite Iron Ore",
    "category": "material",
    "slot": null,
    "tier": 1,
    "description": "Rich ironstone extracted from Deccan basalt outcrops. Refined by blacksmiths into deadly talwars, spearheads, and armour plates.",
    "icon": "ChroniclesOfSwarajya_Art/09_RocksAndMountains/iron_ore_nodes.png",
    "stackable": true,
    "maxStack": 99,
    "sellValue": 4,
    "buyValue": 10
  },
  "leather_hide": {
    "id": "leather_hide",
    "name": "Tanned Buffalo Hide",
    "category": "material",
    "slot": null,
    "tier": 1,
    "description": "Thick, oil-cured leather used for grip bindings, kamarbandh straps, brigandine foundations, and dhal shield facings.",
    "icon": "ChroniclesOfSwarajya_Art/11_VillageAndCamp/camp_assets.png",
    "stackable": true,
    "maxStack": 99,
    "sellValue": 3,
    "buyValue": 8
  },
  "gold_huns": {
    "id": "gold_huns",
    "name": "Swarajya Gold Huns",
    "category": "currency",
    "slot": null,
    "tier": 1,
    "description": "Official gold currency of the realm. Accepted by village smiths, merchants, and armourers across Maharashtra.",
    "icon": "ChroniclesOfSwarajya_Art/09_RocksAndMountains/iron_ore_nodes.png",
    "stackable": true,
    "maxStack": 99999,
    "sellValue": 1,
    "buyValue": 1
  },
  "talwar_basic": {
    "id": "talwar_basic",
    "name": "Forged Steel Talwar",
    "category": "weapon",
    "slot": "weapon",
    "tier": 1,
    "weaponClass": "curved_sword",
    "description": "Hand-forged curved steel talwar with a brass disc pommel. Well-balanced for swift slashes against raiders and sentries.",
    "icon": "ChroniclesOfSwarajya_Art/06_Weapons_OptionB/talwar_basic.png",
    "stats": {
      "atk": 18,
      "speed": 1.0,
      "reach": 28,
      "critChance": 0.05
    },
    "stackable": false,
    "sellValue": 25,
    "buyValue": 60
  },
  "talwar_upgraded": {
    "id": "talwar_upgraded",
    "name": "Pattisa Reinforced Talwar",
    "category": "weapon",
    "slot": "weapon",
    "tier": 2,
    "weaponClass": "curved_sword",
    "description": "Master-forged high-carbon steel talwar with double fullers and spiked basket hilt. Cleaves through enemy mail with ease.",
    "icon": "ChroniclesOfSwarajya_Art/06_Weapons_OptionB/talwar_upgraded.png",
    "stats": {
      "atk": 32,
      "speed": 1.1,
      "reach": 32,
      "critChance": 0.12
    },
    "stackable": false,
    "sellValue": 75,
    "buyValue": 180
  },
  "heavy_curved_sword": {
    "id": "heavy_curved_sword",
    "name": "Khanda Heavy Broadsword",
    "category": "weapon",
    "slot": "weapon",
    "tier": 2,
    "weaponClass": "heavy_sword",
    "description": "Broad double-edged blade reinforced with a spine plate. Delivers crushing downward cleaves capable of staggering shielded foes.",
    "icon": "ChroniclesOfSwarajya_Art/06_Weapons_OptionB/heavy_curved_sword.png",
    "stats": {
      "atk": 42,
      "speed": 0.85,
      "reach": 36,
      "staggerPower": 25
    },
    "stackable": false,
    "sellValue": 90,
    "buyValue": 220
  },
  "spear_bamboo": {
    "id": "spear_bamboo",
    "name": "Maratha Long Bhala (Spear)",
    "category": "weapon",
    "slot": "weapon",
    "tier": 1,
    "weaponClass": "polearm",
    "description": "A 10-foot bamboo shaft tipped with a leaf-shaped steel point. Keeps fierce charging enemies and mounted scouts at distance.",
    "icon": "ChroniclesOfSwarajya_Art/06_Weapons_OptionB/spear.png",
    "stats": {
      "atk": 22,
      "speed": 1.05,
      "reach": 44,
      "critChance": 0.08
    },
    "stackable": false,
    "sellValue": 35,
    "buyValue": 80
  },
  "bow_composite": {
    "id": "bow_composite",
    "name": "Sahyadri Teak Composite Bow",
    "category": "weapon",
    "slot": "weapon",
    "tier": 1,
    "weaponClass": "bow",
    "description": "Reinforced recurve bow made of horn, teak, and sinew. Fires armour-piercing arrows with great accuracy.",
    "icon": "ChroniclesOfSwarajya_Art/06_Weapons_OptionB/bow_and_arrow.png",
    "stats": {
      "atk": 16,
      "speed": 0.95,
      "range": 160,
      "critChance": 0.15
    },
    "stackable": false,
    "sellValue": 40,
    "buyValue": 95
  },
  "dhal_shield_basic": {
    "id": "dhal_shield_basic",
    "name": "Maratha Dhal Buckler",
    "category": "shield",
    "slot": "shield",
    "tier": 1,
    "description": "Convex buffalo-hide shield studded with four polished brass bosses. Absorbs incoming melee blows and projectile fire.",
    "icon": "ChroniclesOfSwarajya_Art/06_Weapons_OptionB/maratha_dhal_shield.png",
    "stats": {
      "def": 8,
      "blockChance": 0.35,
      "staggerResist": 15
    },
    "stackable": false,
    "sellValue": 30,
    "buyValue": 70
  },
  "dhal_shield_reinforced": {
    "id": "dhal_shield_reinforced",
    "name": "Iron-Banded Dhal Greatshield",
    "category": "shield",
    "slot": "shield",
    "tier": 2,
    "description": "Heavy rhino-hide dhal banded in damascened steel plates. Completely deflects ordinary enemy arrows and reduces heavy boss impact.",
    "icon": "ChroniclesOfSwarajya_Art/06_Weapons_OptionB/maratha_dhal_shield.png",
    "stats": {
      "def": 18,
      "blockChance": 0.55,
      "staggerResist": 30
    },
    "stackable": false,
    "sellValue": 85,
    "buyValue": 200
  },
  "angarkha_traditional": {
    "id": "angarkha_traditional",
    "name": "Traditional Cotton Angarkha",
    "category": "armour",
    "slot": "body",
    "tier": 1,
    "description": "Pleated off-white tunic with saffron trim. Offers maximum mobility and heat dissipation through the rugged Sahyadri trails.",
    "icon": "ChroniclesOfSwarajya_Art/00_ArtStyle/option_b_palette.png",
    "stats": {
      "def": 2,
      "speedBonus": 4
    },
    "stackable": false,
    "sellValue": 10,
    "buyValue": 25
  },
  "armour_leather_brigandine": {
    "id": "armour_leather_brigandine",
    "name": "Riveted Leather Brigandine",
    "category": "armour",
    "slot": "body",
    "tier": 1,
    "description": "Hardened buffalo-hide vest fitted with overlapping internal iron scales. Substantially reduces slash damage.",
    "icon": "ChroniclesOfSwarajya_Art/00_ArtStyle/option_b_palette.png",
    "stats": {
      "def": 10,
      "maxHp": 20,
      "staggerResist": 10
    },
    "stackable": false,
    "sellValue": 45,
    "buyValue": 110
  },
  "armour_chainmail_zirah": {
    "id": "armour_chainmail_zirah",
    "name": "Maratha Zirah Chainmail Hauberk",
    "category": "armour",
    "slot": "body",
    "tier": 2,
    "description": "Interlinked riveted iron rings layered over quilted cotton gambeson. Protects vital organs against thrusts, arrows, and sabres.",
    "icon": "ChroniclesOfSwarajya_Art/00_ArtStyle/option_b_palette.png",
    "stats": {
      "def": 22,
      "maxHp": 40,
      "staggerResist": 25
    },
    "stackable": false,
    "sellValue": 120,
    "buyValue": 280
  },
  "pheta_royal": {
    "id": "pheta_royal",
    "name": "Crimson & Saffron Pheta",
    "category": "headgear",
    "slot": "head",
    "tier": 1,
    "description": "Chhatrapati Shivaji Maharaj's iconic royal turban pinned with a jeweled Sirpech brooch and white plume. Symbol of Hindavi Swarajya.",
    "icon": "ChroniclesOfSwarajya_Art/00_ArtStyle/option_b_palette.png",
    "stats": {
      "def": 4,
      "leadership": 10,
      "astraDamageBonus": 0.15
    },
    "stackable": false,
    "sellValue": 50,
    "buyValue": 150
  },
  "mojari_leather": {
    "id": "mojari_leather",
    "name": "Pointed Leather Mojari Boots",
    "category": "footwear",
    "slot": "feet",
    "tier": 1,
    "description": "Traditional curved-toe footwear built from thick cured leather with reinforced soles for gripping wet basalt rocks.",
    "icon": "ChroniclesOfSwarajya_Art/00_ArtStyle/option_b_palette.png",
    "stats": {
      "def": 2,
      "speedBonus": 8,
      "dodgeWindow": 0.04
    },
    "stackable": false,
    "sellValue": 20,
    "buyValue": 45
  },
  "salve_healing": {
    "id": "salve_healing",
    "name": "Sahyadri Herbal Healing Salve",
    "category": "consumable",
    "slot": null,
    "tier": 1,
    "description": "Potent medicinal paste prepared by village elders from crushed neem leaves and wild mountain honey. Restores 50 HP immediately.",
    "icon": "ChroniclesOfSwarajya_Art/07_TerrainTiles/grass_tiles.png",
    "effect": {
      "healHp": 50
    },
    "stackable": true,
    "maxStack": 10,
    "sellValue": 5,
    "buyValue": 15
  },
  "key_kot_fort": {
    "id": "key_kot_fort",
    "name": "Kot Fort Gateway Key",
    "category": "quest_item",
    "slot": null,
    "tier": 1,
    "description": "Heavy wrought-iron key recovered from the enemy outpost commander. Unlocks the monumental ironwood gate of Kot Fort.",
    "icon": "ChroniclesOfSwarajya_Art/10_FortArchitecture/fort_gates.png",
    "stackable": false,
    "sellValue": 0,
    "buyValue": 0
  }
};

const CRAFTING_RECIPES = [
  {
    "id": "craft_talwar_basic",
    "outputItem": "talwar_basic",
    "outputQty": 1,
    "station": "field_or_anvil",
    "unlockedByDefault": true,
    "costs": {
      "wood_sagwan": 4,
      "ore_iron": 3,
      "gold_huns": 0
    },
    "description": "Forge the first steel talwar using gathered teak wood and hematite ore from the forest."
  },
  {
    "id": "craft_dhal_shield_basic",
    "outputItem": "dhal_shield_basic",
    "outputQty": 1,
    "station": "field_or_anvil",
    "unlockedByDefault": true,
    "costs": {
      "wood_sagwan": 3,
      "leather_hide": 2,
      "ore_iron": 1,
      "gold_huns": 0
    },
    "description": "Construct a light Maratha dhal buckler reinforced with brass and iron studs."
  },
  {
    "id": "craft_leather_brigandine",
    "outputItem": "armour_leather_brigandine",
    "outputQty": 1,
    "station": "field_or_anvil",
    "unlockedByDefault": true,
    "costs": {
      "leather_hide": 4,
      "ore_iron": 2,
      "gold_huns": 5
    },
    "description": "Stitch overlapping iron plates inside a tough leather vest (+10 DEF, +20 Max HP)."
  },
  {
    "id": "craft_spear_bamboo",
    "outputItem": "spear_bamboo",
    "outputQty": 1,
    "station": "field_or_anvil",
    "unlockedByDefault": true,
    "costs": {
      "wood_sagwan": 4,
      "ore_iron": 2,
      "gold_huns": 0
    },
    "description": "Affix a sharpened steel spearhead to a long resilient timber shaft."
  },
  {
    "id": "craft_bow_composite",
    "outputItem": "bow_composite",
    "outputQty": 1,
    "station": "field_or_anvil",
    "unlockedByDefault": true,
    "costs": {
      "wood_sagwan": 5,
      "leather_hide": 3,
      "gold_huns": 5
    },
    "description": "Fashion a composite recurve hunting bow strung with cured sinew."
  },
  {
    "id": "craft_salve_healing",
    "outputItem": "salve_healing",
    "outputQty": 2,
    "station": "field_or_anvil",
    "unlockedByDefault": true,
    "costs": {
      "wood_sagwan": 1,
      "gold_huns": 2
    },
    "description": "Prepare soothing herbal compresses using mountain herbs and natural resins."
  },
  {
    "id": "upgrade_talwar_pattisa",
    "outputItem": "talwar_upgraded",
    "outputQty": 1,
    "station": "village_blacksmith",
    "unlockedByDefault": false,
    "unlockCondition": "village_liberated",
    "costs": {
      "talwar_basic": 1,
      "ore_iron": 6,
      "gold_huns": 25
    },
    "description": "Refine the basic talwar at the village forge into a lethal double-fullered Pattisa (+32 ATK)."
  },
  {
    "id": "craft_khanda_heavy",
    "outputItem": "heavy_curved_sword",
    "outputQty": 1,
    "station": "village_blacksmith",
    "unlockedByDefault": false,
    "unlockCondition": "village_liberated",
    "costs": {
      "ore_iron": 10,
      "wood_sagwan": 4,
      "gold_huns": 40
    },
    "description": "Forge a massive Khanda broadsword capable of shattering enemy guard stances (+42 ATK)."
  },
  {
    "id": "upgrade_dhal_iron_banded",
    "outputItem": "dhal_shield_reinforced",
    "outputQty": 1,
    "station": "village_blacksmith",
    "unlockedByDefault": false,
    "unlockCondition": "village_liberated",
    "costs": {
      "dhal_shield_basic": 1,
      "ore_iron": 5,
      "gold_huns": 20
    },
    "description": "Bolt damascened iron bands and heavy rim reinforcement onto the dhal shield (+18 DEF)."
  },
  {
    "id": "craft_chainmail_hauberk",
    "outputItem": "armour_chainmail_zirah",
    "outputQty": 1,
    "station": "village_armourer",
    "unlockedByDefault": false,
    "unlockCondition": "village_liberated",
    "costs": {
      "armour_leather_brigandine": 1,
      "ore_iron": 8,
      "gold_huns": 50
    },
    "description": "Weave interlocking steel rings into a resilient Zirah chainmail hauberk (+22 DEF, +40 Max HP)."
  }
];

const WORLD_REGIONS = {
  "sahyadri_gateway_valley": {
    "id": "sahyadri_gateway_valley",
    "name": "Sahyadri Gateway Valley (Connected Open World)",
    "biome": "Monsoon Teak Forest, Koyna River Valley, Bhavani Nagar, Sahyadri Highlands & Kot Fortress",
    "worldWidth": 120,
    "worldHeight": 70,
    "tileSize": 16,
    "sectorSizeTiles": 8,
    "sectorCols": 15,
    "sectorRows": 9,
    "viewportTarget": {
      "width": 480,
      "height": 270
    },
    "subZones": [
      {
        "id": "forest_clearing",
        "name": "Sacred Awakening Forest",
        "bounds": {
          "x1": 0,
          "y1": 0,
          "x2": 29,
          "y2": 69
        },
        "description": "Lush monsoon teak groves where Shivaji awakens, gathers initial timber and ironstone, and forges his first blade.",
        "musicTrack": "forest_ambient"
      },
      {
        "id": "river_crossing",
        "name": "Koyna River Valley",
        "bounds": {
          "x1": 30,
          "y1": 0,
          "x2": 46,
          "y2": 69
        },
        "description": "Swift mountain river spanned by a main timber footbridge and a northern shallow stone ford.",
        "musicTrack": "river_ambient"
      },
      {
        "id": "sahyadri_highlands",
        "name": "Sahyadri Highlands",
        "bounds": {
          "x1": 47,
          "y1": 0,
          "x2": 76,
          "y2": 14
        },
        "description": "Rugged basalt cliff switchbacks and wind-swept mountain passes overlooking the Koyna basin.",
        "musicTrack": "highland_winds"
      },
      {
        "id": "abandoned_mine_approach",
        "name": "Highland Abandoned Mine Entrance",
        "bounds": {
          "x1": 77,
          "y1": 0,
          "x2": 92,
          "y2": 37
        },
        "description": "Craggy ironstone ridge housing the timber-shored entrance to the subterranean Sahyadri iron cavern.",
        "musicTrack": "highland_winds"
      },
      {
        "id": "village_bhavani_nagar",
        "name": "Bhavani Nagar & Countryside",
        "bounds": {
          "x1": 47,
          "y1": 15,
          "x2": 76,
          "y2": 37
        },
        "description": "Settled Maratha village featuring a stone well, elder's wada, blacksmith forge, and surrounding countryside trails.",
        "musicTrack": "village_theme"
      },
      {
        "id": "raider_outpost",
        "name": "Deshmukh Raider Outpost",
        "bounds": {
          "x1": 47,
          "y1": 38,
          "x2": 92,
          "y2": 69
        },
        "description": "Hostile forward military encampment threatening Bhavani Nagar and guarding the southern supply road to Kot Fort.",
        "musicTrack": "tension_combat"
      },
      {
        "id": "kot_fort_approach",
        "name": "Kot Fort Citadel & Approach",
        "bounds": {
          "x1": 93,
          "y1": 0,
          "x2": 119,
          "y2": 69
        },
        "description": "Monumental basalt walls, the iron-spiked Dilli Darwaja gate, fortified courtyard, and high Buruj flagstaff.",
        "musicTrack": "fortress_march"
      }
    ]
  },
  "sahyadri_iron_cavern": {
    "id": "sahyadri_iron_cavern",
    "name": "Highland Abandoned Iron Mine (Interior Region)",
    "biome": "Subterranean Basalt & Wootz Iron Cavern",
    "isInterior": true,
    "playableInCurrentStep": false,
    "worldWidth": 40,
    "worldHeight": 25,
    "tileSize": 16,
    "parentRegionId": "sahyadri_gateway_valley",
    "entranceWorldPos": {
      "x": 1360,
      "y": 144
    },
    "surfaceReturnPos": {
      "x": 1360,
      "y": 168
    },
    "description": "Registered 40x25 underground mine interior for future subterranean exploration, rare ore mining, and return-to-surface transitions."
  }
};

const MISSIONS_DATABASE = [
  {
    "id": "quest_1_awakening_and_forge",
    "title": "Act I: The Divine Spark & Forest Forging",
    "location": "forest_clearing",
    "giver": "Divine Memory of Goddess Bhavani",
    "prerequisites": [],
    "objectives": [
      {
        "id": "gather_materials",
        "desc": "Gather 4 Sagwan Teak Wood & 3 Ironstone Ore",
        "current": 0,
        "target": 7
      },
      {
        "id": "craft_talwar",
        "desc": "Forge the Steel Talwar via the Field Crafting Anvil [C]",
        "completed": false
      }
    ],
    "rewards": {
      "xp": 100,
      "gold": 15,
      "unlockedRecipe": "craft_dhal_shield_basic"
    },
    "worldStateChanges": {
      "forestCleared": true
    }
  },
  {
    "id": "quest_2_cross_river_to_village",
    "title": "Act II: The Journey to Bhavani Nagar",
    "location": "river_crossing",
    "giver": "Mavala Scout",
    "prerequisites": [
      "quest_1_awakening_and_forge"
    ],
    "objectives": [
      {
        "id": "cross_bridge",
        "desc": "Cross the Koyna Stream Timber Footbridge eastward",
        "completed": false
      },
      {
        "id": "reach_village",
        "desc": "Discover and enter Bhavani Nagar village",
        "completed": false
      }
    ],
    "rewards": {
      "xp": 150,
      "gold": 20
    },
    "worldStateChanges": {
      "villageDiscovered": true
    }
  },
  {
    "id": "quest_3_liberate_village",
    "title": "Act III: Liberation of Bhavani Nagar",
    "location": "raider_camp",
    "giver": "Village Elder",
    "prerequisites": [
      "quest_2_cross_river_to_village"
    ],
    "objectives": [
      {
        "id": "clear_raider_patrols",
        "desc": "Defeat the 4 enemy sentries assaulting the southern road",
        "current": 0,
        "target": 4
      },
      {
        "id": "defeat_raider_captain",
        "desc": "Defeat the Raider Subedar Captain and secure the Camp",
        "completed": false
      }
    ],
    "rewards": {
      "xp": 350,
      "gold": 50,
      "item": "key_kot_fort"
    },
    "worldStateChanges": {
      "villageLiberated": true,
      "blacksmithUnlocked": true,
      "armourerUnlocked": true,
      "raiderCampSecured": true
    }
  },
  {
    "id": "quest_4_storm_kot_fort",
    "title": "Act IV: Storming Kot Fort",
    "location": "kot_fort_approach",
    "giver": "Village Blacksmith & Mavala Allies",
    "prerequisites": [
      "quest_3_liberate_village"
    ],
    "objectives": [
      {
        "id": "unlock_citadel_gate",
        "desc": "Use the recovered Fort Key to breach the Dilli Darwaja gate",
        "completed": false
      },
      {
        "id": "defeat_citadel_garrison",
        "desc": "Overcome the elite shield guards defending the bastion",
        "current": 0,
        "target": 3
      },
      {
        "id": "hoist_bhagwa_zenda",
        "desc": "Hoist the Saffron Bhagwa Zenda banner over the highest Buruj",
        "completed": false
      }
    ],
    "rewards": {
      "xp": 600,
      "gold": 100,
      "title": "Chhatrapati of Kot Fort"
    },
    "worldStateChanges": {
      "kotFortLiberated": true,
      "routesSecured": true,
      "strongholdEstablished": true
    }
  }
];
