from qanda import app, model
from flask import request

@app.route('/twilio/sms/mo', methods=['POST'])
def twilio_sms_mo():
    """Handle incoming SMS."""
    vals: dict = request.form
    sid: str = vals['MessageSid']
    model.new_message(
        body=vals['Body'],
        sid=sid,
        from_=vals['From'],
        to_=vals['To'],
    )
    return "ok"