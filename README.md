# Robot Parts Manager

[![Build Status](https://travis-ci.org/gunthercox/RobotPartsManager.svg?branch=master)](https://travis-ci.org/gunthercox/RobotPartsManager)

This is a parts inventory management application
designed to hold information about parts held in
inventory, the availability of the same part from
different retailers, and which parts each robot is using.

In addition, this application provides API endpoints
through which each robot can authenticate and update
the condition of a given part in the case that it is
damaged and a new one needs to be ordered.

## Setup

1. Clone this repository `https://github.com/gunthercox/RobotPartsManager.git`
2. Change to the project directory `cd RobotPartsManager`
3. Run the server using `python manage.py runserver 0.0.0.0:8000`
4. Go to http://localhost:8000 in your browser

## License

Copyright (c) 2016 Gunther Cox

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
