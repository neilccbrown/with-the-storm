# To update requirements.txt, run:
#   rm requirements.txt ; pigar generate --enable-feature requirement-annotations
from enum import IntEnum
import json
import os.path
from pathlib import Path
from queue import Queue
import tkinter as tk
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from resources import *
from buildings import *

save_file_path = os.path.expandvars("%userprofile%\\appdata\\locallow\\Eremite Games\\Against the Storm\\Save.save")

window = tk.Tk()
window.title("With the Storm")

class Availability(IntEnum):
    never_available = 1 # No way it can be available; raw resource not on map, or blueprints unavailable for crafting
    with_blueprint = 2 # Can only be crafted if future (but available) blueprints are unlocked
    #if_crafted = 3 # Can be made if you build the right currently available buildings
    available = 4 # Available right now as an output of one of your buildings

content = tk.Text()
content.tag_configure(Availability.available.name, foreground="#000")
content.tag_configure(Availability.never_available.name, foreground="#ddd")
content.tag_configure(Availability.with_blueprint.name, foreground="#0cc")
#content.tag_configure(Availability.if_crafted.name, foreground="#800")
content.tag_configure("error", foreground="#f00")

def load():
    content.delete(1.0, "end")

    try:
        with open(save_file_path, "r") as f:
            save = json.load(f)

        # Find all the resource nodes on the level and infer the resource type (see resources.py):
        resources = [WOOD, CLEARANCE, DRIZZLE, STORM]
        for glade in save["world"]["glades"]:
            if len(glade["fields"]) > 0:
                resources.append(FARM_FIELD)
                break

        for resource in save["world"]["resourcesDeposits"]:
            resource_type = resource["Value"]["model"]
            resource_name = ""
            for resource_tag in RESOURCE_NODE_TO_NAME.keys():
                if resource_tag in resource_type:
                    resource_name = RESOURCE_NODE_TO_NAME[resource_tag]
                    break
            if resource_name:
                resources.append(resource_name)
            else:
                raise Exception("Unknown resource type: " + resource_type)

        content.insert("end", "Resources on map:\n    ")
        for resource in list(set(resources)):
            content.insert("end", resource + ", ", "available")
        content.insert("end", "\n")

        available_buildings = []
        for building in save["content"]["buildings"]:
            if building in BUILDINGS_TO_RECIPES:
                available_buildings.append(building)
            else:
                raise Exception("Unknown building: " + building)

        # For now, just assume all blueprints are available:
        available_blueprints = BUILDINGS_TO_RECIPES

        content.insert("end", "Available buildings:\n    ")
        for building in list(set(available_buildings)):
            if len(BUILDINGS_TO_RECIPES[building]) > 0:
                content.insert("end", building + ", ", "available")
        content.insert("end", "\n\n")

        current_choice = []

        # Find the current offer of blueprints:
        for option in save["reputationRewards"]["currentPick"]["options"]:
            if option["building"] in BUILDINGS_TO_RECIPES:
                current_choice.append(option["building"])
            else:
                raise Exception("Unknown building type: " + option["building"])

        cached_availability = {}

        def input_availability(input: And | Or | tuple[int, str], checked_buildings: list[tuple[str, str]]) -> Availability:
            match input:
                case And(items):
                    # Assume all available until proven otherwise
                    worst = Availability.available
                    for item in items:
                        worst = min(worst, input_availability(item, checked_buildings))
                    return worst
                case Or(items):
                    best = Availability.never_available
                    for item in items:
                        best = max(best, input_availability(item, checked_buildings))
                    return best
                case (n, target):
                    return availability(target, checked_buildings)

        def availability(name: str, checked_buildings: list[tuple[str,str]]) -> Availability:
            if name in cached_availability:
                return cached_availability[name]

            best = Availability.never_available
            # Farm fields don't have a collector, they are implicitly available to buildings that consume them:
            if name == FARM_FIELD:
                if name in resources:
                    return Availability.available
                else:
                    return Availability.never_available

            # Check if we have a raw collector for that resource:
            if name in resources:
                for building_name, recipes in BUILDINGS_TO_RECIPES.items():
                    for recipe in recipes:
                        if not isinstance(recipe, tuple) and recipe == name:
                            if building_name in available_buildings:
                                best = max(best, Availability.available)
                            elif building_name in available_blueprints:
                                best = max(best, Availability.with_blueprint)

            # Check if currently craftable all the way down
            # Start by looking through all buildings and all recipes to find end product:
            checked_buildings = checked_buildings.copy()
            for building_name, recipes in BUILDINGS_TO_RECIPES.items():
                for recipe in recipes:
                    # Only look at production buildings, not raw gatherers (which are already checked above):
                    if isinstance(recipe, tuple):
                        # Check RHS (outcome):
                        if recipe[1][1] == name:
                            if (building_name, name) in checked_buildings:
                                continue
                            else:
                                checked_buildings.append((building_name, name))
                            # It's a recipe for the good we want!
                            # Go through LHS (ingredients):
                            recipe_input_availability = input_availability(recipe[0], checked_buildings)
                            match recipe_input_availability:
                                case Availability.never_available:
                                    pass
                                case Availability.with_blueprint:
                                    best = max(best, Availability.with_blueprint)
                                case other:
                                    if building_name in available_buildings:
                                        best = max(best, recipe_input_availability)
                                    elif building_name in available_blueprints:
                                        best = max(best, Availability.with_blueprint)
            cached_availability[name] = best
            return best

        def insert_ingredient(t: tk.Text, item: And | Or | tuple[int, str]) -> Availability:
            match item:
                case And(items):
                    worst = Availability.available
                    t.insert("end", "(")
                    for n, item in enumerate(items):
                        if n > 0:
                            t.insert("end", " & ")
                        worst = min(worst, insert_ingredient(t, item))

                    t.insert("end", ")")
                    return worst
                case Or(items):
                    best = Availability.never_available
                    t.insert("end", "(")
                    for n, item in enumerate(items):
                        if n > 0:
                            t.insert("end", " | ")
                        best = max(best, insert_ingredient(t, item))

                    t.insert("end", ")")
                    return best
                case (n, name):
                    #print("Calculating availability of " + name)
                    a = availability(name, [])
                    t.insert("end", name, a.name)
                    return a

        for o in current_choice:
            content.insert("end", f"{o}\n")
            for recipe in BUILDINGS_TO_RECIPES[o]:
                content.insert("end", f" \u2022 ")
                try:
                    if isinstance(recipe, str):
                        insert_ingredient(content, (1, recipe))
                        content.insert("end", "\n")
                    else:
                        cur_index = content.index("end-1c")
                        a = insert_ingredient(content, recipe[0])
                        content.insert(cur_index, " \u2190 ")
                        content.insert(cur_index, f"{str(recipe[1])}", a.name)
                        content.insert("end", "\n")

                except Exception as e:
                    content.insert("end", f"{e}", "error")

        content.insert("end", "Key:\n")
        for a in Availability:
            content.insert("end", "    \u2022 ")
            match a:
                case Availability.never_available:
                    content.insert("end", a.name + ": No way it can be available on this map", a.name)
                case Availability.with_blueprint:
                    content.insert("end", a.name + ": Available only if you unlock the right blueprint in future", a.name)
                #case Availability.if_crafted:
                    #content.insert("end", a.name + ": Available if you build the right currently available building", a.name)
                case Availability.available:
                    content.insert("end", a.name + ": Available with the currently available set of buildings", a.name)
            content.insert("end", "\n")

    except Exception as e:
        content.insert("end", f"{e}", "error")
load()
content.pack(fill=tk.BOTH, expand=True)

queue = Queue()

class MyFieldSystemEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        queue.put(event)
        window.event_generate("<<WatchdogEvent>>", when="tail")

observer = Observer()
observer.schedule(MyFieldSystemEventHandler(), Path(save_file_path).parent.absolute())
observer.start()

def handle_watchdog_event(event):
    watchdog_event = queue.get()
    load()

window.bind("<<WatchdogEvent>>", handle_watchdog_event)


window.mainloop()

#if len(sys.argv) > 1:
#    # Use given screenshot file for testing:
#    process(cv2.imread(sys.argv[1]))
#else:
#    # Listen for shortcut and take screenshot:
#    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#        listener.join()