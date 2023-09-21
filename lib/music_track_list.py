class MusicList():
    def __init__(self) :
        self.track_list = []

    def add_track(self, track):
        if isinstance(track, str):
            self.track_list.append(track)
            return self.track_list
        else:
            raise Exception('Input must be a string')