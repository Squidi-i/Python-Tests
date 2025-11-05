liked_songs = {
  'Love You Too': 'Vansire',
  'That I Miss You': 'Vansire',
  'Can You Hear The Music': 'Ludwig Göransson'
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        lines = []
        for song, artist in liked_songs.items():
             lines.append(f"{song} - {artist}\n")
        file.writelines(lines)
        
write_liked_songs_to_file(liked_songs, 'playlist.txt')



    

