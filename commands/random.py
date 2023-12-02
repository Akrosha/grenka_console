from functions.randoms import Randoms
def random(self, args = []):
    print(self.randoms.getSeed())
    if len(args) == 0:
        return self.randoms.getRandom()
    if (len(args) == 1) and (args[0].isdigit()):
        return self.randoms.getRandom(max = int(args[0]))
    if (len(args) > 1) and (args[0].isdigit()) and (args[1].isdigit()):
        return self.randoms.getRandom(min = int(args[0]), max = int(args[1]))
    else:
        return "syntax error: random <int:min> <int:max>"