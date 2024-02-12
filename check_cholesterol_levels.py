# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholesterol = 201
ldl = 30
triglyceride = 120


def print_good_cholestrol():
    print('*** Good level of cholesterol ***')


def print_borderline_cholestrol():
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')


def print_bad_cholesterol():
    print('*** High cholesterol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')


def check_total_cholesterol(cholesterol):
    if cholesterol < 200:
        return 'good'
    if 200 < cholesterol < 240:
        return 'borderline'
    if cholesterol > 240:
        return 'bad'


def check_ldl(ldl):
    if ldl < 100:
        return 'good'
    if 130 < ldl < 160:
        return 'borderline'
    if ldl > 160:
        return 'bad'


def check_triglyceride(triglyceride):
    if triglyceride < 150:
        return 'good'
    if 150 <= triglyceride < 200:
        return 'borderline'
    if triglyceride >= 200:
        return 'bad'


cholesterol_status = check_total_cholesterol(total_cholesterol)
ldl_status = check_ldl(ldl)
triglyceride_status = check_triglyceride(triglyceride)

if cholesterol_status == 'bad' or ldl_status == 'bad' or triglyceride_status == 'bad':
    print_bad_cholesterol()
elif cholesterol_status == 'borderline' or ldl_status == 'borderline' or triglyceride_status == 'bordeline':
    print_borderline_cholestrol()
elif cholesterol_status == 'good' or ldl_status == 'good' or triglyceride_status == 'good':
    print_good_cholestrol()

else:
    print('Error: unhandled case.')
