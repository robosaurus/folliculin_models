from modeller import *
from modeller.automodel import *

# this is script will model a bunch of sequences in turn, on the same template.
# it is meant to run after the sequence generator
#first we set up an environment for modeller
log.verbose()
env = environ()
env.io.atom_files_directory = ['.', './sequences', './models']
env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

def model_del(path_to_sequence, path_to_template='./best_model_FLCN.pdb'):
    '''This function invokes sali modeller automodel,
    for a given sequence on a give template'''

    # set up an alignment, this is solely for converting the
    # fasta files to the sali pir format
    aln = alignment(env)
    aln.append(file=path_to_sequence, alignment_format='FASTA')
    aln.write(file=path_to_sequence+'.ali', alignment_format='PIR')
    # We will need the align code later, so let's put that here, this only works if
    path_fields = path_to_sequence.split('/')
    name_field = path_fields[-1]
    name_no_extension = name_field.split('.')[0]
    print(name_no_extension)

    # and now we can set up an alignment for the actual modelling
    aln = alignment(env)
    # read the template
    mdl = model(env, file=path_to_template)#, model_segment=('FIRST:A', 'LAST:A'))
    # add the template to the alignment
    aln.append_model(mdl, align_codes='template')
    # and then we add the sequence with the deletion
    aln.append(file=path_to_sequence+'.ali', align_codes='ALL', alignment_format='PIR')
    # perform an alignment
    aln.align2d()
    # build the model, using the automodel class
    a = automodel(env, alnfile=aln, knowns='template', sequence=name_no_extension, assess_methods = [assess.normalized_dope, assess.DOPE])
    #index of the first model
    a.starting_model = 1
    #index of the last model
    a.ending_model = 25
    a.make()
    a.write(file='/models/'+name_no_extension+'.pdb', model_format='PDB')


model_del('./sequences/folliculin_del_1.fasta')

