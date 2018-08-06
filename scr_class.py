import pygame
import restore_hand


class Screen(object):
    def __init__(self):
        self._wide = 1302
        self._high = 500

        self.screen = None

    def create_screen(self):
        self.screen = pygame.display.set_mode([self._wide, self._high])

        self.screen.fill((255, 255, 255))

    def load_bar(self):
        restore_hand.choice_Rect = pygame.Rect(int(abs(restore_hand.rel[0]) * restore_hand.scale)
                                               + restore_hand.guide_rect.x,
                                               int(abs(restore_hand.rel[1]) * restore_hand.scale)
                                               + restore_hand.guide_rect.y,
                                               500 * restore_hand.scale,
                                               500 * restore_hand.scale)
        self.screen.fill((0, 0, 0), restore_hand.show)
        pygame.draw.line(self.screen, (0, 0, 0), (501, 0), (501, 500), 1)
        pygame.draw.line(self.screen, (0, 0, 0), (701, 0), (701, 500), 1)
        pygame.draw.rect(self.screen, (100, 100, 100), restore_hand.bar, 0)
        pygame.draw.rect(self.screen, (255, 255, 255), restore_hand.show, 0)
        pygame.draw.rect(self.screen, (50, 255, 0), restore_hand.guide, 0)
        pygame.draw.rect(self.screen, (50, 50, 50), restore_hand.guide_rect, 0)
        pygame.draw.rect(self.screen,(255,255,255),restore_hand.choice_Rect,1)

    def load_scr_bg(self):
        self.screen.fill((255, 255, 255))

    def update_scr(self):
        pygame.display.update()
