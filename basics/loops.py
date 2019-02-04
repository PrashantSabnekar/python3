words = ['one', 'two', 'three', 'four', 'five']

for w in words:
    print(w)

x = 10

while x > 0:
    print(x);
    x = x - 1;

for i in range(5):
    print(i)

#loop with comtinue
x = 1000
while x > 0:
    x = x - 1
    if x > 10:
        continue
    else:
        print("non continued iteration", x)

#loop with else clause
x = 5
while x > 0:
    x = x - 1;
    print("x = ", x)

else:
    print("The loop terminates now ...")
