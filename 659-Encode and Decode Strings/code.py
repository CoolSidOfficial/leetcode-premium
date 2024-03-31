class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        final = ""
        for string in strs:
            new_str = str(len(string)) + "#" + string
            final = final + new_str
        return final

    """
    @param: string: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, string):
        respo, i = [], 0
        while i < len(string):
            j = i
            while string[j] != "#":
                j = j + 1
            length = int(string[i:j])
            respo.append(string[j + 1:j + 1 + length])
            i = j + 1 + length

        return respo

# Sample function calls
if __name__ == "__main__":
    solution = Solution()
    
    # Example usage of encode method with Input: ["we", "say", ":", "yes"]
    input_1 = ["we", "say", ":", "yes"]
    encoded_string_1 = solution.encode(input_1)
    print("Encoded string 1:", encoded_string_1)
    
    # Example usage of decode method with Input: ["we", "say", ":", "yes"]
    decoded_list_1 = solution.decode(encoded_string_1)
    print("Decoded list 1:", decoded_list_1)

    # Example usage of encode method with Input: ["lint","code","love","you"]
    input_2 = ["lint", "code", "love", "you"]
    encoded_string_2 = solution.encode(input_2)
    print("Encoded string 2:", encoded_string_2)
    
    # Example usage of decode method with Input: ["lint","code","love","you"]
    decoded_list_2 = solution.decode(encoded_string_2)
    print("Decoded list 2:", decoded_list_2)
