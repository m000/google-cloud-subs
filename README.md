# Google Cloud Subtitles

This is a wrapper that transcribes audio from a video file to srt
subtitles using the Google Cloud Speech-to-Text API.
It is heavily based on this [Medium article][orig] and it's
[source][orig-git].
However the functionality has been rewrapped in a more command-line
friendly way.
Also, substantial improvements have been made in the generation of
the subtitles, so that the output is closer to what a professional
subtitler would create.

## Frequently asked questions

### Why?
Even if your English are good enough to understand every word in a
movie, you may find yourself watching in sub-optimal conditions.
E.g. there are other people speaking nearby. Or you're watching on
a low volume to let your spouse or roommate sleep comfortably.
Or you're simply scrolling your social media feed while watching.
Using subtitles makes for a more comfortable viewing experience in
these cases.

### Is transcription perfect?
No. If you want to have the best results, expect an editorial pass
afterwards. You can use free tools like [Aegisub][aegisub] or
[Jubler][jubler] to make any required fixes.

### Is this project affiliated with Google?
Obviously not, but let's make a statement anyway:
This project is not affiliated with Google LLC in any way.

[orig]: https://medium.com/searce/generate-srt-file-subtitles-using-google-clouds-speech-to-text-api-402b2f1da3bd
[orig-git]: https://github.com/darshan-majithiya/Generate-SRT-File-using-Google-Cloud-s-Speech-to-Text-API
[aegisub]: http://www.aegisub.org/
[jubler]: https://jubler.org/
