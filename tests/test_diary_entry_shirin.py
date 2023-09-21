from lib.diary_entry_shirin import DiaryEntry
import pytest
def test_if_diary_empty_return_error_message():
    diary_entry = DiaryEntry('new entry', '')
    with pytest.raises(Exception) as e:
        diary_entry.format()
    error_message = str(e.value)
    assert error_message == 'Contents string is empty!'

def test_if_format_formats_correctly(): 
    diary_entry = DiaryEntry('New entry', 'This is a test')
    actual = diary_entry.format()
    assert actual == 'New entry: This is a test'
    
        
