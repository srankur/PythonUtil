import Logger.ModuleLogger.ModuleLevelLogger as ml


logg = ml.init_log("Square")


def calc_square(num):
    print("Calculating squares")
    for n in num:
        #print("Square", n*n)
        logg.info( n*n)


if __name__ == "__main__":
    calc_square(range(10))