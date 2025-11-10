from enums.geometry import Corner

corner_translate = {
    (0, 1):  (Corner.TOP_RIGHT,  lambda p: p.y),
    (1, 0):  (Corner.TOP_RIGHT,  lambda p: p.x),
    (0, -1): (Corner.BOTTOM_LEFT, lambda p: p.y),
    (-1, 0): (Corner.BOTTOM_LEFT, lambda p: p.x)
}
