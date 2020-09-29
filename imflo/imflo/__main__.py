import sys

sys.path.append('.')

from imflo import App

app = App()

app.use('basic')
app.use('connect')

app.show('connect')

app.run()
