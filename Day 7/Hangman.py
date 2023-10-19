import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
Word_Bank = ["diabolical", "speedway", "glasscannon", "javascript", "abandoning", "twogirlsonecup", "zebra", "computer", "elephant", "strawberry", "rainbow", "mountain", "sunshine", "butterfly", "waterfall", "chocolate", "guitar", "boulevard", "adventure", "ocean", "paradise", "whisper",
             "umbrella", "keyboard", "eclipse", "fireworks", "laughter", "jazz", "silhouette", "swimming",
             "reflection", "enchanted", "nightfall", "serendipity", "piano", "harmony", "journey", "breeze",
             "moonlight", "carousel", "silence", "sunset", "oasis", "champion", "chocolate", "fantasy", "freedom",
             "discovery", "captain", "treasure", "daydream", "champion", "mystery", "secret", "desire", "imagination",
             "butterfly", "horizon", "whisper", "eternity", "blossom", "crystal", "cascade", "passion", "dream",
             "inspiration", "cascade", "legend", "paradise", "island", "serenity", "reverie", "rhapsody", "infinity",
             "captivate", "marvel", "sunrise", "adventure", "jubilee", "mesmerize", "kaleidoscope", "infinity",
             "wanderlust", "harmony", "reverie", "lullaby", "mystical", "blissful", "fantasia", "incandescent", "whimsical",
             "effervescent", "beautiful", "captivating", "majestic", "graceful", "peaceful", "tranquil", "radiant",
             "glorious", "ecstasy", "elegant", "delightful", "vibrant", "enchantment", "magnificent", "picturesque",
             "charming", "picturesque", "fascination", "exquisite", "fanciful", "ethereal", "dazzling", "serendipity",
             "soothing", "tantalizing", "breathtaking", "sparkling", "mesmerizing", "resplendent",
             "starry", "fairy", "ballet", "symphony", "miracle", "carnival", "embrace", "laughter", "eternal", "freedom",
             "breeze", "victory", "passion", "lighthouse", "reflection", "celebration", "happiness", "celestial", "whisper",
             "paradise", "fantasy", "boulevard", "mystery", "imagination", "inspiration", "discovery", "chocolate", "piano",
             "butterfly", "horizon", "journey", "eclipse", "carousel", "ocean", "silhouette", "swimming", "guitar",
             "champion", "sunshine", "rainbow", "mountain", "strawberry", "elephant", "computer", "zebra", "tiger",
             "tropical", "dream", "illusion", "reflection", "rhapsody", "mesmerize", "enchantment", "infinite", "whimsy",
             "daydream", "sparkle", "treasure", "captivate", "luminous", "harmony", "serenity", "lullaby", "cascading",
             "fantasia", "ethereal", "radiance", "blissful", "majestic", "serendipity", "mesmerizing", "paradise", "embrace",
             "breathtaking", "celestial", "delightful", "graceful", "tranquil", "starry", "majesty", "inspiration", "rhapsody",
             "eternity", "freedom", "victory", "soothing", "captivating", "ecstasy", "imagination", "charming", "kaleidoscope",
             "carnival", "reverie", "magnificent", "wanderlust", "symphony", "blossom", "imagination", "serendipity", "lullaby",
             "breathtaking", "radiance", "mystical", "whimsical", "picturesque", "beautiful", "graceful", "vibrant", "dazzling",
             "tranquil", "enchantment", "glorious", "ecstasy", "charming", "mesmerizing", "fanciful", "effervescent", "fairy",
             "ballet", "celebration", "miracle", "carnival", "embrace", "laughter", "eternal", "freedom", "breeze", "victory",
             "passion", "lighthouse", "reflection", "eternity", "fantasy", "inspiration", "lullaby", "marvel", "mystical", "whimsical",
             "majestic", "blissful", "picturesque", "charming", "mesmerizing", "reverie", "ethereal", "incandescent", "mesmerize",
             "resplendent",  "starry", "fairy", "ballet", "symphony", "miracle", "carnival", "embrace", "laughter",
             "eternal", "freedom", "breeze", "victory", "passion", "lighthouse", "reflection", "celebration", "happiness", "celestial",
             "whisper", "paradise", "fantasy", "boulevard", "mystery", "imagination", "inspiration", "discovery", "chocolate", "piano",
             "butterfly", "horizon", "journey", "eclipse", "carousel", "ocean", "silhouette", "swimming", "guitar",
             "champion", "sunshine", "rainbow", "mountain", "strawberry", "elephant", "computer", "zebra", "tiger",
             "tropical", "dream", "illusion", "reflection", "rhapsody", "mesmerize", "enchantment", "infinite", "whimsy",
             "daydream", "sparkle", "treasure", "captivate", "luminous", "harmony", "serenity", "lullaby", "cascading",
             "fantasia", "ethereal", "radiance", "blissful", "majestic", "serendipity", "mesmerizing", "paradise", "embrace",
             "breathtaking", "celestial", "delightful", "graceful", "tranquil", "starry", "majesty", "inspiration", 'abruptly', 'absurd', 'abyss',
             'affix',
             'askew',
             'avenue',
             'awkward',
             'axiom',
             'azure',
             'bagpipes',
             'bandwagon',
             'banjo',
             'bayou',
             'beekeeper',
             'bikini',
             'blitz',
             'blizzard',
             'boggle',
             'bookworm',
             'boxcar',
             'boxful',
             'buckaroo',
             'buffalo',
             'buffoon',
             'buxom',
             'buzzard',
             'buzzing',
             'buzzwords',
             'caliph',
             'cobweb',
             'cockiness',
             'croquet',
             'crypt',
             'curacao',
             'cycle',
             'daiquiri',
             'dirndl',
             'disavow',
             'dizzying',
             'duplex',
             'dwarves',
             'embezzle',
             'equip',
             'espionage',
             'euouae',
             'exodus',
             'faking',
             'fishhook',
             'fixable',
             'fjord',
             'flapjack',
             'flopping',
             'fluffiness',
             'flyby',
             'foxglove',
             'frazzled',
             'frizzled',
             'fuchsia',
             'funny',
             'gabby',
             'galaxy',
             'galvanize',
             'gazebo',
             'giaour',
             'gizmo',
             'glowworm',
             'glyph',
             'gnarly',
             'gnostic',
             'gossip',
             'grogginess',
             'haiku',
             'haphazard',
             'hyphen',
             'iatrogenic',
             'icebox',
             'injury',
             'ivory',
             'ivy',
             'jackpot',
             'jaundice',
             'jawbreaker',
             'jaywalk',
             'jazziest',
             'jazzy',
             'jelly',
             'jigsaw',
             'jinx',
             'jiujitsu',
             'jockey',
             'jogging',
             'joking',
             'jovial',
             'joyful',
             'juicy',
             'jukebox',
             'jumbo',
             'kayak',
             'kazoo',
             'keyhole',
             'khaki',
             'kilobyte',
             'kiosk',
             'kitsch',
             'kiwifruit',
             'klutz',
             'knapsack',
             'larynx',
             'lengths',
             'lucky',
             'luxury',
             'lymph',
             'marquis',
             'matrix',
             'megahertz',
             'microwave',
             'mnemonic',
             'mystify',
             'naphtha',
             'nightclub',
             'nowadays',
             'numbskull',
             'nymph',
             'onyx',
             'ovary',
             'oxidize',
             'oxygen',
             'pajama',
             'peekaboo',
             'phlegm',
             'pixel',
             'pizazz',
             'pneumonia',
             'polka',
             'pshaw',
             'psyche',
             'puppy',
             'puzzling',
             'quartz',
             'queue',
             'quips',
             'quixotic',
             'quiz',
             'quizzes',
             'quorum',
             'razzmatazz',
             'rhubarb',
             'rhythm',
             'rickshaw',
             'schnapps',
             'scratch',
             'shiv',
             'snazzy',
             'sphinx',
             'spritz',
             'squawk',
             'staff',
             'strength',
             'strengths',
             'stretch',
             'stronghold',
             'stymied',
             'subway',
             'swivel',
             'syndrome',
             'thriftless',
             'thumbscrew',
             'topaz',
             'transcript',
             'transgress',
             'transplant',
             'triphthong',
             'twelfth',
             'twelfths',
             'unknown',
             'unworthy',
             'unzip',
             'uptown',
             'vaporize',
             'vixen',
             'vodka',
             'voodoo',
             'vortex',
             'voyeurism',
             'walkway',
             'waltz',
             'wave',
             'wavy',
             'waxy',
             'wellspring',
             'wheezy',
             'whiskey',
             'whizzing',
             'whomever',
             'wimpy',
             'witchcraft',
             'wizard',
             'woozy',
             'wristwatch',
             'wyvern',
             'xylophone',
             'yachtsman',
             'yippee',
             'yoked',
             'youthful',
             'yummy',
             'zephyr',
             'zigzag',
             'zigzagging',
             'zilch',
             'zipper',
             'zodiac',
             'zombie']
