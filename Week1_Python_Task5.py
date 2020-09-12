if __name__ == '__main__':
  n = int(input())
  # your code here
  a = list(map(int,input().strip().split()))[:n]
  print(sorted(a)[-2])