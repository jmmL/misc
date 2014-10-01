def main():
    """ An attempt at using APIs """
    import spotify
    import threading
    import getpass
    #import logging
    #logging.basicConfig(level=logging.DEBUG)
    """ The check-if-logged-in code is mostly based on the pyspotify reference code """
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
        
    user_login = input("Please input your Spotify username: ")
    user_password = getpass.getpass()
    session.login(user_login,user_password)
    logged_in_event.wait()
    ##############################
    
    print(str(session.user))
    search_active = True
    while search_active:
        user_search = input("Please enter a query (or type\"!quit\" to exit):\n")
        if "!quit" in user_search:
            search_active = False
            break
        
        search = session.search(user_search) #do the search
        search.load() # load the search results
        album = session.get_album(str(search.albums[0].link)) # store the first album of the search in the album variable
        ## user browser.load() as a workaround: album.load() seems to be broken 2014-09-30
        browser = album.browse()
        browser.load()
        
        print("The most popular album for your search is " + str(album.name))
        cover = album.cover(spotify.ImageSize.LARGE)
        cover.load()
        open('/tmp/cover.html', 'w+').write('<img src="%s"> <h1>%s - %s</h1>' % (cover.data_uri, album.artist.name, album.name))

if __name__ == "__main__":
    main()
