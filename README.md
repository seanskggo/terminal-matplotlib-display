# Terminal Matplotlib Display

Personal environment setup tool (since WSL2 does not support X11 forwarding).

Directly display png files from matplotlib.pyplot outputs to terminal on WSL using X server (VcXsrv).

## Setup 

Download <a href="https://sourceforge.net/projects/vcxsrv/" title="VcXsrv">VcXsrv<a/>.

Create symbolic link to xlaunch.exe <strong>in ```x11/```</strong>

```cd x11/ && ln -s path_to_xlaunch.exe```

## Usage

Run

```source check example.py```

Make sure the graph is outputted as .png files

e.g. ```matplotlib.pyplot.savefig("image.png")```

Result:

![1](https://user-images.githubusercontent.com/65769889/106384295-30798980-641e-11eb-8441-4de8d7254dea.PNG)
