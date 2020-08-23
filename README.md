# mfs' Blender related stuff

## Cycle Select Mode Plugin

[cycle_select_mode](https://github.com/mfs/blender-related/tree/master/cycle_select_mode) allows
you to cycle between vertex, edge and face modes. The number keys are awkward to get to one handed
on my keyboard so have this bound to a couple of spare mouse thumb buttons.

## Random CLI commands

I use Blender on Linux and prefer to render all output to PNG files. To convert
to animated GIF or video I use `convert` or `ffmpeg`.

Convert a sequence of PNGs to an mp4 suitable for upload to Twitter.

    ffmpeg -f image2 -i %04d.png -vcodec libx264 -pix_fmt yuv420p -strict 2 video.mp4