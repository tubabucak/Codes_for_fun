# Ridge regression

def ridge_regression_gradient_descent(feature_matrix, output, initial_weights, step_size, l2_penalty, max_iterations=100):
    weights = np.array(initial_weights) # make sure it's a numpy array
    count= 0
    #while not reached maximum number of iterations:
        # compute the predictions based on feature_matrix and weights using your predict_output() function
    while count < max_iterations:
        predictions = predict_output(feature_matrix, weights) 
        # compute the errors as predictions - output
        error = predictions - output
        for i in xrange(len(weights)): # loop over each weight
            # Recall that feature_matrix[:,i] is the feature column associated with weights[i]
            # compute the derivative for weight[i].
            if i==0:
                derivative = feature_derivative_ridge(error, feature_matrix[:,i], weights[i], l2_penalty, True)
            #(Remember: when i=0, you are computing the derivative of the constant!)
            else:
                derivative = feature_derivative_ridge(error, feature_matrix[:,i], weights[i], l2_penalty, False)

            # subtract the step size times the derivative from the current weight
            weights[i] = weights[i] - (step_size * derivative)
        count = count + 1
    return weights
