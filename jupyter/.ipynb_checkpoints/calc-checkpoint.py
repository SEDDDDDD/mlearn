{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "825d5780",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4234\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "\n",
    "a = tf.constant(1234)\n",
    "b = tf.constant(3000)\n",
    "\n",
    "add_op = a + b\n",
    "\n",
    "sess = tf.Session()\n",
    "res = sess.run(add_op)\n",
    "print(res)"
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
