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


## Image Server

### Random Image generator

The random image generator is a simple image server that generates images using opencv you can run it using rye since it doesn't have any additional dependencies

```bash
cd path/to/StreamDiffusion
export PYTHONPATH=${PWD}
cd path/to/touchdesigner-plugin
cd src
export PYTHONPATH=$PYTHONPATH:${PWD}


# for reference `echo $PYTHONPATH` should return sth like this
# /home/<user>/workspace/StreamDiffusion:/home/<user>/workspace/touchdesigner-plugin/src
# now run it
cd path/to/touchdesigner_plugin
rye run python src/touchdesigner_plugin/image_server.py
```

That's it you can now generate colorful images in your techdesigner session.


### Stream Diffusion

#### Installation

To install stream diffusion please follow the instructions on their [Github repository](https://github.com/cumulo-autumn/StreamDiffusion). You have to install it independently from the rye packaged project here and run it in a separate virtual environment. I can't say more because it highly depends on your GPU setup.

#### Run Stream diffusion on server

The stream diffusion is integrated in the [stream_diffusion_server.py](./src/touchdesigner_plugin/stream_diffusion_server.py), please activate your virtual environment and run it and then just start your touchdesigner session and start generating.

```bash
# activate virtual env e.g.
source .venv/bin/activate
python src/touchdesigner/stream_diffusion_server.py
```

That's it you should now be able to use the generate images in touchdesigner.


### Port Forwarding

If you want to forward a port from the remote machine to local e.g. port 8188 remote to 8190 local

```bash
ssh -L 8190:localhost:8188 <user>@<remote-ip>
```

Now access it on the local machine under http://localhost:8190


## FAQ

If you have issues using rye you can always generate a good old requirements.txt by doing the following

```bash
sed '/-e/d' requirements.lock > requirements.txt
# now make python virtualenv e.g.
python3 -m venv .td
source .td/bin/activate
pip install -r requirements.txt
```
