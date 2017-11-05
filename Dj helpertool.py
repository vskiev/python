# Create get_song() helper function that takes two parameters -
# dictionary with songs (see below) and integer argument which
# is a maximum length of a song in seconds.
#
# songs is an array of objects which are formatted as follows:
# {
#  'artist': 'Artist',
#  'title': 'Title String',
#  'playback': '04:30'
# }
# You can expect playback value to be formatted exactly like above.
#
# Result should be a title of the longest song from the database
# that matches the criteria of not being longer than specified time.
# If there's no songs matching criteria in the database, return False.

songs_db = [ {
 'artist': 'Led Zeppelin',
 'title': 'Stairways to heaven',
 'playback': '09:20'
}, {
 'artist': 'Metallica',
 'title': 'Master of puppets',
 'playback': '04:30'
}, {
 'artist': 'Nirvana',
 'title': 'The Man who sold the world',
 'playback': '03:10'
}, {
 'artist': 'Stepan Galyabarda',
 'title': 'Lyst do mamy',
 'playback': '02:20'
}]



def get_song(db, len_seconds):

    def min2sec(time_="0:0"):  # min:sec
        l = time_.split(":")
        seconds = int(l[1])
        return (int(l[0]) * 60 + seconds)

    val = list()
    for i in range(len(db)):
        ctrack = min2sec(db[i].get('playback'))

        val.append(ctrack)

    min1 = min(val)
    max1 = max(val)
    if len_seconds == min1:
        return "Best possible song: {}/{}".format(
                 db[min1]['artist'],
                 db[min1]['title'])
    elif len_seconds == max1:
        return "Best possible song: {}/{}".format(
                 db[max1]['artist'],
                 db[max1]['title'])
    elif len_seconds < min1:
        return False
    elif len_seconds > max1:
        return False
    elif len_seconds > min1 and len_seconds < max1:

         sorted(val)
         result = min1
         for i in range(len(val)):
             if len_seconds < val[i]:
                 continue
             elif len_seconds > val[i]:
                  result = val[i]
                  break

         for i in range(len(db)):
             ctrack = min2sec(db[i].get('playback'))
             if result == ctrack :
                 return "Best possible song: {}/{}".format(
                     db[i]['artist'],
                     db[i]['title'])


print(get_song(songs_db, 145))


