# user stories
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

# Class template


class MusicList():
    # User-facing properties:
    #   

    def __init__(self):
        # Parameters:
        #   
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet
        #track list will  be empty list

    def add_track(self, task):
        # Parameters:
        #   task: string representing a single track
        # Returns:
        #   list with added tracks if track is string
        # Side-effects
        #   if task is not string, raise exception

    '''def task_marker(self, completed_task):
        # Returns:
        #   removes completed tasks
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet'''

# test template

"""
Given a string track
#
"""
music_list = MusicList()
def test_add_given_tracks_to_list_and_return_list():
music_list.add_track(track1)
music_list.add_track(track2)
actual = music_list.add_track(track3)
expected = ['track1', 'track2', 'track3]


"""
Given non string type list
'''
music_list = MusicList()
task_tracker.add(123) => 'track must be a string'


"""
Given completed task
remove task from list and return updated list
'''
task_tracker = TaskTracker()
task_tracker.add_task('#TODO fix the washing machine)
task_tracker.add_task('#TODO do the washing up')
task_tracker.task_marker('do the washing up') => ['fix the washing machine']