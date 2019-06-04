import numpy as np

class MultiClassPerceptron(object):
	def __init__(self,num_class,feature_dim):
		"""Initialize a multi class perceptron model.

		This function will initialize a feature_dim weight vector,
		for each class.

		The LAST index of feature_dim is assumed to be the bias term,
			self.w[:,0] = [w1,w2,w3...,BIAS]
			where wi corresponds to each feature dimension,
			0 corresponds to class 0.

		Args:
		    num_class(int): number of classes to classify
		    feature_dim(int): feature dimension for each example
		"""

		self.w = np.zeros((feature_dim+1,num_class))

	def train(self,train_set,train_label):
		""" Train perceptron model (self.w) with training dataset.

		Args:
		    train_set(numpy.ndarray): training examples with a dimension of (# of examples, feature_dim)
		    train_label(numpy.ndarray): training labels with a dimension of (# of examples, )
		"""

		# YOUR CODE HERE
		#print(train_set.shape)
		#print(train_label.shape)
		#print(self.w.shape)

		lrate = 1/self.w.shape[0]
		num_iter = 30

		self.__train(train_set, train_label, lrate, num_iter)

		pass

	def __train(self, train_set, train_label, lrate=0.1, num_iter=1000):

		# array of 1's shape is (number of examples, 1)
		# add this to training set, so that w and train_set have correct dims
		# for matrix operations
		padding = np.ones((train_set.shape[0], 1))
		train_set = np.concatenate((padding, train_set), 1)
		# print(train_label[0:10])

		number_of_examples = train_set.shape[0]
		number_of_features = train_set.shape[1]
		number_of_classes = self.w.shape[1]

		#print(train_set.shape)
		#print(train_label.shape)

		dot_product = np.zeros(number_of_classes)
		train_label = np.reshape(train_label, (train_label.shape[0], 1))
		#print(train_label.shape)
		#shuffle_array = np.concatenate((train_set, train_label), 1)

		#print(shuffle_array.shape)

		for epochs in range(1,num_iter+1):
			train_label = np.reshape(train_label, (train_label.shape[0], 1))
			shuffle_array = np.concatenate((train_set, train_label), 1)
			np.random.shuffle(shuffle_array)
			train_set = shuffle_array[:,:train_set.shape[1]]
			train_label = shuffle_array[:,train_set.shape[1]:]
			train_label = train_label.astype(int)
			train_label = np.reshape(train_label, train_label.shape[0])
			#print(train_set.shape)
			#print(train_label.shape)
			for example in range(number_of_examples):
				#print(example)
				for classes in range(number_of_classes):
					dot_product[classes] = np.dot(train_set[example], self.w[:,classes])
				predicted_label_index = np.argmax(dot_product)
				if predicted_label_index != train_label[example]:
					#self.w[:,predicted_label_index] -= (1/((epochs*number_of_examples)+(example+1)))*train_set[example,:]
					#self.w[:,train_label[example]] += (1/((epochs*number_of_examples)+(example+1)))*train_set[example,:]
					#self.w[:,predicted_label_index] -= train_set[example,:]
					#self.w[:,train_label[example]] += train_set[example,:]
					#print(self.w.shape)
					#print(train_set.shape)
					#print(train_label.shape)
					self.w[:,predicted_label_index] -= (1/((epochs*number_of_examples)+(example+1)))*train_set[example,:]
					self.w[:,train_label[example]] += (1/((epochs*number_of_examples)+(example+1)))*train_set[example,:]

	def test(self,test_set,test_label):
		""" Test the trained perceptron model (self.w) using testing dataset.
			The accuracy is computed as the average of correctness
			by comparing between predicted label and true label.

		Args:
		    test_set(numpy.ndarray): testing examples with a dimension of (# of examples, feature_dim)
		    test_label(numpy.ndarray): testing labels with a dimension of (# of examples, )

		Returns:
			accuracy(float): average accuracy value
			pred_label(numpy.ndarray): predicted labels with a dimension of (# of examples, )
		"""

		#print(test_set.shape)

		number_of_examples = test_set.shape[0]
		number_of_pixels = test_set.shape[1]
		number_of_classes = self.w.shape[1]
		dot_product = np.zeros(number_of_classes)

		padding = np.ones((test_set.shape[0], 1))
		test_set = np.concatenate((padding, test_set), 1)

		# YOUR CODE HERE
		accuracy = 0
		pred_label = np.zeros((len(test_set)))

		for example in range(number_of_examples):
			for classes in range(number_of_classes):
				dot_product[classes] = np.dot(test_set[example], self.w[:,classes])
			predicted_label_index = np.argmax(dot_product)
			pred_label[example] = predicted_label_index

		correct_prediction = 0

		for example in range(number_of_examples):
			if pred_label[example] == test_label[example]:
				correct_prediction += 1

		accuracy = correct_prediction / number_of_examples
		print(accuracy)

		return accuracy, pred_label

	def guess(self,test_set):
		for classes in range(number_of_classes):
			dot_product[classes] = np.dot(test_set, self.w[:,classes])
		predicted_label_index = np.argmax(dot_product)
		return predicted_label_index

	def save_model(self, weight_file):
		""" Save the trained model parameters
		"""

		np.save(weight_file,self.w)

	def load_model(self, weight_file):
		""" Load the trained model parameters
		"""

		self.w = np.load(weight_file)
