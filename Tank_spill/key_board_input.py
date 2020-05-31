#Martin Økter
import pygame

pygame.init()

print_key = [True]

def key_board():
    for event in pygame.event.get():
        mods = pygame.key.get_mods()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            if mods == pygame.KMOD_LSHIFT:
                return 'A'
            else:
                return 'a'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            if mods == pygame.KMOD_LSHIFT:
                return 'B'
            else:
                return 'b'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            if mods == pygame.KMOD_LSHIFT:
                return 'C'
            else:
                return 'c'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            if mods == pygame.KMOD_LSHIFT:
                return 'D'
            else:
                return 'd'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            if mods == pygame.KMOD_LSHIFT:
                return 'E'
            else:
                return 'e'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            if mods == pygame.KMOD_LSHIFT:
                return 'F'
            else:
                return 'f'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            if mods == pygame.KMOD_LSHIFT:
                return 'G'
            else:
                return 'g'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            if mods == pygame.KMOD_LSHIFT:
                return 'H'
            else:
                return 'h'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            if mods == pygame.KMOD_LSHIFT:
                return 'I'
            else:
                return 'i'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            if mods == pygame.KMOD_LSHIFT:
                return 'J'
            else:
                return 'j'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            if mods == pygame.KMOD_LSHIFT:
                return 'K'
            else:
                return 'k'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            if mods == pygame.KMOD_LSHIFT:
                return 'L'
            else:
                return 'l'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            if mods == pygame.KMOD_LSHIFT:
                return 'M'
            else:
                return 'm'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            if mods == pygame.KMOD_LSHIFT:
                return 'N'
            else:
                return 'n'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
            if mods == pygame.KMOD_LSHIFT:
                return 'O'
            else:
                return 'o'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if mods == pygame.KMOD_LSHIFT:
                return 'P'
            else:
                return 'p'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            if mods == pygame.KMOD_LSHIFT:
                return 'Q'
            else:
                return 'q'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if mods == pygame.KMOD_LSHIFT:
                return 'R'
            else:
                return 'r'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            if mods == pygame.KMOD_LSHIFT:
                return 'S'
            else:
                return 's'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            if mods == pygame.KMOD_LSHIFT:
                return 'T'
            else:
                return 't'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
            if mods == pygame.KMOD_LSHIFT:
                return 'U'
            else:
                return 'u'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            if mods == pygame.KMOD_LSHIFT:
                return 'V'
            else:
                return 'v'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if mods == pygame.KMOD_LSHIFT:
                return 'W'
            else:
                return 'w'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            if mods == pygame.KMOD_LSHIFT:
                return 'X'
            else:
                return 'x'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            if mods == pygame.KMOD_LSHIFT:
                return 'Y'
            else:
                return 'y'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            if mods == pygame.KMOD_LSHIFT:
                return 'Z'
            else:
                return 'z'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            if mods == pygame.KMOD_LSHIFT:
                return '='
            else:
                return '0'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            if mods == pygame.KMOD_LSHIFT:
                return '!'
            else:
                return '1'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            if mods == pygame.KMOD_LSHIFT:
                return '"'
            else:
                return '2'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            if mods == pygame.KMOD_LSHIFT:
                return '#'
            else:
                return '3'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            if mods == pygame.KMOD_LSHIFT:
                return '¤'
            else:
                return '4'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            if mods == pygame.KMOD_LSHIFT:
                return '%'
            else:
                return '5'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            if mods == pygame.KMOD_LSHIFT:
                return '&'
            else:
                return '6'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
            if mods == pygame.KMOD_LSHIFT:
                return '/'
            else:
                return '7'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
            if mods == pygame.KMOD_LSHIFT:
                return '('
            else:
                return '8'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
            if mods == pygame.KMOD_LSHIFT:
                return ')'
            else:
                return '9'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return ' '
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            return '-1'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LESS:
            if mods == pygame.KMOD_LSHIFT:
                return '>'
            else:
                return '<'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            print_key[0] = False
            return ''

def key_key(action=None):
    if action != None:
        print_key[0] = action
    return print_key[0]
