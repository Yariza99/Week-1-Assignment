if __name__ == '__main__':
    n = int(input())
    # your code here
    if n % 2 == 1:
      print('Weird')
    elif n in range(2,6) or n > 20:
      print('Not Weird')
    else:
      print('Weird')