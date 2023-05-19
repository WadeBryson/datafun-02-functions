from player_points_class import player_points

from util_datafun_logger import setup_logger

if __name__ == "__main__":

    logger, logname = setup_logger(__file__)

    name1 = "LeBron James"
    points1 = "points"
    data1 = [24, 28, 42, 24, 33]
    object1 = player_points(name1, points1, data1)

  
    name2 = "Kyrie Irving"
    points2 = "points"
    data2 = [14, 28, 17, 21, 35]
    object2 = player_points(name2, points2, data2)

    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")

    object_list = [object1, object2]

    for object in object_list:
      logger.info(object)
      logger.info(f"Count: {object.count()}")
      logger.info(f"Total Points Scored: {object.sum()}")
      logger.info(f"Average Points Per Game: {object.average()}")
      logger.info(f"Median: {object.median()}")
      logger.info("------------------")

      with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())