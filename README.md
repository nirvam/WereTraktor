# WereTraktor - Online judge tool for "The Werewolves of Millers Hollow"

This is an online version of board game ["The Werewolves of Millers Hollow"](https://en.wikipedia.org/wiki/The_Werewolves_of_Millers_Hollow).

You can create your own room and invite your friends. This app can assign cards and calculate votes.

In the future, this app will deal with all events in the game, and make the game judge-free.

## Getting Started

This project is built with Python 3.6. Python 2 is not tested or supported.

Git clone this project and install prerequisites using pip.

### Prerequisites

WereTraktor uses python-flask and sqlite.

```
pip install -U flask
```

### Running

Copy `config-example.py` to `config.py` and change default settings.

Run this app on localhost:8000 using following command:

```
python main.py
```

Then access `http://localhost:8000` to start a new room or enter an existing room.


## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used

## Contributing

Please send pull requests to [this repository](https://github.com/nirvam/WereTraktor/) for bug fixes and enhancements.

## Authors

* **Marvin Zhang** - *Initial work* - [Nirvam](https://github.com/nirvam)

See also the list of [contributors](https://github.com/nirvam/WereTraktor/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

