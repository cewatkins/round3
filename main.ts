controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    
    projectile = sprites.createProjectileFromSide(assets.image`
        arrows
    `, 50, 50)
    music.play(music.stringPlayable("B A G A G F A C5 ", 666), music.PlaybackMode.UntilDone)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    player69.setVelocity(0, -133)
    music.play(music.stringPlayable("E D G F B A C5 B ", 457), music.PlaybackMode.UntilDone)
})
let projectile : Sprite = null
let player69 : Sprite = null
tiles.setCurrentTilemap(tilemap`
    level1
`)
scene.setBackgroundColor(15)
player69 = sprites.create(assets.image`
    player69
`, SpriteKind.Player)
tiles.placeOnTile(player69, tiles.getTileLocation(2, 1))
player69.ay = 69
scene.cameraFollowSprite(player69)
music.play(music.stringPlayable("C5 A B G A F G E ", 120), music.PlaybackMode.UntilDone)
controller.moveSprite(player69, 100, 0)
