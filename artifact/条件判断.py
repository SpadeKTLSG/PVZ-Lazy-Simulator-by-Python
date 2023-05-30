# -*- coding: utf-8 -*-
def 可否在此种植(x, y, 当前单元格状态):
    sitX = int(x // 80)
    sitY = int((y - 100) // 100)

    if sitX > 8 or sitX < 0 or sitY > 4 or sitY < 0:
        return False, sitX, sitY

    if 当前单元格状态[sitY][sitX] == 1:
        return False, sitX, sitY

    else:
        return True, sitX, sitY


def Change_to_sit(x, y):
    sitX = x // 80
    sitY = (y - 100) // 100
    X = sitX * 80 + 40
    Y = sitY * 100 + 150
    return X, Y
