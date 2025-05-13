import random
import glob
import os
import moviepy
from PIL import Image

# main function 
# 1. calls a function that gives 5 random categories no dupes
# 2. calls each categories function creating it's 10 question moviepy clip
# including any visual edits
# 3. Use the Concatenate_videoclips function to combine the recieved clips
# and the intro and outro clip

# function that picks a random category 

# character category function 
# 1. pick 10 random character images no dupes
# 2. take each character image selected 1 at a time and make temporary 
# blurred versions (seperate function?)
# 3. the goal is to slowly unblur over 10 secs, 30 fps
# 4. Use moviepy to put the edited images together by Concatenating the char_mv_clips together and return that as a video clip

# Character blur function
# take the given character and make the temporary blur'd versions 
# send back to the character category function a movieclip titled something like char_mv_clip_1-10

# Maps category function
# 1. Simple category just need to add 30fps 10 sec timer to the 10 randomly selected images and make it into a video clip together

# Title screen category function
# 1. Simple category just need to add 30fps 10 sec timer to the 10 randomly selected images and make it into a video clip together

# Items category function
# 1. Simple category just need to add 30fps 10 sec timer to the 10 randomly selected images and make it into a video clip together

# Skill_Tree function
# 1. Simple category just need to add 30fps 10 sec timer to the 10 randomly selected images and make it into a video clip together