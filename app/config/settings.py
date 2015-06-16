import os
import motor

settings=dict(
    app_name='luna middleware',
    template_path=os.path.join(os.path.dirname(__file__), "../views"),
    static_path=os.path.join(os.path.dirname(__file__), "../../static"),
    cookie_secret="81o0T==",
    session_secret='08091287&^(01',
    session_dir='/Users/YellowGlue/tmp/session',
    autoreload=True,
    serve_traceback=True,
    debug=True,
    compiled_template_cache=False
    )

db = motor.MotorClient('localhost', 27017).luna
