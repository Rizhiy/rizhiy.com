from pathlib import Path

import sass


# Based on https://github.com/sjl/flask-lesscss/blob/master/flaskext/lesscss.py
def auto_compile_scss(app):
    @app.before_request
    def _render_less_css():
        static_dir = Path(app.root_path + app.static_url_path)

        for path in static_dir.rglob("*.scss"):
            css_path = path.with_suffix(".css")
            css_mtime = -1 if not css_path.exists() else css_path.stat().st_mtime
            if path.stat().st_mtime > css_mtime:
                css_path.write_text(sass.compile(filename=str(path), output_style="compressed"))
