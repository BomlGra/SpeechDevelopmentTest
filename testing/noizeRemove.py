from rnnoise_wrapper import RNNoise
denoiser = RNNoise()
audio = denoiser.read_wav('/content/test.wav')
denoised_audio = denoiser.filter(audio)
denoiser.write_wav('/content/test1.wav', denoised_audio)