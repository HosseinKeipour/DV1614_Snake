# my_string=('Hello Python!')
# for item in my_string:
#     print(item)
# my_list=[1,2,3,4]
# for item in my_list:
#     print (item, end=' ')

# def summ(self):
#     a = self + [1, 3]
#     print(a)

# for part in [[(20, 30), (31, 34)], [(24, 65), (341, 32)]]:
#     v = part.summ()
#     print(v)
snake_body=[[23, 45], (45, 45), (234,432,545)]

head = [[10, 45], (45, 45), (234,432,545)]

snake_body = [head] + [snake_body]
print(snake_body)