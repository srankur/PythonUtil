import Logger.ModuleLogger.ModuleLevelLogger as ml

logger = ml.init_log("Cube")


def calc_cube(num):
    print("Calculating Cubes")
    for n in num:
        logger.debug(n*n*n)


if __name__ == "__main__":
    calc_cube(range(10))
