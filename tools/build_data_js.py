import os
import json
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def build_data_js():
    with open('data/items.json', 'r', encoding='utf-8') as f:
        items = json.load(f)
    with open('data/crafting_recipes.json', 'r', encoding='utf-8') as f:
        recipes = json.load(f)
    with open('data/world_regions.json', 'r', encoding='utf-8') as f:
        regions = json.load(f)
    with open('data/missions.json', 'r', encoding='utf-8') as f:
        missions = json.load(f)

    js_content = f"""// Chronicles of Swarajya: Master Data Registries
// Auto-generated from data/*.json

const ITEM_DATABASE = {json.dumps(items['items'], indent=2)};

const CRAFTING_RECIPES = {json.dumps(recipes['recipes'], indent=2)};

const WORLD_REGIONS = {json.dumps(regions['regions'], indent=2)};

const MISSIONS_DATABASE = {json.dumps(missions['missions'], indent=2)};
"""
    with open('data/data_registries.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("✅ Created data/data_registries.js successfully!")

if __name__ == "__main__":
    build_data_js()
