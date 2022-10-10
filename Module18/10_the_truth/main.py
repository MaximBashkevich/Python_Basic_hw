DATA_SYM = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypter(text, shift_1):
    new_text_1 = ''
    for sym in text:
        if sym in DATA_SYM:
            index = DATA_SYM.find(sym)
            new_text_1 += DATA_SYM[index - shift_1]
        else:
            new_text_1 += sym

    shift_2 = 3
    new_text_2 = ''
    for word in new_text_1.split():
        new_word = ''
        for index in range(len(word)):
            new_word += (word[index - shift_2 % len(word)])
        if new_word.endswith('/'):
            shift_2 += 1
        new_text_2 += new_word + ' '
    translated_step_2 = new_text_2.replace('/ ', '\n')
    return translated_step_2


encrypted_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt ' \
                  'fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm y' \
                  'Dpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ' \
                  'ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj ' \
                  'vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl' \
                  ' ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst ' \
                  'tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/' \
                  'tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ' \
                  'ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof p' \
                  'vt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf ' \
                  'wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou' \
                  ' /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op' \
                  ' gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /' \
                  'jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf ' \
                  'b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(' \
                  'tm pe psfn gp tf"uip'
shift = 1
print(decrypter(encrypted_text, shift))