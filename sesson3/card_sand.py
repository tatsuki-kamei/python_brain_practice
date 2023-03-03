def search(card, n):
   if n == 0:
      return card.index(0)
    
   joker = [-1]

   for l in range(len(card) - n - 1):
      r = l + n + 1

      if card[l] == 0 and card[r] == 0:
         card[l], card[r] = n, n
         joker.append(search(card, n - 1))
         card[l], card[r] = 0, 0
         
   return max(joker)

n = 9
print(search([0]* (2*n +1), n) + 1)
