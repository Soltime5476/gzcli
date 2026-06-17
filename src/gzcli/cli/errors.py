"""Error handling for gzcli"""

import traceback
import click
from gzcli.cli.config import ERROR_LOG
from functools import wraps


def error_wrap(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except click.ClickException:
            raise
        except Exception:
            ERROR_LOG.write_text(traceback.format_exc())
            click.echo(f"an error occured, error log written to {ERROR_LOG}")

    return wrapper
