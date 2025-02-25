import os
import sys
import time
import random
import datetime
import itertools
import re
import json
from typing import List, Dict, Set, Tuple, Any, Optional
from pathlib import Path


# ===== UTILITY FUNCTIONS =====

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')


def print_banner():
    """Display a stylish banner for the tool."""
    banner = """
    ██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
    ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
    ██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
    ██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
    ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                         
    """
    
    print("\033[1;36m" + banner + "\033[0m")  # Cyan color for the banner
    print("\033[1;32m" + "  Original by: Sambhav Mehra" + "\033[0m")  # Green color for author
    print("\033[1;32m" + "  Follow on Instagram: sambhav@7" + "\033[0m")  # Green color for social
    print("\033[1;33m" + "  Enhanced Edition with Platform-Specific Patterns" + "\033[0m")  # Yellow color for enhanced note
    print("\033[1;31m" + "\n  [!] Use for educational purposes only. Be ethical.\n" + "\033[0m")  # Red color for warning


def typing_print(text, delay=0.03):
    """Print text with a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_progress_bar(current, total, bar_length=50):
    """Display a progress bar."""
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * bar_length - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write('\r\033[1;32m[%s%s] %d%%\033[0m' % (arrow, spaces, percent))
    sys.stdout.flush()


def show_spinner(message, duration=3):
    """Show a spinner for the given duration."""
    spinner = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    end_time = time.time() + duration
    i = 0
    
    while time.time() < end_time:
        i = (i + 1) % len(spinner)
        sys.stdout.write(f"\r\033[1;32m[{spinner[i]}] {message}\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
    
    sys.stdout.write(f"\r\033[1;32m[+] {message} Complete!\033[0m" + " " * 20 + "\n")


# ===== USER INTERFACE FUNCTIONS =====

def get_platforms() -> Dict[str, str]:
    """Return a dictionary of supported platforms and their descriptions."""
    return {
        "1": "Instagram",
        "2": "Facebook",
        "3": "Twitter/X",
        "4": "TikTok",
        "5": "Snapchat",
        "6": "LinkedIn",
        "7": "YouTube",
        "8": "Pinterest",
        "9": "Reddit",
        "10": "Discord",
        "11": "Twitch",
        "12": "GitHub",
        "13": "Steam",
        "14": "PlayStation Network",
        "15": "Microsoft/Xbox",
        "0": "Custom/Other"
    }


def display_platforms(platforms: Dict[str, str]):
    """Display the available platforms in a formatted way."""
    print("\033[1;33m" + "\n[+] Available Platforms:" + "\033[0m")
    
    # Calculate the number of columns based on terminal width
    term_width = os.get_terminal_size().columns
    num_columns = max(1, term_width // 30)
    
    # Create a list of platform entries
    platform_entries = [f"  \033[1;36m[{key}]\033[0m \033[1;37m{platform}\033[0m" 
                       for key, platform in platforms.items()]
    
    # Display in columns
    for i in range(0, len(platform_entries), num_columns):
        print("".join(platform_entries[i:i+num_columns]))


def get_user_input(prompt: str, allow_empty: bool = False, 
                  default: str = "", validator: callable = None) -> str:
    """
    Get user input with proper validation.
    
    Parameters:
    - prompt: The prompt to display
    - allow_empty: Whether empty input is allowed
    - default: Default value if input is empty
    - validator: Optional function to validate input
    """
    display_default = f" [{default}]" if default else ""
    
    while True:
        value = input(f"\033[1;34m{prompt}{display_default}: \033[0m").strip()
        
        if not value:
            if default:
                return default
            if allow_empty:
                return ""
            print("\033[1;31m[!] This field cannot be empty. Please try again.\033[0m")
            continue
        
        if validator and not validator(value):
            continue
            
        return value


def get_date_input(prompt: str, allow_empty: bool = True) -> Dict:
    """Get date input with validation and return in multiple formats."""
    while True:
        date_str = get_user_input(prompt, allow_empty)
        
        if not date_str and allow_empty:
            return {}
        
        try:
            # Try different date formats
            for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y", "%Y-%m-%d", "%Y/%m/%d"):
                try:
                    date = datetime.datetime.strptime(date_str, fmt)
                    # Return in multiple formats for wordlist generation
                    return {
                        "raw": date_str,
                        "day": date.day,
                        "month": date.month,
                        "year": date.year,
                        "dmy": f"{date.day}{date.month}{date.year}",
                        "mdy": f"{date.month}{date.day}{date.year}",
                        "ymd": f"{date.year}{date.month}{date.day}",
                        "ddmmyyyy": f"{date.day:02d}{date.month:02d}{date.year}",
                        "mmddyyyy": f"{date.month:02d}{date.day:02d}{date.year}",
                        "yyyymmdd": f"{date.year}{date.month:02d}{date.day:02d}",
                        "dd": f"{date.day:02d}",
                        "mm": f"{date.month:02d}",
                        "yyyy": f"{date.year}",
                        "yy": f"{date.year % 100:02d}"
                    }
                except ValueError:
                    continue
            
            raise ValueError("Invalid date format")
        
        except ValueError:
            print("\033[1;31m[!] Invalid date format. Please use DD/MM/YYYY, DD-MM-YYYY, or YYYY-MM-DD\033[0m")


def collect_additional_words() -> List[str]:
    """Collect additional words from the user."""
    words = []
    print("\n\033[1;33m[+] Enter additional words (one per line, leave empty to finish):\033[0m")
    print("\033[0;37m  Examples: nicknames, places, hobbies, favorite artists, sports teams\033[0m")
    
    while True:
        word = input("  > ").strip()
        if not word:
            break
        words.append(word)
    
    return words


def get_multiple_choice(prompt: str, options: Dict[str, str], 
                        allow_multiple: bool = False) -> List[str]:
    """Get multiple choice input from user."""
    print(f"\n\033[1;33m{prompt}\033[0m")
    
    for key, option in options.items():
        print(f"  \033[1;36m[{key}]\033[0m \033[1;37m{option}\033[0m")
    
    if allow_multiple:
        instruction = "\n\033[1;34m[?] Select options (comma-separated, e.g., 1,3,5): \033[0m"
    else:
        instruction = "\n\033[1;34m[?] Select an option: \033[0m"
    
    while True:
        response = input(instruction).strip()
        
        if not allow_multiple:
            if response in options:
                return [options[response]]
            print("\033[1;31m[!] Invalid selection. Please try again.\033[0m")
        else:
            selected = []
            invalid = False
            
            for choice in response.split(','):
                choice = choice.strip()
                if choice in options:
                    selected.append(options[choice])
                else:
                    print(f"\033[1;31m[!] Invalid option: {choice}\033[0m")
                    invalid = True
                    break
            
            if not invalid and selected:
                return selected
            elif not invalid:
                print("\033[1;31m[!] Please select at least one option.\033[0m")


def get_complexity_options() -> Dict[str, bool]:
    """Get password complexity preferences from user."""
    complexity = {}
    
    options = {
        "1": "Include numbers (0-9)",
        "2": "Include special characters (!@#$%^&*)",
        "3": "Include uppercase letters",
        "4": "Include common leetspeak substitutions (a→4, e→3, etc.)",
        "5": "Include year variations (2020-2025)",
        "6": "Include extra-complex combinations"
    }
    
    selected = get_multiple_choice(
        "[+] Password Complexity Options:", 
        options, 
        allow_multiple=True
    )
    
    complexity["numbers"] = "Include numbers (0-9)" in selected
    complexity["special_chars"] = "Include special characters (!@#$%^&*)" in selected
    complexity["uppercase"] = "Include uppercase letters" in selected
    complexity["leetspeak"] = "Include common leetspeak substitutions (a→4, e→3, etc.)" in selected
    complexity["years"] = "Include year variations (2020-2025)" in selected
    complexity["complex_combos"] = "Include extra-complex combinations" in selected
    
    return complexity


def get_wordlist_size_pref() -> str:
    """Get user preference for wordlist size."""
    options = {
        "1": "Small (fewer, more targeted passwords)",
        "2": "Medium (balanced approach)",
        "3": "Large (comprehensive, but may include unlikely passwords)"
    }
    
    selected = get_multiple_choice(
        "[+] Wordlist Size Preference:", 
        options, 
        allow_multiple=False
    )
    
    return selected[0].split(" ")[0].lower()


def validate_username(value: str) -> bool:
    """Validate a username."""
    if not re.match(r'^[a-zA-Z0-9._-]+$', value):
        print("\033[1;31m[!] Username should only contain letters, numbers, dots, underscores, and hyphens.\033[0m")
        return False
    return True


# ===== WORDLIST GENERATION FUNCTIONS =====

def get_platform_patterns(platform: str) -> Dict[str, Any]:
    """Get platform-specific patterns for wordlist generation."""
    patterns = {
        "Instagram": {
            "max_length": 30,
            "common_patterns": [
                "{username}", "{firstname}{lastname}", "{firstname}_{lastname}",
                "{firstname}.{lastname}", "{firstname}{yy}", "{firstname}{birthyear}",
                "{name}_photography", "{name}_official", "{name}_real", "real_{name}",
                "_{username}_", "{name}.{birthyear}", "the{name}", "{name}the",
                "{name}{random_num}", "{firstinitial}{lastname}"
            ],
            "common_suffixes": ["official", "real", "_", ".__", "._.", 
                                "photography", "photo", "gram", "igdaily"],
            "leet_replacements": True,
            "username_requirements": {
                "max_length": 30,
                "allowed_chars": "letters, numbers, periods, and underscores"
            }
        },
        "Facebook": {
            "max_length": 50,
            "common_patterns": [
                "{firstname}{lastname}", "{firstname}.{lastname}", 
                "{firstinitial}{lastname}", "{firstname}{lastinitial}",
                "{firstname}{birthyear}", "{name}{random_num}",
                "{firstname}.{lastname}.{birthyear}"
            ],
            "common_suffixes": ["fb", "facebook", "{birthyear}"],
            "leet_replacements": False,
            "username_requirements": {
                "min_length": 5,
                "allowed_chars": "letters, numbers, and periods"
            }
        },
        "Twitter/X": {
            "max_length": 15,
            "common_patterns": [
                "{username}", "{name}_{random_num}", "_{name}_", 
                "{firstname}{lastname}", "{firstinitial}{lastname}",
                "{name}{birthyear}", "{name}_{birthyear}", "real{name}",
                "{name}official", "{name}_{locations[0]}"
            ],
            "common_suffixes": ["_x", "_twitter", "official", "real", "_"],
            "leet_replacements": True,
            "username_requirements": {
                "max_length": 15,
                "allowed_chars": "letters, numbers, and underscores"
            }
        },
        "TikTok": {
            "max_length": 24,
            "common_patterns": [
                "{username}", "{name}.tt", "{name}_tt", "{name}{birthyear}",
                "{name}_{random_num}", "{name}.{random_num}", 
                "{firstname}_{lastname}", "{name}_official",
                "{name}_tiktok", "tiktok_{name}", "{name}.tiktok"
            ],
            "common_suffixes": ["tt", "tiktok", "_", ".", "official", "{random_num}"],
            "leet_replacements": True,
            "username_requirements": {
                "min_length": 2,
                "max_length": 24,
                "allowed_chars": "letters, numbers, underscores, and periods"
            }
        },
        "Snapchat": {
            "max_length": 15,
            "common_patterns": [
                "{username}", "{name}snap", "snap{name}", 
                "{name}{birthyear}", "{name}_{random_num}",
                "{firstname}{lastname}", "{firstinitial}{lastname}",
                "{name}_sc", "sc_{name}", "{name}.sc"
            ],
            "common_suffixes": ["snap", "sc", "ghost", "{random_num}", "{birthyear}"],
            "leet_replacements": True,
            "username_requirements": {
                "max_length": 15,
                "allowed_chars": "letters, numbers, and underscores"
            }
        },
        "LinkedIn": {
            "max_length": 100,
            "common_patterns": [
                "{firstname}{lastname}", "{firstname}-{lastname}",
                "{firstinitial}{lastname}", "{firstname}{lastinitial}",
                "{firstname}.{lastname}", "{name}-{profession}"
            ],
            "common_suffixes": ["pro", "linkedin", "{profession}"],
            "leet_replacements": False,
            "username_requirements": {
                "min_length": 3,
                "max_length": 100,
                "allowed_chars": "letters, numbers, hyphens, and underscores"
            }
        },
        "YouTube": {
            "max_length": 30,
            "common_patterns": [
                "{username}", "{name}TV", "{name}Channel", 
                "{name}Tube", "{name}Official", "Official{name}",
                "{firstname}{lastname}", "{name}{birthyear}",
                "{name}_{profession}", "{profession}_{name}"
            ],
            "common_suffixes": ["TV", "Channel", "Tube", "YT", "Official", "Gaming"],
            "leet_replacements": True,
            "username_requirements": {
                "max_length": 30,
                "allowed_chars": "letters, numbers, underscores, hyphens, and periods"
            }
        },
        "Pinterest": {
            "max_length": 30,
            "common_patterns": [
                "{username}", "{firstname}{lastname}", 
                "{name}pins", "pins{name}", "{name}_{profession}",
                "{profession}_{name}", "{name}{birthyear}"
            ],
            "common_suffixes": ["pins", "boards", "ideas", "diy", "crafts"],
            "leet_replacements": False,
            "username_requirements": {
                "max_length": 30,
                "allowed_chars": "letters, numbers, underscores, and periods"
            }
        },
        "Reddit": {
            "max_length": 20,
            "common_patterns": [
                "{username}", "{name}_reddit", "reddit_{name}",
                "{name}_{random_num}", "{name}{birthyear}",
                "_{name}_", "{firstname}{lastname}", 
                "{name}_{interest[0]}", "{interest[0]}_{name}"
            ],
            "common_suffixes": ["reddit", "_", "throwaway", "official", "real", "PM_ME"],
            "leet_replacements": True,
            "username_requirements": {
                "min_length": 3,
                "max_length": 20,
                "allowed_chars": "letters, numbers, underscores, and hyphens"
            }
        },
        "Discord": {
            "max_length": 32,
            "common_patterns": [
                "{username}", "{name}#{random_num}", 
                "{name}_{random_num}", "{name}{random_num}",
                "{name}_{interest[0]}", "{interest[0]}_{name}",
                "{name}_discord", "discord_{name}"
            ],
            "common_suffixes": ["gaming", "gamer", "player", "discord", "#", "{random_num}"],
            "leet_replacements": True,
            "username_requirements": {
                "min_length": 2,
                "max_length": 32,
                "allowed_chars": "letters, numbers, underscores, periods, hyphens"
            }
        },
        "Twitch": {
            "max_length": 25,
            "common_patterns": [
                "{username}", "{name}_tv", "tv_{name}",
                "{name}gaming", "gaming{name}", "{name}stream",
                "{name}_{interest[0]}", "{name}_{random_num}",
                "{name}live", "live{name}"
            ],
            "common_suffixes": ["tv", "gaming", "stream", "twitch", "live", "plays"],
            "leet_replacements": True,
            "username_requirements": {
                "min_length": 4,
                "max_length": 25,
                "allowed_chars": "letters, numbers, and underscores"
            }
        },
        "GitHub": {
            "max_length": 39,
            "common_patterns": [
                "{username}", "{firstname}{lastname}", 
                "{firstinitial}{lastname}", "{name}dev",
                "dev{name}", "{name}code", "code{name}",
                "{name}-{profession}", "{profession}-{name}"
            ],
            "common_suffixes": ["dev", "code", "git", "hub", "io"],
            "leet_replacements": True,
            "username_requirements": {
                "max_length": 39,
                "allowed_chars": "letters, numbers, hyphens"
            }
        },
        "Steam": {
            "max_length": 32,
            "common_patterns": [
                "{username}", "{name}gaming", "gaming{name}",
                "{name}player", "player{name}", "{name}_{random_num}",
                "{name}{birthyear}", "{name}_{interest[0]}"
            ],
            "common_suffixes": ["gaming", "gamer", "player", "steam", "{random_num}"],
            "leet_replacements": True,
            "username_requirements": {
                "min_length": 3,
                "max_length": 32,
                "allowed_chars": "letters, numbers, and special characters"
            }
        },
        "PlayStation Network": {
            "max_length": 16,
            "common_patterns": [
                "{username}", "{name}gaming", "gaming{name}",
                "{name}player", "player{name}", "{name}_{random_num}",
                "{name}{birthyear}", "{name}_{interest[0]}",
                "{name}ps", "ps{name}"
            ],
            "common_suffixes": ["ps", "psn", "gaming", "gamer", "player", "{random_num}"],
            "leet_replacements": True,
            "username_requirements": {
                "min_length": 3,
                "max_length": 16,
                "allowed_chars": "letters, numbers, hyphens, and underscores"
            }
        },
        "Microsoft/Xbox": {
            "max_length": 15,
            "common_patterns": [
                "{username}", "{name}xbox", "xbox{name}",
                "{name}gaming", "gaming{name}", "{name}_{random_num}",
                "{name}{birthyear}", "{name}_{interest[0]}",
                "{name}live", "live{name}"
            ],
            "common_suffixes": ["xbox", "live", "gaming", "gamer", "player", "{random_num}"],
            "leet_replacements": True,
            "username_requirements": {
                "min_length": 3,
                "max_length": 15,
                "allowed_chars": "letters, numbers, spaces, and special characters"
            }
        },
        "Custom/Other": {
            "max_length": 50,
            "common_patterns": [
                "{username}", "{firstname}{lastname}", "{firstname}_{lastname}",
                "{name}{birthyear}", "{name}_{random_num}", "{firstinitial}{lastname}"
            ],
            "common_suffixes": ["123", "321", "{birthyear}", "_", "."],
            "leet_replacements": True,
            "username_requirements": {
                "max_length": 50,
                "allowed_chars": "letters, numbers, and special characters"
            }
        }
    }
    
    return patterns.get(platform, patterns["Custom/Other"])


def apply_leet_speak(word: str) -> List[str]:
    """Apply leetspeak transformations to a word."""
    result = [word]
    
    # Define common leetspeak substitutions
    leet_map = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7'],
        'l': ['1'],
        'z': ['2'],
        'g': ['9', '6'],
        'b': ['8']
    }
    
    # Apply leet substitutions with increasing complexity
    for char, replacements in leet_map.items():
        if char in word.lower():
            new_results = []
            for current in result:
                # Keep the original
                new_results.append(current)
                
                # Apply single character substitution
                for replacement in replacements:
                    new_word = current.lower().replace(char, replacement)
                    new_results.append(new_word)
            
            # Only keep a reasonable number of variations
            result = list(set(new_results))[:10]  # Limit to 10 variations
    
    return result


def generate_platform_specific_combinations(user_data: Dict, platform_patterns: Dict, 
                                           complexity: Dict, size_pref: str) -> Set[str]:
    """Generate platform-specific password combinations."""
    wordlist = set()
    
    # Extract basic information
    username = user_data.get("username", "")
    first_name = user_data.get("first_name", "")
    last_name = user_data.get("last_name", "")
    pet_name = user_data.get("pet_name", "")
    father_name = user_data.get("father_name", "")
    partner_name = user_data.get("partner_name", "")
    locations = user_data.get("locations", [])
    profession = user_data.get("profession", "")
    interests = user_data.get("additional_words", [])
    
    # Extract dates if available
    dob = user_data.get("dob", {})
    partner_dob = user_data.get("partner_dob", {})
    
    # Prepare base data for pattern replacement
    name = username or first_name
    firstname = first_name
    lastname = last_name
    birthyear = dob.get("year", "") if dob else ""
    yy = dob.get("yy", "") if dob else ""
    
    firstinitial = first_name[0].lower() if first_name else ""
    lastinitial = last_name[0].lower() if last_name else ""
    
    # Generate random numbers for patterns
    random_nums = [str(i) for i in range(1, 10)] + [str(i) for i in range(10, 100, 10)]
    
    # Apply the patterns from the platform specific rules
    for pattern in platform_patterns["common_patterns"]:
        # Skip patterns that require missing data
        if "{firstname}" in pattern and not first_name:
            continue
        if "{lastname}" in pattern and not last_name:
            continue
        if "{birthyear}" in pattern and not birthyear:
            continue
        if "{profession}" in pattern and not profession:
            continue
        if "{locations[0]}" in pattern and not locations:
            continue
        if "{interest[0]}" in pattern and not interests:
            continue
        
        # Create base word by replacing variables in pattern
        word = pattern
        word = word.replace("{username}", username.lower())
        word = word.replace("{name}", name.lower())
        word = word.replace("{firstname}", firstname.lower())
        word = word.replace("{lastname}", lastname.lower())
        word = word.replace("{firstinitial}", firstinitial)
        word = word.replace("{lastinitial}", lastinitial)
        word = word.replace("{birthyear}", str(birthyear))
        word = word.replace("{yy}", str(yy))
        word = word.replace("{profession}", profession.lower() if profession else "")
        
        # Handle special cases with random elements
        if "{random_num}" in word:
            for num in random_nums:
                variant = word.replace("{random_num}", num)
                if len(variant) <= platform_patterns["max_length"]:
                    wordlist.add(variant)
            continue
            
        if "{locations[0]}" in word and locations:
            variant = word.replace("{locations[0]}", locations[0].lower())
            if len(variant) <= platform_patterns["max_length"]:
                wordlist.add(variant)
            continue
            
        if "{interest[0]}" in word and interests:
            variant = word.replace("{interest[0]}", interests[0].lower())
            if len(variant) <= platform_patterns["max_length"]:
                wordlist.add(variant)
            continue
        
        # Add the base pattern if it's complete
        if "{" not in word and "}" not in word and len(word) <= platform_patterns["max_length"]:
            wordlist.add(word)
    
    # Add variations with suffixes
    base_words = list(wordlist.copy())  # Make a copy since we're modifying wordlist
    
    for base in base_words:
        for suffix in platform_patterns["common_suffixes"]:
            # Handle special suffix cases
            if suffix == "{random_num}":
                for num in random_nums:
                    variant = f"{base}{num}"
                    if len(variant) <= platform_patterns["max_length"]:
                        wordlist.add(variant)
                continue
                
            if suffix == "{birthyear}" and birthyear:
                variant = f"{base}{birthyear}"
                if len(variant) <= platform_patterns["max_length"]:
                    wordlist.add(variant)
                continue
                
            if suffix == "{profession}" and profession:
                variant = f"{base}{profession.lower()}"
                if len(variant) <= platform_patterns["max_length"]:
                    wordlist.add(variant)
                continue
            
            # Add normal suffix
            variant = f"{base}{suffix}"
            if len(variant) <= platform_patterns["max_length"]:
                wordlist.add(variant)
    
    # Apply leetspeak if enabled
    if platform_patterns["leet_replacements"] and complexity["leetspeak"]:
        leet_words = []
        for word in list(wordlist):
            leet_words.extend(apply_leet_speak(word))
        
        # Add leetspeak variations while respecting max length
        for word in leet_words:
            if len(word) <= platform_patterns["max_length"]:
                wordlist.add(word)
    
    # Apply uppercase first letter if enabled
    if complexity["uppercase"]:
        uppercase_words = []
        for word in list(wordlist):
            if word:
                uppercase_words.append(word[0].upper() + word[1:])
        
        for word in uppercase_words:
            if len(word) <= platform_patterns["max_length"]:
                wordlist.add(word)
    
    # Add numbers if enabled
    if complexity["numbers"]:
        num_words = []
        for word in list(wordlist):
            for num in ["1", "12", "123", "1234", "12345", "0", "00"]:
                num_words.append(f"{word}{num}")
        
        for word in num_words:
            if len(word) <= platform_patterns["max_length"]:
                wordlist.add(word)
    
    # Add years if enabled
    if complexity["years"]:
        year_words = []
        current_year = datetime.datetime.now().year
        years = [str(year) for year in range(current_year - 5, current_year + 1)]
        
        for word in list(wordlist):
            for year in years:
                year_words.append(f"{word}{year}")
                year_words.append(f"{word}{year[-2:]}")
        
        for word in year_words:
            if len(word) <= platform_patterns["max_length"]:
                wordlist.add(word)
    
    # Add special characters if enabled
    if complexity["special_chars"]:
        special_words = []
        special_chars = ["!", "@", "#", "$", "%", "&", "*", "?"]
        
        for word in list(wordlist):
            for char in special_chars:
                special_words.append(f"{word}{char}")
                special_words.append(f"{char}{word}")
                if len(word) > 3:  # Only add middle special chars for longer words
                    special_words.append(f"{word[:len(word)//2]}{char}{word[len(word)//2:]}")
        
        for word in special_words:
            if len(word) <= platform_patterns["max_length"]:
                wordlist.add(word)
    
    # Add extra complex combinations if enabled
    if complexity["complex_combos"]:
        complex_words = []
        
        # Mix personal information
        if pet_name and birthyear:
            complex_words.append(f"{pet_name.lower()}{birthyear}")
        if pet_name and dob.get("ddmmyyyy"):
            complex_words.append(f"{pet_name.lower()}{dob.get('ddmmyyyy')}")
        if username and birthyear:
            complex_words.append(f"{username.lower()}{birthyear}")
        if first_name and birthyear and last_name:
            complex_words.append(f"{first_name.lower()}{birthyear}{last_name.lower()}")
        
        # Add more complex combinations
        if partner_name and partner_dob.get("year"):
            complex_words.append(f"{first_name.lower()}{partner_name.lower()}{partner_dob.get('year')}")
        
        if profession and birthyear:
            complex_words.append(f"{profession.lower()}{birthyear}")
        
        for word in complex_words:
            if len(word) <= platform_patterns["max_length"]:
                wordlist.add(word)
    
    # Limit wordlist size based on preference
    if size_pref == "small":
        limit = 1000
    elif size_pref == "medium":
        limit = 5000
    else:  # large
        limit = 10000
    
    # If over the limit, prioritize shorter passwords
    if len(wordlist) > limit:
        return set(sorted(wordlist, key=len)[:limit])
    
    return wordlist


def collect_user_data() -> Dict:
    """Collect user data for wordlist generation."""
    clear_screen()
    print_banner()
    
    user_data = {}
    
    # Platform selection
    platforms = get_platforms()
    display_platforms(platforms)
    platform_choice = get_user_input("[+] Select target platform (enter number)", validator=lambda x: x in platforms)
    user_data["platform"] = platforms[platform_choice]
    
    typing_print(f"\n\033[1;33m[+] Collecting information for {user_data['platform']} wordlist generation...\033[0m")
    
    # Basic information
    user_data["username"] = get_user_input("Target username", allow_empty=True, validator=validate_username)
    user_data["first_name"] = get_user_input("First name", allow_empty=True)
    user_data["last_name"] = get_user_input("Last name", allow_empty=True)
    user_data["pet_name"] = get_user_input("Pet name (if any)", allow_empty=True)
    user_data["father_name"] = get_user_input("Father's name (if known)", allow_empty=True)
    user_data["partner_name"] = get_user_input("Partner's name (if any)", allow_empty=True)
    
    # Dates of birth
    user_data["dob"] = get_date_input("Date of birth (DD/MM/YYYY)")
    if user_data["partner_name"]:
        user_data["partner_dob"] = get_date_input("Partner's date of birth (DD/MM/YYYY)")
    
    # Important locations
    locations = []
    print("\n\033[1;33m[+] Enter important locations (city, country, etc. - one per line, leave empty to finish):\033[0m")
    while True:
        location = input("  > ").strip()
        if not location:
            break
        locations.append(location)
    user_data["locations"] = locations
    
    # Profession
    user_data["profession"] = get_user_input("Profession or occupation", allow_empty=True)
    
    # Additional words
    user_data["additional_words"] = collect_additional_words()
    
    # Complexity options
    user_data["complexity"] = get_complexity_options()
    
    # Wordlist size preference
    user_data["size_pref"] = get_wordlist_size_pref()
    
    return user_data


def save_wordlist(wordlist: List[str], platform: str, custom_name: str = None) -> str:
    """Save the wordlist to a file and return the filename."""
    # Create directory if it doesn't exist
    output_dir = Path("wordlists")
    output_dir.mkdir(exist_ok=True)
    
    # Generate filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if custom_name:
        filename = output_dir / f"{custom_name}_{timestamp}.txt"
    else:
        filename = output_dir / f"{platform.lower().replace('/', '_')}_{timestamp}.txt"
    
    # Write wordlist to file
    with open(filename, "w") as f:
        for password in sorted(wordlist):
            f.write(f"{password}\n")
    
    return str(filename)


def main():
    """Main function to run the wordlist generator."""
    try:
        clear_screen()
        print_banner()
        
        typing_print("\033[1;33m[+] Welcome to WordlistForge - Advanced Social Platform Wordlist Generator\033[0m")
        
        # Collect user data
        user_data = collect_user_data()
        
        # Get platform-specific patterns
        platform_patterns = get_platform_patterns(user_data["platform"])
        
        # Generate wordlist
        typing_print("\n\033[1;33m[+] Generating wordlist...\033[0m")
        show_spinner("Processing combinations", 3)
        
        wordlist = generate_platform_specific_combinations(
            user_data, 
            platform_patterns, 
            user_data["complexity"],
            user_data["size_pref"]
        )
        
        # Display number of words generated
        word_count = len(wordlist)
        print(f"\n\033[1;36m[+] Generated {word_count} unique passwords for {user_data['platform']}\033[0m")
        
        # Ask user for custom wordlist name
        custom_name = get_user_input("Enter a custom name for your wordlist (or leave empty for default)", allow_empty=True)
        
        # Save wordlist
        show_spinner("Saving wordlist", 2)
        filename = save_wordlist(wordlist, user_data["platform"], custom_name)
        
        # Summary
        print(f"\n\033[1;32m[+] Wordlist generation complete!\033[0m")
        print(f"\033[1;36m[+] Saved to: {filename}\033[0m")
        
        print("\n\033[1;33m[!] Remember to use this tool ethically and responsibly.\033[0m")
        print("\033[1;33m[!] Only use generated wordlists on systems you have permission to test.\033[0m")
    
    except KeyboardInterrupt:
        print("\n\n\033[1;31m[!] Process interrupted by user. Exiting...\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[!] An error occurred: {str(e)}\033[0m")
    finally:
        print("\n\033[1;32m[+] Thank you for using WordlistForge!\033[0m")


if __name__ == "__main__":
    main()
