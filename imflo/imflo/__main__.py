import sys

sys.path.append('.')

from imflo import App

app = App()

app.use('basic')
app.use('connect')
app.use('sine')
app.use('sparks')

app.show('basic')

app.run()
