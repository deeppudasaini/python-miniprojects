from captcha.image import ImageCaptcha  # pip install captcha
from captcha.audio import AudioCaptcha  # pip install captcha
# set width and height of the captcha
captchaImage = ImageCaptcha(Width=200, height=60)
captchaAudio = AudioCaptcha(width=200, height=60)

randomText = captchaImage.generate_random_text(
    length=5)  # generate random text for the captcha
# generate audio for the captcha
randomAudio = audio.generate_audio(randomText)
audiofile = "audio"+randomText+".wav"  # save the audio file
captchaAudio.write(randomAudio, audiofile)  # write the audio file
captchaImage.write(randomText, 'randomText.png')  # write the text on the image
