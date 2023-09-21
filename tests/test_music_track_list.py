from lib.music_track_list import *
import pytest

def test_add_given_tracks_to_list_and_return_list():
    music_list = MusicList()
    music_list.add_track('Black sabbath, War Pigs')
    music_list.add_track('John fahey, sligo river blues')
    actual = music_list.add_track('Tony TS McPhee, The hunt')
    expected = ['Black sabbath, War Pigs', 'John fahey, sligo river blues', 'Tony TS McPhee, The hunt']
    assert actual == expected

def test_error_message_when_give_track_is_not_string():
    music_list = MusicList()
    music_list.add_track('Black sabbath, War Pigs')
    music_list.add_track('John fahey, sligo river blues')
    with pytest.raises(Exception) as e:
        music_list.add_track(1234)
    actual = str(e.value)
    expected = ['Black sabbath, War Pigs', 'John fahey, sligo river blues']