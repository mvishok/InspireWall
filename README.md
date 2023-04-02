<br/>
<p align="center">
  <h3 align="center">InspireWall</h3>

  <p align="center">
    Get inspired every time you log in with InspireWall!
    <br/>
    <br/>
    <a href="https://github.com/mvishok/InspireWall/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/mvishok/InspireWall/total.svg) ![Contributors](https://img.shields.io/github/contributors/mvishok/InspireWall?color=dark-green) ![Forks](https://img.shields.io/github/forks/mvishok/InspireWall?style=social) ![Stargazers](https://img.shields.io/github/stars/mvishok/InspireWall?style=social) ![Issues](https://img.shields.io/github/issues/mvishok/InspireWall) ![License](https://img.shields.io/github/license/mvishok/InspireWall) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Latest Release](#latest-release)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## Latest release
The latest release of InspireWall can be found on the [releases page](https://github.com/mvishok/InspireWall/releases)

## About The Project

InspireWall is a simple desktop application for Windows that fetches quotes using the [Quotable API](https://api.quotable.io) and sets them as the wallpaper on the user's desktop. Each time the user logs in, InspireWall will change the wallpaper to a new quote, providing a fresh dose of inspiration to start the day.

InspireWall was created to help users stay motivated and inspired by displaying a new quote each day. The app is simple to use and can easily be set up to run on startup. Currently, InspireWall is only available for Windows due to the use of the windll library, but plans are in place to expand to other platforms in the future.

With InspireWall, users can enjoy a new quote every day and start their day off on a positive note. Whether you're a student, a professional, or just someone looking to add a bit of motivation to your daily routine, InspireWall is the perfect tool to help you achieve your goals and stay inspired.

## Built With



* [Python 3.10.10](https://www.python.org/downloads/release/python-31010/)
* [Python Imaging Library (PIL)](https://pypi.org/project/Pillow/)
* [Quotable API](https://api.quotable.io)
* [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/)

## Getting Started

To use InspireWall, you will need to download the latest version from the [GitHub repository](https://github.com/mvishok/InspireWall). Follow the steps below to get started:

### Prerequisites

In order to use InspireWall, you will need to have Python 3.x installed on your Windows machine. You can download the latest version of Python from the official website: https://www.python.org/downloads/windows/

Additionally, you will need to install the required Python packages which can be installed using pip, the Python package manager. The required packages are listed in the requirements.txt file in the root directory of the project. You can install them by running the following command in the command prompt:

```sh
pip install -r requirements.txt
```

### Installation

1. Download and install Python 3 on your Windows machine.

2. Clone the InspireWall repository to your local machine:

```sh
git clone https://github.com/mvishok/InspireWall.git
```

3. Install the required dependencies by running the following command in your terminal:
```sh
pip install -r requirements.txt
```

4. Run the app by running the following command in your terminal

```sh
python inspirewall.py
```

5. The app will start running and will change the wallpaper of your Windows machine with a new inspirational quote. Enable the app to launch automatically when you log into Windows.

## Roadmap

See the [open issues](https://github.com/mvishok/InspireWall/issues) for a list of proposed features (and known issues).

## Contributing

The Contributing section is a place where users can learn how to contribute to the Inspirewall project. Here are some guidelines for contributing:

1. Your changes must be compatible with the Apache 2.0 license.
2. Your changes must follow the code formatting conventions used in the project.
3. Your changes must be thoroughly tested and not introduce any new bugs.

### Creating A Pull Request

1. Fork the Inspirewall repository on GitHub.
2. Clone your forked repository to your local machine.
3. Make changes to the codebase.
4. Commit your changes to your local repository.
5. Push your changes to your forked repository on GitHub.
6. Open a pull request to merge your changes with the main Inspirewall repository.

We welcome contributions of any size, from small bug fixes to large feature additions. Thank you for your interest in contributing to Inspirewall!

## License

Distributed under the Apache-2.0 License. See [LICENSE](https://github.com/mvishok/InspireWall/blob/main/LICENSE.md) for more information.

## Authors

* **Vishok M** - *Student* - [Vishok M](https://github.com/mvishok) - *Continuously developing and maintaining the project.*

## Acknowledgements

* [Quotable API](https://github.com/lukePeavey/quotable)
