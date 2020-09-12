# join() joins the iterable with the str separator provided
emails = ['jack@gmail.com', 'rose@gmail.com', 'james@gmail.com', 'titanic@gmail.com']
to_email = ', '.join(emails)
print(to_email)


# split() splits the string and gives an iterable with the separator provided
songs = 'Rasputin-Daddy Cool-Rivers of Babylon-Ma Baker'
song_list = songs.split('-')
print(song_list)
