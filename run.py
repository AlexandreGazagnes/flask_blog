#!/usr/bin/env python3
# coding: utf-8

from flaskblog import create_app

if __name__ == '__main__':

    app = create_app()
    app.run(debug=True)
