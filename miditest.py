import pygame
import time
import pygame.midi

pygame.midi.init()

# print pygame.midi.get_default_input_id()
# print pygame.midi.get_default_output_id()
# print pygame.midi.get_device_info(1)
# print pygame.midi.get_count()

player = pygame.midi.Output(1, 0)
player.set_instrument(0,1)
pygame.midi.MidiException(1)
list=[[1, 96], [0, 0], [1, 95], [1, 34], [1, 92], [0, 0], [1, 29], [0, 0], [1, 94], [0, 0], [0, 0], [1, 117], [0, 0], [0, 0], [1, 53], [0, 0]]
# player.note_on(60, 100)
# time.sleep(1)
# player.note_off(60, 100)

for x in range(0, 2) :
    for x in range(0, len(list)) :
        player.note_on(list[x][0], list[x][1])
        time.sleep(0.1)
        player.note_off(list[x][0], list[x][1])
        time.sleep(0.1)

# import pygame.midi
#
# pygame.midi.init()
#
# port = pygame.midi.get_default_output_id()
# print ("Using Output ID :%s:" % port)
