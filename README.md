<h1 align="center">
  md-scraper
</h1>
> A tool to download all markdown files from a GitHub repository.

A brief description of your project, what it is used for and how does life get
awesome when someone starts to use it.

## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

```shell
git clone https://github.com/fr0ziii/md-scraper.git
cd md-scraper/
pip install requests
pip install beautifulsoup4
python scraper.py https://github.com/fr0ziii/md-scraper
```

This will download all the markdown files from the `fr0ziii/md-scraper` repository into the `/docs/` folder.

### Initial Configuration

Some projects require initial configuration (e.g. access tokens or keys, `npm i`).
This is the section where you would document those requirements.

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone https://github.com/fr0ziii/md-scraper.git
cd md-scraper/
pip install requests
pip install beautifulsoup4
```

And state what happens step-by-step.

### Building

If your project needs some additional steps for the developer to build the
project after some code changes, state them here:

N/A

Here again you should state what actually happens when the code above gets
executed.

### Deploying / Publishing

In case there's some step you have to take that publishes this project to a
server, this is the right time to state it.

N/A

And again you'd need to tell what the previous code actually does.

## Features

What's all the bells and whistles this project can perform?
* Downloads all markdown files from a GitHub repository, including files in subdirectories.
* Saves the markdown files to the `/docs/` folder
* Includes error handling
* Limits recursion depth to 3 to prevent excessive downloads.

## Configuration

Here you should write what are all of the configurations a user can enter when
using the project.

#### Argument 1
Type: `String`  
Default: `N/A`

The URL of the GitHub repository to scrape.

Example:
```bash
python scraper.py https://github.com/adam-p/markdown-here
```

#### Argument 2
Type: `String`  
Default: `docs`

The directory to save the markdown files to.

Copy-paste as many of these as you need.

## Contributing

When you publish something open source, one of the greatest motivations is that
anyone can just jump in and start contributing to your project.

These paragraphs are meant to welcome those kind souls to feel that they are
needed. You should state something like:

"If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome."

If there's anything else the developer needs to know (e.g. the code style
guide), you should link it here. If there's a lot of things to take into
consideration, it is common to separate this section to its own file called
`CONTRIBUTING.md` (or similar). If so, you should say that it exists here.

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Repository: https://github.com/fr0ziii/md-scraper
- Issue tracker: https://github.com/fr0ziii/md-scraper/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!

## Licensing

One really important part: Give your project a proper license. Here you should
state what the license is and how to find the text version of the license.
Something like:

"The code in this project is licensed under MIT license."
