
def solution(genres: list, plays: list):
    result = []
    playlist = []
    
    dict = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in dict:
            dict[genre][0] += play
            dict[genre][1].append((play, i))
        else:
            dict[genre] = [play, [(play, i)]]
            
    for value in dict.values():
        value[1] = sorted(value[1], key=lambda x: (-x[0], x[1]))
        playlist.append(value)
    playlist.sort(reverse = True)
    
    for _, list in playlist:
        for i in range(min(len(list), 2)):
            result.append(list[i][1])
        
    
    return result