def create_placeholder(nh, nw, nc, ny):
    X = tf.placeholder(tf.float32, shape=(None, nh, nw, nc))
    Y = tf.placeholder(tf.float32, shape=(None, ny))
    # None是随着样例m变化的
    retrun X,Y
# X, Y = create_placeholder(64,64,3,6)



def initialize_parameters():
    W1 = tf.get_variable("W1", [4,4,3,8], initializer=tf.contrib.layers.xavier_initializer())
    W2 = tf.get_variable("W2", [2,2,8,16], initializer=tf.contrib.layers.xavier_initializer())

    parameters={"W1": W1,
                "W2": W2}

    return paramaters
# parameters = initialize_parameters()



# 输入X,W1,W2 输出Z3
def forward_propagation(X, parameters):
    W1 = parameters["W1"]
    W2 = parameters["W2"]

    Z1 = tf.nn.conv2d