This project is for modelling folliculin with each aa (in turn) deleted.
Later we will score the structures with cartesian fastrelax, and use
this as a measure for how well the deletions are tolerrated.

First up is the sequence generation. Versions of the FLCN fragment sequence  
with single AA deletions. This is done with sequence_generator.py
The sequences will be put in the sequences/ directory. You need to make 
that first.

Second is the model generation. This is done with model_dels.py. It loops
through all the sequences in sequences/ directory and creates 25 models of
with each deletion. They all end up in this directory. I suggest you move them
somewhere and clean up after.
