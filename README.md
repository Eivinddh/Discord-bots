# Discord-bots

## Discord bots:

- echo kalender
  A simple bot which selects a winner in your voice channel

## Setup

Setup on Linux by following https://docs.discord.red/en/stable/install_linux_mac.html or

Run

```
sudo apt update
sudo apt -y install software-properties-common
sudo add-apt-repository -yu ppa:git-core/ppa
```

Install the pre-requirements with apt:
`sudo apt -y install python3.8 python3.8-dev python3.8-venv python3-pip git default-jre-headless \ build-essential`

Install pipenv with `pip install --user pipenv`

You might need to include pip user installs to PATH.

Download this repo.

Run `cd Discord-bots/` and then `pipenv sync`.

Run `pipenv shell` and then `redbot-setup`
