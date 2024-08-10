# if len(args) == 0
#   random(0, 1)
# if len(args) == 1
#   random(0, args)
# if len(args) > 1
#   random(args, args)

def random(self, args = []):
    """get a random number\n\trandom\n\trandom <int:max>\n\trandom <int:min> $ <int:max>"""
    if len(args) == 0:
        return self.randoms.getRandom()
    if (len(args) == 1) and (args[0].isdigit()):
        return self.randoms.getRandom(max = int(args[0]))
    if (len(args) > 1) and (args[0].isdigit()) and (args[1].isdigit()):
        return self.randoms.getRandom(min = int(args[0]), max = int(args[1]))
    else:
        return "syntax error: random <int:min> $ <int:max>"
