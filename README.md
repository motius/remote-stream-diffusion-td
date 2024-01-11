# touchdesigner-plugin

This touchdesigner plugin is supposed to generate images for a touchdesigner generative video network using ....


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
