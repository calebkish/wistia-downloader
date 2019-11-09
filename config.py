# NOTICE: Chromedriver is requred for this to work.
# Download: https://chromedriver.chromium.org/
# Make sure to install the version that corresponds to your installed Chrome 
# browser version


# The 'link' can be found by right-clicking the Wistia embeded video player and 
# clicking "Copy link and thumbnail".
#
# The 'path' must have an ending "/" (indicates that it is a folder)
#
# The 'filename' will have ".mp4" appended onto it later
videos = [
    # {
    #     'link': '<p><a href="https://www.website.com?wvideo=kqzjaftn6u"><img src="https://embedwistia-a.akamaihd.net/deliveries/b1d23ad43833532b734f11b8c18f8f72.jpg?image_play_button_size=2x&amp;image_crop_resized=960x540&amp;image_play_button=1&amp;image_play_button_color=54bbffe0" style="width: 400px; height: 225px;" width="400" height="225"></a></p><p><a href="https://www.website.com?wvideo=kqzjaphn6u">Video title</a></p>',
    #     'path': 'path/to/file/',
    #     'filename': 'really-cool-file-name'
    # },
    # {
    #     'link': '<p><a href="https://www.website.com?wvideo=kqzjaftn6u"><img src="https://embedwistia-a.akamaihd.net/deliveries/b1d23ad43833532b734f11b8c18f8f72.jpg?image_play_button_size=2x&amp;image_crop_resized=960x540&amp;image_play_button=1&amp;image_play_button_color=54bbffe0" style="width: 400px; height: 225px;" width="400" height="225"></a></p><p><a href="https://www.website.com?wvideo=aduggher45">Video title</a></p>',
    #     'path': 'path/to/file/',
    #     'filename': 'really-cool-file-name-2'
    # }
]

# 720 is the desired quality, and if it doesn't exist then a subsequent quality 
# will be chosen. Rearrange as desired.
qualities = [
    '720',
    '540',
    '1080',
    '360',
    '224'
]