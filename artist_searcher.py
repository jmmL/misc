def main():
    """ An attempt at using APIs """
    import spotify
    import threading
    #import logging
    #logging.basicConfig(level=logging.DEBUG)
    logged_in_event = threading.Event()
    def connection_state_listener(session):
        if session.connection.state is spotify.ConnectionState.LOGGED_IN:
            logged_in_event.set()
            
    session = spotify.Session()
    loop = spotify.EventLoop(session)
    loop.start()
    session.on(
        spotify.SessionEvent.CONNECTION_STATE_UPDATED,
        connection_state_listener)
        
    session.connection.state
    ###############
    user_login = input("Please input your username")
    user_password = input("Please input your password")
    session.login(user_login,user_password)
    ###############
    session.connection.state
    logged_in_event.wait()
    session.connection.state
    ##################################
    
    print(str(session.user))
    search_active = True
    while search_active:
        user_search = input("Please enter a band name (type\"!quit\" to exit):\n")
        if "!quit" in user_search:
            search_active = False
            break
        search = session.search(user_search) #do the search
        search.load() # load the search results
        album = session.get_album(str(search.albums[0].link)) # store the first album of the search in the album variable
        ## user browser.load() as a workaround: album.load() seems to be broken 2014-09-30
        browser = album.browse()
        browser.load()
        
        print("Their most popular album is " + str(album.name))
        cover = album.cover(spotify.ImageSize.LARGE)
        cover.load()
        open('/tmp/cover.html', 'w+').write('<img src="%s"> <h1>%s - %s</h1>' % (cover.data_uri, album.artist.name, album.name))
main()
