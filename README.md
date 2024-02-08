# touchdesigner-plugin

This touchdesigner plugin is supposed to generate images for a touchdesigner generative video network using ....

## Dependencies

Touchdesigner only works on Mac and Windows, this project was built on ARM MacOS. Please download Touchdesigner from the [official derivative website](https://derivative.ca/) and install it.

Currently you have to install [rye package manager](https://rye-up.com/)
to build the project until we get a ci/cd pipeline that builds the dist

First please build and install the project globally

```bash
rye build
pip install dist/touchdesigner_plugin-0.1.0-py3-none-any.whl
```

Now navigate to the td_workflow folder and open the latest version of the td_workflow project `td_workflow.toe`.


## Development

This project uses [rye package manager](https://rye-up.com/). It's simple to use just go to the folder

```bash
rye sync
rye run python ...
```

## FAQ

If you have issues using rye you can always generate a good old requirements.txt by doing the following

```bash
sed '/-e/d' requirements.lock > requirements.txt
# now make python virtualenv e.g.
python3 -m venv .td
source .td/bin/activate
pip install -r requirements.txt
```

## Image Server

### How to run

The image server acts as a file server, so you have to clone this repo on the remote machine and start it, if it's running you will need to forward the port to your local machine.

On the remote machine:

```bash
ssh <user>@<remote-ip>
cd to/where/you/want/to/clone/this/to
git clone ...
rye sync
rye run python src/touchdesigner_plugin/image_server.py
```

On you local machine:

Open a new terminal and forward the port, currently it's set to 5002 you can change that in the `src/touchdesigner_plugin/constants.py`

```bash
ssh -L 5002:localhost:5002 <user>@<remote-ip>
```

### ComfyUI

If you want to use stable diffusion you can forward comfyUI from the remote server to your local machine using

```bash
ssh -L 8188:localhost:8188 <user>@<remote-ip>
```

Now access it on the local machine under http://localhost:8188
