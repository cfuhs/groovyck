if examMark < 0 or examMark > 100:
    print('Invalid mark entered - needs to be in the range 0..100')
elif examMark >= 70:
    print('An exceptional result!')
    print('We expect a first-class project from you.')
elif examMark >= 50:
    print('A satisfactory result!')
    print('You may proceed with your project.')
else:
    print('Sorry, you have failed.')
