import argparse

import flask
from six.moves import configparser as ConfigParser

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def get_hello():
    return "hello"


def parse_command_line_args():
    description = 'Starts the API service for github-followers'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('config_file', type=str, nargs='?',
                        default='/etc/github-followers.conf',
                        help='the path for the config file to be read.')
    return parser.parse_args()


def main():
    args = parse_command_line_args()
    config = ConfigParser.ConfigParser()
    config.read(args.config_file)
    try:
        host = config.get('default', 'host')
    except ConfigParser.NoOptionError:
        host = '127.0.0.1'
    try:
        port = config.getint('default', 'port')
    except ConfigParser.NoOptionError:
        port = 5000
    app.run(debug=True, host=host, port=port)


if __name__ == '__main__':
    main()
