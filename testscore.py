import json
import numpy as np
import os
import tensorflow as tf

saver = tf.train.Saver()
with tf.Session() as sess:
    model = saver.restore(sess,"/outputs/model/")
    a = 3

#model_root = tf.saved_model.loader.load(model_name='patrickmlw-mod-27-11-2019')
#saver = tf.train.import_meta_graph(os.path.join(model_root, 'mnist-tf.model.meta'))

#X = tf.get_default_graph().get_tensor_by_name("network/X:0")
#output = tf.get_default_graph().get_tensor_by_name("network/output/MatMul:0")



#data = np.array(json.loads(raw_data)['data'])
        # make prediction
#        out = output.eval(session = sess, feed_dict = {X: data})
