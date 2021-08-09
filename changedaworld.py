from moviepy.editor import *
import argparse

parser = argparse.ArgumentParser(description="Creates \"Change da world\" video, composing image1 and then image2 after *goodbye*")

defaultFileNames = ["original", "image1", "image2", "final_video"]
defaultFilePaths = ["original.mp4", "image1.jpg", "image2.jpg", "final_video.mp4"]
defaultAbbreviations = ["r", "i1", "i2", "o"]

for a, fn, fp in zip(defaultAbbreviations, defaultFileNames, defaultFilePaths):
    parser.add_argument("-" + a, "--" + fn, help=fn + " clip file path (default: %(default)s)", default=fp)

args = parser.parse_args()

[original_file, image1_file, image2_file, final_video_file] = [vars(args)[fn] for fn in defaultFileNames]

fadingT = 8.3
ratHeight = 352

original_clip = VideoFileClip(original_file)
(videoWidth, videoHeight) = original_clip.size
totalDuration = original_clip.duration
fadingDuration = totalDuration - fadingT - 1

image1_clip = ImageClip(image1_file).resize(width=videoWidth).crop(0,0,videoWidth,ratHeight).set_position(("center", "top")).set_duration(totalDuration)
image2_clip = ImageClip(image2_file).resize(width=videoWidth).crop(0,0,videoWidth,ratHeight).set_position(("center", "top")).set_duration(totalDuration - fadingT)

CompositeVideoClip([original_clip, image1_clip, image2_clip.set_start(fadingT).crossfadein(fadingDuration)], size=(videoWidth, videoHeight)).write_videofile(final_video_file)
