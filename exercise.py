

Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

fdsf



dsf



def cat_dog(str):
  c = 0
  d = 0
  for i in range(len(str)-1):
    if str[i:i+3] == 'dog':
      d += 1
    elif str[i:i+3] == 'cat':
      c += 1
  return c == d




Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())




Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True


def xyz_there(str):
  for i in range(len(str)-1):
    if str[i:i+3] == 'xyz' and str[i-1] != '.':
      return True
  return False



Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6


def sum13(nums):
  total = 0
  i = 0
  
  while i < len(nums):
    if nums[i] == 13:
      i += 1
    else:
      total += nums[i]
    i += 1
  
      
  return total



Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4


def sum67(nums):
  total = 0
  sum_break = False
  for i in nums:
    if i != 6 and sum_break == False:
      total += i
    else:
      sum_break = True
    if i == 7:
      sum_break = False
      
  return total




  def consonant_first(text):
    """Finds a list of unique words in text that start with a consonant
    (letters that are not vowels). Note: all words are returned as
    lowercase and are returned in no particular order.

    Parameters
    ----------
    in_str: string
        A sentence containing no punctuation.
        E.g. "A dog is a good pet and a bear is an awful pet"

    Returns
    -------
    list of strings
        The words from the sentence that do not start with vowels
        ['a', 'e', 'i', 'o', 'u'].
        All strings are returned as lower case.

    Examples
    --------
    >>> consonant_first("A dog is a good pet and a bear is an awful pet")
    ["dog", "good", "pet", "bear"]
    """
    str_list = text.lower().split()
    words = []
    for letter in str_list:
      if letter[0] not in 'aeiou':
        if letter not in words:
        	words.append(letter)
    return words




def keys_geq_cutoff(num_dict, min_cutoff):
    """Returns all the keys (as a set) from num_dict that have
    value greater than or equal to min_cutoff.

    Parameters
    ----------
    num_dict: dictionary
    All the values in num_dict are numeric.
    min_cutoff: float
        Comparison with the num_dict values. Return all keys, where
        their values >= min_cutoff.

    Returns
    -------
    set
        All keys from num_dict whose values meet the cutoff criterion.

    Examples
    --------
    >>> keys_geq_cutoff({'Alice': 21, 'Brett': 20, 'Carlos': 31}, 21)
    {'Alice', 'Carlos'}
    """
    result = set()
    for key, value in num_dict.items():
      if value >= min_cutoff:
        result.add(key)
    return result





wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")




def is_prime(num):
  if num < 2:
      return False
      
  for i in range(2, num):
      if num % i == 0:
          return False
  return True
    
if is_prime(number):
    print ("The number you inputted is a prime number.")
else:
    print ("The number you inputted is not a prime number.")


#Print Number pattern in Python
for num in range(10):
    for i in range(num):
        print (num, end=" ")
    print("\n")


# Output: 
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 
# 8 8 8 8 8 8 8 8 
# 9 9 9 9 9 9 9 9 9


def calculate_median(list_num):
        n = len(list_num)
        sorted_list = sorted(list_num)
        if n < 1:
            return None
        if n % 2 == 1:
            return sorted_list[n//2]
        else:
            return sum(sorted_list[(n//2)-1:(n//2)+1])/2.0




def find_mode(num_list):
        if num_list==[]:
            return None
        else:
            return max(set(num_list), key=num_list.count)



def var_method(lst):
        n = len(lst)
        mean = sum(lst) / float(n)
        return sum((mean - x) ** 2 for x in lst) / float(n - 1)
    
def get_mean_square_error:
    total = 0
    n = len(actual)
    for i in range(0, n):
        difference = actual[i] - predictions[i]
        square_difference = difference**2
        total = total + square_difference
    MSE = total/n
    return MSE

    














