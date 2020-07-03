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

### Is transcription free?
No, but it's cheap. First, Google gives you €268 worth of credit to
get started. You should be able to go a long way with that credit.
E.g. transcription of a 78' film sets you back for around €1.
Do the math.

### What about other transcription backends?
What about them? I wouldn't mind adding other options, but someone has
to do the dirty work of providing a proof-of-concept implementation.
I'm not sure if there's anything out there for free, or as cheap as
Google. Amazon maybe?

### Is this project affiliated with Google?
Obviously not, but let's make a statement anyway:
This project is not affiliated with Google LLC in any way.

### This looks too complicated.
Well, there are services like [HappyScribe][happyscribe] that integrate
transcription,srt creation and srt editing, all in a user-friendly
web interface. Convenience doesn't come for free though.

[orig]: https://medium.com/searce/generate-srt-file-subtitles-using-google-clouds-speech-to-text-api-402b2f1da3bd
[orig-git]: https://github.com/darshan-majithiya/Generate-SRT-File-using-Google-Cloud-s-Speech-to-Text-API
[aegisub]: http://www.aegisub.org/
[jubler]: https://jubler.org/
[happyscribe]: https://www.happyscribe.co/
