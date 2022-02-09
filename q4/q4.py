import scipy
import scipy.io
import scipy.io.wavfile
import scipy.fftpack

def Read_soundfile(filename):
    raw_sound = scipy.io.wavfile.read(filename)
    return raw_sound

def identify_tone(frequenzy):
    tone_dict = {440:'a', 466:'aiss', 494:'b', 523:'c', 554:'ciss', 587:'d', 622:'diss', 659:'e', 699:'f', 740:'fiss', 784:'g', 831:'giss'}
    frequenzy_list = list(tone_dict.keys())
    while frequenzy<440 or frequenzy>880:
        if frequenzy<440:
            frequenzy*=2
        else:
            frequenzy/=2
    frequenzy = round(frequenzy,ndigits=0)
    min = 1000
    tone = str()
    for i in range(len(frequenzy_list)):
        if abs(frequenzy-frequenzy_list[i])<min:
            tone = tone_dict[frequenzy_list[i]]
            min = abs(frequenzy-frequenzy_list[i])
    if min >10:
        print('Stort avstånd till närmaste ton')
        print(min)
    return tone

def main():
    print('Vilken fil vill du läsa in?')
    filename = input('-> ')
    total_time = 3
    raw_sound = Read_soundfile(filename)
    samplingrate, frequenses = raw_sound
    F = scipy.fftpack.fft(frequenses)
    frequens_dict = {}
    for i, ft in enumerate(F):
        frequens_dict[i/total_time] = abs(ft)
    tone_amplitude_dict = sorted(frequens_dict, key=frequens_dict.get, reverse=True)[:6]
    tones = []
    for i in [0,2,4]:
        tones.append(tone_amplitude_dict[i])
    tone = sum(tones)/len(tones)
    print(tones)
    tone = identify_tone(tone)
    print(tone)

if __name__ == '__main__':
    main()