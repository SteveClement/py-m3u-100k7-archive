#!/usr/bin/env python3
from flask import Flask, render_template
from flask_wtf import Form
from wtforms.fields.html5 import DateField
app = Flask(__name__)
app.secret_key = 'coa7674c694607b169e57593a4952ea26fol!'

shows = [ "All", "Mënsch an Ëmwelt","Noriichten","Klassik oder Klassësch","Schwéierpunkt Klassik","Dageschronik","Klassikthema","Sequenza","Prisma","Moies Panorama","Mëttes Panorama","Owes Panorama","Europa an Internationales","Schwéierpunkt Théater","De Komponist vum Mount","Presserevue","Invité vum Dag","Dossier vum Dag","Bits & Bytes","Mixtape","Kultur Thema","Kultur am Gespréisch","Voices","Startup","Liewensformen","Schwéierpunkt Konscht","Radio Zoo","Wirtschafts Wëssen","Wëssenschaft a Fuerschung","Ee Mount een Thema: Welt am ëmbroch","Ee Mount een Thema: Generic","Spezial Emissioun: Referendum","Spezial Emissioun: Generic","Cool Britannia" ]


class Form(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')

@app.route('/', methods=['POST','GET'])
def audioArchiv():
    form = Form()
    if form.validate_on_submit():
        return form.dt.data.strftime('%Y-%m-%d')
    return render_template('audioArchiv.html', form=form,shows=shows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)