Lives = 6
Wins = 0
Loses = 0
Reset = False
GuessedWord = []
print("Welcome to HangMan!")


while True:

    Word_Bank_Choice = random.choice(Word_Bank)
    Board_Length = len(Word_Bank_Choice)
    Board = ["_"] * Board_Length
    Lives = 6
    GuessedWord = []
    print(stages[6])
    print(''.join(Board))
    Reset = False

    while Reset == False:
        print(f"You have guessed: {GuessedWord}")
        Guess = input("Guess your letter, or word \n").lower()

        if Guess in GuessedWord:
            print("You have already tried that letter or word.")
            continue
        GuessedWord.append(Guess)

        if Guess == "firsttime?":
            Wins += 1
            print("That is the correct answer!")
            print("You Win!")
            print(f"Wins: {Wins}")
            print(f"Loses: {Loses}")
            print(f"Lives: {Lives}\n")
            Reset = True
            break
        if Guess in Word_Bank_Choice:
            for Letter_Index in range(len(Word_Bank_Choice)):
                if Word_Bank_Choice[Letter_Index] == Guess:

                    Board[Letter_Index] = Guess
            if Guess == Word_Bank_Choice:
                Wins += 1
                print("That is the correct answer!")
                print("You Win!")
                print(f"Wins: {Wins}")
                print(f"Loses: {Loses}")
                print(f"Lives: {Lives}\n")
                Reset = True
                break
            else:
                print(f"{Guess} is present in the word")
                print("\n")
            if Lives == 6:
                print(stages[6])
            elif Lives == 5:
                print(stages[5])
            elif Lives == 4:
                print(stages[4])
            elif Lives == 3:
                print(stages[3])
            elif Lives == 2:
                print(stages[2])
            elif Lives == 1:
                print(stages[1])
            print(''.join(Board))

        else:
            Lives -= 1
            if Lives == 0:
                Loses += 1
                print(stages[0])
                print("You Lose, HA HA HA.")
                print(f"Wins: {Wins}")
                print(f"Loses: {Loses}")
                print(f"Lives: {Lives}\n")
                Reset = True
                break
            elif len(Guess) > 3:
                print("That guess is incorrect.")
                print(f"Lives: {Lives}\n")
                if Lives == 6:
                    print(stages[6])
                elif Lives == 5:
                    print(stages[5])
                elif Lives == 4:
                    print(stages[4])
                elif Lives == 3:
                    print(stages[3])
                elif Lives == 2:
                    print(stages[2])
                elif Lives == 1:
                    print(stages[1])
                print(''.join(Board))
                continue

            else:
                print(f"{Guess} is not present in the word, try again")
                print(f"Lives: {Lives}\n")
                if Lives == 6:
                    print(stages[6])
                elif Lives == 5:
                    print(stages[5])
                elif Lives == 4:
                    print(stages[4])
                elif Lives == 3:
                    print(stages[3])
                elif Lives == 2:
                    print(stages[2])
                elif Lives == 1:
                    print(stages[1])
                print(''.join(Board))
                continue
        if "_" not in Board:
            Wins += 1
            print("You Win!")
            print(f"Wins: {Wins}")
            print(f"Loses: {Loses}")
            print(f"Lives: {Lives}\n")
            Reset = True
            break
