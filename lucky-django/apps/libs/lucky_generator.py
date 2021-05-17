import random


# import time


def create_lucky(seed):
    LUCKY_SEED = int(seed)
    redball = list(range(1, 36))
    blueball = list(range(1, 13))
    redball_left = 35
    blueball_left = 12

    redball_pool = []
    blueball_pool = []
    random.shuffle(redball)
    random.shuffle(blueball)
    for i in range(5):
        # time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % redball_left):
            random.shuffle(redball)
        lucky_ball = redball.pop()
        redball_pool.append(lucky_ball)
        redball_left = redball_left - 1

    for i in range(2):
        # time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % blueball_left):
            random.shuffle(blueball)
        lucky_ball = blueball.pop()
        blueball_pool.append(lucky_ball)
        blueball_left = blueball_left - 1

    redball_pool.sort()
    blueball_pool.sort()

    lottery = "{red_ball_pool} + {blue_ball_pool}".format(
        red_ball_pool=str(redball_pool),
        blue_ball_pool=str(blueball_pool)
    )

    return lottery


def create_dantuo(seed):
    LUCKY_SEED = int(seed)
    redball = list(range(1, 36))
    blueball = list(range(1, 13))
    redball_left = 35
    blueball_left = 12
    redballdan_pool = []
    redballtuo_pool = []
    blueballdan_pool = []
    blueballtuo_pool = []
    random.shuffle(redball)
    random.shuffle(blueball)
    for i in range(4):
        # time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % redball_left):
            random.shuffle(redball)
        lucky_ball = redball.pop()
        redballdan_pool.append(lucky_ball)
        redball_left = redball_left - 1

    for i in range(7):
        # time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % redball_left):
            random.shuffle(redball)
        lucky_ball = redball.pop()
        redballtuo_pool.append(lucky_ball)
        redball_left = redball_left - 1

    for i in range(1):
        # time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % blueball_left):
            random.shuffle(blueball)
        lucky_ball = blueball.pop()
        blueballdan_pool.append(lucky_ball)
        blueball_left = blueball_left - 1

    for i in range(2):
        # time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % blueball_left):
            random.shuffle(blueball)
        lucky_ball = blueball.pop()
        blueballtuo_pool.append(lucky_ball)
        blueball_left = blueball_left - 1

    redballdan_pool.sort()
    redballtuo_pool.sort()
    blueballdan_pool.sort()
    blueballtuo_pool.sort()

    lottery = "{red_ball_dan}+{red_ball_tuo}  {blue_ball_dan}+{blue_ball_tuo}".format(
        red_ball_dan=str(redballdan_pool),
        red_ball_tuo=str(redballtuo_pool),
        blue_ball_dan=str(blueballdan_pool),
        blue_ball_tuo=str(blueballtuo_pool)
    )

    return lottery
