def seq2pairwise(incoming):
    L = tf.shape(incoming)[1]
    #save the indexes of each position
    v = tf.range(0, L, 1)
    i, j = tf.meshgrid(v, v)
    m = (i+j)/2
    #switch batch dim with L dim to put L at first
    incoming2 = tf.transpose(incoming, perm=[1, 0, 2])
    #full matrix i with element in incomming2 indexed i[i][j]
    out1 = tf.nn.embedding_lookup(incoming2, i)
    out2 = tf.nn.embedding_lookup(incoming2, j)
    out3 = tf.nn.embedding_lookup(incoming2, m)
    #concatante final feature dim together
    out = tf.concat([out1, out2, out3], axis=3)
    #return to original dims
    output = tf.transpose(out, perm=[2, 0, 1, 3])
    return output

output_1d=seq2pairwise(input_1d)
