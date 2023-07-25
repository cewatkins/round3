def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_side(assets.image("""
        arrows
    """), 50, 50)
    music.play(music.string_playable("B A G A G F A C5 ", 666),
        music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    player69.set_velocity(0, -133)
    music.play(music.string_playable("E D G F B A C5 B ", 457),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

projectile: Sprite = None
player69: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.set_background_color(15)
player69 = sprites.create(assets.image("""
    player69
"""), SpriteKind.player)
tiles.place_on_tile(player69, tiles.get_tile_location(2, 1))
player69.ay = 69
scene.camera_follow_sprite(player69)
music.play(music.string_playable("C5 A B G A F G E ", 120),
    music.PlaybackMode.UNTIL_DONE)
controller.move_sprite(player69, 100, 0)