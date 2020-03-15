# Date" 2020/3/14

import pygame

# the setting of window
SIZE = WIDTH, HEIGHT = 600, 400  # The width and height of our screen
BACKGROUND_COLOR = pygame.Color('white')  # The background color of our window
FPS = 10  # Frames per second


# Creating our Sprite
class MySprite(pygame.sprite.Sprite):
    def __init__(self):  # need to study more
        super(MySprite, self).__init__()

        self.images = []  # adding all the images to sprite array

        # add images to images array
        self.images.append(pygame.image.load('images/walk1.png'))
        self.images.append(pygame.image.load('images/walk2.png'))
        self.images.append(pygame.image.load('images/walk3.png'))
        self.images.append(pygame.image.load('images/walk4.png'))
        self.images.append(pygame.image.load('images/walk5.png'))
        self.images.append(pygame.image.load('images/walk6.png'))
        self.images.append(pygame.image.load('images/walk7.png'))
        self.images.append(pygame.image.load('images/walk8.png'))
        self.images.append(pygame.image.load('images/walk9.png'))
        self.images.append(pygame.image.load('images/walk10.png'))

        # index values to get the image from image array
        # initially it is 0
        self.index = 0

        # now the image that we will display will be the window
        self.image = self.images[self.index]

        # creating a rect at position x, y (5,5) of size (150,198)
        # which is the size of sprite

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1  # when the update method is called, we will increment the index

        if self.index >= len(self.images):  # we will make the index to 0 again
            self.index = 0

        self.image = self.images[self.index]  # finally we will update the images that will be displayed

def main():  # initiallizing pygame
    pygame.init()

    # gettind the screen of the specified size
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('MySprite ver 1,0')

    # creating our sprite object
    my_sprite = MySprite()

    # creating a group with our sprite
    my_group = pygame.sprite.Group(my_sprite)

    # getting the pygame clock for handling fps
    clock = pygame.time.Clock()

    while True:
        # getting the events
        for event in pygame.event.get():

            # if the event is quit means we clicked on the close window button
            if event.type == pygame.QUIT:
                # quit the game
                pygame.quit()
                quit()

        # updating the sprite
        my_group.update()

        # filling the screen with background color
        screen.fill(BACKGROUND_COLOR)

        # drawing the sprite
        my_group.draw(screen)

        # updating the display
        pygame.display.update()

        # finally delaying the loop to with clock tick for 10fps
        clock.tick(10)

if __name__ == '__main__':
    main()
