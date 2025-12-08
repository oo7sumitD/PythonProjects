"""
1) Write a generator to produce the first 10 Fibonacci numbers.

Output:
0
1
1
2
3
5
8
13
21
34
"""
def fibonacci_generator():
    a, b = 0, 1
    while True:  # infinite generator, but we will take first 10
        yield a
        a, b = b, a + b

fib = fibonacci_generator()

for _ in range(10):
    print(next(fib))


"""
2) Write a generator infinite_multiples(n) that yields multiples of the given base value indefinitely.

Input: n = 3
Output:
3
6
9
12
15
...
"""
def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n

gen_mult = infinite_multiples(3)

# Print first 10 multiples for demonstration
for _ in range(10):
    print(next(gen_mult))


"""
3) Write a generator repeat_word(word, times) that yields the word the given number of times.

word = "hello"
times = 5
"""
def repeat_word(word, times):
    for _ in range(times):
        yield word

gen_repeat = repeat_word("hello", 5)

for w in gen_repeat:
    print(w)
