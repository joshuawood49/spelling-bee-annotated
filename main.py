import streamlit as st
import random

# Full annotated word data
level_words = {
  "Level 1": [
    {
      "word": "above",
      "pronunciation": "uh-buv",
      "definition": "adverb: in",
      "example": "a higher place"
    },
    {
      "word": "block",
      "pronunciation": "blok",
      "definition": "noun: a",
      "example": "solid piece of hard material"
    },
    {
      "word": "breeze",
      "pronunciation": "breez",
      "definition": "noun: a",
      "example": "light wind"
    },
    {
      "word": "brick",
      "pronunciation": "brik",
      "definition": "noun: a",
      "example": "small hard block of baked earth, used for building"
    },
    {
      "word": "canter",
      "pronunciation": "kan-tuh",
      "definition": "noun: an",
      "example": "easy gait of a horse or other animal, between a trot and a gallop"
    },
    {
      "word": "carpet",
      "pronunciation": "kah-puht",
      "definition": "noun: a",
      "example": "thick, woven floor covering"
    },
    {
      "word": "chair",
      "pronunciation": "chair",
      "definition": "noun: a",
      "example": "seat with a back and often with arms"
    },
    {
      "word": "clock",
      "pronunciation": "klok",
      "definition": "noun: something",
      "example": "which measures and tells you the time"
    },
    {
      "word": "cloud",
      "pronunciation": "klowd",
      "definition": "noun: a",
      "example": "white or grey mass of water vapour, ice, smoke or dust that floats in the air"
    },
    {
      "word": "comet",
      "pronunciation": "kom-uht",
      "definition": "noun: an",
      "example": "object in space that moves around the sun and has a bright central part  surrounded by a misty part that finishes in the shape of a tail"
    },
    {
      "word": "crew",
      "pronunciation": "krooh",
      "definition": "noun: a",
      "example": "group of people operating a ship, boat, or aircraft"
    },
    {
      "word": "crowd",
      "pronunciation": "krowd",
      "definition": "noun: a",
      "example": "large number of people or things gathered closely together"
    },
    {
      "word": "crutch",
      "pronunciation": "kruch",
      "definition": "noun: a",
      "example": "stick or support which fits under the arm to help an injured person walk  One crutch was all I needed to help me walk with my broken ankle but two crutches"
    },
    {
      "word": "cube",
      "pronunciation": "kyoohb",
      "definition": "noun: a",
      "example": "solid shape with six equal square sides"
    },
    {
      "word": "drink",
      "pronunciation": "dringk",
      "definition": "verb: to",
      "example": "swallow liquid"
    },
    {
      "word": "dusk",
      "pronunciation": "dusk",
      "definition": "noun: the",
      "example": "time of the evening when it is half light and half dark"
    },
    {
      "word": "elf",
      "pronunciation": "elf",
      "definition": "noun: a",
      "example": "small being in fairytales who often plays tricks on people"
    },
    {
      "word": "enjoy",
      "pronunciation": "en-joy",
      "definition": "verb: to",
      "example": "get pleasure from something"
    },
    {
      "word": "era",
      "pronunciation": "ear-ruh",
      "definition": "noun: a",
      "example": "major division of geological time"
    },
    {
      "word": "field",
      "pronunciation": "feeld",
      "definition": "noun: a",
      "example": "piece of open ground or space"
    },
    {
      "word": "flint",
      "pronunciation": "flint",
      "definition": "noun: a",
      "example": "hard kind of stone which gives off sparks when hit with something hard"
    },
    {
      "word": "forget",
      "pronunciation": "fuh-get",
      "definition": "verb: to",
      "example": "cease or fail to remember something"
    },
    {
      "word": "fort",
      "pronunciation": "fawt",
      "definition": "noun: a",
      "example": "place like a castle, which is strongly built and armed against enemy attack"
    },
    {
      "word": "glass",
      "pronunciation": "glahs",
      "definition": "noun: a",
      "example": "container that you drink from, made of glass"
    },
    {
      "word": "groom",
      "pronunciation": "groohm",
      "definition": "noun: a",
      "example": "person in charge of horses or a stable"
    },
    {
      "word": "heat",
      "pronunciation": "heet",
      "definition": "noun: warmth",
      "example": "or the quality of being hot"
    },
    {
      "word": "jumper",
      "pronunciation": "jum-puh",
      "definition": "noun: a",
      "example": "piece of warm clothing worn on the top half of your body, often over other  clothes"
    },
    {
      "word": "learn",
      "pronunciation": "lern",
      "definition": "verb: to",
      "example": "come to have knowledge of something, or skill in doing it"
    },
    {
      "word": "lemon",
      "pronunciation": "lem-uhn",
      "definition": "noun: a",
      "example": "yellow fruit with a sour taste"
    },
    {
      "word": "loud",
      "pronunciation": "lowd",
      "definition": "adjective: noisy",
      "example": "and able to be heard very clearly"
    },
    {
      "word": "male",
      "pronunciation": "mayl",
      "definition": "adjective: of",
      "example": "the same sex as a man"
    },
    {
      "word": "match",
      "pronunciation": "mach",
      "definition": "noun: a",
      "example": "game between two or more people or teams"
    },
    {
      "word": "next",
      "pronunciation": "nekst",
      "definition": "adjective: immediately",
      "example": "following"
    },
    {
      "word": "open",
      "pronunciation": "oh-puhn",
      "definition": "adjective: not",
      "example": "shut or locked"
    },
    {
      "word": "oval",
      "pronunciation": "oh-vuhl",
      "definition": "noun: a",
      "example": "field for playing sport on"
    },
    {
      "word": "pancake",
      "pronunciation": "pan-kayk",
      "definition": "noun: a",
      "example": "thin, flat cake made of batter, cooked in a frying pan"
    },
    {
      "word": "pasta",
      "pronunciation": "pah-stuh or pa-stuh",
      "definition": "noun: a",
      "example": "dough made from a paste of flour, salt, water, and sometimes egg"
    },
    {
      "word": "pilot",
      "pronunciation": "puy-luht",
      "definition": "noun: someone",
      "example": "who flies an aircraft"
    },
    {
      "word": "plastic",
      "pronunciation": "plass-tik",
      "definition": "noun: a",
      "example": "substance which can be shaped when soft and then hardened"
    },
    {
      "word": "plenty",
      "pronunciation": "plen-tee",
      "definition": "noun: an",
      "example": "amount which is large or more than enough"
    },
    {
      "word": "polite",
      "pronunciation": "puh-luyt",
      "definition": "adjective: behaving",
      "example": "well to other people"
    },
    {
      "word": "radio",
      "pronunciation": "ray-dee-oh",
      "definition": "noun: the",
      "example": "sending of electrical signals through the air to a set which receives them"
    },
    {
      "word": "record",
      "pronunciation": "rek-awd",
      "definition": "noun: a",
      "example": "self-contained piece of data on a computer database"
    },
    {
      "word": "rein",
      "pronunciation": "rayn",
      "definition": "noun: one",
      "example": "of the long, thin straps which a rider uses to direct a horse or other animal"
    },
    {
      "word": "robe",
      "pronunciation": "rohb",
      "definition": "noun: a",
      "example": "long loose gown worn by men or women  The purple robe hanging from the king's shoulders dragged along the ground as he"
    },
    {
      "word": "rubbish",
      "pronunciation": "rub-ish",
      "definition": "noun: useless",
      "example": "unwanted material to be thrown away  I hate how some people drop their rubbish on the ground instead of putting it in the"
    },
    {
      "word": "rustic",
      "pronunciation": "rus-tik",
      "definition": "adjective: simple",
      "example": "and unsophisticated"
    },
    {
      "word": "saddle",
      "pronunciation": "sad-uhl",
      "definition": "noun: a",
      "example": "seat for the rider of a horse"
    },
    {
      "word": "silent",
      "pronunciation": "suy-luhnt",
      "definition": "adjective: making",
      "example": "no sound or not talking"
    },
    {
      "word": "silver",
      "pronunciation": "sil-vuh",
      "definition": "noun: a",
      "example": "shiny grey metal used for making things like jewellery"
    },
    {
      "word": "skill",
      "pronunciation": "skil",
      "definition": "noun: the",
      "example": "ability to do something well"
    },
    {
      "word": "speak",
      "pronunciation": "speek",
      "definition": "verb: to",
      "example": "say words using your voice"
    },
    {
      "word": "stone",
      "pronunciation": "stohn",
      "definition": "noun: the",
      "example": "hard substance which rocks are made of"
    },
    {
      "word": "target",
      "pronunciation": "tah-guht",
      "definition": "noun: something",
      "example": "that you aim at and try to hit or reach"
    }
  ],
  "Level 2": [
    {
      "word": "asset",
      "pronunciation": "ass-et",
      "definition": "noun: something",
      "example": "you own"
    },
    {
      "word": "athlete",
      "pronunciation": "ath-leet",
      "definition": "noun: someone",
      "example": "who trains and competes in some kind of sport, especially running or  jumping events"
    },
    {
      "word": "attach",
      "pronunciation": "uh-tach",
      "definition": "verb: to",
      "example": "add or join one thing to something else"
    },
    {
      "word": "backspin",
      "pronunciation": "bak-spin",
      "definition": "noun: the",
      "example": "reverse spinning of a ball causing it to bounce backwards or stop in the  shortest possible time"
    },
    {
      "word": "balm",
      "pronunciation": "bahm",
      "definition": "noun: a",
      "example": "sweet-smelling ointment or oil which heals or makes something less painful"
    },
    {
      "word": "barrel",
      "pronunciation": "bar-uhl",
      "definition": "noun: a",
      "example": "large, rounded container made of narrow pieces of wood held in place by  iron bands"
    },
    {
      "word": "beetroot",
      "pronunciation": "beet-rooht",
      "definition": "noun: the",
      "example": "dark red root of the beet plant which is eaten as a vegetable"
    },
    {
      "word": "belief",
      "pronunciation": "buh-leef",
      "definition": "noun: something",
      "example": "that you believe and accept as true"
    },
    {
      "word": "bereft",
      "pronunciation": "buh-reft",
      "definition": "adjective: lacking",
      "example": "The experiment called for working out a way of guiding the ants from point A to point  B but we were completely bereft of ideas."
    },
    {
      "word": "billet",
      "pronunciation": "bil-uht",
      "definition": "noun: a",
      "example": "place for someone to live for a while, usually in someone else's home"
    },
    {
      "word": "billion",
      "pronunciation": "bil-yuhn",
      "definition": "adjective: amounting",
      "example": "to a thousand times a million"
    },
    {
      "word": "birth",
      "pronunciation": "berth",
      "definition": "noun: the",
      "example": "act of being born"
    },
    {
      "word": "bleat",
      "pronunciation": "bleet",
      "definition": "verb: a",
      "example": "noise like a soft cry"
    },
    {
      "word": "blight",
      "pronunciation": "bluyt",
      "definition": "noun: a",
      "example": "damaging effect"
    },
    {
      "word": "bodice",
      "pronunciation": "bod-uhs",
      "definition": "noun: the",
      "example": "part of a woman's dress above the waist"
    },
    {
      "word": "bodily",
      "pronunciation": "bod-uh-lee",
      "definition": "adjective: of",
      "example": "or relating to the body"
    },
    {
      "word": "bogus",
      "pronunciation": "boh-guhs",
      "definition": "adjective: not",
      "example": "real or true"
    },
    {
      "word": "booth",
      "pronunciation": "boohdh or boohth",
      "definition": "noun: a",
      "example": "small, closed-in place, usually made just big enough for one person to fit in"
    },
    {
      "word": "bounce",
      "pronunciation": "bownce",
      "definition": "verb: to",
      "example": "throw something such as a ball against a surface to make it spring back  towards you"
    },
    {
      "word": "boxing",
      "pronunciation": "boks-ing",
      "definition": "noun: the",
      "example": "sport of fighting with your fists, especially with protective gloves"
    },
    {
      "word": "braid",
      "pronunciation": "brayd",
      "definition": "verb: to",
      "example": "weave or plait something"
    },
    {
      "word": "brake",
      "pronunciation": "brayk",
      "definition": "noun: something",
      "example": "which slows or stops a machine"
    },
    {
      "word": "brazen",
      "pronunciation": "bray-zuhn",
      "definition": "adjective: shameless",
      "example": "or impudent"
    },
    {
      "word": "breach",
      "pronunciation": "breech",
      "definition": "noun: a",
      "example": "failure to keep or observe a rule, etc."
    },
    {
      "word": "breakage",
      "pronunciation": "brayk-ij",
      "definition": "noun: the",
      "example": "breaking of something"
    },
    {
      "word": "brie",
      "pronunciation": "bree",
      "definition": "noun: a",
      "example": "kind of salted, white, soft cheese"
    },
    {
      "word": "bruise",
      "pronunciation": "broohz",
      "definition": "noun: a",
      "example": "blue-black mark on the body, caused by injury"
    },
    {
      "word": "burgle",
      "pronunciation": "ber-guhl",
      "definition": "verb: to",
      "example": "perform a theft in"
    },
    {
      "word": "bushfire",
      "pronunciation": "boosh-fuy-uh",
      "definition": "noun: a",
      "example": "big fire in the bush or forest"
    },
    {
      "word": "canoe",
      "pronunciation": "kuh-nooh",
      "definition": "noun: a",
      "example": "light, narrow boat that you move by using paddles"
    },
    {
      "word": "capsule",
      "pronunciation": "kap-shoohl or kap-shuhl",
      "definition": "noun: a",
      "example": "very small container that has powdered medicine inside it"
    },
    {
      "word": "carbon",
      "pronunciation": "kah-buhn",
      "definition": "noun: a",
      "example": "common chemical element"
    },
    {
      "word": "carob",
      "pronunciation": "ka-ruhb",
      "definition": "noun: a",
      "example": "substitute for chocolate which comes from the seed pods of a  Mediterranean tree"
    },
    {
      "word": "chafe",
      "pronunciation": "chayf",
      "definition": "verb: to",
      "example": "wear down or make sore by rubbing"
    },
    {
      "word": "channel",
      "pronunciation": "chan-uhl",
      "definition": "noun: a",
      "example": "frequency band for radio or television"
    },
    {
      "word": "chapel",
      "pronunciation": "chap-uhl",
      "definition": "noun: a",
      "example": "small church, or part of a church"
    },
    {
      "word": "chatter",
      "pronunciation": "chat-uh",
      "definition": "verb: to",
      "example": "talk quickly and continuously about unimportant things"
    },
    {
      "word": "cobbler",
      "pronunciation": "kob-luh",
      "definition": "noun: someone",
      "example": "who mends shoes"
    },
    {
      "word": "cockroach",
      "pronunciation": "kok-rohch",
      "definition": "noun: an",
      "example": "insect, usually active at night, with a flattened body and long feelers, which  is a common household pest"
    },
    {
      "word": "combat",
      "pronunciation": "kom-bat",
      "definition": "noun: the",
      "example": "fighting that takes place between opposing armies"
    },
    {
      "word": "comfort",
      "pronunciation": "kum-fuht",
      "definition": "verb: to",
      "example": "cheer someone up or make them feel less sad or worried"
    },
    {
      "word": "compete",
      "pronunciation": "kuhm-peet",
      "definition": "verb: to",
      "example": "set yourself against another person or other people to win something  Our school team will compete in the district cross-country competition -- I hope we"
    },
    {
      "word": "context",
      "pronunciation": "kon-tekst",
      "definition": "noun: the",
      "example": "circumstances or facts that surround a particular situation or event"
    },
    {
      "word": "contort",
      "pronunciation": "kuhn-tawt",
      "definition": "verb: to",
      "example": "become twisted and no longer hold a natural shape"
    },
    {
      "word": "cordial",
      "pronunciation": "kaw-dee-uhl",
      "definition": "noun: a",
      "example": "fruit-flavoured syrup that you mix with water to make a drink"
    },
    {
      "word": "count",
      "pronunciation": "kownt",
      "definition": "verb: to",
      "example": "add up"
    },
    {
      "word": "course",
      "pronunciation": "kawce",
      "definition": "noun: the",
      "example": "ground or water on which a race takes place"
    },
    {
      "word": "cousin",
      "pronunciation": "kuz-uhn",
      "definition": "noun: a",
      "example": "son or daughter of your uncle or aunt"
    },
    {
      "word": "cruise",
      "pronunciation": "kroohz",
      "definition": "noun: a",
      "example": "holiday on a ship"
    },
    {
      "word": "crux",
      "pronunciation": "kruks",
      "definition": "noun: the",
      "example": "most important point"
    },
    {
      "word": "cue",
      "pronunciation": "kyooh",
      "definition": "noun: a",
      "example": "long tapered stick with a leather tip, used to hit the ball in billiards, etc."
    },
    {
      "word": "curd",
      "pronunciation": "kerd",
      "definition": "noun: a",
      "example": "jelly-like substance which forms in milk, eaten fresh or used for making  cheese"
    },
    {
      "word": "curtain",
      "pronunciation": "ker-tuhn",
      "definition": "noun: a",
      "example": "piece of material hanging from a rod over a window"
    },
    {
      "word": "damage",
      "pronunciation": "dam-ij",
      "definition": "verb: to",
      "example": "harm or spoil something"
    },
    {
      "word": "damsel",
      "pronunciation": "dam-zuhl",
      "definition": "noun: an",
      "example": "old-fashioned word for a young unmarried woman"
    },
    {
      "word": "decor",
      "pronunciation": "day-kaw or dek-aw",
      "definition": "noun: the",
      "example": "way a room is decorated or furnished"
    },
    {
      "word": "defeat",
      "pronunciation": "duh-feet",
      "definition": "verb: to",
      "example": "overcome or beat in a battle or contest"
    },
    {
      "word": "denim",
      "pronunciation": "den-uhm",
      "definition": "noun: a",
      "example": "heavy cotton material used to make jeans and other clothes"
    },
    {
      "word": "discard",
      "pronunciation": "dis-kahd",
      "definition": "verb: to",
      "example": "throw something away"
    },
    {
      "word": "discomfort",
      "pronunciation": "dis-kum-fuht",
      "definition": "noun: pain",
      "example": "or uneasiness"
    },
    {
      "word": "dispute",
      "pronunciation": "duhs-pyooht",
      "definition": "noun: an",
      "example": "argument or disagreement  There was a dispute between the workers and their employer, but it was resolved"
    },
    {
      "word": "dodge",
      "pronunciation": "doj",
      "definition": "verb: to",
      "example": "duck or move aside quickly, so as to avoid something"
    },
    {
      "word": "domestic",
      "pronunciation": "duh-mes-tik",
      "definition": "adjective: having",
      "example": "to do with the home or family"
    },
    {
      "word": "downpour",
      "pronunciation": "down-paw",
      "definition": "noun: a",
      "example": "heavy fall of rain  I got caught in the downpour on my way home from school and am absolutely"
    },
    {
      "word": "earn",
      "pronunciation": "ern",
      "definition": "verb: to",
      "example": "receive money as payment for a job you have done"
    },
    {
      "word": "edam",
      "pronunciation": "ee-duhm or ed-uhm",
      "definition": "noun: a",
      "example": "hard, round, yellow cheese, with a red wax rind"
    },
    {
      "word": "elite",
      "pronunciation": "ee-leet",
      "definition": "adjective: belonging",
      "example": "to the group of people with the most talent or skill  My cousin is training six days a week with other elite cyclists in preparation for the"
    },
    {
      "word": "empty",
      "pronunciation": "emp-tee",
      "definition": "adjective: containing",
      "example": "nothing"
    },
    {
      "word": "enforce",
      "pronunciation": "en-force",
      "definition": "verb: to",
      "example": "make sure of obedience to something"
    },
    {
      "word": "explore",
      "pronunciation": "uhk-splaw",
      "definition": "verb: to",
      "example": "travel over an area to discover things or places"
    },
    {
      "word": "famished",
      "pronunciation": "fam-isht",
      "definition": "adjective: very",
      "example": "hungry"
    },
    {
      "word": "famous",
      "pronunciation": "fay-muhs",
      "definition": "adjective: renowned",
      "example": "or widely known"
    },
    {
      "word": "fateful",
      "pronunciation": "fayt-fuhl",
      "definition": "adjective: important",
      "example": "because of a disastrous outcome"
    },
    {
      "word": "fault",
      "pronunciation": "fawlt or folt",
      "definition": "noun: responsibility",
      "example": "or cause for blame"
    },
    {
      "word": "fickle",
      "pronunciation": "fik-uhl",
      "definition": "adjective: changeable",
      "example": "or likely to have changes of mind"
    },
    {
      "word": "figment",
      "pronunciation": "fig-muhnt",
      "definition": "noun: something",
      "example": "that is only imaginary"
    },
    {
      "word": "flicker",
      "pronunciation": "flik-uh",
      "definition": "verb: to",
      "example": "burn unsteadily or shine with a wavering light"
    },
    {
      "word": "fondue",
      "pronunciation": "fon-dooh or fon-dyooh",
      "definition": "noun: a",
      "example": "meal cooked at the table in which pieces of food are speared on the end of  long forks and cooked or dipped in melted cheese, hot oil or melted chocolate"
    },
    {
      "word": "fortieth",
      "pronunciation": "faw-tee-uhth",
      "definition": "adjective: next",
      "example": "after the 39th"
    },
    {
      "word": "foul",
      "pronunciation": "fowl",
      "definition": "noun: an",
      "example": "unfair action in sport"
    },
    {
      "word": "fountain",
      "pronunciation": "fown-tuhn",
      "definition": "noun: a",
      "example": "decorated structure with flowing water, often situated in a public place"
    },
    {
      "word": "freeze",
      "pronunciation": "freez",
      "definition": "verb: to",
      "example": "keep fresh by putting in a freezer"
    },
    {
      "word": "fretful",
      "pronunciation": "fret-fuhl",
      "definition": "adjective: irritable",
      "example": "or peevish"
    },
    {
      "word": "fringe",
      "pronunciation": "frinj",
      "definition": "noun: hair",
      "example": "which has been cut across the forehead"
    },
    {
      "word": "fumble",
      "pronunciation": "fum-buhl",
      "definition": "verb: to",
      "example": "handle something clumsily"
    },
    {
      "word": "gallop",
      "pronunciation": "gal-uhp",
      "definition": "noun: the",
      "example": "fastest pace a horse can run at"
    },
    {
      "word": "garland",
      "pronunciation": "gah-luhnd",
      "definition": "noun: a",
      "example": "string of flowers or leaves you wear as an ornament"
    },
    {
      "word": "grandstand",
      "pronunciation": "gran-stand",
      "definition": "noun: a",
      "example": "building with seats rising in tiers, at a sports field or similar outdoor place of  entertainment"
    },
    {
      "word": "greasy",
      "pronunciation": "gree-zee",
      "definition": "adjective: smeared",
      "example": "or soiled with a fatty or oily substance"
    },
    {
      "word": "great",
      "pronunciation": "grayt",
      "definition": "adjective: large",
      "example": "Great herds of animals once roamed the plains.  greenhouse"
    },
    {
      "word": "grief",
      "pronunciation": "greef",
      "definition": "noun: great",
      "example": "sadness"
    },
    {
      "word": "gritty",
      "pronunciation": "grit-ee",
      "definition": "adjective: sandy",
      "example": "or grainy"
    },
    {
      "word": "guest",
      "pronunciation": "gest",
      "definition": "noun: a",
      "example": "visitor or someone who is entertained at your house"
    },
    {
      "word": "guilty",
      "pronunciation": "gil-tee",
      "definition": "adjective: responsible",
      "example": "for a wrongdoing"
    },
    {
      "word": "kendo",
      "pronunciation": "ken-doh",
      "definition": "noun: a",
      "example": "Japanese style of fencing derived from ancient Japanese sword-fighting"
    },
    {
      "word": "pirate",
      "pronunciation": "puy-ruht",
      "definition": "noun: someone",
      "example": "who attacks and robs ships at sea"
    },
    {
      "word": "snooker",
      "pronunciation": "snooh-kuh",
      "definition": "noun: a",
      "example": "game like billiards or pool, played on a table with a cue and different- coloured balls"
    },
    {
      "word": "solar",
      "pronunciation": "soh-luh",
      "definition": "adjective: to",
      "example": "do with the sun  We have a solar hot water system on our roof, to heat our water using the rays from"
    },
    {
      "word": "spice",
      "pronunciation": "spuys",
      "definition": "noun: a",
      "example": "substance made from a plant, which is used to flavour or preserve food"
    },
    {
      "word": "sprain",
      "pronunciation": "sprayn",
      "definition": "verb: to",
      "example": "twist or bend a joint in your body accidentally so that it swells and bruises"
    },
    {
      "word": "squeamish",
      "pronunciation": "skweem-ish",
      "definition": "adjective: easily",
      "example": "sickened"
    },
    {
      "word": "squirm",
      "pronunciation": "skwerm",
      "definition": "verb: to",
      "example": "wriggle uncomfortably"
    },
    {
      "word": "stagnant",
      "pronunciation": "stag-nuhnt",
      "definition": "adjective: still",
      "example": "and dirty"
    },
    {
      "word": "stake",
      "pronunciation": "stayk",
      "definition": "noun: a",
      "example": "stick which is often pointed at one end"
    },
    {
      "word": "stalemate",
      "pronunciation": "stayl-mayt",
      "definition": "noun: a",
      "example": "situation where no progress can be made"
    },
    {
      "word": "station",
      "pronunciation": "stay-shuhn",
      "definition": "noun: a",
      "example": "rural property for raising sheep or cattle"
    },
    {
      "word": "steady",
      "pronunciation": "sted-ee",
      "definition": "adjective: constant",
      "example": "or regular"
    },
    {
      "word": "steak",
      "pronunciation": "stayk",
      "definition": "noun: a",
      "example": "thick slice of meat or fish"
    },
    {
      "word": "stetson",
      "pronunciation": "stet-suhn",
      "definition": "noun: a",
      "example": "hat with a broad brim and a wide crown, as worn by cowboys  The cowboy was wearing a stetson, chequered shirt, riding trousers and elastic-sided"
    },
    {
      "word": "stifling",
      "pronunciation": "stuyf-ling",
      "definition": "adjective: oppressively",
      "example": "airless or hot"
    },
    {
      "word": "strange",
      "pronunciation": "straynj",
      "definition": "adjective: unusual",
      "example": "or not what you would expect"
    },
    {
      "word": "stumble",
      "pronunciation": "stum-buhl",
      "definition": "verb: to",
      "example": "nearly fall over"
    },
    {
      "word": "style",
      "pronunciation": "stuyl",
      "definition": "noun: a",
      "example": "particular kind or type, especially of music, art, architecture and so on"
    },
    {
      "word": "subsist",
      "pronunciation": "suhb-sist",
      "definition": "verb: to",
      "example": "continue to live or stay alive, especially when food and other needs are in  short supply"
    },
    {
      "word": "suburb",
      "pronunciation": "sub-erb",
      "definition": "noun: an",
      "example": "area of a city with its own shopping centre, school and other facilities"
    },
    {
      "word": "suffix",
      "pronunciation": "suf-iks",
      "definition": "noun: a",
      "example": "word part added to the end of a word"
    },
    {
      "word": "sultan",
      "pronunciation": "sul-tuhn",
      "definition": "noun: a",
      "example": "ruler in some Islamic countries"
    },
    {
      "word": "sunrise",
      "pronunciation": "sun-ruyz",
      "definition": "noun: the",
      "example": "appearance of the sun above the horizon in the morning, or the time when  this happens"
    },
    {
      "word": "surfboard",
      "pronunciation": "serf-bawd",
      "definition": "noun: a",
      "example": "long, narrow board used to ride waves towards the shore"
    },
    {
      "word": "swagger",
      "pronunciation": "swag-uh",
      "definition": "noun: a",
      "example": "very confident or arrogant walk or manner  When he saw that people were watching him, he started to walk with an"
    },
    {
      "word": "sweaty",
      "pronunciation": "swet-ee",
      "definition": "adjective: covered",
      "example": "with perspiration"
    },
    {
      "word": "swimsuit",
      "pronunciation": "swim-sooht",
      "definition": "noun: an",
      "example": "item of clothing to wear when you are swimming"
    },
    {
      "word": "sword",
      "pronunciation": "sawd",
      "definition": "noun: a",
      "example": "weapon with a long pointed blade fixed in a handle"
    },
    {
      "word": "tabloid",
      "pronunciation": "tab-loyd",
      "definition": "noun: a",
      "example": "newspaper with many pictures and short articles and with pages that are  about half the size of an ordinary newspaper"
    },
    {
      "word": "termite",
      "pronunciation": "ter-muyt",
      "definition": "noun: a",
      "example": "white insect that eats wood and which can destroy houses"
    },
    {
      "word": "tribute",
      "pronunciation": "trib-yooht",
      "definition": "noun: a",
      "example": "gift or speech made to show respect for someone"
    },
    {
      "word": "turncoat",
      "pronunciation": "tern-koht",
      "definition": "noun: someone",
      "example": "who changes their party or principles"
    },
    {
      "word": "turnip",
      "pronunciation": "ter-nuhp",
      "definition": "noun: a",
      "example": "plant with a thick white or yellow root which is eaten as a vegetable"
    },
    {
      "word": "understood",
      "pronunciation": "un-duh-stood",
      "definition": "adjective: agreed",
      "example": "upon by all  It is generally understood in our house that the person who cooks the dinner does not"
    },
    {
      "word": "undertone",
      "pronunciation": "un-duh-tohn",
      "definition": "noun: a",
      "example": "low or quietened tone of speaking"
    },
    {
      "word": "unlikely",
      "pronunciation": "un-luyk-lee",
      "definition": "adjective: probably",
      "example": "not true  It seemed unlikely that they could have broken into the house without making a"
    },
    {
      "word": "upstage",
      "pronunciation": "up-stayj",
      "definition": "verb: to",
      "example": "steal attention from, by placing yourself in a more favourable position"
    },
    {
      "word": "vanish",
      "pronunciation": "van-ish",
      "definition": "verb: to",
      "example": "completely disappear"
    },
    {
      "word": "vanity",
      "pronunciation": "van-uh-tee",
      "definition": "noun: extreme",
      "example": "pride in yourself"
    },
    {
      "word": "various",
      "pronunciation": "vair-ree-uhs",
      "definition": "adjective: several",
      "example": "or many"
    },
    {
      "word": "vegan",
      "pronunciation": "vee-guhn",
      "definition": "noun: a",
      "example": "person who follows a strict vegetarian diet which excludes any animal  products, such as eggs and dairy products"
    },
    {
      "word": "venom",
      "pronunciation": "ven-uhm",
      "definition": "noun: the",
      "example": "poison that some spiders and snakes release when they bite"
    },
    {
      "word": "verdict",
      "pronunciation": "ver-dikt",
      "definition": "noun: what",
      "example": "a judge or a jury decides about a prisoner in a court of law"
    },
    {
      "word": "viable",
      "pronunciation": "vuy-uh-buhl",
      "definition": "adjective: able",
      "example": "to be used or likely to succeed"
    },
    {
      "word": "village",
      "pronunciation": "vil-ij",
      "definition": "noun: a",
      "example": "small town in a country area"
    },
    {
      "word": "vision",
      "pronunciation": "vizh-uhn",
      "definition": "noun: the",
      "example": "power or sense of seeing"
    },
    {
      "word": "waiter",
      "pronunciation": "wayt-uh",
      "definition": "noun: someone",
      "example": "who serves food and drink to you at your table in a restaurant or  hotel"
    },
    {
      "word": "waterproof",
      "pronunciation": "waw-tuh-proohf",
      "definition": "adjective: not",
      "example": "letting water through"
    }
  ],
  "Level 3": [
    {
      "word": "abandon",
      "pronunciation": "uh-ban-duhn",
      "definition": "verb: to",
      "example": "leave completely and finally"
    },
    {
      "word": "abduct",
      "pronunciation": "uhb-dukt",
      "definition": "verb: to",
      "example": "kidnap someone or carry them away by force"
    },
    {
      "word": "abrupt",
      "pronunciation": "uh-brupt",
      "definition": "adjective: something",
      "example": "that is sudden or unexpected"
    },
    {
      "word": "absence",
      "pronunciation": "ab-suhns",
      "definition": "noun: a",
      "example": "state or period of being away"
    },
    {
      "word": "abstain",
      "pronunciation": "uhb-stayn",
      "definition": "verb: to",
      "example": "refrain from doing something"
    },
    {
      "word": "accident",
      "pronunciation": "ak-suh-duhnt",
      "definition": "noun: an",
      "example": "unwanted or unlucky happening"
    },
    {
      "word": "according",
      "pronunciation": "uh-kawd-ing",
      "definition": "adverb: as",
      "example": "said by someone"
    },
    {
      "word": "accounting",
      "pronunciation": "uh-kown-ting",
      "definition": "noun: the",
      "example": "theory and system of setting up and looking after the books of a business,  so that its financial position can be examined and the owners can find out how well"
    },
    {
      "word": "achieve",
      "pronunciation": "uh-cheev",
      "definition": "verb: to",
      "example": "bring something about by trying hard"
    },
    {
      "word": "acrobat",
      "pronunciation": "ak-ruh-bat",
      "definition": "noun: someone",
      "example": "who performs gymnastic tricks"
    },
    {
      "word": "activate",
      "pronunciation": "ak-tuh-vayt",
      "definition": "verb: to",
      "example": "make something active or set it in motion"
    },
    {
      "word": "adamant",
      "pronunciation": "ad-uh-muhnt",
      "definition": "adjective: staying",
      "example": "firm in what you decide"
    },
    {
      "word": "addition",
      "pronunciation": "uh-dish-uhn",
      "definition": "noun: the",
      "example": "act of adding numbers together"
    },
    {
      "word": "admire",
      "pronunciation": "uhd-muy-uh",
      "definition": "verb: to",
      "example": "think that someone or something is very good"
    },
    {
      "word": "aerate",
      "pronunciation": "air-rayt",
      "definition": "verb: to",
      "example": "charge or treat with air or gas, especially with carbon dioxide"
    },
    {
      "word": "agenda",
      "pronunciation": "uh-jen-duh",
      "definition": "noun: the",
      "example": "list or plan of what has to be done or talked about, especially at a meeting"
    },
    {
      "word": "aghast",
      "pronunciation": "uh-gahst",
      "definition": "adjective: shocked",
      "example": "and frightened"
    },
    {
      "word": "alias",
      "pronunciation": "ay-lee-uhs",
      "definition": "noun: a",
      "example": "false name"
    },
    {
      "word": "allocate",
      "pronunciation": "al-uh-kayt",
      "definition": "verb: to",
      "example": "set aside for a particular purpose"
    },
    {
      "word": "almond",
      "pronunciation": "ah-muhnd",
      "definition": "noun: an",
      "example": "oval-shaped, cream-coloured nut with a sweet taste"
    },
    {
      "word": "anchor",
      "pronunciation": "ang-kuh",
      "definition": "noun: a",
      "example": "heavy object chained to a boat and dropped into the water to stop the boat f"
    },
    {
      "word": "annual",
      "pronunciation": "an-yooh-uhl",
      "definition": "adjective: happening",
      "example": "once a year  It was the annual surfing competition and I was determined to do better this year"
    },
    {
      "word": "annul",
      "pronunciation": "uh-nul",
      "definition": "verb: to",
      "example": "abolish or wipe out"
    },
    {
      "word": "appease",
      "pronunciation": "uh-peez",
      "definition": "verb: to",
      "example": "make someone peaceful, quiet or happy"
    },
    {
      "word": "appraise",
      "pronunciation": "uh-prayz",
      "definition": "verb: to",
      "example": "make a judgement about something's value"
    },
    {
      "word": "aqua",
      "pronunciation": "ak-wuh",
      "definition": "adjective: light",
      "example": "blue-green or greenish blue"
    },
    {
      "word": "archery",
      "pronunciation": "ah-chuh-ree",
      "definition": "noun: the",
      "example": "sport of shooting with a bow and arrows"
    },
    {
      "word": "assertive",
      "pronunciation": "uh-ser-tiv",
      "definition": "adjective: assured",
      "example": "and strong"
    },
    {
      "word": "attain",
      "pronunciation": "uh-tayn",
      "definition": "verb: to",
      "example": "accomplish by continued effort"
    },
    {
      "word": "avatar",
      "pronunciation": "av-uh-tah",
      "definition": "noun: the",
      "example": "representation of a person in virtual reality on a computer screen"
    },
    {
      "word": "avocado",
      "pronunciation": "av-uh-kah-doh",
      "definition": "noun: a",
      "example": "green, pear-shaped fruit with a large seed"
    },
    {
      "word": "awesome",
      "pronunciation": "aw-suhm",
      "definition": "adjective: filling",
      "example": "you with feelings of respect and fear  I'm not surprised that so much damage was caused by the awesome power of the"
    },
    {
      "word": "banquet",
      "pronunciation": "bang-kwuht",
      "definition": "noun: a",
      "example": "large formal dinner for many guests, usually held for a special occasion"
    },
    {
      "word": "bargain",
      "pronunciation": "bah-guhn",
      "definition": "noun: something",
      "example": "you buy for less than you expected to pay for it"
    },
    {
      "word": "basset",
      "pronunciation": "bas-uht",
      "definition": "noun: a",
      "example": "long-bodied dog with short legs and long ears  My basset loves to run in the dog park but he can't go very fast because his legs are"
    },
    {
      "word": "battery",
      "pronunciation": "bat-uh-ree",
      "definition": "noun: a",
      "example": "container which stores electricity"
    },
    {
      "word": "bauble",
      "pronunciation": "baw-buhl",
      "definition": "noun: a",
      "example": "bright ornament"
    },
    {
      "word": "beginning",
      "pronunciation": "buh-gin-ing",
      "definition": "noun: the",
      "example": "time or place when something starts"
    },
    {
      "word": "beige",
      "pronunciation": "bayzh",
      "definition": "adjective: very",
      "example": "light brown"
    },
    {
      "word": "benefit",
      "pronunciation": "ben-uh-fuht",
      "definition": "noun: anything",
      "example": "that is good for you"
    },
    {
      "word": "berth",
      "pronunciation": "berth",
      "definition": "noun: a",
      "example": "place to sleep on a boat or train  Because it was such a long trip, he reserved a cabin with a berth so he could get some"
    },
    {
      "word": "blockade",
      "pronunciation": "blok-ayd",
      "definition": "noun: the",
      "example": "closing of a port by enemy ships or soldiers to stop supplies from going in  or out"
    },
    {
      "word": "boundary",
      "pronunciation": "bown-dree",
      "definition": "noun: a",
      "example": "dividing line or limit"
    },
    {
      "word": "bovine",
      "pronunciation": "boh-vuyn",
      "definition": "adjective: having",
      "example": "to do with the family of cud-chewing animals that includes cows,  bulls and oxen"
    },
    {
      "word": "brilliant",
      "pronunciation": "bril-yuhnt",
      "definition": "adjective: when",
      "example": "something shines with a very bright light  My teacher said it was a great day for a carnival -- brilliant sunshine and a light"
    },
    {
      "word": "budget",
      "pronunciation": "buj-uht",
      "definition": "noun: a",
      "example": "plan showing what money you will earn and how you will spend it"
    },
    {
      "word": "bureau",
      "pronunciation": "byooh-roh",
      "definition": "noun: a",
      "example": "government office where people can get information"
    },
    {
      "word": "bypass",
      "pronunciation": "buy-pahs",
      "definition": "noun: a",
      "example": "road built to take traffic around the edge rather than through a town or a  busy traffic area"
    },
    {
      "word": "cajole",
      "pronunciation": "kuh-johl",
      "definition": "verb: to",
      "example": "persuade, using pleasantness and flattery"
    },
    {
      "word": "calamari",
      "pronunciation": "kal-uh-mah-ree",
      "definition": "noun: squid",
      "example": "when it is used as food"
    },
    {
      "word": "caramel",
      "pronunciation": "ka-ruh-muhl",
      "definition": "noun: a",
      "example": "type of sweet, or a colouring or flavouring made from burnt sugar"
    },
    {
      "word": "carnival",
      "pronunciation": "kah-nuh-vuhl",
      "definition": "noun: a",
      "example": "time of processions and public celebrations, usually for a special occasion"
    },
    {
      "word": "cashier",
      "pronunciation": "kash-ear",
      "definition": "noun: someone",
      "example": "who is in charge of the money in a shop or bank"
    },
    {
      "word": "causeway",
      "pronunciation": "kawz-way",
      "definition": "noun: a",
      "example": "raised road or path across low or wet ground"
    },
    {
      "word": "chaplain",
      "pronunciation": "chap-luhn",
      "definition": "noun: a",
      "example": "member of the clergy who works in a school, hospital or the armed forces"
    },
    {
      "word": "cheerleader",
      "pronunciation": "chear-leed-uh",
      "definition": "noun: one",
      "example": "of a group of people who encourage cheering, especially at sports  matches"
    },
    {
      "word": "chemist",
      "pronunciation": "kem-uhst",
      "definition": "noun: someone",
      "example": "whose job is to make and sell medicines"
    },
    {
      "word": "coconut",
      "pronunciation": "koh-kuh-nut",
      "definition": "noun: the",
      "example": "large, hard nut of a kind of palm tree, which is lined with white flesh and  contains a clear milk"
    },
    {
      "word": "collection",
      "pronunciation": "kuh-lek-shuhn",
      "definition": "noun: something",
      "example": "which is gathered or acquired"
    },
    {
      "word": "column",
      "pronunciation": "kol-uhm",
      "definition": "noun: a",
      "example": "long, upright support"
    },
    {
      "word": "compulsory",
      "pronunciation": "kuhm-pul-suh-ree",
      "definition": "adjective: relating",
      "example": "to something that you must do"
    },
    {
      "word": "concede",
      "pronunciation": "kuhn-seed",
      "definition": "verb: to",
      "example": "admit that something is true"
    },
    {
      "word": "conch",
      "pronunciation": "konch or kongk",
      "definition": "noun: the",
      "example": "spiral shell of a sea snail, which can make a sound if you blow it"
    },
    {
      "word": "concoct",
      "pronunciation": "kuhn-kokt",
      "definition": "verb: to",
      "example": "make up or invent a story, account or excuse  The teacher grouped us in pairs and asked us to concoct a story that contained an"
    },
    {
      "word": "constraint",
      "pronunciation": "kuhn-straynt",
      "definition": "noun: something",
      "example": "that restricts or controls the way you behave or what you can do at  certain times"
    },
    {
      "word": "contradict",
      "pronunciation": "kon-truh-dikt",
      "definition": "verb: to",
      "example": "deny or say the opposite of"
    },
    {
      "word": "convene",
      "pronunciation": "kuhn-veen",
      "definition": "verb: to",
      "example": "call or gather together"
    },
    {
      "word": "corridor",
      "pronunciation": "ko-ruh-daw",
      "definition": "noun: a",
      "example": "connecting passage in a building"
    },
    {
      "word": "cosmonaut",
      "pronunciation": "koz-muh-nawt",
      "definition": "noun: a",
      "example": "person trained as a pilot, to take part in the flight of a spacecraft"
    },
    {
      "word": "coup",
      "pronunciation": "kooh",
      "definition": "noun: a",
      "example": "sudden, forceful move, especially to take over power"
    },
    {
      "word": "cryptic",
      "pronunciation": "krip-tik",
      "definition": "adjective: mysterious,",
      "example": "or difficult to understand"
    },
    {
      "word": "crystal",
      "pronunciation": "kriss-tuhl",
      "definition": "noun: a",
      "example": "clear mineral which looks like ice"
    },
    {
      "word": "curious",
      "pronunciation": "kyooh-ree-uhs",
      "definition": "adjective: anxious",
      "example": "or eager to learn"
    },
    {
      "word": "geranium",
      "pronunciation": "juh-ray-nee-uhm",
      "definition": "noun: a",
      "example": "common garden plant with red, pink or purple flowers  I don't have much luck getting things to grow in the garden but I have a nice"
    },
    {
      "word": "glorious",
      "pronunciation": "glaw-ree-uhs",
      "definition": "adjective: beautiful,",
      "example": "wonderful, or delightful"
    },
    {
      "word": "gnarled",
      "pronunciation": "nahld",
      "definition": "adjective: twisted",
      "example": "and having many woody lumps"
    },
    {
      "word": "gorgeous",
      "pronunciation": "gaw-juhs",
      "definition": "adjective: beautiful",
      "example": "or attractive"
    },
    {
      "word": "gracious",
      "pronunciation": "gray-shuhs",
      "definition": "adjective: showing",
      "example": "kindness and good manners"
    },
    {
      "word": "grazier",
      "pronunciation": "gray-zee-uh",
      "definition": "noun: a",
      "example": "farmer who usually has a large area of land on which cattle or sheep are kept"
    },
    {
      "word": "gristle",
      "pronunciation": "griss-uhl",
      "definition": "noun: a",
      "example": "firm part in meat that is hard to chew"
    },
    {
      "word": "headache",
      "pronunciation": "hed-ayk",
      "definition": "noun: a",
      "example": "pain in the head  I'm surprised our builder didn't get a headache with all of the hammering and drilling"
    },
    {
      "word": "herbicide",
      "pronunciation": "herb-uh-suyd",
      "definition": "noun: a",
      "example": "chemical that kills plants"
    },
    {
      "word": "hospital",
      "pronunciation": "hos-pi-tl",
      "definition": "noun: a",
      "example": "place where sick and injured people are given medical treatment"
    },
    {
      "word": "hypnosis",
      "pronunciation": "hip-noh-suhs",
      "definition": "noun: a",
      "example": "sleep-like state brought about by allowing someone to control your mind  and actions"
    },
    {
      "word": "idiom",
      "pronunciation": "id-ee-uhm",
      "definition": "noun: an",
      "example": "expression which usually has a meaning that is different to the literal  meaning of the words"
    },
    {
      "word": "impartial",
      "pronunciation": "im-pah-shuhl",
      "definition": "adjective: not",
      "example": "taking one side or the other"
    },
    {
      "word": "inhumane",
      "pronunciation": "in-hyooh-mayn",
      "definition": "adjective: showing",
      "example": "no pity or compassion"
    },
    {
      "word": "influence",
      "pronunciation": "in-flooh-uhns",
      "definition": "noun: some",
      "example": "force or power that affects someone or something else"
    },
    {
      "word": "inquest",
      "pronunciation": "in-kwest",
      "definition": "noun: a",
      "example": "legal or judicial inquiry, especially before a jury"
    },
    {
      "word": "insomnia",
      "pronunciation": "in-som-nee-uh",
      "definition": "noun: difficulty",
      "example": "in sleeping"
    },
    {
      "word": "inspiration",
      "pronunciation": "in-spuh-ray-shuhn",
      "definition": "noun: something",
      "example": "that gives you a new idea, thought, feeling, and so on"
    },
    {
      "word": "insulin",
      "pronunciation": "in-shuh-luhn or in-syuh-luhn",
      "definition": "noun: a",
      "example": "substance your body produces to help it use the sugar in the food you eat"
    },
    {
      "word": "irrigate",
      "pronunciation": "i-ruh-gayt",
      "definition": "verb: to",
      "example": "supply land with water using a system of canals and pipes"
    },
    {
      "word": "javelin",
      "pronunciation": "jav-uh-luhn",
      "definition": "noun: a",
      "example": "spear which is thrown in sporting contests"
    },
    {
      "word": "kindergarten",
      "pronunciation": "kin-duh-gah-tuhn",
      "definition": "noun: a",
      "example": "school or class for very young children which prepares them for primary  school"
    },
    {
      "word": "kitchen",
      "pronunciation": "kich-uhn",
      "definition": "noun: the",
      "example": "room or place where food is cooked and prepared"
    },
    {
      "word": "lavender",
      "pronunciation": "lav-uhn-duh",
      "definition": "noun: a",
      "example": "pale bluish-purple colour"
    },
    {
      "word": "ledger",
      "pronunciation": "lej-uh",
      "definition": "noun: an",
      "example": "account book used to record money that is paid out and paid in"
    },
    {
      "word": "lenient",
      "pronunciation": "lee-nee-uhnt",
      "definition": "adjective: not",
      "example": "severe in treatment, spirit, or tendency"
    },
    {
      "word": "malfunction",
      "pronunciation": "mal-fungk-shuhn",
      "definition": "verb: to",
      "example": "fail to work properly  The factory didn't expect their machinery to malfunction because they had it serviced"
    },
    {
      "word": "mansion",
      "pronunciation": "man-shuhn",
      "definition": "noun: a",
      "example": "very large house"
    },
    {
      "word": "marmalade",
      "pronunciation": "mah-muh-layd",
      "definition": "noun: a",
      "example": "jam made of citrus fruits, such as oranges and grapefruit"
    },
    {
      "word": "meanwhile",
      "pronunciation": "meen-wuyl or meen-wuyl",
      "definition": "adverb: at",
      "example": "the same time  My sister was inside doing her homework. Meanwhile, her friends were playing"
    },
    {
      "word": "measles",
      "pronunciation": "mee-zuhlz",
      "definition": "noun: a",
      "example": "type of infectious disease occurring mostly in children, with a fever and rash"
    },
    {
      "word": "minority",
      "pronunciation": "muy-no-ruh-tee or muh-no-ruh-tee",
      "definition": "noun: the",
      "example": "smaller number of something, or less than half of it"
    },
    {
      "word": "mortified",
      "pronunciation": "maw-tuh-fuyd",
      "definition": "adjective: shamed,",
      "example": "as by a severe wound to the pride"
    },
    {
      "word": "mundane",
      "pronunciation": "mun-dayn",
      "definition": "adjective: ordinary",
      "example": "or boring"
    },
    {
      "word": "nostalgia",
      "pronunciation": "noss-tal-juh",
      "definition": "noun: a",
      "example": "longing for the past and all the things that belonged to it"
    },
    {
      "word": "numerous",
      "pronunciation": "nyooh-muh-ruhs",
      "definition": "adjective: very",
      "example": "many"
    },
    {
      "word": "obsession",
      "pronunciation": "uhb-sesh-uhn",
      "definition": "noun: a",
      "example": "strong idea or feeling which controls someone's behaviour"
    },
    {
      "word": "occasion",
      "pronunciation": "uh-kay-zhuhn",
      "definition": "noun: a",
      "example": "particular time or event  The teacher said that on this occasion she would give us extra time to get our"
    },
    {
      "word": "opponent",
      "pronunciation": "uh-poh-nuhnt",
      "definition": "noun: someone",
      "example": "who is on the opposite side to you in a competition or fight"
    },
    {
      "word": "oracle",
      "pronunciation": "aw-gan-zuh",
      "definition": "noun: someone",
      "example": "who answers difficult questions or reveals the future"
    },
    {
      "word": "organza",
      "pronunciation": "aw-gan-zuh",
      "definition": "noun: a",
      "example": "material made from a mixture of silk or nylon with cotton"
    },
    {
      "word": "original",
      "pronunciation": "uh-rij-uh-nuhl",
      "definition": "adjective: first",
      "example": "or earliest"
    },
    {
      "word": "overbearing",
      "pronunciation": "oh-vuh-bair-ring",
      "definition": "adjective: domineering",
      "example": "and bossy"
    },
    {
      "word": "ozone",
      "pronunciation": "oh-zohn",
      "definition": "noun: a",
      "example": "form of oxygen with three atoms to the molecule, having a peculiar smell"
    },
    {
      "word": "pageant",
      "pronunciation": "paj-uhnt",
      "definition": "noun: a",
      "example": "colourful public show, often including a procession of people in costume"
    },
    {
      "word": "palatial",
      "pronunciation": "puh-lay-shuhl",
      "definition": "adjective: large",
      "example": "and grand"
    },
    {
      "word": "pallor",
      "pronunciation": "pal-uh",
      "definition": "noun: unnatural",
      "example": "paleness"
    },
    {
      "word": "pamphlet",
      "pronunciation": "pam-fluht",
      "definition": "noun: a",
      "example": "very small paper-covered book"
    },
    {
      "word": "paramedic",
      "pronunciation": "pa-ruh-med-ik",
      "definition": "noun: a",
      "example": "person who provides medical care to injured or sick people before they get  to hospital"
    },
    {
      "word": "parishioner",
      "pronunciation": "puh-rish-uh-nuh",
      "definition": "noun: someone",
      "example": "who is a member of a church parish"
    },
    {
      "word": "parity",
      "pronunciation": "pa-ruh-tee",
      "definition": "noun: equality",
      "example": "in amount, status, or character"
    },
    {
      "word": "parsley",
      "pronunciation": "pahs-lee",
      "definition": "noun: a",
      "example": "herb used as a garnish or to season food"
    },
    {
      "word": "pashmina",
      "pronunciation": "pash-mee-nuh",
      "definition": "noun: a",
      "example": "shawl made from fine wool from Himalayan goats, sometimes mixed with  silk"
    },
    {
      "word": "passionate",
      "pronunciation": "pash-uh-nuht",
      "definition": "adjective: having",
      "example": "or showing very strong feelings"
    },
    {
      "word": "peculiar",
      "pronunciation": "puh-kyooh-lyuh",
      "definition": "adjective: strange",
      "example": "or unusual"
    },
    {
      "word": "pedicure",
      "pronunciation": "ped-uh-kyooh-uh",
      "definition": "noun: professional",
      "example": "care or treatment of the feet"
    },
    {
      "word": "pedigree",
      "pronunciation": "ped-uh-gree",
      "definition": "noun: a",
      "example": "line of ancestors or line of descent, especially when recorded, of people or  animals"
    },
    {
      "word": "perilous",
      "pronunciation": "pe-ruh-luhs",
      "definition": "adjective: hazardous",
      "example": "or dangerous"
    },
    {
      "word": "periscope",
      "pronunciation": "pe-ruh-skohp",
      "definition": "noun: an",
      "example": "instrument made of a tube with an arrangement of mirrors, used to see  something from a position below or behind it"
    },
    {
      "word": "perpetual",
      "pronunciation": "puh-pech-ooh-uhl",
      "definition": "adjective: continuing",
      "example": "without a break"
    },
    {
      "word": "persona",
      "pronunciation": "per-soh-nuh",
      "definition": "noun: the",
      "example": "outer or public personality, which is presented to the world"
    },
    {
      "word": "pesticide",
      "pronunciation": "pest-uh-suyd",
      "definition": "noun: a",
      "example": "chemical for killing animals, such as insects, that are dangerous or harmful"
    },
    {
      "word": "pinafore",
      "pronunciation": "pin-uh-faw",
      "definition": "noun: an",
      "example": "apron"
    },
    {
      "word": "pittance",
      "pronunciation": "pit-uhns",
      "definition": "noun: a",
      "example": "very small amount of money"
    },
    {
      "word": "platinum",
      "pronunciation": "plat-uh-nuhm",
      "definition": "noun: a",
      "example": "greyish-white, metallic element  I knew that platinum is often used for making jewellery but I was surprised to find out"
    },
    {
      "word": "possessive",
      "pronunciation": "puh-zes-iv",
      "definition": "adjective: wanting",
      "example": "to keep or control something or someone all by yourself  The collector was possessive of all his model ships and wouldn't let anyone touch"
    },
    {
      "word": "poultry",
      "pronunciation": "pohl-tree",
      "definition": "noun: birds",
      "example": "that are kept for their eggs or meat"
    },
    {
      "word": "precious",
      "pronunciation": "presh-uhs",
      "definition": "adjective: of",
      "example": "great price or value"
    },
    {
      "word": "preservative",
      "pronunciation": "pruh-zerv-uh-tiv",
      "definition": "noun: a",
      "example": "chemical substance that prevents something, such as food, from going bad"
    },
    {
      "word": "profound",
      "pronunciation": "pruh-fownd",
      "definition": "adjective: very",
      "example": "deep"
    },
    {
      "word": "progression",
      "pronunciation": "pruh-gresh-uhn",
      "definition": "noun: forward",
      "example": "or onward movement"
    },
    {
      "word": "prominent",
      "pronunciation": "prom-uh-nuhnt",
      "definition": "adjective: very",
      "example": "noticeable"
    },
    {
      "word": "pronounce",
      "pronunciation": "pruh-nowns",
      "definition": "verb: to",
      "example": "make the sound of a word"
    },
    {
      "word": "prosperous",
      "pronunciation": "pross-puh-ruhs",
      "definition": "adjective: wealthy",
      "example": "and successful  The prosperous family owned a chalet in the mountains as well as an amazing house"
    },
    {
      "word": "purport",
      "pronunciation": "per-pawt",
      "definition": "verb: to",
      "example": "claim  These men purport to be from the local council, but check their identification to make"
    },
    {
      "word": "pyramid",
      "pronunciation": "pi-ruh-mid",
      "definition": "noun: a",
      "example": "structure with a square base and with sides sloping to a point"
    },
    {
      "word": "quadrangle",
      "pronunciation": "kwod-rang-guhl",
      "definition": "noun: a",
      "example": "square or rectangular courtyard surrounded by buildings"
    },
    {
      "word": "quantity",
      "pronunciation": "kwon-tuh-tee",
      "definition": "noun: an",
      "example": "amount or measure  I must have put the wrong quantity of flour in the mixture, because the cake was very"
    },
    {
      "word": "quarry",
      "pronunciation": "kwo-ree",
      "definition": "noun: a",
      "example": "large, open pit where stone used for building is cut or blasted out of the  ground"
    },
    {
      "word": "quarterly",
      "pronunciation": "kwaw-tuh-lee",
      "definition": "adjective: happening",
      "example": "or done every three months"
    },
    {
      "word": "rational",
      "pronunciation": "rash-uhn-uhl",
      "definition": "adjective: in",
      "example": "possession of one's reason"
    },
    {
      "word": "receptionist",
      "pronunciation": "ruh-sep-shuhn-uhst",
      "definition": "noun: someone",
      "example": "employed in an office or hotel to look after callers or guests  The receptionist managed three separate phone lines and a waiting room full of"
    },
    {
      "word": "reconstruct",
      "pronunciation": "ree-kuhn-strukt",
      "definition": "verb: to",
      "example": "rebuild  The engineers had to reconstruct the drone piece by piece after they flew it into a"
    },
    {
      "word": "referee",
      "pronunciation": "ref-uh-ree",
      "definition": "noun: someone",
      "example": "who makes sure that the rules in a sporting match are followed"
    },
    {
      "word": "regime",
      "pronunciation": "ray-zheem",
      "definition": "noun: a",
      "example": "system of rule or government"
    },
    {
      "word": "relaxation",
      "pronunciation": "ree-lak-say-shuhn",
      "definition": "noun: a",
      "example": "stopping of bodily or mental effort"
    },
    {
      "word": "remarkable",
      "pronunciation": "ruh-mahk-uh-buhl",
      "definition": "adjective: worthy",
      "example": "of notice because unusual or extraordinary"
    },
    {
      "word": "replenish",
      "pronunciation": "ruh-plen-ish",
      "definition": "verb: to",
      "example": "make full or complete again"
    },
    {
      "word": "replica",
      "pronunciation": "rep-lik-uh",
      "definition": "noun: a",
      "example": "copy or reproduction, especially of a work of art  Egyptian authorities have unveiled a replica of Tutankhamen's tomb in an effort to"
    },
    {
      "word": "residue",
      "pronunciation": "rez-uh-dyooh",
      "definition": "noun: what",
      "example": "is left after a process like burning or chemical change"
    },
    {
      "word": "respectable",
      "pronunciation": "ruh-spek-tuh-buhl",
      "definition": "adjective: worthy",
      "example": "of high regard"
    },
    {
      "word": "restaurant",
      "pronunciation": "res-tuh-ront",
      "definition": "noun: a",
      "example": "place where meals are served to customers"
    },
    {
      "word": "retina",
      "pronunciation": "ret-uh-nuh",
      "definition": "noun: the",
      "example": "coating on the back part of your eyeball which receives the image of what  you see"
    },
    {
      "word": "ricotta",
      "pronunciation": "ruh-kot-uh",
      "definition": "noun: a",
      "example": "soft, fresh white cheese with a delicate flavour"
    },
    {
      "word": "ridicule",
      "pronunciation": "rid-uh-kyoohl",
      "definition": "verb: to",
      "example": "make fun of someone"
    },
    {
      "word": "salient",
      "pronunciation": "say-lee-uhnt",
      "definition": "adjective: standing",
      "example": "out or easily seen"
    },
    {
      "word": "sausage",
      "pronunciation": "soss-ij",
      "definition": "noun: finely",
      "example": "chopped up meat packed into a thin skin"
    },
    {
      "word": "scarab",
      "pronunciation": "ska-ruhb",
      "definition": "noun: a",
      "example": "type of beetle, regarded as sacred by the ancient Egyptians  I bought a replica of a scarab when I was in Egypt -- they were regarded as sacred by"
    },
    {
      "word": "scrounge",
      "pronunciation": "skrownj",
      "definition": "verb: to",
      "example": "forage or search for something"
    },
    {
      "word": "scrutiny",
      "pronunciation": "skrooh-tuh-nee",
      "definition": "noun: close",
      "example": "examination"
    },
    {
      "word": "secrecy",
      "pronunciation": "seek-ruh-see",
      "definition": "noun: the",
      "example": "state of being private or concealed  It was essential that the spies met in secrecy otherwise all their plans would be for"
    },
    {
      "word": "semblance",
      "pronunciation": "sem-bluhns",
      "definition": "noun: an",
      "example": "appearance or likeness  She tried to arrange her thoughts into some semblance of order before starting her"
    },
    {
      "word": "semicolon",
      "pronunciation": "sem-ee-koh-luhn",
      "definition": "noun: a",
      "example": "punctuation mark which looks like a full stop over a comma, used to show a  break between parts of a sentence"
    },
    {
      "word": "sensor",
      "pronunciation": "sen-suh",
      "definition": "noun: any",
      "example": "device that can detect something and respond to it, usually by setting off a  signal"
    },
    {
      "word": "sensory",
      "pronunciation": "sen-suh-ree or sen'sawreeuhl",
      "definition": "adjective: having",
      "example": "to do with feeling"
    },
    {
      "word": "serene",
      "pronunciation": "suh-reen",
      "definition": "adjective: calm",
      "example": "and peaceful"
    },
    {
      "word": "shambolic",
      "pronunciation": "sham-bol-ik",
      "definition": "adjective: confused",
      "example": "or disorderly  I didn't think I'd have much luck finding the receipt I wanted in my shambolic mess of"
    },
    {
      "word": "shepherd",
      "pronunciation": "shep-uhd",
      "definition": "noun: someone",
      "example": "who looks after sheep"
    },
    {
      "word": "siesta",
      "pronunciation": "see-ess-tuh",
      "definition": "noun: a",
      "example": "midday or afternoon rest"
    },
    {
      "word": "silicone",
      "pronunciation": "sil-uh-kohn",
      "definition": "noun: a",
      "example": "synthetic material which can withstand extreme temperatures"
    },
    {
      "word": "sinuous",
      "pronunciation": "sin-yooh-uhs",
      "definition": "adjective: having",
      "example": "many curves, bends, or turns"
    },
    {
      "word": "slalom",
      "pronunciation": "slay-luhm or slah-luhm",
      "definition": "noun: a",
      "example": "skiing race with a winding course"
    },
    {
      "word": "sludge",
      "pronunciation": "sluj",
      "definition": "noun: soft",
      "example": "muddy substance"
    },
    {
      "word": "solvent",
      "pronunciation": "sol-vuhnt",
      "definition": "noun: a",
      "example": "substance, usually liquid, that can dissolve other substances in it"
    },
    {
      "word": "sombre",
      "pronunciation": "som-buh",
      "definition": "adjective: dark",
      "example": "or serious in a way that makes you feel gloomy"
    },
    {
      "word": "sorbet",
      "pronunciation": "saw-bay or saw-buht",
      "definition": "noun: a",
      "example": "frozen dessert made with fruit and egg whites"
    },
    {
      "word": "spiritual",
      "pronunciation": "spi-ruh-chooh-uhl",
      "definition": "adjective: having",
      "example": "to do with holy, religious, or supernatural things"
    },
    {
      "word": "sporadic",
      "pronunciation": "spuh-rad-ik",
      "definition": "adjective: irregular",
      "example": "and not very frequent"
    },
    {
      "word": "squalid",
      "pronunciation": "skwol-uhd",
      "definition": "adjective: dirty",
      "example": "or filthy"
    },
    {
      "word": "stampede",
      "pronunciation": "stam-peed",
      "definition": "noun: a",
      "example": "sudden rush of a group of animals or people, often in fright"
    },
    {
      "word": "sternum",
      "pronunciation": "ster-nuhm",
      "definition": "noun: the",
      "example": "breastbone"
    },
    {
      "word": "studious",
      "pronunciation": "styooh-dee-uhs",
      "definition": "adjective: liking",
      "example": "to learn by studying"
    },
    {
      "word": "substitute",
      "pronunciation": "sub-stuh-tyooht",
      "definition": "verb: to",
      "example": "put a person or thing in the place of another"
    },
    {
      "word": "subtle",
      "pronunciation": "sut-uhl",
      "definition": "adjective: so",
      "example": "fine or slight as to not be obvious or clear"
    },
    {
      "word": "surgeon",
      "pronunciation": "ser-juhn",
      "definition": "noun: a",
      "example": "doctor who performs surgery"
    },
    {
      "word": "surveyor",
      "pronunciation": "ser-vay-uh",
      "definition": "noun: someone",
      "example": "whose job is taking surveys, particularly of land"
    }
  ],
  "Level 4": [
    {
      "word": "adhesive",
      "pronunciation": "uhd-hee-siv or uhd-hee-ziv",
      "definition": "noun: a",
      "example": "substance which sticks things together"
    },
    {
      "word": "admission",
      "pronunciation": "uhd-mish-uhn",
      "definition": "noun: the",
      "example": "process of entering"
    },
    {
      "word": "aggrieved",
      "pronunciation": "uh-greevd",
      "definition": "adjective: feeling",
      "example": "hurt or wronged"
    },
    {
      "word": "alligator",
      "pronunciation": "al-uh-gay-tuh",
      "definition": "noun: an",
      "example": "animal like a crocodile, but with a broader snout"
    },
    {
      "word": "amicable",
      "pronunciation": "am-ik-uh-buhl",
      "definition": "adjective: friendly",
      "example": "I hope this committee meeting will be amicable, without the arguments of last time.  animosity"
    },
    {
      "word": "anxiety",
      "pronunciation": "ang-zuy-uh-tee",
      "definition": "noun: feelings",
      "example": "of worry or fear"
    },
    {
      "word": "appalled",
      "pronunciation": "uh-pawld",
      "definition": "adjective: filled",
      "example": "with horror"
    },
    {
      "word": "arbiter",
      "pronunciation": "ah-buh-tuh",
      "definition": "noun: a",
      "example": "person in a position to decide points of disagreement"
    },
    {
      "word": "attribute",
      "pronunciation": "uh-trib-yooht",
      "definition": "verb: to",
      "example": "consider as an effect to a cause"
    },
    {
      "word": "bouquet",
      "pronunciation": "booh-kay or boh-kay",
      "definition": "noun: a",
      "example": "bunch of flowers"
    },
    {
      "word": "boycott",
      "pronunciation": "boy-kot",
      "definition": "verb: to",
      "example": "stop buying or using something, especially as a form of protest"
    },
    {
      "word": "burrito",
      "pronunciation": "buh-ree-toh",
      "definition": "noun: (in",
      "example": "Mexican cooking) a tortilla folded over a filling of meat, cheese or beans"
    },
    {
      "word": "celebrity",
      "pronunciation": "suh-leb-ruh-tee",
      "definition": "noun: a",
      "example": "famous or well-known person  The celebrity was followed by hundreds of photographers as she jogged along the"
    },
    {
      "word": "ceremonious",
      "pronunciation": "se-ruh-mohn-ee-uhs",
      "definition": "adjective: marked",
      "example": "by formalities"
    },
    {
      "word": "clavicle",
      "pronunciation": "klav-ik-uhl",
      "definition": "noun: either",
      "example": "of two slender bones each connecting the breastbone with a shoulder  blade and forming the front part of the shoulder"
    },
    {
      "word": "coagulate",
      "pronunciation": "koh-ag-yuh-layt",
      "definition": "verb: to",
      "example": "change from a fluid into a thickened mass"
    },
    {
      "word": "coax",
      "pronunciation": "kohks",
      "definition": "verb: to",
      "example": "persuade someone gently and patiently"
    },
    {
      "word": "coerce",
      "pronunciation": "koh-erce",
      "definition": "verb: to",
      "example": "force someone into doing something"
    },
    {
      "word": "comprehensive",
      "pronunciation": "kom-pruh-hen-siv",
      "definition": "adjective: including",
      "example": "a great deal"
    },
    {
      "word": "condensation",
      "pronunciation": "kon-den-say-shuhn",
      "definition": "noun: the",
      "example": "changing of a gas to a liquid or solid"
    },
    {
      "word": "consummate",
      "pronunciation": "kon-syooh-muht or kon-suh-muht",
      "definition": "adjective: complete",
      "example": "or perfect  The great actor was regarded as a consummate performer, and had won many"
    },
    {
      "word": "convertible",
      "pronunciation": "kuhn-ver-tuh-buhl",
      "definition": "noun: a",
      "example": "car with a top that you can remove"
    },
    {
      "word": "corroborate",
      "pronunciation": "kuh-rob-uh-rayt",
      "definition": "verb: to",
      "example": "strengthen the certainty of something with extra evidence"
    },
    {
      "word": "culminate",
      "pronunciation": "kul-muh-nayt",
      "definition": "verb: to",
      "example": "reach the highest point of something after a period of gradual development"
    },
    {
      "word": "dalmatian",
      "pronunciation": "dal-may-shuhn",
      "definition": "noun: a",
      "example": "breed of dog with a white coat marked with black or brown spots"
    },
    {
      "word": "debacle",
      "pronunciation": "day-bah-kuhl or duh-bah-kuhl",
      "definition": "noun: a",
      "example": "disastrous failure  Unfortunately, the restaurant's opening night was a complete debacle with the chef"
    },
    {
      "word": "delectable",
      "pronunciation": "duh-lek-tuh-buhl",
      "definition": "adjective: delicious",
      "example": "The food at the wedding reception was delectable.  derelict"
    },
    {
      "word": "despicable",
      "pronunciation": "duh-spik-uh-buhl",
      "definition": "adjective: deserving",
      "example": "scorn"
    },
    {
      "word": "diabolical",
      "pronunciation": "duy-uh-bol-ik-uhl",
      "definition": "adjective: devilish",
      "example": "or wicked"
    },
    {
      "word": "diaphanous",
      "pronunciation": "duy-af-uh-nuhs",
      "definition": "adjective: transparent",
      "example": "or translucent"
    },
    {
      "word": "effusive",
      "pronunciation": "uh-fyooh-siv",
      "definition": "adjective: showing",
      "example": "too much feeling"
    },
    {
      "word": "equivalent",
      "pronunciation": "ee-kwiv-uh-luhnt",
      "definition": "adjective: equal",
      "example": "or matching"
    },
    {
      "word": "ethanol",
      "pronunciation": "eth-uh-nol or ee-thuh-nol",
      "definition": "noun: an",
      "example": "alcohol produced from crops and used as a biofuel"
    },
    {
      "word": "exhaustive",
      "pronunciation": "eg-zaws-tiv",
      "definition": "adjective: thorough",
      "example": "or intensive"
    },
    {
      "word": "frivolous",
      "pronunciation": "friv-uh-luhs",
      "definition": "adjective: not",
      "example": "serious"
    },
    {
      "word": "grandeur",
      "pronunciation": "gran-juh",
      "definition": "noun: imposing",
      "example": "greatness or grandness"
    },
    {
      "word": "gruelling",
      "pronunciation": "grooh-uh-ling",
      "definition": "adjective: very",
      "example": "tiring"
    },
    {
      "word": "haphazard",
      "pronunciation": "hap-haz-uhd",
      "definition": "adjective: not",
      "example": "tidily planned or organised"
    },
    {
      "word": "heirloom",
      "pronunciation": "air-loohm",
      "definition": "noun: something",
      "example": "valuable that is handed down from generation to generation in a  family"
    },
    {
      "word": "humorous",
      "pronunciation": "hyooh-muh-ruhs",
      "definition": "adjective: funny",
      "example": "and amusing  We thought it was humorous when my little brother said that a caterpillar was a"
    },
    {
      "word": "imminent",
      "pronunciation": "im-uh-nuhnt",
      "definition": "adjective: likely",
      "example": "to happen at any moment"
    },
    {
      "word": "incidental",
      "pronunciation": "in-suh-den-tuhl",
      "definition": "adjective: coming",
      "example": "as a small accompaniment to something else  You often don't notice the incidental music playing in the background of a film scene,"
    },
    {
      "word": "journalist",
      "pronunciation": "jer-nuhl-uhst",
      "definition": "noun: someone",
      "example": "who writes, edits or produces newspapers and magazines, or news  and current affairs programs on television and radio"
    },
    {
      "word": "lacklustre",
      "pronunciation": "lak-luss-tuh",
      "definition": "adjective: lacking",
      "example": "brightness; dull"
    },
    {
      "word": "likelihood",
      "pronunciation": "luyk-lee-hood",
      "definition": "noun: chance",
      "example": "or probability"
    },
    {
      "word": "locum",
      "pronunciation": "loh-kuhm",
      "definition": "noun: a",
      "example": "temporary stand-in for a doctor, lawyer, and so on"
    },
    {
      "word": "luxury",
      "pronunciation": "luk-shuh-ree",
      "definition": "noun: anything",
      "example": "that makes life extremely pleasant or comfortable"
    },
    {
      "word": "malachite",
      "pronunciation": "mal-uh-kuyt",
      "definition": "noun: a",
      "example": "green mineral often used for ornamental articles"
    },
    {
      "word": "malnutrition",
      "pronunciation": "mal-nyooh-trish-uhn",
      "definition": "noun: illness",
      "example": "caused by not having enough food"
    },
    {
      "word": "marquee",
      "pronunciation": "mah-kee",
      "definition": "noun: a",
      "example": "big tent used for outdoor parties, circuses and so on"
    },
    {
      "word": "millionaire",
      "pronunciation": "mil-yuh-nair",
      "definition": "noun: someone",
      "example": "who has a million dollars or more"
    },
    {
      "word": "miniature",
      "pronunciation": "min-uh-chuh",
      "definition": "noun: a",
      "example": "very small copy or model of something"
    },
    {
      "word": "motif",
      "pronunciation": "moh-teef or moh-tuhf",
      "definition": "noun: an",
      "example": "idea that is repeated in various ways throughout a piece of writing or music  or in the work of an artist"
    },
    {
      "word": "motivation",
      "pronunciation": "moh-tuh-vay-shuhn",
      "definition": "noun: the",
      "example": "desire to achieve a goal"
    },
    {
      "word": "muesli",
      "pronunciation": "myoohz-lee or moohz-lee",
      "definition": "noun: a",
      "example": "breakfast cereal made from oats, chopped fruit and nuts"
    },
    {
      "word": "mysterious",
      "pronunciation": "muhs-tear-ree-uhs",
      "definition": "adjective: puzzling",
      "example": "or full of mystery"
    },
    {
      "word": "niche",
      "pronunciation": "neesh",
      "definition": "noun: a",
      "example": "place or position suitable for a person or thing"
    },
    {
      "word": "onyx",
      "pronunciation": "on-iks",
      "definition": "noun: a",
      "example": "type of quartz consisting of straight bands which differ in colour"
    },
    {
      "word": "opportunity",
      "pronunciation": "op-uh-tyooh-nuh-tee",
      "definition": "noun: a",
      "example": "suitable time or occasion"
    },
    {
      "word": "palaver",
      "pronunciation": "puh-lah-vuh",
      "definition": "noun: any",
      "example": "unnecessarily long business or bother"
    },
    {
      "word": "paperweight",
      "pronunciation": "pay-puh-wayt",
      "definition": "noun: a",
      "example": "small, heavy object laid on papers to keep them from moving  If I want to work with the window open I need a paperweight to stop all my papers"
    },
    {
      "word": "parfait",
      "pronunciation": "pah-fay or pah-fay",
      "definition": "noun: a",
      "example": "dessert, served in a tall glass, made from layers of ice cream, fruit, jelly,  syrup and nuts"
    },
    {
      "word": "participate",
      "pronunciation": "pah-tis-uh-payt",
      "definition": "verb: to",
      "example": "have a part in something or do something with other people"
    },
    {
      "word": "perfectionist",
      "pronunciation": "puh-fek-shuhn-uhst",
      "definition": "noun: someone",
      "example": "who demands nothing less than the best in any area of activity,  behaviour, and so on"
    },
    {
      "word": "permeate",
      "pronunciation": "per-mee-ayt",
      "definition": "verb: to",
      "example": "spread through, pervade or saturate  As the tide came in, a feeling of fear began to permeate through the group in the"
    },
    {
      "word": "persimmon",
      "pronunciation": "per-suh-muhn or puh-sim-uhn",
      "definition": "noun: a",
      "example": "red or orange plum-like fruit"
    },
    {
      "word": "pharmacist",
      "pronunciation": "fahm-uh-suhst",
      "definition": "noun: a",
      "example": "professional person who prepares and dispenses medicines"
    },
    {
      "word": "phenomenon",
      "pronunciation": "fuh-nom-uh-nuhn",
      "definition": "noun: something",
      "example": "or someone that is outside the ordinary"
    },
    {
      "word": "piazza",
      "pronunciation": "pee-at-suh  pee-aht-suh",
      "definition": "noun: an",
      "example": "open square or public place in a city or town"
    },
    {
      "word": "pollution",
      "pronunciation": "puh-looh-shuhn",
      "definition": "noun: harmful",
      "example": "or poisonous substances in the air, rivers, seas, or the water that  people drink"
    },
    {
      "word": "posterior",
      "pronunciation": "poss-teer-ree-uh",
      "definition": "adjective: from",
      "example": "or at the back"
    },
    {
      "word": "precedent",
      "pronunciation": "pree-suh-duhnt or press-uh-duhnt",
      "definition": "noun: an",
      "example": "event or case which may be used as an example for future action  Winning the championship has set a precedent that might be hard to live up to in the"
    },
    {
      "word": "precursory",
      "pronunciation": "pree-ker-suh-ree",
      "definition": "adjective: indicative",
      "example": "of something to follow  The system sent out an alert when it detected the precursory indications of the"
    },
    {
      "word": "prescription",
      "pronunciation": "pruh-skrip-shuhn",
      "definition": "noun: a",
      "example": "written order by the doctor to the pharmacist for the preparation and use of  a medicine"
    },
    {
      "word": "primitive",
      "pronunciation": "prim-uh-tiv",
      "definition": "adjective: being",
      "example": "the earliest in existence"
    },
    {
      "word": "principle",
      "pronunciation": "prin-suh-puhl",
      "definition": "noun: a",
      "example": "general truth or rule"
    },
    {
      "word": "procession",
      "pronunciation": "pruh-sesh-uhn",
      "definition": "noun: an",
      "example": "orderly line of people, cars or floats moving along in a ceremony or as a  show"
    },
    {
      "word": "procrastinate",
      "pronunciation": "pruh-kras-tuh-nayt",
      "definition": "verb: to",
      "example": "put off doing something until another time"
    },
    {
      "word": "professor",
      "pronunciation": "pruh-fess-uh",
      "definition": "noun: a",
      "example": "university teacher of the highest rank"
    },
    {
      "word": "prosperity",
      "pronunciation": "pross-pe-ruh-tee",
      "definition": "noun: flourishing,",
      "example": "or thriving condition  The fishermen were experiencing a season of great prosperity with record hauls of"
    },
    {
      "word": "provincial",
      "pronunciation": "pruh-vin-shuhl",
      "definition": "adjective: having",
      "example": "characteristics considered to be typical of people living away from a  city"
    },
    {
      "word": "qualify",
      "pronunciation": "kwol-uh-fuy",
      "definition": "verb: to",
      "example": "become eligible for a competition by reaching a certain standard  To qualify for the state championships, I have to take two seconds off my personal"
    },
    {
      "word": "quartz",
      "pronunciation": "kwawts",
      "definition": "noun: a",
      "example": "common mineral, used in making clocks and watches"
    },
    {
      "word": "queue",
      "pronunciation": "kyooh",
      "definition": "noun: a",
      "example": "line of people or vehicles waiting in turn for something"
    },
    {
      "word": "raspberry",
      "pronunciation": "rahz-buh-ree",
      "definition": "noun: a",
      "example": "soft, juicy, red berry"
    },
    {
      "word": "raucous",
      "pronunciation": "raw-kuhs",
      "definition": "adjective: harsh-sounding",
      "example": "James is known for his raucous belly laughs.  ravenous"
    },
    {
      "word": "rebellion",
      "pronunciation": "ruh-bel-yuhn",
      "definition": "noun: open,",
      "example": "organised, and armed resistance to a government"
    },
    {
      "word": "receipt",
      "pronunciation": "ruh-seet",
      "definition": "noun: a",
      "example": "signed piece of paper proving that you have received goods and paid money  for them"
    },
    {
      "word": "recipient",
      "pronunciation": "ruh-sip-ee-uhnt",
      "definition": "noun: someone",
      "example": "who receives something"
    },
    {
      "word": "reiki",
      "pronunciation": "ray-kee",
      "definition": "noun: a",
      "example": "method of treating illness or injury in which energy is thought to be released  through the hands of a trained practitioner"
    },
    {
      "word": "remembrance",
      "pronunciation": "ruh-mem-bruhns",
      "definition": "noun: the",
      "example": "act of thinking of and honouring someone"
    },
    {
      "word": "repetition",
      "pronunciation": "rep-uh-tish-uhn",
      "definition": "noun: the",
      "example": "act of doing something over and over"
    },
    {
      "word": "reprehensible",
      "pronunciation": "rep-ruh-hen-suh-buhl",
      "definition": "adjective: very",
      "example": "bad and deserving harsh criticism"
    },
    {
      "word": "requiem",
      "pronunciation": "rek-wee-uhm or ray-kwee-uhm",
      "definition": "noun: music",
      "example": "composed to honour the memory of the dead"
    },
    {
      "word": "resistance",
      "pronunciation": "ruh-zis-tuhns",
      "definition": "noun: the",
      "example": "act of resisting, opposing, or withstanding"
    },
    {
      "word": "restitution",
      "pronunciation": "res-tuh-tyooh-shuhn",
      "definition": "noun: a",
      "example": "paying back of something to someone who has suffered a loss or injury, as  compensation"
    },
    {
      "word": "resumption",
      "pronunciation": "ruh-zump-shuhn",
      "definition": "noun: the",
      "example": "continuation of something after a break or interruption"
    },
    {
      "word": "rueful",
      "pronunciation": "rooh-fuhl",
      "definition": "adjective: feeling,",
      "example": "showing, or expressing sorrow or pity"
    },
    {
      "word": "salinity",
      "pronunciation": "suh-lin-uh-tee",
      "definition": "noun: the",
      "example": "rising of salt from under the ground, making the water in rivers and lakes  too salty to drink, and the soil too salty for farming"
    },
    {
      "word": "salubrious",
      "pronunciation": "suh-looh-bree-uhs",
      "definition": "adjective: of",
      "example": "a place, attractive and prosperous"
    },
    {
      "word": "scythe",
      "pronunciation": "suydh",
      "definition": "noun: a",
      "example": "tool with a long, curved blade joined at an angle to a long handle"
    },
    {
      "word": "secondment",
      "pronunciation": "suh-kond-muhnt",
      "definition": "noun: the",
      "example": "temporary transfer of a worker to another post or organisation  I normally work in IT support but I have a six-month secondment to teach a subject at"
    },
    {
      "word": "seniority",
      "pronunciation": "see-nee-o-ruh-tee",
      "definition": "noun: the",
      "example": "condition or fact of being senior, in age or position  Because of their seniority in the company, they were given the front seats in the"
    },
    {
      "word": "simplicity",
      "pronunciation": "sim-plis-uh-tee",
      "definition": "noun: the",
      "example": "condition or quality of being easy to do or understand  The process was easy to understand due to the simplicity with which it was"
    },
    {
      "word": "skirmish",
      "pronunciation": "sker-mish",
      "definition": "noun: any",
      "example": "short exchange of arguments between people"
    },
    {
      "word": "solace",
      "pronunciation": "so-luhs",
      "definition": "noun: comfort",
      "example": "in sorrow or trouble"
    },
    {
      "word": "spaghetti",
      "pronunciation": "spuh-get-ee",
      "definition": "noun: a",
      "example": "type of pasta, formed into long thin strips, usually served with a sauce"
    },
    {
      "word": "spectre",
      "pronunciation": "spek-tuh",
      "definition": "noun: a",
      "example": "ghost"
    },
    {
      "word": "squadron",
      "pronunciation": "skwod-ruhn",
      "definition": "noun: a",
      "example": "fighting unit in the armed forces, especially in the air force or navy"
    },
    {
      "word": "squire",
      "pronunciation": "skwuy-uh",
      "definition": "noun: an",
      "example": "English country gentleman  We weren't surprised to find out that the large estate we could see in the distance"
    },
    {
      "word": "stalwart",
      "pronunciation": "stawl-wuht",
      "definition": "adjective: strong",
      "example": "and brave"
    },
    {
      "word": "strategist",
      "pronunciation": "strat-uh-juhst",
      "definition": "noun: someone",
      "example": "skilled in devising or planning action or policy  I'm not a military strategist but it would seem sensible not to have our lights on if we"
    },
    {
      "word": "suffice",
      "pronunciation": "suh-fuys",
      "definition": "verb: to",
      "example": "be enough"
    },
    {
      "word": "surmise",
      "pronunciation": "ser-muyz",
      "definition": "verb: to",
      "example": "think something without certain or strong evidence"
    },
    {
      "word": "sustainable",
      "pronunciation": "suh-stayn-uh-buhl",
      "definition": "adjective: able",
      "example": "to continue for a long time without damaging the environment"
    },
    {
      "word": "symbolic",
      "pronunciation": "sim-bol-ik",
      "definition": "adjective: serving",
      "example": "as something that stands for or means something else"
    },
    {
      "word": "syndicate",
      "pronunciation": "sin-duh-kuht",
      "definition": "noun: a",
      "example": "group of people or business companies who combine to carry out an  expensive project"
    },
    {
      "word": "tarragon",
      "pronunciation": "ta-ruh-guhn",
      "definition": "noun: a",
      "example": "strong-smelling herb used in cooking and salads"
    },
    {
      "word": "terracotta",
      "pronunciation": "te-ruh-kot-uh",
      "definition": "noun: a",
      "example": "brownish-red colour"
    },
    {
      "word": "testimonial",
      "pronunciation": "tes-tuh-moh-nee-uhl",
      "definition": "noun: a",
      "example": "statement about someone or something giving an account of their good  qualities"
    },
    {
      "word": "threadbare",
      "pronunciation": "thred-bair",
      "definition": "adjective: worn",
      "example": "and thin"
    },
    {
      "word": "tournament",
      "pronunciation": "taw-nuh-muhnt",
      "definition": "noun: a",
      "example": "meeting for contests in sport or other games"
    },
    {
      "word": "transportation",
      "pronunciation": "trans-paw-tay-shuhn",
      "definition": "noun: a",
      "example": "means of transport  The train is the best form of transportation for moving large groups of people at the"
    },
    {
      "word": "triage",
      "pronunciation": "tree-ahzh",
      "definition": "verb: to",
      "example": "sort sick or injured people according to how urgently they need to be given  medical care"
    },
    {
      "word": "typify",
      "pronunciation": "tip-uh-fuy",
      "definition": "verb: to",
      "example": "be a typical sign of"
    },
    {
      "word": "ultimatum",
      "pronunciation": "ul-tuh-may-tuhm",
      "definition": "noun: a",
      "example": "final statement of terms or conditions  The coach gave an ultimatum that if we didn't come to training, we would not be in"
    },
    {
      "word": "umami",
      "pronunciation": "ooh-mah-mee",
      "definition": "noun: a",
      "example": "taste category, distinguished from sweet, sour, salt, and bitter, which is  common to savoury food such as meat, cheese, mushrooms, etc."
    },
    {
      "word": "uncouth",
      "pronunciation": "un-koohth",
      "definition": "adjective: rough",
      "example": "and bad-mannered"
    },
    {
      "word": "undeniable",
      "pronunciation": "un-duh-nuy-uh-buhl",
      "definition": "adjective: not",
      "example": "able to be proved false"
    },
    {
      "word": "undeterred",
      "pronunciation": "un-duh-terd",
      "definition": "adjective: not",
      "example": "put off one's chosen path or actions"
    },
    {
      "word": "university",
      "pronunciation": "yooh-nuh-ver-suh-tee",
      "definition": "noun: a",
      "example": "place where you can study after you have finished high school"
    }
  ],
  "Level 5": [
    {
      "word": "augment",
      "pronunciation": "awg-ment",
      "definition": "verb: to",
      "example": "make larger"
    },
    {
      "word": "awry",
      "pronunciation": "uh-ruy",
      "definition": "adverb: out",
      "example": "of the proper order"
    },
    {
      "word": "battalion",
      "pronunciation": "buh-tal-yuhn",
      "definition": "noun: a",
      "example": "large army unit"
    },
    {
      "word": "beautician",
      "pronunciation": "byooh-tish-uhn",
      "definition": "noun: a",
      "example": "person skilled in cosmetic treatment"
    },
    {
      "word": "bohemian",
      "pronunciation": "boh-hee-mee-uhn",
      "definition": "adjective: unconventional",
      "example": "and artistic  We were attracted by the bohemian feel of the area, with its cafes, bars and"
    },
    {
      "word": "breathalyser",
      "pronunciation": "breth-uh-luy-zuh",
      "definition": "noun: a",
      "example": "machine used to measure the amount of alcohol in someone's breath"
    },
    {
      "word": "brogue",
      "pronunciation": "brohg",
      "definition": "noun: a",
      "example": "strong accent, especially an Irish one"
    },
    {
      "word": "burgundy",
      "pronunciation": "ber-guhn-dee",
      "definition": "noun: a",
      "example": "purplish-red colour"
    },
    {
      "word": "camphor",
      "pronunciation": "kam-fuh",
      "definition": "noun: a",
      "example": "substance with a strong smell, used to keep moths and other insects away  To prevent damage from moths, some people store their winter clothes with"
    },
    {
      "word": "capacious",
      "pronunciation": "kuh-pay-shuhs",
      "definition": "adjective: able",
      "example": "to hold a lot"
    },
    {
      "word": "cartilage",
      "pronunciation": "kah-tuh-lij",
      "definition": "noun: a",
      "example": "firm elastic tissue found in various parts of the body"
    },
    {
      "word": "cauliflower",
      "pronunciation": "kol-ee-flow-uh",
      "definition": "noun: a",
      "example": "vegetable with a large round head of white flowers"
    },
    {
      "word": "chalet",
      "pronunciation": "shal-ay",
      "definition": "noun: a",
      "example": "small house in the mountains, sometimes used as a holiday house"
    },
    {
      "word": "chenille",
      "pronunciation": "shuh-neel",
      "definition": "noun: a",
      "example": "type of fabric with short tufts of cotton"
    },
    {
      "word": "chiropractor",
      "pronunciation": "kuy-ruh-prak-tuh",
      "definition": "noun: someone",
      "example": "trained to treat back pain and other types of illness by massaging  and adjusting the spine"
    },
    {
      "word": "collaborate",
      "pronunciation": "kuh-lab-uh-rayt",
      "definition": "verb: to",
      "example": "work together in order to achieve something"
    },
    {
      "word": "colloquial",
      "pronunciation": "kuh-loh-kwee-uhl",
      "definition": "adjective: suitable",
      "example": "for casual, informal, or everyday language"
    },
    {
      "word": "compatible",
      "pronunciation": "kuhm-pat-uh-buhl",
      "definition": "adjective: able",
      "example": "to agree or exist side by side  The various emergency services have set up compatible systems to improve response"
    },
    {
      "word": "corps",
      "pronunciation": "kaw",
      "definition": "noun: a",
      "example": "unit of soldiers"
    },
    {
      "word": "creche",
      "pronunciation": "kraysh or kresh",
      "definition": "noun: an",
      "example": "establishment, or an area temporarily set aside, for the minding of babies  or young children for their parents"
    },
    {
      "word": "dachshund",
      "pronunciation": "daks-uhnd or dash-uhnd",
      "definition": "noun: a",
      "example": "small dog with a long body and very short legs"
    },
    {
      "word": "derogatory",
      "pronunciation": "duh-rog-uh-tree or duh-rog-uh-tuh-ree",
      "definition": "adjective: dismissive",
      "example": "or critical"
    },
    {
      "word": "diagnosis",
      "pronunciation": "duy-uhg-noh-suhs",
      "definition": "noun: the",
      "example": "identification of an illness or condition by examination of the symptoms"
    },
    {
      "word": "duplicitous",
      "pronunciation": "dyooh-plis-uh-tuhs",
      "definition": "adjective: deceitful",
      "example": "She may have got the results she was after but the way she did it was slightly  duplicitous."
    },
    {
      "word": "euphoric",
      "pronunciation": "yooh-fo-rik",
      "definition": "adjective: feeling",
      "example": "a sense of great wellbeing"
    },
    {
      "word": "facade",
      "pronunciation": "fuh-sahd",
      "definition": "noun: the",
      "example": "face or front of the main part of a building"
    },
    {
      "word": "hallucinate",
      "pronunciation": "huh-looh-suh-nayt",
      "definition": "verb: to",
      "example": "see and experience things that are not really there"
    },
    {
      "word": "irrespective",
      "pronunciation": "i-ruh-spek-tiv",
      "definition": "adjective: without",
      "example": "regard to or independent of"
    },
    {
      "word": "jewellery",
      "pronunciation": "jooh-uhl-ree",
      "definition": "noun: articles",
      "example": "you can wear, made of gold, silver and precious stones  Her hand was heavy from the many pieces of gold and silver jewellery she liked to"
    },
    {
      "word": "knowledgeable",
      "pronunciation": "nol-uh-juh-buhl",
      "definition": "adjective: possessing",
      "example": "knowledge or understanding"
    },
    {
      "word": "monotonous",
      "pronunciation": "muh-not-uh-nuhs",
      "definition": "adjective: tiresomely",
      "example": "lacking in variety"
    },
    {
      "word": "osteopath",
      "pronunciation": "oss-tee-uh-path",
      "definition": "noun: a",
      "example": "person who treats others by realigning bones in the body"
    },
    {
      "word": "pacifist",
      "pronunciation": "pas-uh-fuhst",
      "definition": "noun: someone",
      "example": "who opposes all war or violence"
    },
    {
      "word": "prophecy",
      "pronunciation": "prof-uh-see",
      "definition": "noun: a",
      "example": "statement telling what is going to happen in the future"
    },
    {
      "word": "prosciutto",
      "pronunciation": "pruh-shooh-toh",
      "definition": "noun: a",
      "example": "dry-cured, spiced ham, originally made in Italy and often sold very thinly  sliced"
    },
    {
      "word": "psychic",
      "pronunciation": "suy-kik",
      "definition": "adjective: seeming",
      "example": "to have supernatural mental powers, such as the ability to see the  future"
    },
    {
      "word": "pugilist",
      "pronunciation": "pyooh-juh-luhst",
      "definition": "noun: a",
      "example": "boxer, usually a professional"
    },
    {
      "word": "reiterate",
      "pronunciation": "ree-it-uh-rayt",
      "definition": "verb: to",
      "example": "say or do again"
    },
    {
      "word": "relegation",
      "pronunciation": "rel-uh-gay-shuhn",
      "definition": "noun: being",
      "example": "sent to some lower position, place, or condition"
    },
    {
      "word": "reminisce",
      "pronunciation": "rem-uh-niss",
      "definition": "verb: to",
      "example": "recollect and tell of past experiences or events"
    }
  ]
}

