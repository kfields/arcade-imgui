import sys

sys.path.append('.')

from imflo import App

app = App()

app.use('basic')
app.use('connect')
app.use('sine')

app.show('connect')

app.run()
