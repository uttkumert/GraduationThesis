import moviepy.editor as mpe

def combine_audio(vidname, audname, outname, fps=60): 
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

combine_audio("./mp4s/test.mp4", "RAI.mp3", "test_over.mp4") # i create a new file
#combine_audio("test.mp4", "test.mp3", "test.mp4") # i rewrite on the same file```