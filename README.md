# Word of The Hour API

## About

[Word of The Hour](https://wordofthehour.org) is a platform for learning words in multiple languages.

This is the official Python API for [Word of The Hour](https://wordofthehour.org).

## How does it work?

First, you need to import the Python module using the following code: `from woth_api import WothAPI`.

Then, you can simply call `woth_data = WothAPI.fetch()` to retrieve the data for the current word from the [Word of The Hour](https://wordofthehour.org) servers.

Finally, you can access the retrieved data using the `woth_data` variable.

For example:

- You can access the current word using `woth_data["word"]`.

- You can access the array of current definitions using `woth_data["definitions"]["english"]`.

- You can access the dictionary of current translations using `woth_data["translations"]`.

## Translations and Corrections

New translations and data corrections come from the [r/Word_of_The_Hour](https://www.reddit.com/r/Word_of_The_Hour/) language [crowdsourcing project](https://www.reddit.com/r/Word_of_The_Hour/comments/95v7rk/we_need_your_help_help_us_improve_our_translations/).

## Usage

The MIT License applies to the Python Code provided within this repository.

We offer no guarantees regarding performance or the data retrieved by this API.

If you incorporate this code into your applications, then we ask that you consider limiting how many `WothAPI.fetch()` calls that you make.  For example, an application should not need to call `WothAPI.fetch()` more than once per hour.
