# Terminal Matplotlib Display

Personal environment setup tool (since WSL2 does not support X11 forwarding).

Directly display png files from matplotlib.pyplot outputs to terminal on WSL using X server (VcXsrv).

## Setup 

Download VcxSrv.

Create symbolic link to xlaunch.exe <strong>in ```x11/```</strong>

```cd x11/ && ln -s path_to_xlaunch.exe```

## Usage

Run

```source check example.py```

Make sure the graph is outputted as .png files

```matplotlib.pyplot.savefig("image.png")```



