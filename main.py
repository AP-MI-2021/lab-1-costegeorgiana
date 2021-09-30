'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
nr = int( input('Numarul este:'))
d = 0
 for i in range(2,nr-1):
 	if nr%i==0: d=d + 1;
 if(d==0): print('Este prim')
 	else: print('Nu este prim')
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  
  
def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()
