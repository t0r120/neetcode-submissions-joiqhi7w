class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # Te dan un arreglo de precios
        # cada indice es el precio de una moneda X
        # Cada Indice es un dia
        # Elige un dia para comprar la moneda y otro para venderla
        # Retorna la ganancia maxima 

# 1. **El precio más barato que has visto hasta ahora (`min_price`):** Si encuentras un precio menor 
# al que tenías registrado, actualizas esta variable. Este es tu punto ideal de compra actual.
# 2. **La ganancia máxima calculada hasta ahora (`max_profit`):** En cada día que evalúas, asumes que 
# vendes a ese precio. Calculas `precio_actual - min_price`. Si ese número es mayor que tu ganancia 
# máxima histórica, lo actualizas.

        max_profit = 0
        min_price = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            

        return max_profit
