import argparse
import json

import flask
from six.moves import configparser as ConfigParser

from github_followers import client

app = flask.Flask(__name__)


def _get_followers(login, level, max_level, max_degree):
    followers = client.get_followers(login, limit=max_degree)
    followers = [f['login'] for f in followers]
    if level == max_level - 1:
        return followers
    result = []
    for follower in followers:
        result.append({follower: _get_followers(
            follower, level + 1, max_level, max_degree)})
    return result


@app.route('/followers/<string:login>', methods=['GET'])
def get_followers(login):
    max_level = int(flask.request.args.get('level', 3))
    max_degree = int(flask.request.args.get('max_degree', 5))
    result = _get_followers(login, 0, max_level, max_degree)
    return json.dumps(result)


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
