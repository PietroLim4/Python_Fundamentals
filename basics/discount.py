"""
Exercise: Discount Calculation
Description: Calculates the total price of a purchase based on unit price and quantity, applying a 10% discount.
"""

preco = float(input('Digite o preço unitário: '))
qtd = float(input('Digite a quantidade: '))
total = (preco*qtd)*0.9
print(f'Total a pagar: R${total:.2f}')
