"""
Função para determinar a quantidade de números primos abaixo de N
"""
def qty_prime_numbers(num):
    count = 0
    if num >= 2:
        prime = [2]
    else:
        prime = []
 
    for ele in range(3, num + 1, 2):
        for i in prime:
            if i > ele//2:
                break
            elif ele % i == 0:
                count = 1
                break
        if count == 0:
            prime.append(ele)
        else:
            count = 0
    return f'Prime numbers {prime}\n' \
           f'Quantity of prime numbers {len(prime)}'