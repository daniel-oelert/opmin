import sys
import site
site.addsitedir('/home/do/opmin_env/lib/python3.9/site-packages')
sys.path.insert(0, '/var/www/opmin/opmin')
sys.stdout = sys.stderr
from app import app as application