# aliengame
this code is content of book named <python Crash Course : A Hands-On,Project-Based Introduction to Programming>.
This is the first time I touch with game, it easy to make a game with python library pygame.
Beafore the practice, you should kown some knowlede about computer, computer is orgnized by display and keyboard, game control by keyboard and mouse, game is displayed by display.

so the main code is :
    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, sb, stats)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, sb, stats, play_button)
	
    you response to the keyboard, and change the postion of ship bullet and alien, if bullet and alien meet, the alien is kill and dismiss, if ship and alien meet, the ship is crash and begin a new game.
    this project is simple but worth to remeber.




