
from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video1.avi")
clip1 = clip1.resize(width = 200, height=200)
clip2 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video2.avi")
clip2 = clip2.resize(width = 200, height=200)
clip3 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video3.avi")
clip3 = clip3.resize(width = 200, height=200)
clip4 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video4.avi")
clip4 = clip4.resize(width = 200, height=200)
clip5 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video5.avi")
clip5 = clip5.resize(width = 200, height=200)
clip6 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video6.avi")
clip6 = clip6.resize(width = 200, height=200)
clip7 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video7.avi")
clip7 = clip7.resize(width = 200, height=200)
clip8 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video8.avi")
clip8 = clip8.resize(width = 200, height=200)
clip9 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video9.avi")
clip9 = clip9.resize(width = 200, height=200)
clip10 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video10.avi")
clip10 = clip10.resize(width = 200, height=200)
clip11 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video11.avi")
clip11 = clip11.resize(width = 200, height=200)
clip12 = VideoFileClip("/home/roman/projects/predicting-the-car-on-video/video12.avi")
clip12 = clip12.resize(width = 200, height=200)

final_clip = clips_array([[clip1, clip2, clip3, clip4],
						  [clip5, clip6, clip7, clip8],
                          [clip9, clip10, clip11, clip12]])


final_clip.write_videofile("my_stack.mp4")