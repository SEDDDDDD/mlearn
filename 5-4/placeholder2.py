import tensorflow as tf

a = tf.placeholder(tf.int32, [None])
b= tf.constant(30)
xnone_op = a * b

sess = tf.Session()

r1 = sess.run(xnone_op, feed_dict={a:[1,2,3,4,5]})
print(r1)
r2 = sess.run(xnone_op, feed_dict={a:[234, 252, 1, 236, 523]})
print(r2)