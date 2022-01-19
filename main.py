from random import randint

def name_generator(N, syllables):
    names = []
    if N is None:
        N=10

    if syllables is None:
        syllables = 3
    prefix = ["de", "shaz", "ste", "zach", "za", "shiz", "rod", "cher", "char", "dar", "ever", "xan", "xe", "liz"]
    main = ["la", "bon", "dom", "bon", "sho", "ixi", "ca", "sam", "no", "na", "man", "liz"]
    suffix = ["ienne", "lea", "dea", "nea", "anne", "lee", "mae", "ine", "iana", "ela", "ena", "aela", "on", "lise", "liz"]

    def getrand(ls):
        return ls[randint(0, len(ls) - 1)]

    for i in range(int(N)):
        middle = "".join([getrand(main) for i in range(int(syllables) - 2)])
        name = name_mod = getrand(prefix) + middle + getrand(suffix)
        if "x" not in name:
            if randint(1, 3) == 3:
                name_mod = []
                for n in name:
                    name_mod.append(n)
                    if randint(1, 50) == 50:
                        name_mod.append("🍋")
        elif "z" not in name:
            if randint(1, 3) == 3:
                name_mod = []
                for n in name:
                    name_mod.append(n)
                    if randint(1, 100) == 100:
                        name_mod.append("zaela")
        name = "".join(name_mod)
        names.append(name)
    return names
