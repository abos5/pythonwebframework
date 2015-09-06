print('ok msg')
print('ok msg')
try:
    import syntax_error_trigger
    dir(syntax_error_trigger)
except SyntaxError, msg:
    print('error : %s\n file: %s, line %d\n content:\n%s' % (msg[0], msg[1][0], msg[1][1], msg[1][3]))

print('ok msg')

#eof
