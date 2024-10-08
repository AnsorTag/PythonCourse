import sys

sys.path.append("./Section9/9) Importing from ZIP Archives/common.zip")


import common
import common.models as models
import common.validators as validators
import common.helpers as helpers


validators.is_boolean("true")
validators.is_json("{}")
validators.is_numeric(10)
validators.is_date("2018-01-01")

john_post = models.Post()
john_posts = models.Post()
john = models.User()

print("\n\n ********** self *********")
for k in dict(globals()).keys():
    print(k)

print("\n\n ********** common ***********")
for k in common.__dict__.keys():
    print(k)

# print("\n\n ********** validators ***********")
# for k in validators.__dict__.keys():
#     print(k)

# print("\n\n ********** numeric ***********")
# for k in validators.numeric.__dict__.keys():
#     print(k)

# print("\n\n ********** models ***********")
# for k in common.models.__dict__.keys():
#     print(k)

# print("\n\n ********** posts (package) ***********")
# for k in common.models.posts.__dict__.keys():
#     print(k)

print("\n\n ********** models ***********")
for k in models.__dict__.keys():
    print(k)

print(helpers.say_hello("Anos"))
print(helpers.factorial(5))


import asyncio
import email
