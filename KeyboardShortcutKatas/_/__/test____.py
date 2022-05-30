import hashlib

yesterday = "You're done! - Great job!"

"""
Hopefully, you recognized the lyrics of the song. ;-) 
Guess the name of the band, assign it to the variable below and run the test below to check.
"""
band_name = ""


def test_band_name():
    assert band_name, "You have to fill in the band name in the variable 'band_name' in line 9."
    assert is_band_name_correct(), f"Your guess '{band_name}' is the wrong name of the band"


def is_band_name_correct():
    return (hashlib.md5(band_name.lower().encode()).hexdigest()) in [
        'ff9f90893603fffc16cffa8d11c8292c',
        '2a9ea35253dbec60e76166ec8420fbda'
    ]
