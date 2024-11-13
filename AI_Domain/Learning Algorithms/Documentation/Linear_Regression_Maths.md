# Theory for Linear Regression
To perform supervised learning, we must decide how we’re going to represent functions/hypotheses \( h \) in a computer. As an initial choice, let’s say
we decide to approximate \( y \) as a linear function of \( x \):
$$ h_{\theta}(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 $$

Here, the \( \theta_i \)'s are the parameters (also called weights) parameterizing the space of linear functions mapping from \( X \) to \( Y \). In the following equation, let us consider \( \theta \) and \( x \) to be vectors, and \( d \) is the number of input variables excluding \( x_0 \). To simplify our notation, we also introduce the convention of letting \( x_0 = 1 \) (intercept term), so that:
$$ h(x) = \sum_{i=0}^{d} \theta_i x_i = \theta^T x $$

To choose the parameters, we want to make \( h(x) \) close to \( y \), at least for the training examples we have. To formalize this, we will define a function that measures, for each value of the \( \theta \)'s, how close the \( h(x^{(i)}) \)'s are to the corresponding \( y^{(i)} \)'s. We define the cost function:
$$ J(\theta) = \frac{1}{2} \sum_{i=1}^{n} \left( h_{\theta}(x^{(i)}) - y^{(i)} \right)^2 $$

## Gradient Descent Algorithms

Gradient descent is an optimization algorithm used to minimize the cost function of a machine learning model. The goal of gradient descent is to iteratively update the model's parameters in the direction of the negative gradient of the cost function.

### Batch Gradient Descent

In Batch Gradient Descent, the model parameters are updated based on the average of the gradients computed using the entire dataset. This approach can be computationally expensive when dealing with large datasets but ensures convergence to the global minimum in convex functions.  
Given the cost function \( J(\theta) \), where \( \theta \) represents the parameters (weights), and \( m \) is the number of training examples, the gradient descent update rule for Batch Gradient Descent is:

$$
\theta^{(t+1)} = \theta^{(t)} - \frac{\alpha}{m} \sum_{i=1}^{m} \nabla_\theta J(\theta^{(t)}, x^{(i)}, y^{(i)})
$$

In this equation:
- \( \theta^{(t)} \) is the current parameter vector at iteration \( t \),
- \( \alpha \) is the learning rate,
- \( m \) is the total number of training examples,
- \( \nabla_\theta J(\theta^{(t)}, x^{(i)}, y^{(i)}) \) is the gradient of the cost function with respect to \( \theta \) for the \( i \)-th training example \( (x^{(i)}, y^{(i)}) \).

In Batch Gradient Descent, the update step is computed using the entire dataset at each iteration.

### Stochastic Gradient Descent 

In Stochastic Gradient Descent, the model parameters are updated after computing the gradient using a single training example. This makes the algorithm much faster and allows it to start learning from the very first example. However, the updates are noisy and may not converge as smoothly as Batch Gradient Descent.  
For Stochastic Gradient Descent, the update rule becomes:

$$
\theta^{(t+1)} = \theta^{(t)} - \alpha \nabla_\theta J(\theta^{(t)}, x^{(i)}, y^{(i)})
$$

In this equation:
- \( \theta^{(t)} \) is the current parameter vector at iteration \( t \),
- \( \alpha \) is the learning rate,
- \( \nabla_\theta J(\theta^{(t)}, x^{(i)}, y^{(i)}) \) is the gradient of the cost function with respect to \( \theta \) for the \( i \)-th training example \( (x^{(i)}, y^{(i)}) \).

In Stochastic Gradient Descent, the update is made using only a single training example \( (x^{(i)}, y^{(i)}) \) at each iteration. This results in faster updates but can lead to fluctuations in the cost function.
