from enums.geometry import Edge

edges={
    [(6,12),(6,6)]:Edge.LEFT_FRONT,     #left(Corner.TOP_RIGHT):front(Corner.BOTTOM_LEFT)
    [(12,12),(12,6)]:Edge.FRONT_RIGHT,     #front(Corner.TOP_RIGHT):right(Corner.BOTTOM_LEFT)
    [(18,12),(18,6)]:Edge.RIGHT_BACK,     #right(Corner.TOP_RIGHT):back(Corner.BOTTOM_LEFT)
    [(12,12),(6,12)]:Edge.FRONT_TOP,    #front(Corner.TOP_RIGHT):top(Corner.BOTTOM_LEFT)
    [(12,6),(6,6)]:Edge.BOTTOM_FRONT,     #bottom(Corner.TOP_RIGHT):front(Corner.BOTTOM_LEFT)
    [(6,0),(18,6)]:Edge.BOTTOM_BACK,     #bottom(Corner.BOTTOM_LEFT):back(Corner.BOTTOM_LEFT)
    [(24,12),(12,18)]:Edge.BACK_TOP,    #back(Corner.TOP_RIGHT):top(Corner.TOP_RIGHT)
    [(0,6),(24,12)]:Edge.LEFT_BACK,     #left(Corner.BOTTOM_LEFT):back(Corner.TOP_RIGHT)
    [(18,12),(12,12)]:Edge.RIGHT_BACK,    #right(Corner.TOP_RIGHT):top(front.Corner.TOP_RIGHT)
    [(6,12),(24,12)]:Edge.LEFT_TOP,    #left(Corner.TOP_RIGHT):top(back.Coner.TOP_RIGHT)
    [(12,6),(18,6)]:Edge.RIGHT_BOTTOM,     #right(Corner.BOTTOM_LEFT):bottom(back.Corner.BOTTOM_LEFT)
    [(0,6),(6,6)]:Edge.LEFT_BOTTOM     #left(Corner.BOTTOM_LEFT):bottom(front.Corner.BOTTOM_LEFT)
}