# ML-Hungyi-Lee
Code implementation for the lecture Machine Learning by Hungyi-Lee from National Taiwan university.

## Proxy
This server can not access kaggle.com... So you set a proxy.

You run trojan in forward server. The protocol for trojan is socks5, but kaggle command use http. So you install `Proxychains` to forward the http request to trojan listening port in socks5 protocol.

To do this, just use: `proxychains kaggle ... `

Or more generally `proxychains <command>`, like wget, curl, etc.

Also do not forget you open a screen named 'trojan' running trojan. 

## Data
All data are located in /data/zys/

## Virtual environemnt
Note: this folder is also a virtual environment folder

Since this server does not support conda...

To creat a vitual environment:

`virtualenv project_name`

to active a environment:

`source project_name/bin/activate`

now we are in a new python environment. We can see the python we using is within this environment:

`which python/pip`

`pip list`

all pip install package will by installed into this environment

To get out and return to the global environment, use `deactivate`

