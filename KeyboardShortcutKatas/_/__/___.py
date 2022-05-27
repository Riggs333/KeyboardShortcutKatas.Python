import hashlib

yesterday = "You're done! - Great job!"

"""
Hopefully, you recognized the lyrics of a song. 
Type in the name of the band and run the test below to check.
"""
band_name = ""


def test_band_name():
    assert (hashlib.md5(band_name.lower().encode()).hexdigest()) in [
        'ff9f90893603fffc16cffa8d11c8292c',
        '2a9ea35253dbec60e76166ec8420fbda'
    ]
