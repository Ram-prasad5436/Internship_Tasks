# Problem 18: Lists
# HackerRank: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    n = int(input())
    my_list = []

    for _ in range(n):
        command, *args = input().split()
        args = list(map(int, args))

        if command == "insert":
            my_list.insert(args[0], args[1])
        elif command == "print":
            print(my_list)
        elif command == "remove":
            my_list.remove(args[0])
        elif command == "append":
            my_list.append(args[0])
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()
