from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
    Blueprint,
)
from main_app.models import TestLog

main_bp = Blueprint("main_bp", __name__)


@main_bp.route('/')
def index():
    return render_template('index.html', title='Home Page')


@main_bp.route('/testlogs')
def testLogs():
    testLogs = TestLog.query.all()
    return render_template('index.html', title='Test Logs', testLogs=testLogs)
