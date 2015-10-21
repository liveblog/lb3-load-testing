# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : GNU General Public License
# -----------------------------------------------------------------------------

PROJECT_NAME = "Liveblog-load-testing"
HOST?="http://liveblogdevel.dev.superdesk.org"
BLOG?="55fa9e3de95d73002ef2931b"
CLIENTS?="1000"
HATCH?="250"
REQUESTS?="10000"

install:
	virtualenv env --no-site-packages --distribute -p python2.7 --prompt=$(PROJECT_NAME)
	. `pwd`/.env ; pip install --upgrade pip
	. `pwd`/.env ; pip install -r requirements.txt
	@echo "installed"

test:
	. `pwd`/.env ; BLOG_ID=$(BLOG) locust --no-web --host=$(HOST) --clients=$(CLIENTS) --hatch-rate=$(HATCH) --num-request=$(REQUESTS) --only-summary