st.set_page_config(page_title="Spelling Bee Annotated Generator", layout="centered")
st.title("🐝 Annotated Spelling Bee Word Generator")
st.markdown("Pick a level to generate a random annotated word. Each includes pronunciation, definition, and sentence. Words won’t repeat until you reset.")

selected_level = st.selectbox("Choose a spelling level:", list(level_words.keys()))

# Set up session state for used words tracking
if "used_words" not in st.session_state:
    st.session_state.used_words = {}
if selected_level not in st.session_state.used_words:
    st.session_state.used_words[selected_level] = []

col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 Generate Word"):
        unused_words = [
            word for word in level_words[selected_level]
            if word["word"] not in [w["word"] for w in st.session_state.used_words[selected_level]]
        ]
        if unused_words:
            new_word = random.choice(unused_words)
            st.session_state.used_words[selected_level].append(new_word)
            st.markdown(f"### 📝 {new_word['word']}")
            st.markdown(f"**Pronunciation:** {new_word['pronunciation']}")
            st.markdown(f"**Definition:** {new_word['definition']}")
            st.markdown(f"**Example:** {new_word['example']}")
        else:
            st.warning("✅ All words shown for this level. Please reset to start again.")

with col2:
    if st.button("🔁 Reset Words"):
        st.session_state.used_words[selected_level] = []
        st.info(f"{selected_level} word list has been reset.")
