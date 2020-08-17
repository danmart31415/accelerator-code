# accelerator-code
This is almost correct. The python script can now:
  - create seperate files
  - read the arduino serial without the \x00 bug
  - plot the given values

However, the plots are really weird. I think this is beause the files are written in dstrings and not floats. So I will convert everything to a float and see if that works for the next one.
