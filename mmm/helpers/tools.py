import os
import re
import json


def get_minecraft_version():
    current_dir = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
    minecraft_version = os.path.basename(parent_dir)
    if re.search(r'(\d+)\.(\d+)(\.\d+)?', minecraft_version):
        return minecraft_version
    else:
        return None
    
def initial_message():
    print("\nWelcome to the mods.json setup wizard.")
    print("This tool will guide you through creating a mods.json file for your Minecraft modpack.")
    print("You only need to provide a Minecraft version and Mod Loader if you are not planning to distribute the modpack.")
    print("For more detailed information, use `mmm init --help`.\n")
    print("Once the setup is complete, use `mmm install <mod_name>` to install mods.")
    print("Press Ctrl+C at any time to exit this wizard.\n")
    
def confirm_mods_json(json_data):
    print(json.dumps(json_data, indent=4))
    user_confirmation = input("\nIs this information correct? (y/n) :")
    return yes_or_no(user_confirmation)

def confirm_overwrite():
    if os.path.exists("mods.json"):
        print("mods.json already exists. You can use --force or -f to overwrite it.")
        overwrite_confirmation = input("Are you sure you want to overwrite it? (y/n)")
        first_confirmation = yes_or_no(overwrite_confirmation)
        if first_confirmation:
            final_confirmation = input("You will lose all of your mod info in your mods.json file. Are you really sure? (y/n)")
            final_decision = yes_or_no(final_confirmation)
            return final_decision
    else:
        return True
    
def yes_or_no(answer, type=None):
    
    valid_answers = ["y", "n", ""]
    prompt = "Please enter 'y' or 'n': "
    if type == "next":
        valid_answers.append("s")
        prompt = "Please enter 'y', 'n', or 's':"
    
    while answer.strip().lower() not in valid_answers:
        answer = input(prompt).strip().lower()
    
    if answer == "s":
        return "skip"
    
    return answer in ["y", ""]


        

        

