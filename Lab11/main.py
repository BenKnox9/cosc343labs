from WordEnc import WordEnc

my_word_enc = WordEnc(max_words=100)
my_word_enc.fit("my dear lady families")
X = my_word_enc.transform("my dear lady families")
