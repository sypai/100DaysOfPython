partner_1 = input("What is your name?")
partner_2 = input("What is the name of your better half?")

partner_1 = partner_1.lower()
partner_2 = partner_2.lower()

t_count = partner_1.count('t') + partner_2.count('t')
r_count = partner_1.count('r') + partner_2.count('r')
u_count = partner_1.count('u') + partner_2.count('u')
e_count = partner_1.count('e') + partner_2.count('e')
true_total = t_count + r_count + u_count + e_count

l_count = partner_1.count('l') + partner_2.count('l')
o_count = partner_1.count('o') + partner_2.count('o')
v_count = partner_1.count('v') + partner_2.count('v')
e_count = partner_1.count('e') + partner_2.count('e')
love_total = l_count + o_count + v_count + e_count

compatibility = str(true_total) + str(love_total)

if int(compatibility) < 10 or int(compatibility) > 90:
    print(f'Your score is {compatibility}, you go together like coke and mentos.')
elif 40 < int(compatibility) < 50:
    print(f'Your score is {compatibility}, you are alright together.')
else:
    print(f'Your score is {compatibility}.')
