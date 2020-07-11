#!/usr/bin/python3
import random

red_ball = []
while True:
    # 生成一位随机数
    a = random.randint(1, 33)

    # 避免重复
    if a not in red_ball:
        # 把不重复的数字，添加到列表
        red_ball.append(a)

        # 返回6个不重复的红球
        if len(red_ball) == 6:
            print("红球:", sorted(red_ball))
            break

# 生成蓝球
blue_ball = random.randint(1, 16)
print("蓝球:", blue_ball)
