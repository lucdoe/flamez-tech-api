from waitress import serve
import flaskapp.flaskapp

serve(flaskapp.flaskapp.app, host='0.0.0.0', port=80)

