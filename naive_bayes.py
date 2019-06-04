import numpy as np
import math

class NaiveBayes(object):
	def __init__(self,num_class,feature_dim,num_value):
		"""Initialize a naive bayes model.

		This function will initialize prior and likelihood, where
		prior is P(class) with a dimension of (# of class,)
			that estimates the empirical frequencies of different classes in the training set.
		likelihood is P(F_i = f | class) with a dimension of
			(# of features per example, # of possible values per feature, # of class),
			that computes the probability of every feature location i being value f for every class label.

		Args:
		    num_class(int): number of classes to classify (ex: num of unique picture labels)
		    feature_dim(int): feature dimension for each example (ex: num of pixels per picture)
		    num_value(int): max number of possible values for any feature (ex: num of colors in a pixel)
		"""

		self.num_value = num_value
		self.num_class = num_class
		self.feature_dim = feature_dim
		self.label_table = dict()
		self.index_of_labels = dict()
		self.num_examples = 0

		self.prior_counts = np.zeros((num_class))
		self.prior = np.zeros((num_class)) ##P(class)
		self.likelihood_counts = np.zeros((feature_dim, num_value, num_class))
		self.likelihood = np.zeros((feature_dim, num_value, num_class)) #P(Fi | class)
		#P(Fi = f | class) = (# of times featuref i has value f in training examples from this class) / (Total # of training examples from this class)

	def train(self,train_set,train_label):
		""" Train naive bayes model (self.prior and self.likelihood) with training dataset.
			self.prior(numpy.ndarray): training set class prior (in log) with a dimension of (# of class,),
			self.likelihood(numpy.ndarray): traing set likelihood (in log) with a dimension of
				(# of features per image, # of possible values per feature, # of class).
			You should apply Laplace smoothing to compute the likelihood.

		Args:
		    train_set(numpy.ndarray): training examples with a dimension of (# of examples, feature_dim)
		    train_label(numpy.ndarray): training labels with a dimension of (# of examples)
		"""
		# set variables for for loop ranges
		#print(train_set.shape)
		#print(train_label.shape)

		laplace_smoothing_value = 0.1
		self.num_examples = train_set.shape[0]
		number_of_features = train_set.shape[1]

		# index value for hash table starting at zero
		count = 0

		# preprocessing to find all labels that are in training set to
		# associate a label name with an index number, no guarantee that
		# number of unqiue examples seen is equal to num_classes
		for example in range(self.num_examples):
			if train_label[example] not in self.label_table:
				self.label_table[train_label[example]] = count
				count += 1
			self.prior_counts[self.label_table[train_label[example]]] += 1

		for key in self.label_table:
			self.index_of_labels[self.label_table[key]] = key

		# print(self.label_table)
		# print(self.index_of_labels)

		# loop through each example, and the features of each example
		# feature_dim = pixel number 0-784
		# num_value = value of pixel, 0-255
		# num_classes = index of class
		# self.likelihood[feature_dim][num_value][num_class]
		for example in range(self.num_examples):
			for feature in range(number_of_features):
				feature_value = train_set[example][feature]
				self.likelihood_counts[feature][feature_value][train_label[example]] += 1

		self.likelihood_counts += laplace_smoothing_value
		self.prior_counts += laplace_smoothing_value

		self.prior = np.copy(self.prior_counts)
		self.likelihood = np.copy(self.likelihood_counts)
		for sample in range(self.num_class):
			np.divide(self.likelihood[:,:,sample], self.prior[sample])
		np.divide(self.prior, self.num_examples)

	def test(self,test_set,test_label):
		""" Test the trained naive bayes model (self.prior and self.likelihood) on testing dataset,
			by performing maximum a posteriori (MAP) classification.
			The accuracy is computed as the average of correctness
			by comparing between predicted label and true label.

		Args:
		    test_set(numpy.ndarray): testing examples with a dimension of (# of examples, feature_dim)
		    test_label(numpy.ndarray): testing labels with a dimension of (# of examples, )

		Returns:
			accuracy(float): average accuracy value
			pred_label(numpy.ndarray): predicted labels with a dimension of (# of examples, )
		"""
		number_of_examples = test_set.shape[0]
		number_of_features = test_set.shape[1]
		best_prediction = 0
		correct_predictions = 0
		# YOUR CODE HERE

		accuracy = 0
		pred_label = np.zeros((len(test_set)))

		for example in range(number_of_examples):
			for classes in range(len(self.prior)):
				current_prediction = math.log(self.prior[classes])
				for feature in range(number_of_features):
					feature_value = test_set[example][feature]
					current_prediction += math.log(self.likelihood[feature][feature_value][classes])
				if current_prediction > best_prediction:
					best_prediction = current_prediction
					#predicted_label = self.index_of_labels[classes]
					predicted_label = classes
			pred_label[example] = predicted_label
			best_prediction = 0

		for pred in range(len(pred_label)):
			if pred_label[pred] == test_label[pred]:
				correct_predictions += 1
		accuracy = correct_predictions / number_of_examples
		#pass
		print(accuracy)
		return accuracy, pred_label

	def guess(self,test_set):
		"""
		test_set(numpy.ndarray): current play with a dimension of (feature_dim)
		"""
		best_prediction = 0
		correct_predictions = 0
		number_of_features = test_set.shape[0]
		for classes in range(len(self.prior)):
			current_prediction = math.log(self.prior[classes])
			for feature in range(number_of_features):
				feature_value = test_set[feature]
				current_prediction += math.log(self.likelihood[feature][feature_value][classes])
			if current_prediction > best_prediction:
				best_prediction = current_prediction
				#predicted_label = self.index_of_labels[classes]
				predicted_label = classes
		return predicted_label

	def update(self, test_set, test_label):
		number_of_features = test_set.shape[0]

		self.num_examples += 1
		self.prior_counts[self.label_table[test_label]] += 1
		for feature in range(number_of_features):
			feature_value = test_set[feature]
			self.likelihood_counts[feature][feature_value][test_label] += 1

		self.prior = np.copy(self.prior_counts)
		self.likelihood = np.copy(self.likelihood_counts)

		for sample in range(self.num_class):
			np.divide(self.likelihood[:,:,sample], self.prior[sample])
		np.divide(self.prior, self.num_examples)

	def save_model(self, prior, likelihood):
		""" Save the trained model parameters
		"""

		np.save(prior, self.prior)
		np.save(likelihood, self.likelihood)

	def load_model(self, prior, likelihood):
		""" Load the trained model parameters
		"""

		self.prior = np.load(prior)
		self.likelihood = np.load(likelihood)

	def intensity_feature_likelihoods(self, likelihood):
		"""
		Get the feature likelihoods for high intensity pixels for each of the classes,
			by summing the probabilities of the top 128 intensities at each pixel location,
			sum k<-128:255 P(F_i = k | c).
			This helps generate visualization of trained likelihood images.

		Args:
			likelihood(numpy.ndarray): likelihood (in log) with a dimension of
				(# of features/pixels per image, # of possible values per pixel, # of class)
		Returns:
			feature_likelihoods(numpy.ndarray): feature likelihoods for each class with a dimension of
				(# of features/pixels per image, # of class)
		"""
		feature_likelihoods = np.zeros((likelihood.shape[0],likelihood.shape[2]))

		number_of_pixels = likelihood.shape[0]
		number_of_pixel_values = likelihood.shape[1]
		number_of_classes = likelihood.shape[2]

		log_sum = 0

		for classes in range(number_of_classes):
			for pixel in range(number_of_pixels):
				for pixel_val in range(128, number_of_pixel_values):
					log_sum += math.log(likelihood[pixel][pixel_val][classes])
				feature_likelihoods[pixel][classes] = log_sum
				log_sum = 0


		return feature_likelihoods
