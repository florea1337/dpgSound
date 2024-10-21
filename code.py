import dearpygui.dearpygui as dpg
import pygame
import threading

sound_file = "inlovewav.wav"

pygame.mixer.init()
pygame.mixer.music.load(sound_file)

def play_sound():
    pygame.mixer.music.play(-1)

def stop_sound():
    pygame.mixer.music.stop()

def set_volume(sender, app_data):
    volume = app_data / 100.0
    pygame.mixer.music.set_volume(volume)

def start_playing():
    threading.Thread(target=play_sound).start()

dpg.create_context()

with dpg.window(label="Sound Player"):
    dpg.add_button(label="Stop Sound", callback=stop_sound)
    dpg.add_slider_int(label="Volume", default_value=50, min_value=0, max_value=100, callback=set_volume)

start_playing()

dpg.create_viewport(title='Sound Player', width=400, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
