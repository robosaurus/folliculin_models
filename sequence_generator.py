# this script generates all the sequences, each with a single AA deletion.

def sequence_generator(path_to_fasta, name='folliculin_'):
    fasta_file=open(path_to_fasta)
    fasta_lines = fasta_file.readlines()
    fasta_file.close()

    # first let us get the sequence as a string
    original_seq = ''
    for line in fasta_lines[1:]:
        original_seq = original_seq + line.strip()

    print(original_seq)
    # for each AA in the sequence crete a new sequence without that one
    for number in range(len(original_seq)):
        deletion_seq = original_seq[0:number] + original_seq[number+1:]
        print(deletion_seq)
        del_file_name = name+'del_' + str(number+1)
        deletion_fasta = open('./sequences/'+del_file_name + '.fasta', 'w')
        deletion_fasta.write('>'+del_file_name + '\n')
        deletion_fasta.write(deletion_seq + '\n')
        deletion_fasta.close()

sequence_generator('./3v42.fasta')
