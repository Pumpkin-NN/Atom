# Change Return Program
# - The user enters a cost and then the amount of money given.
#The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

def remainder_check(n):
    count = 0
    while True:
        r = r - n
        count = count + 1
        if r < n:
            break
    return count

def change(c, m):

    ce = round(m-c, 2)
    print(f'The change is ${ce}')
    if ce // 1 != 0:
        print(f'The dollar: {round(ce // 1,1)}')
        r = round((ce - (ce // 1)), 2)
        if r != 0:
            print(f'The remainder is :{r}')
            if r >= 0.25:
                count = 0
                while True:
                    r = r - 0.25
                    count = count + 1
                    if r < 0.25:
                        break
                print(f'The quarter(s) is(are): {count}')
            elif r >= 0.10:
                count = 0
                while True:
                    r = r - 0.10
                    count = count + 1
                    if r < 0.10:
                        break
                print(f'The dime(s) is(are): {count}')
            elif r >= 0.05:
                count = 0
                while True:
                    r = r - 0.05
                    count = count + 1
                    if r < 0.05:
                        break
                print(f'The nickel(s) is(are): {count}')
            else:
                count = 0
                while True:
                    r = r - 0.01
                    count = count + 1
                    if r < 0.01:
                        break
                print(f'The penny(s) is(are): {count}')


    else:
        print(f'The change dollar is :{0}')
        if r != 0:
            print(f'The remainder is :{r}')
            if r >= 0.25:
                count = 0
                while True:
                    r = r - 0.25
                    count = count + 1
                    if r < 0.25:
                        break
                print(f'The quarter(s) is(are): {count}')

                r = r - 0.25 * count
                if r >= 0.10:
                    count = 0
                    while True:
                        r = r - 0.10
                        count = count + 1
                        if r < 0.10:
                            break
                    print(f'The dime(s) is(are): {count}')

                    r = r - 0.10 * count
                    if r >= 0.05:
                        count = 0
                        while True:
                            r = r - 0.05
                            count = count + 1
                            if r < 0.05:
                                break
                        print(f'The nickel(s) is(are): {count}')

                        r = r - 0.05 * count
                        if r >= 0.01:
                            count = 0
                            while True:
                                r = r - 0.01
                                count = count + 1
                                if r < 0.01:
                                    break
                            print(f'The penny(s) is(are): {count}')

            elif r >= 0.10:
                count = 0
                while True:
                    r = r - 0.10
                    count = count + 1
                    if r < 0.10:
                        break
                print(f'The dime(s) is(are): {count}')

                r = r - 0.10 * count
                if r >= 0.05:
                    count = 0
                    while True:
                        r = r - 0.05
                        count = count + 1
                        if r < 0.05:
                            break
                    print(f'The nickel(s) is(are): {count}')

                    r = r - 0.05 * count
                    if r >= 0.01:
                        count = 0
                        while True:
                            r = r - 0.01
                            count = count + 1
                            if r < 0.01:
                                break
                        print(f'The penny(s) is(are): {count}')



            elif r >= 0.05:
                count = 0
                while True:
                    r = r - 0.05
                    count = count + 1
                    if r < 0.05:
                        break
                print(f'The nickel(s) is(are): {count}')

                r = r - 0.05 * count
                if r >= 0.01:
                    count = 0
                    while True:
                        r = r - 0.01
                        count = count + 1
                        if r < 0.01:
                            break
                    print(f'The penny(s) is(are): {count}')


            else:
                count = 0
                while True:
                    r = r - 0.01
                    count = count + 1
                    if r < 0.01:
                        break
                print(f'The penny(s) is(are): {count}')


    return ce

if __name__ == '__main__':
    cost = float(input("Please enter a cost:\n"))
    amount = float(input("Please enter the amount of money given:\n"))
    change = change(cost, amount)
    print(change)
