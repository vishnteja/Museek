""" args is a 1d List """
def writeExceptions(e, args):
    try:
        with open("../../log.txt", "a+") as f:
            for element in args:
                f.write("%s\t%s\t%s"%(__name__, str(e), element))
            
        f.close()
    except Exception as e:
        print("Failed to write Log")