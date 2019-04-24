from waitress import serve
import flaskapp.flaskapp.py

serve(flaskapp.flaskapp.py.app, host='0.0.0.0', port=80)
