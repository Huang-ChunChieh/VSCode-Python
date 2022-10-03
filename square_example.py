# 此範例中，透過設定 height 變數破壞了正方形的概念。
# 此正方形的編碼方式需要叫用 set_side() 方法，讓正方形正常顯現。
class Square:
     def __init__(self):
         self.height = 2
         self.width = 2
     def set_side(self, new_side):
         self.height = new_side
         self.width = new_side

square = Square()
square.height = 3 # not a square anymore

#存取層級
#一個前置底線 (_) 是告訴外部世界可能不該觸及這項資料
class Square:
      def __init__(self):
          self._height = 2
          self._width = 2
      def set_side(self, new_side):
          self._height = new_side
          self._width = new_side

  square = Square()
  square._height = 3 # not a square anymore

#一個前置底線仍然可修改資料，這在 Python 表示為「受保護」。
#可以使用兩個前置底線 (__) 來表示為「私用」
class Square:
      def __init__(self):
          self.__height = 2
          self.__width = 2
    def set_side(self, new_side):
          self.__height = new_side
          self.__width = new_side

  square = Square()
  square.__height = 3 # raises AttributeError

#Python 只是變更基礎資料的名稱。只要輸入此程式碼，您然可變更其值：
square = Square()
square._Square__height = 3 # is allowed



#getter和setter(也稱為「存取子」和「更動子」)是專門用來讀取或變更資料的方法。
#getter讓外部可讀取內部資料 
#setter可直接變更資料的方法。此概念是讓 setter 擔任防護，使無法設定「_不正確的」值。
#出正方形類別中getter和setter的作用：
class Square:
      def __init__(self):
          self.__height = 2
          self.__width = 2
      def set_side(self, new_side):
          self.__height = new_side
          self.__width = new_side
      def get_height(self):
          return self.__height
      def set_height(self, h):
          if h >= 0:
              self.__height = h
          else:
              raise Exception("value needs to be 0 or larger")

  square = Square()
  square.__height = 3 # raises AttributeError
#set_height() 方法會阻止您將值設定為負值。 如果設定負值，就會引發例外狀況。



# 對getter和setter使用裝飾項目
# 裝飾項目是Python的重要主體。屬於較大的主體，稱為「中繼程式設計」。
# 裝飾項目是將函式作為輸入的函式。概念是將可重複使用的功能編碼為「裝飾項目函式」，然後用以「裝飾」其他函式。
# 旨在為函式提供過去沒有的功能。 例如，裝飾項目可將欄位新增至物件、測量叫用函式所需的時間，以及執行更多功能。

# 在OOP及getter和setter的內容中有個特定的裝飾項目 @property有助新增getter和setter時移除一些未定案程式碼
# @property裝飾項目會執行下列動作：

# 建立支援欄位：當使用 @property 裝飾項目裝飾函式時，其會建立私用的支援欄位。 您可隨時覆寫此行為，但有預設行為其實還不錯。
# 識別 setter：setter 方法可變更支援欄位。
# 識別 getter：此函式應該會傳回支援欄位。
# 識別 delete 函數：此函式可刪除欄位。
class Square:
    def __init__(self, w, h):
        self.height = h
        self.__width = w
  
    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("Value must be larger than 0")