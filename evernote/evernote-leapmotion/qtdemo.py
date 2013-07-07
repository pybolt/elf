import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplicaiton(sys.argv)

web=QWebView()
web.load(QUrl("http://google.pl"))
web.show()

sys.exit(app.exec_())
