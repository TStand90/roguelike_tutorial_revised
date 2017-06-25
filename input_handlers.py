import libtcodpy as libtcod


def handle_keys(key):
    key_char = chr(key.c)

    # Movement keys
    if key.vk in (libtcod.KEY_UP, libtcod.KEY_KP8) or key_char == 'k':
        return {'move': (0, -1)}
    elif key.vk in (libtcod.KEY_DOWN, libtcod.KEY_KP2) or key_char == 'j':
        return {'move': (0, 1)}
    elif key.vk in (libtcod.KEY_LEFT, libtcod.KEY_KP4) or key_char == 'h':
        return {'move': (-1, 0)}
    elif key.vk in (libtcod.KEY_RIGHT, libtcod.KEY_KP6) or key_char == 'l':
        return {'move': (1, 0)}
    elif key.vk in (libtcod.KEY_KP7,) or key_char == 'y':
        return {'move': (-1, -1)}
    elif key.vk in (libtcod.KEY_KP9,) or key_char == 'u':
        return {'move': (1, -1)}
    elif key.vk in (libtcod.KEY_KP1,) or key_char == 'b':
        return {'move': (-1, 1)}
    elif key.vk in (libtcod.KEY_KP3,) or key_char == 'n':
        return {'move': (1, 1)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}