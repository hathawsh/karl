import traceback

from ZODB.POSException import ReadOnlyError

from karl.log import get_logger
import webob


def error_log_middleware(app):
    """
    Logs exceptions to Karl syslog.

    XXX Is this overlapping with repoze.error_log?  Is there room for
    integration?
    """
    def middleware(environ, start_response):
        try:
            return app(environ, start_response)
        except Exception, e:
            if not isinstance(e, ReadOnlyError):
                request = webob.Request(environ)
                msg = ['Exception when processing %s' % request.url]
                msg.append('Referer: %s' % request.referer)
                msg.append(traceback.format_exc())
                get_logger().error('\n'.join(msg))
            raise

    return middleware


def make_middleware(app, global_config, **config):
    """
    PasteDeploy entry point.
    """
    return error_log_middleware(app)
