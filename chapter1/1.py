
# This is the single line  comment. 'Single hash (#)' is used for a single line comment

# statements

## print: Output strings, integers, or any other datatype.
print("Hello World") # comment can also be present

# variables
this_is_greeting = 'Welcome to the world of Python!'

print("{}".format(this_is_greeting))

## import the datetime module
import datetime
current_date_and_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print("{} => {}".format(this_is_greeting, current_date_and_time))