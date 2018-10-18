import tensorflow as tf


class Exercise01:

  @staticmethod
  def matrix_multi(matrix):
        with tf.Session():
            x = tf.constant(matrix)
            z = tf.matmul(x, x)
            return z.eval()