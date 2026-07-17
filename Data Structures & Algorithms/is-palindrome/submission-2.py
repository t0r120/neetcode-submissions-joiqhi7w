class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Dado un string llamdo s
        # retorna verdadero si es palindrome
        # Un palindrome es un una palabra que se lee
        # de la misma forma al derecho y al reves 
        #
        
        
        forward = ''.join(word for word in s if word.isalnum()).lower()
        backward = forward[::-1]
        # Iterar por forward de atras para delante y si es igual retornar true
        #wasitacaroracatisaw
        return forward == backward
    
        
    
        