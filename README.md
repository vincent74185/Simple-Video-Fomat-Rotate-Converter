# Simple-Video-Fomat-Rotate-Converter
This is a python program that can convert your video file format and rotate the video. For example, mp4 to mkv, rotate your video 90, 180, and 270 degree clockwise. 

Features:
1. Convert file type and/or rotate multiple video just few simple click. Instead of convert it one by one. 
2. The current version only support video to video. Other conversion is not tested. 
3. The conversion preserve the original quality. (Well, if you want to convert to something else... Wrong place)

How it work:
1. Select "Use Folder" to convert every file within the folder or "Use Files" for specific files
2. Click either "Select Folder" or "Select Files" base on previous choice. Browse and open the desire folder or files. 
3. Select Rotate Clockwise to rotate the video with certain degree. 
4. Select Hard Encdoe Enable. 
    On: Re-Encode the entire video (Slow, but supported by all media player)
    Off: Only change the metadata flag (Quick, but not all media player supports it)
5. If Hard Encode Enable is "on", you can choose to use the same file format as input, or type your own desire file extension. 
6. Select Ouput, Click on "Select Folder" to browse desire destination.
7. Finally, Click "Start Converting" button to start.

Caution:
1. IMPORTANT: YOU CAN NOT SET YOUR OUTPUT FOLDER AS SAME YOUR INPUT DIRECTORY!! Reason is because I do not change the name of converted file from input file. 
2. These is no progress bar, so you have to be patient.
3. Hard Encode your video = nearly 100% CPU usage, so I suggest run it when your not doing important task.
4. I'm am still imporving on it... So there might be some bugs that I haven't figure out yet.

Desclaimer:
This program is made for educational purpose.
