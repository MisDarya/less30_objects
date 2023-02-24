class Solution:
  def quadric_solve(self, a, b, c): #ax^2+bx+c=0
    d=b*b-4*a*c
    
    if d > 0:
      d=d**0.5
      return (0.5*(d-b)/a, -0.5*(d+b)/a)
    elif d == 0:
      return -0.5*b/a
    else:
      return None

  # Greeting: Ivan Ivanov 14 years old
  def hello(self, name='Ivan', surname='Ivanov', age='14'):
    print('Hello,', name, surname+',', age, 'years old!\n')


  # Build Tree *
  def tree(self, rows=3, smb='*'):
    kol = rows * 2    # Максимальное кол-во символов в строке
  
    if (len(smb)>1):  # проверка на кол-во введенных символов
      smb=smb[0]      # берем первый символ в строке

    print('"Елочка". Количество уровней -', rows)
    for i in range(1, rows+1, 1):
      str=''                          # обнуляем текущую строку
      for j in range(0, i*2-1, 1):    # кол-во символов в строке
         str=str+smb                  # формируем значимую (видимую) часть строки
      space=rows-i                    # кол-во пробелов в начале строки
      print(' '*space, str)           # выводим готовую (сформированную) строку
      

a = Solution()

# print(a.quadric_solve(1,2,-3))
# print(a.quadric_solve(1, 2, 1))
# print(a.quadric_solve(1,2,3))


print('Задание №1')
a.hello('Petya', 'Sidorov')

print('Задание №2')
a.tree(5, '*')