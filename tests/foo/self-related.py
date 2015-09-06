
try:
    class foo(object):
        bad = foo

except(NameError):
    print("NameError raised")

# eof
