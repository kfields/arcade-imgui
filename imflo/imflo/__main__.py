import os, sys

sys.path.append(os.getcwd())

from imflo import App

app = App()

app.use('basic')
app.use('connect')
app.use('sine')
app.use('sparks')

app.show('basic')

app.run()
