{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3039c88d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4 6]\n",
      "[20 40 20]\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "\n",
    "a = tf.placeholder(tf.int32, [3])\n",
    "\n",
    "\n",
    "b = tf.constant(2)\n",
    "x2_op = a * b\n",
    "\n",
    "sess = tf.Session()\n",
    "\n",
    "r1 = sess.run(x2_op, feed_dict={a: [1, 2, 3]})\n",
    "print(r1)\n",
    "r2 = sess.run(x2_op, feed_dict={a: [10, 20, 10]})\n",
    "print(r2)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
