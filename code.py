import tensorflow as tf
import numpy as np

vocab_size=10
w_dim=4
random_visualize=np.random.randint(0,10,[8,10])
print(random_visualize)
a=tf.placeholder(dtype=tf.int32,shape=[None,None])
word_embedding=tf.get_variable('embedding',[vocab_size,w_dim],dtype=tf.float32)
lookup=tf.nn.embedding_lookup(word_embedding,a)
print("lookup",lookup)

with tf.Session() as tt:
    tt.run(tf.global_variables_initializer())
    print("word_embedding",tt.run(word_embedding))
    a_=tt.run(lookup, feed_dict={a:random_visualize})
    print("output",a_)
    
    
    
    #output:
    
 [[5 2 2 2 7 0 3 0 0 1]
 [8 7 4 7 0 2 7 4 7 3]
 [0 2 9 0 6 3 8 9 3 7]
 [6 9 7 1 5 1 7 1 9 8]
 [3 0 1 0 9 7 3 7 2 9]
 [4 9 6 5 9 9 1 1 6 6]
 [9 0 3 4 5 1 3 5 6 8]
 [8 7 2 2 1 5 9 8 6 4]]
 
 
lookup Tensor("embedding_lookup:0", shape=(?, ?, 4), dtype=float32)



word_embedding [[-0.3357317   0.35316253 -0.08783084 -0.42482477]
 [-0.03084826  0.59296393  0.18084818  0.41846383]
 [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
 [ 0.44059885 -0.5770989  -0.5394542  -0.05016881]
 [ 0.5572101   0.27575094 -0.50864446  0.33067745]
 [ 0.19633412 -0.13632196 -0.03892672 -0.07145476]
 [-0.00544322  0.1312648  -0.38406688  0.4417777 ]
 [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
 [ 0.65425086  0.531126    0.00976431 -0.2947178 ]
 [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]]
 
 
output [[[ 0.19633412 -0.13632196 -0.03892672 -0.07145476]
  [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
  [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
  [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [ 0.44059885 -0.5770989  -0.5394542  -0.05016881]
  [-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [-0.03084826  0.59296393  0.18084818  0.41846383]]

 [[ 0.65425086  0.531126    0.00976431 -0.2947178 ]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [ 0.5572101   0.27575094 -0.50864446  0.33067745]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [ 0.5572101   0.27575094 -0.50864446  0.33067745]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [ 0.44059885 -0.5770989  -0.5394542  -0.05016881]]

 [[-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [-0.00544322  0.1312648  -0.38406688  0.4417777 ]
  [ 0.44059885 -0.5770989  -0.5394542  -0.05016881]
  [ 0.65425086  0.531126    0.00976431 -0.2947178 ]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [ 0.44059885 -0.5770989  -0.5394542  -0.05016881]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]]

 [[-0.00544322  0.1312648  -0.38406688  0.4417777 ]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [-0.03084826  0.59296393  0.18084818  0.41846383]
  [ 0.19633412 -0.13632196 -0.03892672 -0.07145476]
  [-0.03084826  0.59296393  0.18084818  0.41846383]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [-0.03084826  0.59296393  0.18084818  0.41846383]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [ 0.65425086  0.531126    0.00976431 -0.2947178 ]]

 [[ 0.44059885 -0.5770989  -0.5394542  -0.05016881]
  [-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [-0.03084826  0.59296393  0.18084818  0.41846383]
  [-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [ 0.44059885 -0.5770989  -0.5394542  -0.05016881]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]]

 [[ 0.5572101   0.27575094 -0.50864446  0.33067745]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [-0.00544322  0.1312648  -0.38406688  0.4417777 ]
  [ 0.19633412 -0.13632196 -0.03892672 -0.07145476]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [-0.03084826  0.59296393  0.18084818  0.41846383]
  [-0.03084826  0.59296393  0.18084818  0.41846383]
  [-0.00544322  0.1312648  -0.38406688  0.4417777 ]
  [-0.00544322  0.1312648  -0.38406688  0.4417777 ]]

 [[-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [-0.3357317   0.35316253 -0.08783084 -0.42482477]
  [ 0.44059885 -0.5770989  -0.5394542  -0.05016881]
  [ 0.5572101   0.27575094 -0.50864446  0.33067745]
  [ 0.19633412 -0.13632196 -0.03892672 -0.07145476]
  [-0.03084826  0.59296393  0.18084818  0.41846383]
  [ 0.44059885 -0.5770989  -0.5394542  -0.05016881]
  [ 0.19633412 -0.13632196 -0.03892672 -0.07145476]
  [-0.00544322  0.1312648  -0.38406688  0.4417777 ]
  [ 0.65425086  0.531126    0.00976431 -0.2947178 ]]

 [[ 0.65425086  0.531126    0.00976431 -0.2947178 ]
  [-0.28333992 -0.15406847 -0.05600113  0.4475937 ]
  [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
  [ 0.5918895   0.3200553  -0.1287759  -0.34408343]
  [-0.03084826  0.59296393  0.18084818  0.41846383]
  [ 0.19633412 -0.13632196 -0.03892672 -0.07145476]
  [-0.2778009  -0.5765728  -0.14617336  0.6499275 ]
  [ 0.65425086  0.531126    0.00976431 -0.2947178 ]
  [-0.00544322  0.1312648  -0.38406688  0.4417777 ]
  [ 0.5572101   0.27575094 -0.50864446  0.33067745]]]
