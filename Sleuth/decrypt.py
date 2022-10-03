# 秘密訊息解碼器
# This is a comment that won't be interpreted as a command.
print("Hello, Contosoville!")

# Associate variable town with the value "Contosoville" 設置變量town
town = "Contosoville"

# Print a message about the secret location
print("The town I am looking for is " + town)

# Define a power (function) to chant a phrase 定義函數 函數名稱:chant 參數:phrase(變數)


def chant(phrase):
    # Glue three copies together and print it as a message 列印三次phrase訊息
    print(phrase + phrase + phrase)


# Invoke the power to chant on the phrase "Contosoville!" 調用chant函數 設置phrase變數為"Contosoville!"
chant("Contosoville!")
#-----------------------------------------------------------------------------------------------------#

# 訊息  "Ncevy"、"gpvsui"、"ugflgkg"、"wjmmf"
# 位移數   13        25       -18        -1
# Caesar加密(所有字母在字母表中的順序都略有變動)
# 建立含兩個參數的函式lasso_letter()。
# 第一個參數letter，保留要解碼的字母。
# 第二個參數shift_amount，指出字母的位移距離。
# ASCII 字元碼是代表字母和數字的數位編碼
# ord()函式，將字元轉換為對應的 ASCII 字元碼

# 將一個字母轉換成小寫以保持一致性。
# 使用 ord() 函式，將字母轉換為對應的 ASCII 字元碼。

#---------------------------------------------------------------------------------------#
# 未考慮字母循環 程式碼
# def lasso_letter(letter, shift_amount):
#     # 呼叫lower()函式將值轉為小寫->呼叫ord()函式將轉為小寫的值轉為ASCII字元碼
#     letter_code = ord(letter.lower())
#     decode_letter_code = letter_code + shift_amount  # 將轉換後的字元碼加上位移數
#     decode_letter = chr(decode_letter_code)  # 呼叫chr()函式將ASCII字元碼轉換為對應字符
#     return decode_letter
#---------------------------------------------------------------------------------------#

# letter='N'                    N->n
# letter_code                   ord('n')=110
# shift_amount= 13              110+13=123
# decoded_letter                chr(123) ={
# 必須變更取得decoded_letter_code值的公式，才能找出解碼信件的「真正」字元碼，而不是直接相加 shift_amount 值和 letter_code。

# a~z 的ASCII字元碼轉換為 97~122
# >=123須回到97繼續計算
# 運用mod(%)運算子 -->取餘數  ex:three_two = 3/2 = 1餘數1 值 = 1    ex:eleven_four = 11/4 = 2餘數3 值 = 3

# 新增2個變數
# a_ascii：保留字母 'a' 的 ASCII 代碼值。 我們藉由呼叫 ord('a') 函式並傳入字母來取得此值。
# alphabet_size：保留英文字母表中的字母數目，26。

# 找出 true_letter_code 值的公式： 範例:n
# a_ascii + ((( letter_code - a_ascii) + shift_amount) % alphabet_size)
# ord('a')       ord('密碼')  ord('a')     位移值          英文字母數目
#   97                          97                             26
#   97    + (((     110     -   97   )  +   13)        %       26
#   97 + 0 = 97

# Define a function to find the truth by shifting the letter by the specified amount
# 定義函式lasso_letter()，透過字母位移後轉換為真正的字母

#--------------------------------------------轉換單獨字母--------------------------------------------------#


def lasso_letter(letter, shift_amount):
    # Invoke the ord function to translate the letter to its ASCII code     調用ord函數將字母翻譯成ASCII碼
    # Save the code to the letter_code variable                             將代碼保存到 letter_code 變量中
    letter_code = ord(letter.lower())

    # The ASCII number representation of lowercase letter 'a'               小寫字母'a'的ASCII數字表示
    a_ascii = ord('a')

    # The number of letters in the alphabet                                 英文字母數目
    alphabet_size = 26

    # The formula to calculate the ASCII number for the decoded letter      計算解碼字母的 ASCII 數的公式
    # Take into account looping around the alphabet                         考慮到字母表的循環
    true_letter_code = a_ascii + \
        (((letter_code - a_ascii) + shift_amount) % alphabet_size)

    # Convert the ASCII number to the character or letter                   將 ASCII 數字轉換為字符或字母
    decoded_letter = chr(true_letter_code)

    # Send the decoded letter back                                          回傳解碼後的字母
    return decoded_letter
#---------------------------------------------------------------------------------------------------------#

# 使用 For 迴圈列出反覆項目
# for 語法
# for item in list:
#     do something

# Define a function to find the truth in a secret message
# Shift the letters in a word by a specified amount to discover the hidden word
# 將單詞中的字母移動指定的量以發現隱藏的單詞

#-----------------------------------------------------------轉換訊息----------------------------------------------------------------#


def lasso_word(word, shift_amount):

    # This variable is updated each time another letter is decoded                      每次解碼另一個字母時都會更新此變量
    decoded_word = ""

    # This for loop iterates through each letter in the word parameter
    for letter in word:
        # The lasso_letter() function is invoked with each letter and the shift amount
        # The result (the decoded letter) is stored in a variable called decoded_letter
        decoded_letter = lasso_letter(letter, shift_amount)

        # The decoded_letter value is added to the end of the decoded_word value        decoded_letter值被添加到decoded_word值的末尾
        decoded_word = decoded_word + decoded_letter

    # The decoded_word is sent back to the line of code that invoked this function
    return decoded_word
#----------------------------------------------------------------------------------------------------------------------------------#

# TEST
# Try to decode the word "terra"
# print("Shifting 'terra' by 13 gives: \n" + lasso_word("terra", 13))


# 訊息  "Ncevy"、"gpvsui"、"ugflgkg"、"wjmmf"
# 位移數   13        25       -18        -1
print("Shifting 'Ncevy' by 13 gives: " + lasso_word("Ncevy", 13))
print("Shifting 'gpvsui' by 25 gives: " + lasso_word("gpvsui", 25))
print("Shifting 'ugflgkg' by -18 gives: " + lasso_word("ugflgkg", -18))
print("Shifting 'wjmmf' by -1 gives: " + lasso_word("wjmmf", -1))
