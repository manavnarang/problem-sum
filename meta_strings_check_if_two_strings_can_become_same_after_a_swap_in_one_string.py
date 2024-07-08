# Below are steps used in the algorithm. 

# Check if both strings are of equal length or not, if not return false.
# Otherwise, start comparing both strings and count number of unmatched characters and also store the index of unmatched characters.
# If unmatched characters are more than 2 then return false.
# Otherwise check if on swapping any of these two characters in any string would make the string equal or not.
# If yes then return true. Otherwise return false.

# Python program to check if two strings
# are meta strings

# Returns true if str1 and str2 are meta strings
def areMetaStrings( str1, str2) :
    len1 = len(str1)
    len2 = len(str2)
      
    # Return false if both are not of equal length
    if (len1 != len2) :
        return False
      
    if str1 == str2:
        char_seen = []
        for char in str1:
            if char not in char_seen:
                char_seen.append(char)
        if len(char_seen) < len(str1):
            return True
        return False        
      
    # To store indexes of previously mismatched
    # characters
    prev = -1
    curr = -1
      
    count = 0 
    i = 0
    while i < len1 :
            
        # If current character doesn't match
        if (str1[i] != str2[i] ) :
       
        # Count number of unmatched character
            count = count + 1
      
            # If unmatched are greater than 2,
            # then return false
            if (count > 2) :
                return False
      
            # Store both unmatched characters of
            # both strings
            prev = curr
            curr = i
            
        i = i + 1
      
    # Check if previous unmatched of string1
    # is equal to curr unmatched of string2
    # and also check for curr unmatched character,
    # if both are same, then return true
    return (count == 2 and str1[prev] == str2[curr]
               and str1[curr] == str2[prev])
    
# Driver method
str1 = "converse"
str2 = "converse"
if ( areMetaStrings(str1,str2) ) :
    print("Yes")
else:
    print("No")

# Output
# Yes
# Time Complexity: O(N*log N) where N is the length of the string.
# Auxiliary Space: O(N)
