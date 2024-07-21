# framework
experimental port of msf from Ruby to Python lol


## Outline
My original goal was to do a complete rewrite of the [Metasploit Framework](https://metasploit.com), primarily [msfconsole] from `Ruby` to [Python](https://python.org). I wanted to do this because I wanted to learn more about exploit development & the typical structure of a framework like Metasploit. I also wanted to take advantage of the `Python` ecosystem.


Now, my goals have shifted & there are some additional features I would like to add to this project.


First and foremost, we want to write this in python using statically typed annotations. This will allow for better code completion & error checking. We will also use [Black](https://black.readthedocs.io/en/stable/) for code formatting. We are using `pdm` as our package manager. We are using `pytest` for testing. We are using `mypy` for static type checking. 

The base application is a [Rich](https://github.com/Textualize/rich) based `cli application`.

I would like to add a `REST API` to this project. This would allow for easier integration with other tools & services. For this we will use [Litestar](https://litestar.dev/), formerly known as `Starlite`.

Eventually I would also like to add a `Web UI` to this project. This would allow for easier use of the framework for those who are not comfortable with the command line, however this is a lower priority than the `REST API` & the `cli app`.