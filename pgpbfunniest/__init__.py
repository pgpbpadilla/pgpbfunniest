# This is to allow:
# import pgpgfunniest
# from pgpbfunniest.text import joke
# print joke()
__all__ = ["text"]

# This is to allow:
# > import pgpgfunniest
# > print pgpbfunniest.joke()
#
# you can also do:
#
# > from pgpbfunniest.text import joke as j
# > print j()
from pgpbfunniest.text import joke

