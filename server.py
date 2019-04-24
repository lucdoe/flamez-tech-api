from waitress import serve
import flaskapp.__init__

serve(flaskapp.__init__.app, host='0.0.0.0', port=80)
