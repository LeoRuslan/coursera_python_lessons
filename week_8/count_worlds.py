# Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys) записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.

# 19

import sys

print(
    len(
        set(
            sys.stdin.read().strip('\n').split()
        )
    )
)
