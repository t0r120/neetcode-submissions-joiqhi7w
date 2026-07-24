class Solution:

    def encode(self, strs: List[str]) -> str:
        #strs = ["Lista","de","string"]
        #AGrega un delimitador y el la longitud de la lista
        #str = "Listadestring"
        
        code_str = []

        for string in strs:
            #len(string) -> la longitud de la palabra que te mandan
            code_str.append(str(len(string)))
            code_str.append("#")
            code_str.append(string)\
    # ["5","#","Hello"]
        return "".join(code_str) 
    #"5#Hello"

    def decode(self, s: str) -> List[str]:
        response = []
        counter = 0
        while counter < len(s):
            pointer = counter #Pointer inicia en cero
            while s[pointer] != "#":
                pointer += 1
            length = int(s[counter:pointer]) # c = 0 "5#Hello"
            counter = pointer + 1
            response.append(s[counter:counter+length]) 
            counter += length

            # l = 0


        return response
