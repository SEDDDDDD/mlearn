{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0c4f5bb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "390\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "\n",
    "# 상수정의\n",
    "\n",
    "a = tf.constant(120, name=\"a\")\n",
    "b = tf.constant(130, name=\"b\")\n",
    "c = tf.constant(140, name=\"c\")\n",
    "\n",
    "#변수정의\n",
    "\n",
    "v = tf.Variable(0, name=\"v\")\n",
    "\n",
    "# 데이터 플로우 그래프 정의\n",
    "calc_op = a + b + c\n",
    "assign_op = tf.assign(v, calc_op)\n",
    "\n",
    "# 세선 실행\n",
    "sess = tf.Session()\n",
    "sess.run(assign_op)\n",
    "\n",
    "# v 내용 출력\n",
    "\n",
    "print(sess.run(v))\n",
    "\n"
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
